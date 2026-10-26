from AoE2ScenarioParser.datasets.object_support import Civilization
from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
import os

folder = "input/"  

BRITONS = "BRITON"
FRANKS = "FRANKISH"
GOTHS = "GOTHIC"
TEUTONS = "TEUTONIC"
JAPANESE = "JAPANESE"
CHINESE = "CHINESE"
BYZANTINES = "BYZANTINE"
PERSIANS = "PERSIAN"
SARACENS = "SARACEN"
TURKS = "TURKISH"
VIKINGS = "VIKING"
MONGOLS = "MONGOL"
CELTS = "CELTIC"

SPANISH = "SPANISH"
AZTECS = "AZTEC"
MAYANS = "MAYAN"
HUNS = "HUN"
KOREANS = "KOREAN"

ITALIANS = "ITALIAN"
HINDUSTANIS = "INDIAN"
INCAS = "INCAN"
MAGYARS = "MAGYAR"
SLAVS = "SLAVIC"

PORTUGUESE = "PORTUGUESE"
ETHIOPIANS = "ETHIOPIAN"
MALIANS = "MALIAN"
BERBERS = "BERBERS"

KHMER = "KHMER"
MALAY = "MALAY"
BURMESE = "BURMESE"
VIETNAMESE = "VIETNAMESE"

BULGARIANS = "BULGARIANS"
TATARS = "TATARS"
CUMANS = "CUMANS"
LITHUANIANS = "LITHUANIANS"

BURGUNDIANS = "BURGUNDIANS"
SICILIANS = "SICILIANS"

POLES = "POLES"
BOHEMIANS = "BOHEMIANS"

DRAVIDIANS = "DRAVIDIANS"
BENGALIS = "BENGALIS"
GURJARAS = "GURJARAS"


for file in os.listdir(folder):

    scenario = AoE2DEScenario.from_file(os.path.join(folder, file))
    player_manager = scenario.player_manager

    for i in [PlayerId.ONE, PlayerId.TWO, PlayerId.THREE, PlayerId.FOUR,PlayerId.FIVE, PlayerId.SIX, PlayerId.SEVEN, PlayerId.EIGHT]:
        player = player_manager.players[i]
        if str(player.civilization).split('.')[-1] == 'ROMANS':
            player.civilization = Civilization.BYZANTINES

    scenario.write_to_file(f"output/{file.split('.')[0]}_output.aoe2scenario")