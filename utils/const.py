
#trigger

NONE = 0
"""Attributes for the **none** effect are: \n
... none... Just like Conditions... People these days... """
CHANGE_DIPLOMACY = 1
"""Attributes for the **change_diplomacy** effect are: \n
- diplomacy
- source_player
- target_player"""
RESEARCH_TECHNOLOGY = 2
"""Attributes for the **research_technology** effect are: \n
- source_player
- technology
- force_research_technology"""
SEND_CHAT = 3
"""Attributes for the **send_chat** effect are: \n
- source_player
- string_id
- message
- sound_name"""
PLAY_SOUND = 4
"""Attributes for the **play_sound** effect are: \n
- source_player
- location_x
- location_y
- location_object_reference
- global_sound
- sound_name"""
TRIBUTE = 5
"""Attributes for the **tribute** effect are: \n
- quantity
- tribute_list
- source_player
- target_player"""
UNLOCK_GATE = 6
"""Attributes for the **unlock_gate** effect are: \n
- selected_object_ids"""
LOCK_GATE = 7
"""Attributes for the **lock_gate** effect are: \n
- selected_object_ids"""
ACTIVATE_TRIGGER = 8
"""Attributes for the **activate_trigger** effect are: \n
- trigger_id"""
DEACTIVATE_TRIGGER = 9
"""Attributes for the **deactivate_trigger** effect are: \n
- trigger_id"""
AI_SCRIPT_GOAL = 10
"""Attributes for the **deactivate_trigger** effect are: \n
- ai_script_goal"""
CREATE_OBJECT = 11
"""Attributes for the **create_object** effect are: \n
- object_list_unit_id
- source_player
- location_x
- location_y
- facet
- disable_sound"""
TASK_OBJECT = 12
"""Attributes for the **task_object** effect are: \n
- object_list_unit_id
- source_player
- location_x
- location_y
- location_object_reference
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- action_type
- selected_object_ids
- disable_garrison_unload_sound
- max_units_affected
- issue_group_command
- queue_action"""
DECLARE_VICTORY = 13
"""Attributes for the **declare_victory** effect are: \n
- source_player
- enabled"""
KILL_OBJECT = 14
"""Attributes for the **kill_object** effect are: \n
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- selected_object_ids
- max_units_affected"""
REMOVE_OBJECT = 15
"""Attributes for the **remove_object** effect are: \n
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- object_state
- selected_object_ids
- max_units_affected"""
CHANGE_VIEW = 16
"""Attributes for the **change_view** effect are: \n
- quantity
- source_player
- location_x
- location_y
- scroll"""
UNLOAD = 17
"""Attributes for the **unload** effect are: \n
- object_list_unit_id
- source_player
- location_x
- location_y
- location_object_reference
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- selected_object_ids
- max_units_affected"""
CHANGE_OWNERSHIP = 18
"""Attributes for the **change_ownership** effect are: \n
- object_list_unit_id
- source_player
- target_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- flash_object
- selected_object_ids
- max_units_affected"""
PATROL = 19
"""Attributes for the **patrol** effect are: \n
- object_list_unit_id
- source_player
- location_x
- location_y
- location_object_reference
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- selected_object_ids
- max_units_affected"""
DISPLAY_INSTRUCTIONS = 20
"""Attributes for the **display_instructions** effect are: \n
- object_list_unit_id
- source_player
- string_id
- display_time
- instruction_panel_position
- play_sound
- message
- sound_name
- use_tag_color_for_icon"""
CLEAR_INSTRUCTIONS = 21
"""Attributes for the **clear_instructions** effect are: \n
- instruction_panel_position"""
FREEZE_OBJECT = 22
"""Attributes for the **freeze_object** effect are: \n
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- selected_object_ids
- max_units_affected"""
USE_ADVANCED_BUTTONS = 23
"""Attributes for the **use_advanced_buttons** effect are: \n
None. \n
Please don't use this effect. Please."""
DAMAGE_OBJECT = 24
"""Attributes for the **damage_object** effect are: \n
- quantity
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- selected_object_ids
- max_units_affected"""
PLACE_FOUNDATION = 25
"""Attributes for the **place_foundation** effect are: \n
- object_list_unit_id
- source_player
- location_x
- location_y"""
CHANGE_OBJECT_NAME = 26
"""Attributes for the **change_object_name** effect are: \n
- object_list_unit_id
- source_player
- string_id
- area_x1
- area_y1
- area_x2
- area_y2
- message
- selected_object_ids
- max_units_affected"""
CHANGE_OBJECT_HP = 27
"""Attributes for the **change_object_hp** effect are: \n
- quantity
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- operation
- selected_object_ids
- max_units_affected"""
CHANGE_OBJECT_ATTACK = 28
"""Attributes for the **change_object_attack** effect are: \n
- armour_attack_quantity
- armour_attack_class
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- operation
- selected_object_ids
- max_units_affected"""
STOP_OBJECT = 29
"""Attributes for the **stop_object** effect are: \n
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- selected_object_ids
- max_units_affected"""
ATTACK_MOVE = 30
"""Attributes for the **attack_move** effect are: \n
- object_list_unit_id
- source_player
- location_x
- location_y
- location_object_reference
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- selected_object_ids
- max_units_affected"""
CHANGE_OBJECT_ARMOR = 31
"""Attributes for the **change_object_armor** effect are: \n
- armour_attack_quantity
- armour_attack_class
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- operation
- selected_object_ids
- max_units_affected"""
CHANGE_OBJECT_RANGE = 32
"""Attributes for the **change_object_range** effect are: \n
- quantity
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- operation
- selected_object_ids
- max_units_affected"""
CHANGE_OBJECT_SPEED = 33
"""Attributes for the **change_object_speed** effect are: \n
- quantity
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- selected_object_ids
- max_units_affected"""
HEAL_OBJECT = 34
"""Attributes for the **heal_object** effect are: \n
- quantity
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- selected_object_ids
- max_units_affected"""
TELEPORT_OBJECT = 35
"""Attributes for the **teleport_object** effect are: \n
- object_list_unit_id
- source_player
- location_x
- location_y
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- selected_object_ids
- max_units_affected"""
CHANGE_OBJECT_STANCE = 36
"""Attributes for the **change_object_stance** effect are: \n
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- attack_stance
- selected_object_ids
- max_units_affected"""
DISPLAY_TIMER = 37
"""Attributes for the **display_timer** effect are: \n
- string_id
- display_time
- time_unit
- timer
- reset_timer
- message"""
ENABLE_DISABLE_OBJECT = 38
"""Attributes for the **enable_disable_object** effect are: \n
- object_list_unit_id
- source_player
- enabled"""
ENABLE_DISABLE_TECHNOLOGY = 39
"""Attributes for the **enable_disable_technology** effect are: \n
- source_player
- technology
- enabled"""
CHANGE_OBJECT_COST = 40
"""Attributes for the **change_object_cost** effect are: \n
- object_list_unit_id
- source_player
- resource_1
- resource_1_quantity
- resource_2
- resource_2_quantity
- resource_3
- resource_3_quantity"""
SET_PLAYER_VISIBILITY = 41
"""Attributes for the **set_player_visibility** effect are: \n
- source_player
- target_player
- visibility_state"""
CHANGE_OBJECT_ICON = 42
"""Attributes for the **change_object_icon** effect are: \n
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- object_list_unit_id_2
- selected_object_ids
- max_units_affected"""
REPLACE_OBJECT = 43
"""Attributes for the **replace_object** effect are: \n
- object_list_unit_id
- source_player
- target_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- object_list_unit_id_2
- selected_object_ids
- facet2
- max_units_affected"""
CHANGE_OBJECT_DESCRIPTION = 44
"""Attributes for the **change_object_description** effect are: \n
- object_list_unit_id
- source_player
- string_id
- message"""
CHANGE_PLAYER_NAME = 45
"""Attributes for the **change_player_name** effect are: \n
- source_player
- string_id
- message"""
CHANGE_TRAIN_LOCATION = 46
"""Attributes for the **change_train_location** effect are: \n
- object_list_unit_id
- source_player
- object_list_unit_id_2
- button_location"""
CHANGE_TECHNOLOGY_LOCATION = 47
"""Attributes for the **change_technology_location** effect are: \n
- source_player
- technology
- object_list_unit_id_2
- button_location"""
CHANGE_CIVILIZATION_NAME = 48
"""Attributes for the **change_civilization_name** effect are: \n
- source_player
- string_id
- message"""
CREATE_GARRISONED_OBJECT = 49
"""Attributes for the **create_garrisoned_object** effect are: \n
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_list_unit_id_2
- selected_object_ids
- max_units_affected
- disable_sound"""
ACKNOWLEDGE_AI_SIGNAL = 50
"""Attributes for the **acknowledge_ai_signal** effect are: \n
- ai_signal_value"""
MODIFY_ATTRIBUTE = 51
"""Attributes for the **modify_attribute** effect are: \n
- quantity
- quantity_float
- object_list_unit_id
- source_player
- operation
- object_attributes
- message"""
MODIFY_RESOURCE = 52
"""Attributes for the **modify_resource** effect are: \n
- quantity
- tribute_list
- source_player
- operation"""
MODIFY_RESOURCE_BY_VARIABLE = 53
"""Attributes for the **modify_resource_by_variable** effect are: \n
- tribute_list
- source_player
- operation
- variable"""
SET_BUILDING_GATHER_POINT = 54
"""Attributes for the **set_building_gather_point** effect are: \n
- object_list_unit_id
- source_player
- location_x
- location_y
- area_x1
- area_y1
- area_x2
- area_y2
- selected_object_ids
- max_units_affected"""
SCRIPT_CALL = 55
"""Attributes for the **script_call** effect are: \n
- string_id
- message"""
CHANGE_VARIABLE = 56
"""Attributes for the **change_variable** effect are: \n
- quantity
- operation
- variable
- message"""
CLEAR_TIMER = 57
"""Attributes for the **clear_timer** effect are: \n
- timer"""
CHANGE_OBJECT_PLAYER_COLOR = 58
"""Attributes for the **change_object_player_color** effect are: \n
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- player_color
- selected_object_ids
- max_units_affected"""
CHANGE_OBJECT_CIVILIZATION_NAME = 59
"""Attributes for the **change_object_civilization_name** effect are: \n
- string_id
- area_x1
- area_y1
- area_x2
- area_y2
- selected_object_ids
- max_units_affected"""
CHANGE_OBJECT_PLAYER_NAME = 60
"""Attributes for the **change_object_player_name** effect are: \n
- object_list_unit_id
- source_player
- string_id
- area_x1
- area_y1
- area_x2
- area_y2
- max_units_affected
- selected_object_ids"""
DISABLE_UNIT_TARGETING = 61
"""Attributes for the **disable_unit_targeting** effect are: \n
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- selected_object_ids
- max_units_affected"""
ENABLE_UNIT_TARGETING = 62
"""Attributes for the **enable_unit_targeting** effect are: \n
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- selected_object_ids
- max_units_affected"""
CHANGE_TECHNOLOGY_COST = 63
"""Attributes for the **change_technology_cost** effect are: \n
- source_player
- technology
- resource_1
- resource_1_quantity
- resource_2
- resource_2_quantity
- resource_3
- resource_3_quantity"""
CHANGE_TECHNOLOGY_RESEARCH_TIME = 64
"""Attributes for the **change_technology_research_time** effect are: \n
- quantity
- source_player
- technology"""
CHANGE_TECHNOLOGY_NAME = 65
"""Attributes for the **change_technology_name** effect are: \n
- source_player
- technology
- string_id
- message"""
CHANGE_TECHNOLOGY_DESCRIPTION = 66
"""Attributes for the **change_technology_description** effect are: \n
- source_player
- technology
- string_id
- message"""
ENABLE_TECHNOLOGY_STACKING = 67
"""Attributes for the **enable_technology_stacking** effect are: \n
- source_player
- technology"""
DISABLE_TECHNOLOGY_STACKING = 68
"""Attributes for the **disable_technology_stacking** effect are: \n
- source_player
- technology"""
ACKNOWLEDGE_MULTIPLAYER_AI_SIGNAL = 69
"""Attributes for the **acknowledge_multiplayer_ai_signal** effect are: \n
- ai_signal_value
"""
DISABLE_OBJECT_SELECTION = 70
"""Attributes for the **disable_object_selection** effect are: \n
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- selected_object_ids
- max_units_affected"""
ENABLE_OBJECT_SELECTION = 71
"""Attributes for the **enable_object_selection** effect are: \n
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- selected_object_ids
- max_units_affected"""
CHANGE_COLOR_MOOD = 72
"""Attributes for the **change_color_mood** effect are: \n
- quantity
- color_mood

This effect was added in: 1.42
"""
ENABLE_OBJECT_DELETION = 73
"""Attributes for the **enable_object_deletion** effect are: \n
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- selected_object_ids
- max_units_affected

This effect was added in: 1.46
"""
DISABLE_OBJECT_DELETION = 74
"""Attributes for the **disable_object_deletion** effect are: \n
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- selected_object_ids
- max_units_affected

This effect was added in: 1.46
"""
TRAIN_UNIT = 75
"""Attributes for the **train_unit** effect are: \n
- quantity
- object_list_unit_id
- source_player
- location_x
- location_y
- area_x1
- area_y1
- area_x2
- area_y2
- selected_object_ids
- max_units_affected

This effect was added in: 1.51 & Trigger Version 3.5
"""
INITIATE_RESEARCH = 76
"""Attributes for the **initiate_research** effect are: \n
- source_player
- technology
- selected_object_ids

This effect was added in: 1.51 & Trigger Version 3.5
"""
CREATE_OBJECT_ATTACK = 77
"""Attributes for the **create_object_attack** effect are: \n
- armour_attack_quantity
- armour_attack_class
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- operation
- selected_object_ids
- max_units_affected

This effect was added in: 1.51 & Trigger Version 3.5
"""
CREATE_OBJECT_ARMOR = 78
"""Attributes for the **create_object_armor** effect are: \n
- armour_attack_quantity
- armour_attack_class
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- operation
- selected_object_ids
- max_units_affected

This effect was added in: 1.51 & Trigger Version 3.5
"""
MODIFY_ATTRIBUTE_BY_VARIABLE = 79
"""Attributes for the **modify_attribute_by_variable** effect are: \n
- object_list_unit_id
- source_player
- operation
- object_attributes
- variable
- message
- armour_attack_class

This effect was added in: 1.51 & Trigger Version 3.5
"""
SET_OBJECT_COST = 80
"""Attributes for the **set_object_cost** effect are: \n
- object_list_unit_id
- source_player
- quantity
- tribute_list

This effect was added in: 1.54 & Trigger Version 3.9
"""
LOAD_KEY_VALUE = 81
"""Attributes for the **load_key_value** effect are: \n
- variable
- message
- quantity

This effect was added in: 1.54 & Trigger Version 3.9
"""
STORE_KEY_VALUE = 82
"""Attributes for the **store_key_value** effect are: \n
- variable
- message

This effect was added in: 1.54 & Trigger Version 3.9
"""
DELETE_KEY = 83
"""Attributes for the **delete_key** effect are: \n
- message

This effect was added in: 1.54 & Trigger Version 3.9
"""
CHANGE_TECHNOLOGY_ICON = 84
"""Attributes for the **change_technology_icon** effect are: \n
- technology
- source_player
- quantity

This effect was added in: 1.54 & Trigger Version 3.9
"""
CHANGE_TECHNOLOGY_HOTKEY = 85
"""Attributes for the **change_technology_hotkey** effect are: \n
- technology
- source_player
- quantity

This effect was added in: 1.54 & Trigger Version 3.9
"""
MODIFY_VARIABLE_BY_RESOURCE = 86
"""Attributes for the **modify_variable_by_resource** effect are: \n
- tribute_list
- source_player
- operation
- variable

This effect was added in: 1.54 & Trigger Version 3.9
"""
MODIFY_VARIABLE_BY_ATTRIBUTE = 87
"""Attributes for the **modify_variable_by_attribute** effect are: \n
- object_list_unit_id
- source_player
- operation
- object_attributes
- variable
- message
- armour_attack_class

This effect was added in: 1.54 & Trigger Version 3.9
"""
CHANGE_OBJECT_CAPTION = 88
"""Attributes for the **change_object_caption** effect are: \n
- object_list_unit_id
- source_player
- string_id
- message
- selected_object_ids
- area_x1
- area_y1
- area_x2
- area_y2

This effect was added in: 1.54 & Trigger Version 3.9
"""
CHANGE_PLAYER_COLOR = 89
"""Attributes for the **change_player_color** effect are: \n
- source_player
- player_color

This effect was added in: 1.54 & Trigger Version 3.9
"""
CREATE_DECISION = 90
"""Attributes for the **create_decision** effect are: \n
- string_id
- decision_id
- string_id_option1
- string_id_option2
- message
- message_option1
- message_option2

This effect was added in: 1.54 & Trigger Version 4.1
"""
DISABLE_UNIT_ATTACKABLE = 98
"""Attributes for the **disable_unit_attackable** effect are: \n
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- selected_object_ids
- max_units_affected

This effect was added in: 1.54 & Trigger Version 4.1
"""
ENABLE_UNIT_ATTACKABLE = 99
"""Attributes for the **enable_unit_attackable** effect are: \n
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- selected_object_ids
- max_units_affected

This effect was added in: 1.54 & Trigger Version 4.1
"""
MODIFY_VARIABLE_BY_VARIABLE = 100
"""Attributes for the **modify_variable_by_variable** effect are: \n
- operation
- variable
- variable2

This effect was added in: 1.54 & Trigger Version 4.1
"""
COUNT_UNITS_INTO_VARIABLE = 101
"""Attributes for the **count_units_into_variable** effect are: \n
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- variable2  // Why FE?! Why the 2nd!?

This effect was added in: 1.54 & Trigger Version 4.1
"""
ADD_TRAIN_LOCATION = 102
"""Attributes for the **add_train_location** effect are: \n
- object_list_unit_id
- source_player
- object_list_unit_id_2
- button_location
- train_time
- hotkey

This effect was added in: 1.55 & Trigger Version 4.5
"""
RESEARCH_LOCAL_TECHNOLOGY = 103
"""Attributes for the **research_local_technology** effect are: \n
- local_technology
- source_player
- selected_object_ids
- area_x1
- area_y1
- area_x2
- area_y2
- object_list_unit_id_2
    
This effect was added in: 1.55 & Trigger Version 4.5
"""
MODIFY_ATTRIBUTE_FOR_CLASS = 104
"""Attributes for the **modify_attribute_for_class** effect are: \n
- object_group2
- source_player
- object_attributes
- message
- operation
- quantity
- quantity_float
- armour_attack_class
    
This effect was added in: 1.55 & Trigger Version 4.5
"""
MODIFY_OBJECT_ATTRIBUTE = 105
"""Attributes for the **modify_object_attribute** effect are: \n
- object_list_unit_id
- source_player
- object_attributes
- selected_object_ids
- area_x1
- area_y1
- area_x2
- area_y2
- operation
- message
- quantity
- quantity_float
- armour_attack_class
- object_filter

This effect was added in: 1.55 & Trigger Version 4.5
"""
MODIFY_OBJECT_ATTRIBUTE_BY_VARIABLE = 106
"""Attributes for the **modify_object_attribute_by_variable** effect are: \n
- object_list_unit_id
- source_player
- object_attributes
- selected_object_ids
- area_x1
- area_y1
- area_x2
- area_y2
- operation
- message
- variable
- armour_attack_class
    
This effect was added in: 1.55 & Trigger Version 4.5
"""
CHANGE_OBJECT_VISIBILITY = 107
"""Attributes for the **change_object_visibility** effect are: \n
- source_player
- target_player
- area_x1
- area_y1
- area_x2
- area_y2
- visibility_state
- max_units_affected
- selected_object_ids
    
This effect was added in: 1.55 & Trigger Version 4.5
"""

