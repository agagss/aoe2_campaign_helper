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

    scenario = AoE2DEScenario.from_file(os.path.join(folder, file))
    player_manager = scenario.player_manager

    player_two = player_manager.players[PlayerId.TWO]
    for i in [PlayerId.ONE, PlayerId.TWO, PlayerId.THREE, PlayerId.FOUR,PlayerId.FIVE, PlayerId.SIX, PlayerId.SEVEN, PlayerId.EIGHT]:
        player = player_manager.players[i]
        print('aaaaa', )
        if player.civilization == 'ROMANS':
            player.civilization = Civilization.BYZANTINES
    scenario.write_to_file(f"output/{file.split('.')[0]}_output.aoe2scenario")