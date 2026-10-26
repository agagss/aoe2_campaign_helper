#from aoe2_translate import *
from utils.const import *
from utils.instruction_helper import *
from utils.aoe2_translate import *
from utils.change_unavailable_civ import *
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario





if __name__ == "__main__":


    #scenario = AoE2DEScenario.from_file("input/example.aoe2scenario")

    # 翻译.aoe2scenario文件/ translate .aoe2scenario file
    #asyncio.run(translate_scenario(scenario=scenario, src='zh-cn', dest='en', replace=False))

    
    #翻译 整个战役文件夹/ translate whole campaign folder ...
    #campaign_name = "xxx" # 需要翻译的战役文件夹名称/ name of the campaign folder to be translated
    #asyncio.run(translate_trans_campaign_folder(campaign_name))
    
    # 随机替换战役dlc文明/ randomly replace dlc civ in scenario
    #randomly_replace_dlc_civ(scenario)