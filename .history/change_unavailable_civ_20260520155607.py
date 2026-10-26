from AoE2ScenarioParser.datasets.object_support import Civilization
from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
import os

input_folder = "input/change_civ"
output_folder = "output/change_civ"

os.makedirs(output_folder, exist_ok=True)
os.makedirs(input_folder, exist_ok=True)

input_folder = "input/change_civ"  
base_civs = [
    "BRITON", "FRANKISH", "GOTHIC", "TEUTONIC", "JAPANESE", "CHINESE",
    "BYZANTINE", "PERSIAN", "SARACEN", "TURKISH", "VIKING", "MONGOL", "CELTIC",
    "SPANISH", "AZTEC", "MAYAN", "HUN", "KOREAN",
    "ITALIAN", "INDIAN", "INCAN", "MAGYAR", "SLAVIC",
    "PORTUGUESE", "ETHIOPIAN", "MALIAN", "BERBERS",
    "KHMER", "MALAY", "BURMESE", "VIETNAMESE",
    "BULGARIANS", "TATARS", "CUMANS", "LITHUANIANS",
    "BURGUNDIANS", "SICILIANS",
    "POLES", "BOHEMIANS",
    "DRAVIDIANS", "BENGALIS", "GURJARAS"
]

for file in os.listdir(input_folder):

    scenario = AoE2DEScenario.from_file(os.path.join(input_folder, file))
    player_manager = scenario.player_manager

    for i in [PlayerId.ONE, PlayerId.TWO, PlayerId.THREE, PlayerId.FOUR,PlayerId.FIVE, PlayerId.SIX, PlayerId.SEVEN, PlayerId.EIGHT]:
        player = player_manager.players[i]
        if not str(player.civilization).split('.')[-1] in base_civs:
            player.civilization = Civilization.RANDOM

    scenario.write_to_file(f"{output_folder}/{file.split('.')[0]}_output.aoe2scenario")