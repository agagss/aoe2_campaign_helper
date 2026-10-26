from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from pathlib import Path
from pprint import pformat
from AoE2ScenarioParser.datasets.effects import EffectId
import ast
import json
import copy

def save_trigger_instructions(scenario_path):
    scenario = AoE2DEScenario.from_file(str(scenario_path))

    output_dir = Path("output/info")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / f"{Path(scenario_path).stem}_instructions.json"

    instructions = {}

    for trigger in scenario.trigger_manager.triggers:
        texts = [
            effect.message
            for effect in trigger.effects
            if effect.effect_type == 20
        ]

        if texts:
            instructions[trigger.name] = texts

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(instructions, file, indent=4, ensure_ascii=False)

    return instructions





def inject_instructions_to_scenario(scenario, instructions_path, inplace=True):
    """Replace the display-instruction effects of named triggers with saved text.

    Input:  scenario (AoE2DEScenario) - scenario to modify;
            instructions_path (str | Path) - JSON file {trigger_name: [text, ...]};
            inplace (bool) - if False, work on a deep copy.
    Output: AoE2DEScenario - the modified scenario (the copy if inplace=False).
    """
    if not inplace:
        scenario = copy.deepcopy(scenario)

    with Path(instructions_path).open("r", encoding="utf-8") as file:
        instructions = json.load(file)

    for trigger in scenario.trigger_manager.triggers:
        if trigger.name not in instructions:
            continue

        texts = instructions[trigger.name]
        if isinstance(texts, str):
            texts = [texts]

        # Remove existing display instructions to avoid duplicates.
        for effect in list(trigger.effects):
            if effect.effect_type == EffectId.DISPLAY_INSTRUCTIONS:
                trigger.remove_effect(effect=effect)

        # Inject the saved display instructions.
        for text in texts:
            trigger.new_effect.display_instructions(message=text)


    return scenario
