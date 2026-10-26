#from aoe2_translate import *
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.objects.support.trigger_select import TS
from utils.const import *
from utils.instruction_helper import *
from utils.aoe2_translate import *
import sys
from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.datasets.techs import TechInfo
from AoE2ScenarioParser.datasets.trigger_lists import Attribute
from AoE2ScenarioParser.datasets.conditions import ConditionId

RESOURCE_IDS = {
    "food": 0,
    "wood": 1,
    "stone": 2,
    "gold": 3,
}

UNIT_IDS = {
    "man_at_arms": 75,
    "huskarl": 41,
    "elite_huskarl": 555,
    "spearman": 93,
    "archer": 4,
    "skirmisher": 7,
    "light_cavalry": 546,
    "knight": 38,
    "cavalier": 283,
    "jarl": 2708,
    "elite_monaspa": 1805,
}

UNIT_NAMES_ZH = {
        "man_at_arms": "剑士",
        "huskarl": "近卫军",
        "spearman": "长矛兵",
        "archer": "弓箭手",
        "skirmisher": "投矛手",
        "light_cavalry": "轻骑兵",
        "knight": "骑士",
        "cavalier": "重装骑士",
        "elite_huskarl": "精英近卫军",
        "jarl": "掷斧骑兵",
        "elite_monaspa": "哥特精锐骑兵",
    }

UNIT_COSTS = {
        "man_at_arms":    {"food": 50, "wood": 0,  "gold": 25, "stone": 0},
        "huskarl":        {"food": 60, "wood": 0,  "gold": 30, "stone": 0},
        "elite_huskarl":  {"food": 70, "wood": 0,  "gold": 35, "stone": 0},
        "spearman":       {"food": 50, "wood": 30, "gold": 0,  "stone": 0},
        "archer":         {"food": 30, "wood": 40, "gold": 0,  "stone": 0},
        "skirmisher":     {"food": 25, "wood": 35, "gold": 0,  "stone": 0},
        "light_cavalry":  {"food": 80, "wood": 0,  "gold": 0,  "stone": 0},
        "knight":         {"food": 60, "wood": 0,  "gold": 70, "stone": 0},
        "cavalier":       {"food": 70, "wood": 0,  "gold": 70, "stone": 0},
        "jarl":           {"food": 50, "wood": 0,  "gold": 60, "stone": 0},
        "elite_monaspa":  {"food": 60, "wood": 0,  "gold": 75, "stone": 0},
    }


limited_stack_units = {
    "jarl",
    "elite_huskarl",
    "elite_monaspa",
}






from pathlib import Path
from pprint import pformat
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario



from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.trigger_lists import Operation
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from utils.instruction_helper import *

"""Add a trigger to an AoE2 DE scenario object that enables techs 1180+ as
Castle buttons, sets their costs, research time, stacking, Chinese name and
description ("训练 <unit>"), and the icon of the matching unit.

Usage:
    scenario = AoE2DEScenario.from_file("in.aoe2scenario")
    scenario = add_castle_unit_techs(scenario)
    scenario.write_to_file("out.aoe2scenario")
"""


from copy import deepcopy

unit_costs = {
    "man_at_arms":    {"food": 50, "wood": 0,  "gold": 25, "stone": 0},
    "huskarl":        {"food": 60, "wood": 0,  "gold": 30, "stone": 0},
    "spearman":       {"food": 50, "wood": 30, "gold": 0,  "stone": 0},
    "archer":         {"food": 30, "wood": 40, "gold": 0,  "stone": 0},
    "skirmisher":     {"food": 25, "wood": 35, "gold": 0,  "stone": 0},
    "light_cavalry":  {"food": 80, "wood": 0,  "gold": 0,  "stone": 0},
    "knight":         {"food": 60, "wood": 0,  "gold": 70, "stone": 0},
    "cavalier":       {"food": 70, "wood": 0,  "gold": 70, "stone": 0},
    "elite_huskarl":  {"food": 70, "wood": 0,  "gold": 35, "stone": 0},
    "jarl":           {"food": 50, "wood": 0,  "gold": 60, "stone": 0},
    "elite_monaspa":  {"food": 60, "wood": 0,  "gold": 75, "stone": 0},
}

