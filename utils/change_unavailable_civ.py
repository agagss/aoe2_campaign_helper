from AoE2ScenarioParser.datasets.object_support import Civilization
from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
import os

def randomly_replace_dlc_civ(scenario):
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

    player_manager = scenario.player_manager

    for i in [
        PlayerId.ONE, PlayerId.TWO, PlayerId.THREE, PlayerId.FOUR,
        PlayerId.FIVE, PlayerId.SIX, PlayerId.SEVEN, PlayerId.EIGHT
    ]:
        player = player_manager.players[i]

        if str(player.civilization).split('.')[-1] not in base_civs:
            player.civilization = Civilization.RANDOM

    return scenario