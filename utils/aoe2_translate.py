from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.objects.support.trigger_select import TS
import os
from googletrans import Translator
import asyncio
import json
import shutil

input_dir = "input/translate_scenario"
output_dir = "output/translate_scenario"

os.makedirs(input_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)


async def translate_scenario(scenario, src='zh-cn', dest='en'):
    '''
    scenario: An AoE2DEScenario object
    src: Source language code, e.g. 'zh-cn'
    dest: Destination language code, e.g. 'en'
    '''
    async with Translator() as translator:
        raw_text = []
        setters = []

        # Player tribe names
        player_manager = scenario.player_manager

        for player_id in PlayerId:
            player = player_manager.players[player_id]
            if player.tribe_name:
                raw_text.append(player.tribe_name)
                setters.append(
                    lambda text, p=player: setattr(p, 'tribe_name', text)
                )

        # Scenario messages
        message_manager = scenario.message_manager

        for attr in [
            'instructions', 'hints', 'history',
            'loss', 'scouts', 'victory'
        ]:
            value = getattr(message_manager, attr)
            if value:
                raw_text.append(value)
                setters.append(
                    lambda text, obj=message_manager, a=attr:
                        setattr(obj, a, text)
                )

        # Trigger descriptions and effect messages
        for trigger in scenario.trigger_manager.triggers:
            for attr in ['description', 'short_description']:
                value = getattr(trigger, attr)
                if value:
                    raw_text.append(value)
                    setters.append(
                        lambda text, t=trigger, a=attr:
                            setattr(t, a, text)
                    )

            for effect in trigger.effects:
                if effect.message:
                    raw_text.append(effect.message)
                    setters.append(
                        lambda text, e=effect: setattr(e, 'message', text)
                    )

        # Translate and apply results
        if not raw_text:
            return scenario

        translated = await translator.translate(
            raw_text, src=src, dest=dest
        )

        for setter, result in zip(setters, translated):
            setter(result.text)

    return scenario



async def translate_cascade_dict(obj, target_key, translator):
    '''
    翻译嵌套字典或列表中目标键的值/ translate the value of the target key in a nested dictionary or list
    '''
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == target_key and isinstance(value, str):
                translated = await translator.translate(value, src='zh-cn', dest='en')
                obj[key] = translated.text
            else:
                await translate_cascade_dict(obj[key], target_key, translator)

    elif isinstance(obj, list):
        for i in range(len(obj)):
            await translate_cascade_dict(obj[i], target_key, translator)