tech_ids = {
    "man_at_arms":   TechInfo.MAN_AT_ARMS.ID,        # 222
    "huskarl":       TechInfo.LONG_SWORDSMAN.ID,     # 207
    "spearman":      TechInfo.PIKEMAN.ID,            # 197
    "archer":        TechInfo.CROSSBOWMAN.ID,        # 100
    "skirmisher":    TechInfo.ELITE_SKIRMISHER.ID,   # 98
    "light_cavalry": TechInfo.HUSSAR.ID,             # 428
    "knight":        TechInfo.CAVALIER.ID,           # 209
    "cavalier":      TechInfo.PALADIN.ID,            # 265
    "elite_huskarl": TechInfo.ELITE_HUSKARL.ID,      # 365
    "jarl":          TechInfo.ELITE_JARL.ID,         # 1472
    "elite_monaspa": TechInfo.ELITE_MONASPA.ID,      # 920
}
# Chinese unit names (edit freely); text becomes "训练 <name>"
unit_names_zh = {
    "man_at_arms": "剑士",
    "huskarl": "近卫军",
    "spearman": "长矛兵",
    "archer": "弓箭手",
    "skirmisher": "投矛兵",
    "light_cavalry": "轻骑兵",
    "knight": "骑士",
    "cavalier": "重装骑士",
    "elite_huskarl": "精英近卫军",
    "jarl": "掷斧奇兵",
    "elite_monaspa": "精英哥特骑手",
}

# Resource ids used by the cost effect (food=0, wood=1, stone=2, gold=3)
resource_ids = {
    "food": Attribute.FOOD_STORAGE,
    "wood": Attribute.WOOD_STORAGE,
    "gold": Attribute.GOLD_STORAGE,
    "stone": Attribute.STONE_STORAGE,
}

def cost_slots(cost):
    """Build the three (resource_id, quantity) slots the cost effect accepts.

    Input:  cost (dict) - food/wood/gold/stone values (at most 3 non-zero).
    Output: list[tuple[int, int]] - exactly 3 slots; non-zero costs first,
            padded with explicit zero-cost resources.
    """
    slots = [(resource_ids[r], q) for r, q in cost.items() if q > 0]
    for r, rid in resource_ids.items():
        if len(slots) == 3:
            break
        if cost[r] == 0:
            slots.append((rid, 0))
    return slots



