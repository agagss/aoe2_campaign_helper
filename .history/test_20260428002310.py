from AoE2ScenarioParser.datasets.object_support import Civilization
from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
import os
# File & Folder setup
# Define paths to the scenario folder.
# You can find this folder by opening AoE2:DE and going to scenarios and clicking on 'open folder'
folder = "input/"  # <-- Final slash is important
scenario_name = "name_of_your_scenario"

for file in os.listdir(folder):
# Define Scenario file
scenario = AoE2DEScenario.from_file(f"{scenario_folder}{scenario_name}.aoe2scenario")

# Save the player manager and the second player
player_manager = scenario.player_manager
player_two = player_manager.players[PlayerId.TWO]

player_two.civilization = Civilization.BYZANTINES