async def translate_other(campaign_name, src='zh-cn', dest='en'):
    '''
    campaign_name: 需要翻译的战役文件夹名称/ name of the campaign folder to be translated

    确保文件结构至少包含以下文件/ make sure the file structure contains at least the following files:
    确保所有文件前缀都和文件夹同名，此处都为'my_campaign'/ make sure all files have the same name as the folder, here it's all 'my_campaign'

    my_campaign\
    │
    ├── info.json
    └── resources\
        └── _common\
            └── campaign\
                ├── my_campaign.aoe2campaign
                |── my_campaign_layout.json
                |── my_campaign.json
    '''
    campaign_json_file = f"{input_dir}/{campaign_name}/resources/_common/campaign/{campaign_name}.json"
    with open(campaign_json_file, 'r', encoding='utf-8') as f:
        campaign_data = json.load(f)
        await translate_cascade_dict(campaign_data, "String", Translator())

    with open(campaign_json_file, 'w', encoding='utf-8') as f_out:
        json.dump(campaign_data, f_out, ensure_ascii=False, indent=4)
    os.rename(campaign_json_file, campaign_json_file.replace('.json', f'_{dest}.json'))

    

    campaign_layout_json = f"{input_dir}/{campaign_name}/resources/_common/campaign/{campaign_name}_layout.json"
    with open(campaign_layout_json, 'r', encoding='utf-8') as f:
        campaign_layout_data = json.load(f)
        await translate_cascade_dict(campaign_layout_data, "Text", Translator())

        campaign_layout_data["UserMaterials"][0]["Material"] = campaign_name + f"_{dest}"
        campaign_layout_data["UserMaterials"][0]["FileName"] = campaign_name + f"_{dest}.dds"
        campaign_layout_data["BackgroundMaterial"] = campaign_name + f"_{dest}"

    with open(campaign_layout_json, 'w', encoding='utf-8') as f_out:
        json.dump(campaign_layout_data, f_out, ensure_ascii=False, indent=4)
    os.rename(campaign_layout_json, campaign_layout_json.replace('.json', f'_{dest}.json'))



    info_json_file = f"{input_dir}/{campaign_name}/info.json"
    with open(info_json_file, 'r', encoding='utf-8') as f:
        info_data = json.load(f)

        description = info_data["Description"]
        translated = await Translator().translate(description, src=src, dest=dest)
        info_data["Description"] = translated.text

        title = info_data["Title"]
        translated = await Translator().translate(title, src=src, dest=dest)
        info_data["Title"] = translated.text
        
    with open(info_json_file, 'w', encoding='utf-8') as f_out:
        json.dump(info_data, f_out, ensure_ascii=False, indent=4)



    campaign_file = f"{input_dir}/{campaign_name}/resources/_common/campaign/{campaign_name}.aoe2campaign"
    os.rename(campaign_file, campaign_file.replace('.aoe2campaign', f'_{dest}.aoe2campaign'))



    campaign_dds_file = f"{input_dir}/{campaign_name}/resources/_common/campaign/{campaign_name}.dds"
    if os.path.exists(campaign_dds_file):
        os.rename(campaign_dds_file, campaign_dds_file.replace('.dds', f'_{dest}.dds'))


    
    campaign_folder = f"{input_dir}/{campaign_name}"
    os.rename(campaign_folder, campaign_folder.replace(campaign_name, campaign_name + f"_{dest}"))




async def trans_campaign_folder(
    campaign_name,
    src='zh-cn',
    dest='en',
    output_folder=output_dir
):
    '''
    campaign_name: 战役文件夹名称
    src: 源语言代码
    dest: 目标语言代码
    output_folder: 翻译后的战役文件夹输出目录

    翻译内容：
    1. 战役文件夹中的所有 .aoe2scenario 场景文件
    2. 战役 JSON 文件和布局 JSON 文件
    3. info.json 中的战役标题和描述
    4. 战役文件及文件夹名称

    原始文件不会被修改。
    '''

    # Original campaign folder
    source_folder = os.path.join(input_dir, campaign_name)

    if not os.path.isdir(source_folder):
        raise FileNotFoundError(
            f"Campaign folder not found: {source_folder}"
        )

    # Create output directory
    os.makedirs(output_folder, exist_ok=True)

    # Copy campaign into output folder
    copied_folder = os.path.join(output_folder, campaign_name)

    if os.path.exists(copied_folder):
        raise FileExistsError(
            f"Output campaign already exists: {copied_folder}"
        )

    shutil.copytree(source_folder, copied_folder)

    print(f"Campaign copied to: {copied_folder}")

    # --------------------------------------------------
    # 1. Translate all scenario files in the copied folder
    # --------------------------------------------------

    for root, dirs, files in os.walk(copied_folder):
        for filename in files:
            if filename.endswith('.aoe2scenario'):
                scenario_file = os.path.join(root, filename)

                print(f"Translating scenario: {scenario_file}")

                scenario = AoE2DEScenario.from_file(scenario_file)

                await translate_scenario(
                    scenario,
                    src=src,
                    dest=dest
                )

                scenario.write_to_file(scenario_file)

    # --------------------------------------------------
    # 2. Translate campaign metadata and rename campaign files
    # --------------------------------------------------

    await translate_other(
        campaign_name,
        src=src,
        dest=dest,
        base_dir=output_folder
    )

    print(
        f"Campaign translation completed: "
        f"{os.path.join(output_folder, campaign_name + '_' + dest)}"
    )