def add_castle_unit_techs(scenario):
    """Add the Castle unit-tech trigger (1x and 10x techs) to a scenario object.

    Input:  scenario (AoE2DEScenario) - scenario to modify.
    Output: AoE2DEScenario - the same scenario object, now containing the
            "Castle Unit Techs" trigger.
    """

    players = [
        PlayerId.ONE,
    ]

    unit_costs = {
        "man_at_arms":    {"food": 50, "wood": 0,  "gold": 25, "stone": 0},
        "huskarl":        {"food": 60, "wood": 0,  "gold": 30, "stone": 0},
        "spearman":       {"food": 50, "wood": 30, "gold": 0,  "stone": 0},
        "archer":         {"food": 30, "wood": 40, "gold": 0,  "stone": 0},
        "skirmisher":     {"food": 25, "wood": 35, "gold": 0,  "stone": 0},
        "light_cavalry":  {"food": 80, "wood": 0,  "gold": 0,  "stone": 0},
        "knight":         {"food": 60, "wood": 0,  "gold": 70, "stone": 0},
        "cavalier":       {"food": 70, "wood": 0,  "gold": 70, "stone": 0},
        "elite_huskarl":  {"food": 70, "wood": 0,  "gold": 35, "stone": 0},
        "jarl":           {"food": 50, "wood": 0,  "gold": 60, "stone": 0},
        "elite_monaspa":  {"food": 60, "wood": 0,  "gold": 75, "stone": 0},
    }
    # Tech id used for each unit's 1x button (existing upgrade techs).
    tech_ids = {
        "man_at_arms":   TechInfo.MAN_AT_ARMS.ID,        # 222
        "huskarl":       TechInfo.LONG_SWORDSMAN.ID,     # 207
        "spearman":      TechInfo.PIKEMAN.ID,            # 197
        "archer":        TechInfo.CROSSBOWMAN.ID,        # 100
        "skirmisher":    TechInfo.ELITE_SKIRMISHER.ID,   # 98
        "light_cavalry": TechInfo.HUSSAR.ID,             # 428
        "knight":        TechInfo.CAVALIER.ID,           # 209
        "cavalier":      TechInfo.PALADIN.ID,            # 265
        "elite_huskarl": TechInfo.ELITE_HUSKARL.ID,      # 365
        "jarl":          TechInfo.ELITE_JARL.ID,         # 1472
        "elite_monaspa": TechInfo.ELITE_MONASPA.ID,      # 920
    }

    # Resource ids used by the cost effect (food=0, wood=1, stone=2, gold=3)
    resource_ids = {
        "food": Attribute.FOOD_STORAGE,
        "wood": Attribute.WOOD_STORAGE,
        "gold": Attribute.GOLD_STORAGE,
        "stone": Attribute.STONE_STORAGE,
    }
    chinese_names = {
        0: "食物",
        1: "木材",
        2: "石头",
        3: "黄金",
    }

    def cost_slots(cost):
        """Build the three (resource_id, quantity) slots the cost effect accepts.

        Input:  cost (dict) - food/wood/gold/stone values (at most 3 non-zero).
        Output: list[tuple[int, int]] - exactly 3 slots; non-zero costs first,
                padded with explicit zero-cost resources.
        """
        slots = [(resource_ids[r], q) for r, q in cost.items() if q > 0]
        for r, rid in resource_ids.items():
            if len(slots) == 3:
                break
            if cost[r] == 0:
                slots.append((rid, 0))
        return slots

    def add_effects(trigger, player, tech_id, button, unit, cost, multiplier=1):
        """Append all effects for one tech and player.

        Input:  trigger - AoE2ScenarioParser Trigger to add effects to;
                player (PlayerId) - player the tech is set up for;
                tech_id (int) - technology id;
                button (int) - castle button slot (1-based);
                unit (str) - key from unit_costs;
                cost (dict) - food/wood/gold/stone values for ONE unit;
                multiplier (int) - 1 for the single-unit tech, 10 for the
                10-unit tech (scales the cost and changes the label).
        Output: None (mutates the trigger).
        """
        cost = {r: q * multiplier for r, q in cost.items()}
        slots = cost_slots(cost)
        count_text = f"{multiplier}个" if multiplier > 1 else ""
        name_label = f"训练 {count_text}{unit_names_zh[unit]}"
        cost_text = ""
        for i in range(3):
            if slots[i][1] > 0:
                cost_text += "(" + str(slots[i][1]) + chinese_names[slots[i][0]] + ")"
        desc_label = name_label + cost_text

        trigger.new_effect.enable_disable_technology(
            source_player=player,
            technology=tech_id,
            enabled=1,
        )
        trigger.new_effect.change_technology_location(
            source_player=player,
            technology=tech_id,
            object_list_unit_id_2=BuildingInfo.CASTLE.ID,
            button_location=button,
        )
        trigger.new_effect.change_technology_cost(
            source_player=player,
            technology=tech_id,
            resource_1=slots[0][0], resource_1_quantity=slots[0][1],
            resource_2=slots[1][0], resource_2_quantity=slots[1][1],
            resource_3=slots[2][0], resource_3_quantity=slots[2][1],
        )
        trigger.new_effect.change_technology_name(
            source_player=player,
            technology=tech_id,
            message=name_label,
        )
        trigger.new_effect.change_technology_description(
            source_player=player,
            technology=tech_id,
            message=desc_label,
        )

    matches = [
        t for t in scenario.trigger_manager.triggers
        if t.name.strip() == "Castle Unit Techs"
    ]
    if len(matches) != 1:
        raise ValueError(f"Expected one 'Castle Unit Techs' trigger, found {len(matches)}.")
    trigger = matches[0]


    # 1x techs: existing upgrade tech ids, castle buttons 1-4, 6-12 (5 skipped).
    buttons_1x = [1, 2, 3, 4] + list(range(6, 13))
    for i, unit in enumerate(unit_costs):
        for player in players:
            add_effects(trigger, player, tech_ids[unit], buttons_1x[i], unit, unit_costs[unit])
    # 10x techs: ids 1180-1190, castle buttons 21-24 then 26-35 (25 skipped).
    # Same unit order as tech_ids, with skirmisher moved to the end.
    first_tech_id_10x = 1180
    buttons_10x = [21, 22, 23, 24] + list(range(26, 36))
    units_10x = [u for u in tech_ids if u != "skirmisher"] + ["skirmisher"]

    for i, unit in enumerate(units_10x):
        for player in players:
            add_effects(
                trigger, player, first_tech_id_10x + i, buttons_10x[i],
                unit, unit_costs[unit], multiplier=10,
            )

    return scenario

