from AoE2ScenarioParser.datasets.object_support import Civilization
from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
import os

folder = "input/"  

BRITONS = "BRITON-CIV"
FRANKS = "FRANKISH-CIV"
GOTHS = "GOTHIC-CIV"
TEUTONS = "TEUTONIC-CIV"
JAPANESE = "JAPANESE-CIV"
CHINESE = "CHINESE-CIV"
BYZANTINES = "BYZANTINE-CIV"
PERSIANS = "PERSIAN-CIV"
SARACENS = "SARACEN-CIV"
TURKS = "TURKISH-CIV"
VIKINGS = "VIKING-CIV"
MONGOLS = "MONGOL-CIV"
CELTS = "CELTIC-CIV"

SPANISH = "SPANISH-CIV"
AZTECS = "AZTEC-CIV"
MAYANS = "MAYAN-CIV"
HUNS = "HUN-CIV"
KOREANS = "KOREAN-CIV"

ITALIANS = "ITALIAN-CIV"
HINDUSTANIS = "INDIAN-CIV"
INCAS = "INCAN-CIV"
MAGYARS = "MAGYAR-CIV"
SLAVS = "SLAVIC-CIV"

PORTUGUESE = "PORTUGUESE-CIV"
ETHIOPIANS = "ETHIOPIAN-CIV"
MALIANS = "MALIAN-CIV"
BERBERS = "BERBERS-CIV"

KHMER = "KHMER-CIV"
MALAY = "MALAY-CIV"
BURMESE = "BURMESE-CIV"
VIETNAMESE = "VIETNAMESE-CIV"

BULGARIANS = "BULGARIANS-CIV"
TATARS = "TATARS-CIV"
CUMANS = "CUMANS-CIV"
LITHUANIANS = "LITHUANIANS-CIV"

BURGUNDIANS = "BURGUNDIANS-CIV"
SICILIANS = "SICILIANS-CIV"

POLES = "POLES-CIV"
BOHEMIANS = "BOHEMIANS-CIV"

DRAVIDIANS = "DRAVIDIANS-CIV"
BENGALIS = "BENGALIS-CIV"
GURJARAS = "GURJARAS-CIV"


for file in os.listdir(folder):

    scenario = AoE2DEScenario.from_file(os.path.join(folder, file))
    player_manager = scenario.player_manager

    for i in [PlayerId.ONE, PlayerId.TWO, PlayerId.THREE, PlayerId.FOUR,PlayerId.FIVE, PlayerId.SIX, PlayerId.SEVEN, PlayerId.EIGHT]:
        player = player_manager.players[i]
        if str(player.civilization).split('.')[-1] == 'ROMANS':
            player.civilization = Civilization.BYZANTINES

    scenario.write_to_file(f"output/{file.split('.')[0]}_output.aoe2scenario")