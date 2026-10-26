from AoE2ScenarioParser.datasets.object_support import Civilization
from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
import os

folder = "input/"  

for file in os.listdir(folder):

    scenario = AoE2DEScenario.from_file(os.path.join(folder, file))
    player_manager = scenario.player_manager

    for i in [PlayerId.ONE, PlayerId.TWO, PlayerId.THREE, PlayerId.FOUR,PlayerId.FIVE, PlayerId.SIX, PlayerId.SEVEN, PlayerId.EIGHT]:
        player = player_manager.players[i]
        if str(player.civilization).split('.')[-1] == 'ROMANS':
            player.civilization = Civilization.BYZANTINES

    scenario.write_to_file(f"output/{file.split('.')[0]}_output.aoe2scenario")