def add_unit_triggers(scenario):
    """Clone the 'train man-at-arms' template into one trigger per unit.

    Input:  scenario (AoE2DEScenario) - scenario that already contains exactly
            one trigger named 'train man-at-arms'.
    Output: AoE2DEScenario - the same scenario with one 'train <unit>' trigger
            added per entry in UNIT_IDS (existing names are skipped).
    """


    triggers = scenario.trigger_manager.triggers

    # Find the template trigger.
    templates = [
        trigger
        for trigger in triggers
        if trigger.name.strip().lower() == "train man at arms"
    ]

    if len(templates) != 1:
        raise ValueError(
            f"Expected one 'train man at arms' trigger, found {len(templates)}."
        )

    template = deepcopy(templates[0])

    existing_names = {
        trigger.name.strip().lower()
        for trigger in triggers
    }

    # Generate triggers for units 1-10, using technologies 1180-1189.
    tech_ids = {
        "man_at_arms":   TechInfo.MAN_AT_ARMS.ID,        # 222
        "huskarl":       TechInfo.LONG_SWORDSMAN.ID,     # 207
        "spearman":      TechInfo.PIKEMAN.ID,            # 197
        "archer":        TechInfo.CROSSBOWMAN.ID,        # 100
        "skirmisher":    TechInfo.ELITE_SKIRMISHER.ID,   # 98
        "light_cavalry": TechInfo.HUSSAR.ID,             # 428
        "knight":        TechInfo.CAVALIER.ID,           # 209
        "cavalier":      TechInfo.PALADIN.ID,            # 265
        "elite_huskarl": TechInfo.ELITE_HUSKARL.ID,      # 365
        "jarl":          TechInfo.ELITE_JARL.ID,         # 1472
        "elite_monaspa": TechInfo.ELITE_MONASPA.ID,      # 920
    }

    # Generate one trigger per unit in UNIT_IDS.
    for unit_name, unit_id in UNIT_IDS.items():

        if unit_name not in tech_ids:
            raise ValueError(f"No tech id defined for unit '{unit_name}'.")
        tech_id = tech_ids[unit_name]
        trigger_name = f"train {unit_name.replace('_', ' ')}"

        if trigger_name.lower() in existing_names:
            continue

        trigger = deepcopy(template)
        trigger.name = trigger_name
        trigger.trigger_id = len(triggers)

        # Update researching technology condition.
        tech_conditions = [
            condition
            for condition in trigger.conditions
            if condition.condition_type == 17
        ]

        if len(tech_conditions) != 1:
            raise ValueError(
                f"{trigger_name}: expected exactly one researching-technology condition, "
                f"found {len(tech_conditions)}."
            )

        tech_conditions[0].technology = tech_id

        # Update replacement unit ID.
        replace_effects = [
            effect
            for effect in trigger.effects
            if (effect.effect_type==43)
        ]

        if len(replace_effects) != 1:
            print(replace_effects)
            raise ValueError(
                f"{trigger_name}: expected exactly one replace-object effect."
            )

        replace_effects[0].object_list_unit_id_2 = unit_id
        replace_effects[0].max_affected_units = 1

        slots = cost_slots(unit_costs[unit_name])


        for i in range(3):
            print(slots[i][1])
            if slots[i][1] >0:
                trigger.new_effect.tribute(
                    quantity=slots[i][1],
                    tribute_list=slots[i][0],
                    source_player=PlayerId.ONE,
                    target_player=PlayerId.GAIA

                )

        # Add the trigger to the same scenario.
        triggers.append(trigger)
        existing_names.add(trigger_name.lower())

    return scenario