BUILD_OBJECT = 108
"""Attributes for the **build_object** effect are: \n
- object_list_unit_id
- source_player
- location_x
- location_y
- location_object_reference
- area_x1
- area_y1
- area_x2
- area_y2
- wall_x1
- wall_y1
- wall_x2
- wall_y2
- object_group
- object_type
- building_list
- selected_object_ids
- disable_garrison_unload_sound
- max_units_affected
- issue_group_command
- queue_action

This effect was added in: 1.57 & Trigger Version 4.6
"""
MIRROR_DIPLOMACY = 109
"""Attributes for the **mirror_diplomacy** effect are: \n
- source_player
- target_player
- enabled

This effect was added in: 1.57 & Trigger Version 4.6
"""




# resource 
resource_names = [
    "!Food Storage",
    "!Wood Storage",
    "!Stone Storage",
    "!Gold Storage",
    "Population Headroom",
    "Conversion Range",
    "Current Age",
    "Relics Captured",
    "Unused Resource 08",
    "Trade Goods",
    "Unused Resource 10",
    "Current Population",
    "Corpse Decay Time",
    "Remarkable Discovery",
    "Monuments Captured",
    "Meat Storage",
    "Berry Storage",
    "Fish Storage",
    "Civilization Voice Override",
    "Total Units Owned",
    "Units Killed",
    "Technology Count",
    "% Map Explored",
    "Castle Age Tech ID",
    "Imperial Age Tech ID",
    "Feudal Age Tech ID",
    "Attack Warning Sound ID",
    "Enable Monk Conversion",
    "Enable Building Conversion",
    "Enable Siege Conversion",
    "Unused Resource 030",
    "Unused Resource 031",
    "Population Cap",
    "Effect Function Number",
    "Unused Resource 034",
    "Unused Resource 035",
    "Farm Food Amount",
    "Civilian Population",
    "Villager Population",
    "All Techs Achieved",
    "Military Population",
    "Conversions",
    "Standing Wonders",
    "Razings",
    "Kill Ratio",
    "Survival to Finish",
    "Tribute Inefficiency",
    "Gold Mining Productivity",
    "Town Center Unavailable",
    "Gold Counter",
    "Reveal Ally",
    "Unused Resource 051",
    "Monasteries",
    "Tribute Sent",
    "All Monuments Captured",
    "All Relics Captured",
    "Ore Storage",
    "Kidnap Storage",
    "Dark Age Tech ID",
    "Unused Resource 059",
    "Unused Resource 060",
    "Unused Resource 061",
    "Building Housing Rate",
    "Tax Gather Rate",
    "Gather Accumulator",
    "Salvage Decay Rate",
    "Unused Resource 066",
    "Can Convert",
    "Hit Points Killed",
    "Farm Food Multiplier",
    "Source Market or Dock X Coordinate",
    "Source Market or Dock Y Coordinate",
    "Unused Resource 72",
    "Waypoint Sprite Graphic ID",
    "Unused Resource 074",
    "Unused Resource 075",
    "Unused Resource 076",
    "Conversion Resistance",
    "Trade Vig Rate",
    "Stone Mining Productivity",
    "Queued Units",
    "Training Count",
    "Start with Unit 444 (PTWC)",
    "Unused Resource 083",
    "Starting Villagers",
    "Research Cost Modifier",
    "Research Time Modifier",
    "Convert Boats",
    "Fish Trap Food Amount",
    "Heal Rate Modifier",
    "Healing Range",
    "Starting Food",
    "Starting Wood",
    "Starting Stone",
    "Starting Gold",
    "Enable PTWC / Kidnap / Loot",
    "No Dropsite Farmers",
    "Dominant Sheep Control",
    "Building Cost Sum",
    "Tech Cost Sum",
    "Relic Income Sum",
    "Trade Income Sum",
    "Naval Trade Wood",
    "Unused Resource 103",
    "Unused Resource 104",
    "Unused Resource 105",
    "Unused Resource 106",
    "Unused Resource 107",
    "Unused Resource 108",
    "Unused Resource 109",
    "Unused Resource 110",
    "Unused Resource 111",
    "Unused Resource 112",
    "Unused Resource 113",
    "Unused Resource 114",
    "Unused Resource 115",
    "Unused Resource 116",
    "Unused Resource 117",
    "Unused Resource 118",
    "Unused Resource 119",
    "Unused Resource 120",
    "Unused Resource 121",
    "Unused Resource 122",
    "Unused Resource 123",
    "Unused Resource 124",
    "Unused Resource 125",
    "Unused Resource 126",
    "Unused Resource 127",
    "Unused Resource 128",
    "Unused Resource 129",
    "Unused Resource 130",
    "Unused Resource 131",
    "Unused Resource 132",
    "Unused Resource 133",
    "Standing Castles",
    "Hit Points Razed",
    "Unused Resource 136",
    "Unused Resource 137",
    "Unused Resource 138",
    "Unused Resource 139",
    "Unused Resource 140",
    "Unused Resource 141",
    "Unused Resource 142",
    "Unused Resource 143",
    "Unused Resource 144",
    "Unused Resource 145",
    "Unused Resource 146",
    "Unused Resource 147",
    "Unused Resource 148",
    "Unused Resource 149",
    "Unused Resource 150",
    "Unused Resource 151",
    "Value Killed by Others",
    "Value Razed by Others",
    "Killed by Others",
    "Razed by Others",
    "Unused Resource 156",
    "Unused Resource 157",
    "Unused Resource 158",
    "Unused Resource 159",
    "Unused Resource 160",
    "Unused Resource 161",
    "Unused Resource 162",
    "Unused Resource 163",
    "Value Current Units",
    "Value Current Buildings",
    "Food Total",
    "Wood Total",
    "Stone Total",
    "Gold Total",
    "Total Value of Kills",
    "Total Tribute Received",
    "Total Value of Razings",
    "Total Castles Built",
    "Total Wonders Built",
    "Tribute score",
    "Convert Min Adjustment",
    "Convert Max Adjustment",
    "Convert Resist Min Adjustment",
    "Convert Resist Max Adjustment",
    "Convert Building Min",
    "Convert Building Max",
    "Convert Building Chance",
    "Reveal Enemy",
    "Value Wonders Castles",
    "Food Score",
    "Wood Score",
    "Stone Score",
    "Gold Score",
    "Chopping Productivity",
    "Food Gathering Productivity",
    "Relic Gold Production Rate",
    "Converted Units Die",
    "Theocracy",
    "Unused Resource 194",
    "Construction Rate Modifier",
    "Wonder Timer Modifier",
    "Spies Discount",
    "Relic Timer Modifier",
    "Unused Resource 199",
    "Unused Resource 200",
    "Unused Resource 201",
    "Unused Resource 202",
    "Map Reveal",
    "Unit Reveal",
    "Feitoria Food Productivity",
    "Feitoria Wood Productivity",
    "Feitoria Stone Productivity",
    "Feitoria Gold Productivity",
    "Reveal Enemy Town Centers",
    "Relics Visible on Map",
    "Elevation Higher Bonus",
    "Elevation Lower Bonus",
    "Raiding Productivity",
    "Mercenary Kipchak Count",
    "Bonus Forager Food",
    "Shepherd Productivity",
    "Shared Line of Sight",
    "Early Town Center Limit",
    "Fishing Productivity",
    "Unused Resource 220",
    "Monument Food Productivity",
    "Monument Wood Productivity",
    "Monument Stone Productivity",
    "Monument Gold Productivity",
    "Relic Food Production Rate",
    "Villagers Killed by Gaia",
    "Villagers Killed by Animals",
    "Villagers Killed by AI Player",
    "Villagers Killed by Human Player",
    "Food Generation Rate",
    "Wood Generation Rate",
    "Stone Generation Rate",
    "Gold Generation Rate",
    "Spawn Limit",
    "Flemish Militia Population",
    "Farming Gold Productivity",
    "Folwark Collection Amount",
    "Folwark Attribute Type",
    "Folwark Building Type",
    "Units Converted",
    "Stone Mining Gold Productivity",
    "Trade Workshop Food Productivity",
    "Trade Workshop Wood Productivity",
    "Trade Workshop Stone Productivity",
    "Trade Workshop Gold Productivity",
    "Units Value Total",
    "Buildings Value Total",
    "Villagers Created Total",
    "Villagers Idle Periods Total",
    "Villagers Idle Seconds Total",
    "Trade Food Percent",
    "Trade Wood Percent",
    "Trade Stone Percent",
    "Livestock Food Productivity",
    "Unused Resource 255",
    "Unused Resource 256",
    "Unused Resource 257",
    "Unused Resource 258",
    "Unused Resource 259",
    "Unused Resource 260",
    "Unused Resource 261",
    "Civilization Name Override",
    "Starting Scout ID",
    "Relic Wood Production Rate",
    "Relic Stone Production Rate",
    "Chopping Gold Productivity",
    "Foraging Wood Productivity",
    "Hunter Productivity",
    "Technology Reward Effect",
    "Unit Repair Cost",
    "Building Repair Cost",
    "Elevation Higher Damage",
    "Elevation Lower Damage",
    "Infantry Kill Reward",
    "Fyrd Discount Level",
    "Bonus Gold Productivity",
    "Red Cliffs Tactics Damage",
    "Razing Bounty",
    "Military Can Convert",
    "Military Convert Range",
    "Military Convert Chance",
    "Military Convert Recharge",
    "Spawn Inside",
    "Cavalry Kill Reward",
    "Shared Visibility",
    "Shared Exploration",
    "Military Food Productivity",
    "Pasture Food Amount",
    "Pasture Animal Count",
    "Pasture Herder Count",
    "Razing Pillage",
    "Animal Decay Prevention",
    "Herder Food Productivity",
    "Shepherd Food Productivity",
    "Unit Refund",
    "Forager Productivity",
    "Varangian Gold Generation",
    "Butcher Gold Productivity",
    "Bonus Food Productivity",
    "Killed Gaia",
    "Killed P1",
    "Killed P2",
    "Killed P3",
    "Killed P4",
    "Killed P5",
    "Killed P6",
    "Killed P7",
    "Killed P8",
    "Unused Resource 309",
    "Unused Resource 310",
    "Unused Resource 311",
    "Unused Resource 312",
    "Unused Resource 313",
    "Unused Resource 314",
    "Unused Resource 315",
    "Unused Resource 316",
    "Unused Resource 317",
    "Unused Resource 318",
    "Unused Resource 319",
    "Unused Resource 320",
    "Unused Resource 321",
    "Unused Resource 322",
    "Unused Resource 323",
    "Unused Resource 324",
    "Kills by Gaia",
    "Kills by P1",
    "Kills by P2",
    "Kills by P3",
    "Kills by P4",
    "Kills by P5",
    "Kills by P6",
    "Kills by P7",
    "Kills by P8",
    "Unused Resource 334",
    "Unused Resource 335",
    "Unused Resource 336",
    "Unused Resource 337",
    "Unused Resource 338",
    "Unused Resource 339",
    "Unused Resource 340",
    "Unused Resource 341",
    "Unused Resource 342",
    "Unused Resource 343",
    "Unused Resource 344",
    "Unused Resource 345",
    "Unused Resource 346",
    "Unused Resource 347",
    "Unused Resource 348",
    "Unused Resource 349",
    "Gaia Razings",
    "P1 Razings",
    "P2 Razings",
    "P3 Razings",
    "P4 Razings",
    "P5 Razings",
    "P6 Razings",
    "P7 Razings",
    "P8 Razings",
    "Unused Resource 359",
    "Unused Resource 360",
    "Unused Resource 361",
    "Unused Resource 362",
    "Unused Resource 363",
    "Unused Resource 364",
    "Unused Resource 365",
    "Unused Resource 366",
    "Unused Resource 367",
    "Unused Resource 368",
    "Unused Resource 369",
    "Unused Resource 370",
    "Unused Resource 371",
    "Unused Resource 372",
    "Unused Resource 373",
    "Unused Resource 374",
    "Razings by Gaia",
    "Razings by P1",
    "Razings by P2",
    "Razings by P3",
    "Razings by P4",
    "Razings by P5",
    "Razings by P6",
    "Razings by P7",
    "Razings by P8",
    "Unused Resource 384",
    "Unused Resource 385",
    "Unused Resource 386",
    "Unused Resource 387",
    "Unused Resource 388",
    "Unused Resource 389",
    "Unused Resource 390",
    "Unused Resource 391",
    "Unused Resource 392",
    "Unused Resource 393",
    "Unused Resource 394",
    "Unused Resource 395",
    "Unused Resource 396",
    "Unused Resource 397",
    "Unused Resource 398",
    "Unused Resource 399",
    "Gaia Kill Value",
    "P1 Kill Value",
    "P2 Kill Value",
    "P3 Kill Value",
    "P4 Kill Value",
    "P5 Kill Value",
    "P6 Kill Value",
    "P7 Kill Value",
    "P8 Kill Value",
    "Unused Resource 409",
    "Unused Resource 410",
    "Unused Resource 411",
    "Unused Resource 412",
    "Unused Resource 413",
    "Unused Resource 414",
    "Unused Resource 415",
    "Unused Resource 416",
    "Unused Resource 417",
    "Unused Resource 418",
    "Unused Resource 419",
    "Unused Resource 420",
    "Unused Resource 421",
    "Unused Resource 422",
    "Unused Resource 423",
    "Unused Resource 424",
    "Gaia Razing Value",
    "P1 Razing Value",
    "P2 Razing Value",
    "P3 Razing Value",
    "P4 Razing Value",
    "P5 Razing Value",
    "P6 Razing Value",
    "P7 Razing Value",
    "P8 Razing Value",
    "Unused Resource 434",
    "Unused Resource 435",
    "Unused Resource 436",
    "Unused Resource 437",
    "Unused Resource 438",
    "Unused Resource 439",
    "Unused Resource 440",
    "Unused Resource 441",
    "Unused Resource 442",
    "Unused Resource 443",
    "Unused Resource 444",
    "Unused Resource 445",
    "Unused Resource 446",
    "Unused Resource 447",
    "Unused Resource 448",
    "Unused Resource 449",
    "Gaia Tribute",
    "P1 Tribute",
    "P2 Tribute",
    "P3 Tribute",
    "P4 Tribute",
    "P5 Tribute",
    "P6 Tribute",
    "P7 Tribute",
    "P8 Tribute",
    "Unused Resource 459",
    "Unused Resource 460",
    "Unused Resource 461",
    "Unused Resource 462",
    "Unused Resource 463",
    "Unused Resource 464",
    "Unused Resource 465",
    "Unused Resource 466",
    "Unused Resource 467",
    "Unused Resource 468",
    "Unused Resource 469",
    "Unused Resource 470",
    "Unused Resource 471",
    "Unused Resource 472",
    "Unused Resource 473",
    "Unused Resource 474",
    "Tribute from Gaia",
    "Tribute from P1",
    "Tribute from P2",
    "Tribute from P3",
    "Tribute from P4",
    "Tribute from P5",
    "Tribute from P6",
    "Tribute from P7",
    "Tribute from P8",
    "Unused Resource 484",
    "Unused Resource 485",
    "Unused Resource 486",
    "Unused Resource 487",
    "Unused Resource 488",
    "Unused Resource 489",
    "Unused Resource 490",
    "Unused Resource 491",
    "Unused Resource 492",
    "Unused Resource 493",
    "Unused Resource 494",
    "Unused Resource 495",
    "Unused Resource 496",
    "Unused Resource 497",
    "Unused Resource 498",
    "Unused Resource 499",
    "Unused Resource 500",
    "Polemarch Build Limit",
    "Athenian Chopping Food Productivity",
    "Wood Trade Ratio",
    "Unused Resource 504",
    "Unused Resource 505",
    "Achaemenid Town Center Local Upgrade",
    "Unused Resource 507",
    "Fortified Outpost Local Upgrade",
    "Mercenary Hoplite Productivity",
    "Odomantian Raiders Productivity",
    "Dii Plunderers Productivity",
    "Stone Mining Food Productivity",
    "Emplacement Local Upgrade",
    "Helepolis Limit",
    "Scythian Horse Archer Productivity",
    "<!--RESERVED-->",
    "Unused Resource 517",
    "Unused Resource 518",
    "Unused Resource 519",
    "Lysanders Raider Productivity",
    "Peloponnesian League Productivity",
    "Base Hoplite Aura Enabled",
    "Agoge Hoplite Aura Enabled",
    "Xyphos Hoplite Aura Enabled",
    "Base Strategos Aura Enabled",
    "Taxiarchs Strategos Aura Enabled",
    "Hippeus Aura No Tech",
    "Hippeus Aura With Techs",
    "Unused Resource 529",
    "Unused Resource 530",
    "Scenario Resource 01",
    "Scenario Resource 02",
    "Scenario Resource 03",
    "Scenario Resource 04",
    "Scenario Resource 05",
    "Scenario Resource 06",
    "Scenario Resource 07",
    "Scenario Resource 08",
    "Scenario Resource 09",
    "Scenario Resource 10",
    "Scenario Resource 11",
    "Scenario Resource 12",
    "Scenario Resource 13",
    "Scenario Resource 14",
    "Scenario Resource 15",
    "Scenario Resource 16",
    "Scenario Resource 17",
    "Unused Resource 548",
    "Unused Resource 549",
    "Camel Raider Productivity",
    "Tyranny Productivity",
    "null",
    "null",
    "Unused Resource 554",
    "Unused Resource 555",
    "Unused Resource 556",
    "Unused Resource 557",
    "Unused Resource 558",
    "Unused Resource 559",
    "Ends of the World Productivity",
    "Pattiyodha Longbowman Default",
    "Pattiyodha Longbowman Upgraded",
    "Shepherd Gold Productivity",
    "Unused Resource 564",
    "Unused Resource 565",
    "Unused Resource 566",
    "Unused Resource 567",
    "Unused Resource 568",
    "Unused Resource 569",
    "Unused Resource 570",
    "Unused Resource 571",
    "Unused Resource 572",
    "Unused Resource 573",
    "Unused Resource 574",
    "Unused Resource 575",
    "Unused Resource 576",
    "Unused Resource 577",
    "Unused Resource 578",
    "Unused Resource 579",
    "Unused Resource 580",
    "Unused Resource 581",
    "Unused Resource 582",
    "Unused Resource 583",
    "Unused Resource 584",
    "Unused Resource 585",
    "Unused Resource 586",
    "Unused Resource 587",
    "Unused Resource 588",
    "Unused Resource 589",
    "Unused Resource 590",
    "Unused Resource 591",
    "Unused Resource 592",
    "Unused Resource 593",
    "Unused Resource 594",
    "Unused Resource 595",
    "Unused Resource 596",
    "Unused Resource 597",
    "Unused Resource 598",
    "Unused Resource 599",
    "Unused Resource 600"
]