def add_10x_unit_triggers(scenario):
    """Clone each 'train <unit>' trigger into a 'train <unit> 10x' trigger.

    Each clone listens for the unit's 10x tech multiplies the tribute
    effect amounts by 10, and multiplies the replace-object effect's
    max_units_affected by 10.

    Input:  scenario (AoE2DEScenario) - scenario that already contains the
            1x 'train <unit>' triggers.
    Output: AoE2DEScenario - the same scenario with the 10x triggers appended
            (existing '... 10x' names are skipped).
    """
    # Same order as the 10x castle techs, skirmisher last.
    units_10x = [
        "man_at_arms", "huskarl", "spearman", "archer", "light_cavalry",
        "knight", "cavalier", "elite_huskarl", "jarl", "elite_monaspa",
        "skirmisher",
    ]
    first_tech_id_10x = 1180
    multiplier = 10

    triggers = scenario.trigger_manager.triggers
    by_name = {t.name.strip().lower(): t for t in triggers}

    for i, unit in enumerate(units_10x):
        label = unit.replace("_", " ")
        new_name = f"train {label} 10x"
        if new_name in by_name:
            continue

        # 1x source trigger, e.g. 'train jarl' ('train man-at-arms' also accepted).
        source = by_name.get(f"train {label}") or by_name.get(f"train {unit.replace('_', '-')}")
        if source is None:
            raise ValueError(f"No 1x trigger found for '{unit}' (looked for 'train {label}').")

        trigger = deepcopy(source)
        trigger.name = new_name
        trigger.trigger_id = len(triggers)

        # Point the researching-technology condition at the 10x tech.
        tech_conditions = [
            c for c in trigger.conditions
            if c.condition_type == ConditionId.RESEARCHING_TECH
        ]
        if len(tech_conditions) != 1:
            raise ValueError(
                f"{new_name}: expected exactly one researching-tech condition, "
                f"found {len(tech_conditions)}."
            )
        tech_conditions[0].technology = first_tech_id_10x + i

        # Scale tribute amounts and the replace-object unit cap.
        for effect in trigger.effects:
            if effect.effect_type == EffectId.TRIBUTE and effect.quantity > 0:
                effect.quantity *= multiplier
            elif effect.effect_type == EffectId.REPLACE_OBJECT and effect.max_units_affected > 0:
                effect.max_units_affected *= multiplier

        triggers.append(trigger)
        by_name[new_name] = trigger

    return scenario

if __name__ == "__main__":


    asyncio.run(trans_campaign_folder(campaign_name='adrianople'))



    # 翻译.aoe2scenario文件/ translate .aoe2scenario file
    #asyncio.run(translate_scenario(src='zh-cn', dest='en', replace=False))

    
    #翻译 info.json/layout.json .../ translate info.json/layout.json ...
    #campaign_name = "mingliang" # 需要翻译的战役文件夹名称/ name of the campaign folder to be translated
    #asyncio.run(translate_other(campaign_name))
    