RESOURCE_IDS = {
    name: idx
    for idx, name in enumerate(resource_names)
    if name is not None
}



"""
This enum class provides the integer values used to reference the effects in the game. Used in every effect to
indicate which type of effect it is

**Examples**

>>> EffectId.RESEARCH_TECHNOLOGY
>>> 2
"""
NONE = 0
"""Attributes for the **none** effect are: \n
... none... Just like Conditions... People these days... """
CHANGE_DIPLOMACY = 1
"""Attributes for the **change_diplomacy** effect are: \n
- diplomacy
- source_player
- target_player"""
RESEARCH_TECHNOLOGY = 2
"""Attributes for the **research_technology** effect are: \n
- source_player
- technology
- force_research_technology"""
SEND_CHAT = 3
"""Attributes for the **send_chat** effect are: \n
- source_player
- string_id
- message
- sound_name"""
PLAY_SOUND = 4
"""Attributes for the **play_sound** effect are: \n
- source_player
- location_x
- location_y
- location_object_reference
- global_sound
- sound_name"""
TRIBUTE = 5
"""Attributes for the **tribute** effect are: \n
- quantity
- tribute_list
- source_player
- target_player"""
UNLOCK_GATE = 6
"""Attributes for the **unlock_gate** effect are: \n
- selected_object_ids"""
LOCK_GATE = 7
"""Attributes for the **lock_gate** effect are: \n
- selected_object_ids"""
ACTIVATE_TRIGGER = 8
"""Attributes for the **activate_trigger** effect are: \n
- trigger_id"""
DEACTIVATE_TRIGGER = 9
"""Attributes for the **deactivate_trigger** effect are: \n
- trigger_id"""
AI_SCRIPT_GOAL = 10
"""Attributes for the **deactivate_trigger** effect are: \n
- ai_script_goal"""
CREATE_OBJECT = 11
"""Attributes for the **create_object** effect are: \n
- object_list_unit_id
- source_player
- location_x
- location_y
- facet
- disable_sound"""
TASK_OBJECT = 12
"""Attributes for the **task_object** effect are: \n
- object_list_unit_id
- source_player
- location_x
- location_y
- location_object_reference
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- action_type
- selected_object_ids
- disable_garrison_unload_sound
- max_units_affected
- issue_group_command
- queue_action"""
DECLARE_VICTORY = 13
"""Attributes for the **declare_victory** effect are: \n
- source_player
- enabled"""
KILL_OBJECT = 14
"""Attributes for the **kill_object** effect are: \n
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- selected_object_ids
- max_units_affected"""
REMOVE_OBJECT = 15
"""Attributes for the **remove_object** effect are: \n
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- object_state
- selected_object_ids
- max_units_affected"""
CHANGE_VIEW = 16
"""Attributes for the **change_view** effect are: \n
- quantity
- source_player
- location_x
- location_y
- scroll"""
UNLOAD = 17
"""Attributes for the **unload** effect are: \n
- object_list_unit_id
- source_player
- location_x
- location_y
- location_object_reference
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- selected_object_ids
- max_units_affected"""
CHANGE_OWNERSHIP = 18
"""Attributes for the **change_ownership** effect are: \n
- object_list_unit_id
- source_player
- target_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- flash_object
- selected_object_ids
- max_units_affected"""
PATROL = 19
"""Attributes for the **patrol** effect are: \n
- object_list_unit_id
- source_player
- location_x
- location_y
- location_object_reference
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- selected_object_ids
- max_units_affected"""
DISPLAY_INSTRUCTIONS = 20
"""Attributes for the **display_instructions** effect are: \n
- object_list_unit_id
- source_player
- string_id
- display_time
- instruction_panel_position
- play_sound
- message
- sound_name
- use_tag_color_for_icon"""
CLEAR_INSTRUCTIONS = 21
"""Attributes for the **clear_instructions** effect are: \n
- instruction_panel_position"""
FREEZE_OBJECT = 22
"""Attributes for the **freeze_object** effect are: \n
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- selected_object_ids
- max_units_affected"""
USE_ADVANCED_BUTTONS = 23
"""Attributes for the **use_advanced_buttons** effect are: \n
None. \n
Please don't use this effect. Please."""
DAMAGE_OBJECT = 24
"""Attributes for the **damage_object** effect are: \n
- quantity
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- selected_object_ids
- max_units_affected"""
PLACE_FOUNDATION = 25
"""Attributes for the **place_foundation** effect are: \n
- object_list_unit_id
- source_player
- location_x
- location_y"""
CHANGE_OBJECT_NAME = 26
"""Attributes for the **change_object_name** effect are: \n
- object_list_unit_id
- source_player
- string_id
- area_x1
- area_y1
- area_x2
- area_y2
- message
- selected_object_ids
- max_units_affected"""
CHANGE_OBJECT_HP = 27
"""Attributes for the **change_object_hp** effect are: \n
- quantity
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- operation
- selected_object_ids
- max_units_affected"""
CHANGE_OBJECT_ATTACK = 28
"""Attributes for the **change_object_attack** effect are: \n
- armour_attack_quantity
- armour_attack_class
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- operation
- selected_object_ids
- max_units_affected"""
STOP_OBJECT = 29
"""Attributes for the **stop_object** effect are: \n
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- selected_object_ids
- max_units_affected"""
ATTACK_MOVE = 30
"""Attributes for the **attack_move** effect are: \n
- object_list_unit_id
- source_player
- location_x
- location_y
- location_object_reference
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- selected_object_ids
- max_units_affected"""
CHANGE_OBJECT_ARMOR = 31
"""Attributes for the **change_object_armor** effect are: \n
- armour_attack_quantity
- armour_attack_class
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- operation
- selected_object_ids
- max_units_affected"""
CHANGE_OBJECT_RANGE = 32
"""Attributes for the **change_object_range** effect are: \n
- quantity
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- operation
- selected_object_ids
- max_units_affected"""
CHANGE_OBJECT_SPEED = 33
"""Attributes for the **change_object_speed** effect are: \n
- quantity
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- selected_object_ids
- max_units_affected"""
HEAL_OBJECT = 34
"""Attributes for the **heal_object** effect are: \n
- quantity
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- selected_object_ids
- max_units_affected"""
TELEPORT_OBJECT = 35
"""Attributes for the **teleport_object** effect are: \n
- object_list_unit_id
- source_player
- location_x
- location_y
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- selected_object_ids
- max_units_affected"""
CHANGE_OBJECT_STANCE = 36
"""Attributes for the **change_object_stance** effect are: \n
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- attack_stance
- selected_object_ids
- max_units_affected"""
DISPLAY_TIMER = 37
"""Attributes for the **display_timer** effect are: \n
- string_id
- display_time
- time_unit
- timer
- reset_timer
- message"""
ENABLE_DISABLE_OBJECT = 38
"""Attributes for the **enable_disable_object** effect are: \n
- object_list_unit_id
- source_player
- enabled"""
ENABLE_DISABLE_TECHNOLOGY = 39
"""Attributes for the **enable_disable_technology** effect are: \n
- source_player
- technology
- enabled"""
CHANGE_OBJECT_COST = 40
"""Attributes for the **change_object_cost** effect are: \n
- object_list_unit_id
- source_player
- resource_1
- resource_1_quantity
- resource_2
- resource_2_quantity
- resource_3
- resource_3_quantity"""
SET_PLAYER_VISIBILITY = 41
"""Attributes for the **set_player_visibility** effect are: \n
- source_player
- target_player
- visibility_state"""
CHANGE_OBJECT_ICON = 42
"""Attributes for the **change_object_icon** effect are: \n
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- object_list_unit_id_2
- selected_object_ids
- max_units_affected"""
REPLACE_OBJECT = 43
"""Attributes for the **replace_object** effect are: \n
- object_list_unit_id
- source_player
- target_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- object_list_unit_id_2
- selected_object_ids
- facet2
- max_units_affected"""
CHANGE_OBJECT_DESCRIPTION = 44
"""Attributes for the **change_object_description** effect are: \n
- object_list_unit_id
- source_player
- string_id
- message"""
CHANGE_PLAYER_NAME = 45
"""Attributes for the **change_player_name** effect are: \n
- source_player
- string_id
- message"""
CHANGE_TRAIN_LOCATION = 46
"""Attributes for the **change_train_location** effect are: \n
- object_list_unit_id
- source_player
- object_list_unit_id_2
- button_location"""
CHANGE_TECHNOLOGY_LOCATION = 47
"""Attributes for the **change_technology_location** effect are: \n
- source_player
- technology
- object_list_unit_id_2
- button_location"""
CHANGE_CIVILIZATION_NAME = 48
"""Attributes for the **change_civilization_name** effect are: \n
- source_player
- string_id
- message"""
CREATE_GARRISONED_OBJECT = 49
"""Attributes for the **create_garrisoned_object** effect are: \n
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_list_unit_id_2
- selected_object_ids
- max_units_affected
- disable_sound"""
ACKNOWLEDGE_AI_SIGNAL = 50
"""Attributes for the **acknowledge_ai_signal** effect are: \n
- ai_signal_value"""
MODIFY_ATTRIBUTE = 51
"""Attributes for the **modify_attribute** effect are: \n
- quantity
- quantity_float
- object_list_unit_id
- source_player
- operation
- object_attributes
- message"""
MODIFY_RESOURCE = 52
"""Attributes for the **modify_resource** effect are: \n
- quantity
- tribute_list
- source_player
- operation"""
MODIFY_RESOURCE_BY_VARIABLE = 53
"""Attributes for the **modify_resource_by_variable** effect are: \n
- tribute_list
- source_player
- operation
- variable"""
SET_BUILDING_GATHER_POINT = 54
"""Attributes for the **set_building_gather_point** effect are: \n
- object_list_unit_id
- source_player
- location_x
- location_y
- area_x1
- area_y1
- area_x2
- area_y2
- selected_object_ids
- max_units_affected"""
SCRIPT_CALL = 55
"""Attributes for the **script_call** effect are: \n
- string_id
- message"""
CHANGE_VARIABLE = 56
"""Attributes for the **change_variable** effect are: \n
- quantity
- operation
- variable
- message"""
CLEAR_TIMER = 57
"""Attributes for the **clear_timer** effect are: \n
- timer"""
CHANGE_OBJECT_PLAYER_COLOR = 58
"""Attributes for the **change_object_player_color** effect are: \n
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- player_color
- selected_object_ids
- max_units_affected"""
CHANGE_OBJECT_CIVILIZATION_NAME = 59
"""Attributes for the **change_object_civilization_name** effect are: \n
- string_id
- area_x1
- area_y1
- area_x2
- area_y2
- selected_object_ids
- max_units_affected"""
CHANGE_OBJECT_PLAYER_NAME = 60
"""Attributes for the **change_object_player_name** effect are: \n
- object_list_unit_id
- source_player
- string_id
- area_x1
- area_y1
- area_x2
- area_y2
- max_units_affected
- selected_object_ids"""
DISABLE_UNIT_TARGETING = 61
"""Attributes for the **disable_unit_targeting** effect are: \n
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- selected_object_ids
- max_units_affected"""
ENABLE_UNIT_TARGETING = 62
"""Attributes for the **enable_unit_targeting** effect are: \n
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- selected_object_ids
- max_units_affected"""
CHANGE_TECHNOLOGY_COST = 63
"""Attributes for the **change_technology_cost** effect are: \n
- source_player
- technology
- resource_1
- resource_1_quantity
- resource_2
- resource_2_quantity
- resource_3
- resource_3_quantity"""
CHANGE_TECHNOLOGY_RESEARCH_TIME = 64
"""Attributes for the **change_technology_research_time** effect are: \n
- quantity
- source_player
- technology"""
CHANGE_TECHNOLOGY_NAME = 65
"""Attributes for the **change_technology_name** effect are: \n
- source_player
- technology
- string_id
- message"""
CHANGE_TECHNOLOGY_DESCRIPTION = 66
"""Attributes for the **change_technology_description** effect are: \n
- source_player
- technology
- string_id
- message"""
ENABLE_TECHNOLOGY_STACKING = 67
"""Attributes for the **enable_technology_stacking** effect are: \n
- source_player
- technology"""
DISABLE_TECHNOLOGY_STACKING = 68
"""Attributes for the **disable_technology_stacking** effect are: \n
- source_player
- technology"""
ACKNOWLEDGE_MULTIPLAYER_AI_SIGNAL = 69
"""Attributes for the **acknowledge_multiplayer_ai_signal** effect are: \n
- ai_signal_value
"""
DISABLE_OBJECT_SELECTION = 70
"""Attributes for the **disable_object_selection** effect are: \n
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- selected_object_ids
- max_units_affected"""
ENABLE_OBJECT_SELECTION = 71
"""Attributes for the **enable_object_selection** effect are: \n
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- selected_object_ids
- max_units_affected"""
CHANGE_COLOR_MOOD = 72
"""Attributes for the **change_color_mood** effect are: \n
- quantity
- color_mood

This effect was added in: 1.42
"""
ENABLE_OBJECT_DELETION = 73
"""Attributes for the **enable_object_deletion** effect are: \n
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- selected_object_ids
- max_units_affected

This effect was added in: 1.46
"""
DISABLE_OBJECT_DELETION = 74
"""Attributes for the **disable_object_deletion** effect are: \n
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- selected_object_ids
- max_units_affected

This effect was added in: 1.46
"""
TRAIN_UNIT = 75
"""Attributes for the **train_unit** effect are: \n
- quantity
- object_list_unit_id
- source_player
- location_x
- location_y
- area_x1
- area_y1
- area_x2
- area_y2
- selected_object_ids
- max_units_affected

This effect was added in: 1.51 & Trigger Version 3.5
"""
INITIATE_RESEARCH = 76
"""Attributes for the **initiate_research** effect are: \n
- source_player
- technology
- selected_object_ids

This effect was added in: 1.51 & Trigger Version 3.5
"""
CREATE_OBJECT_ATTACK = 77
"""Attributes for the **create_object_attack** effect are: \n
- armour_attack_quantity
- armour_attack_class
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- operation
- selected_object_ids
- max_units_affected

This effect was added in: 1.51 & Trigger Version 3.5
"""
CREATE_OBJECT_ARMOR = 78
"""Attributes for the **create_object_armor** effect are: \n
- armour_attack_quantity
- armour_attack_class
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- object_type
- operation
- selected_object_ids
- max_units_affected

This effect was added in: 1.51 & Trigger Version 3.5
"""
MODIFY_ATTRIBUTE_BY_VARIABLE = 79
"""Attributes for the **modify_attribute_by_variable** effect are: \n
- object_list_unit_id
- source_player
- operation
- object_attributes
- variable
- message
- armour_attack_class

This effect was added in: 1.51 & Trigger Version 3.5
"""
SET_OBJECT_COST = 80
"""Attributes for the **set_object_cost** effect are: \n
- object_list_unit_id
- source_player
- quantity
- tribute_list

This effect was added in: 1.54 & Trigger Version 3.9
"""
LOAD_KEY_VALUE = 81
"""Attributes for the **load_key_value** effect are: \n
- variable
- message
- quantity

This effect was added in: 1.54 & Trigger Version 3.9
"""
STORE_KEY_VALUE = 82
"""Attributes for the **store_key_value** effect are: \n
- variable
- message

This effect was added in: 1.54 & Trigger Version 3.9
"""
DELETE_KEY = 83
"""Attributes for the **delete_key** effect are: \n
- message

This effect was added in: 1.54 & Trigger Version 3.9
"""
CHANGE_TECHNOLOGY_ICON = 84
"""Attributes for the **change_technology_icon** effect are: \n
- technology
- source_player
- quantity

This effect was added in: 1.54 & Trigger Version 3.9
"""
CHANGE_TECHNOLOGY_HOTKEY = 85
"""Attributes for the **change_technology_hotkey** effect are: \n
- technology
- source_player
- quantity

This effect was added in: 1.54 & Trigger Version 3.9
"""
MODIFY_VARIABLE_BY_RESOURCE = 86
"""Attributes for the **modify_variable_by_resource** effect are: \n
- tribute_list
- source_player
- operation
- variable

This effect was added in: 1.54 & Trigger Version 3.9
"""
MODIFY_VARIABLE_BY_ATTRIBUTE = 87
"""Attributes for the **modify_variable_by_attribute** effect are: \n
- object_list_unit_id
- source_player
- operation
- object_attributes
- variable
- message
- armour_attack_class

This effect was added in: 1.54 & Trigger Version 3.9
"""
CHANGE_OBJECT_CAPTION = 88
"""Attributes for the **change_object_caption** effect are: \n
- object_list_unit_id
- source_player
- string_id
- message
- selected_object_ids
- area_x1
- area_y1
- area_x2
- area_y2

This effect was added in: 1.54 & Trigger Version 3.9
"""
CHANGE_PLAYER_COLOR = 89
"""Attributes for the **change_player_color** effect are: \n
- source_player
- player_color

This effect was added in: 1.54 & Trigger Version 3.9
"""
CREATE_DECISION = 90
"""Attributes for the **create_decision** effect are: \n
- string_id
- decision_id
- string_id_option1
- string_id_option2
- message
- message_option1
- message_option2

This effect was added in: 1.54 & Trigger Version 4.1
"""
DISABLE_UNIT_ATTACKABLE = 98
"""Attributes for the **disable_unit_attackable** effect are: \n
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- selected_object_ids
- max_units_affected

This effect was added in: 1.54 & Trigger Version 4.1
"""
ENABLE_UNIT_ATTACKABLE = 99
"""Attributes for the **enable_unit_attackable** effect are: \n
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- selected_object_ids
- max_units_affected

This effect was added in: 1.54 & Trigger Version 4.1
"""
MODIFY_VARIABLE_BY_VARIABLE = 100
"""Attributes for the **modify_variable_by_variable** effect are: \n
- operation
- variable
- variable2

This effect was added in: 1.54 & Trigger Version 4.1
"""
COUNT_UNITS_INTO_VARIABLE = 101
"""Attributes for the **count_units_into_variable** effect are: \n
- object_list_unit_id
- source_player
- area_x1
- area_y1
- area_x2
- area_y2
- object_group
- variable2  // Why FE?! Why the 2nd!?

This effect was added in: 1.54 & Trigger Version 4.1
"""
ADD_TRAIN_LOCATION = 102
"""Attributes for the **add_train_location** effect are: \n
- object_list_unit_id
- source_player
- object_list_unit_id_2
- button_location
- train_time
- hotkey

This effect was added in: 1.55 & Trigger Version 4.5
"""
RESEARCH_LOCAL_TECHNOLOGY = 103
"""Attributes for the **research_local_technology** effect are: \n
- local_technology
- source_player
- selected_object_ids
- area_x1
- area_y1
- area_x2
- area_y2
- object_list_unit_id_2
    
This effect was added in: 1.55 & Trigger Version 4.5
"""
MODIFY_ATTRIBUTE_FOR_CLASS = 104
"""Attributes for the **modify_attribute_for_class** effect are: \n
- object_group2
- source_player
- object_attributes
- message
- operation
- quantity
- quantity_float
- armour_attack_class
    
This effect was added in: 1.55 & Trigger Version 4.5
"""
MODIFY_OBJECT_ATTRIBUTE = 105
"""Attributes for the **modify_object_attribute** effect are: \n
- object_list_unit_id
- source_player
- object_attributes
- selected_object_ids
- area_x1
- area_y1
- area_x2
- area_y2
- operation
- message
- quantity
- quantity_float
- armour_attack_class
- object_filter

This effect was added in: 1.55 & Trigger Version 4.5
"""
MODIFY_OBJECT_ATTRIBUTE_BY_VARIABLE = 106
"""Attributes for the **modify_object_attribute_by_variable** effect are: \n
- object_list_unit_id
- source_player
- object_attributes
- selected_object_ids
- area_x1
- area_y1
- area_x2
- area_y2
- operation
- message
- variable
- armour_attack_class
    
This effect was added in: 1.55 & Trigger Version 4.5
"""
CHANGE_OBJECT_VISIBILITY = 107
"""Attributes for the **change_object_visibility** effect are: \n
- source_player
- target_player
- area_x1
- area_y1
- area_x2
- area_y2
- visibility_state
- max_units_affected
- selected_object_ids
    
This effect was added in: 1.55 & Trigger Version 4.5
"""

BUILD_OBJECT = 108
"""Attributes for the **build_object** effect are: \n
- object_list_unit_id
- source_player
- location_x
- location_y
- location_object_reference
- area_x1
- area_y1
- area_x2
- area_y2
- wall_x1
- wall_y1
- wall_x2
- wall_y2
- object_group
- object_type
- building_list
- selected_object_ids
- disable_garrison_unload_sound
- max_units_affected
- issue_group_command
- queue_action

This effect was added in: 1.57 & Trigger Version 4.6
"""
MIRROR_DIPLOMACY = 109
"""Attributes for the **mirror_diplomacy** effect are: \n
- source_player
- target_player
- enabled

This effect was added in: 1.57 & Trigger Version 4.6
"""