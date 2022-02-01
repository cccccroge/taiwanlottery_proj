from enum import Enum


class Game(Enum):
    GINTSAI_539 = "今彩539"
    BIG_LOTTERY = "大樂透"


CRAWLING_META = {
    Game.GINTSAI_539: {
        "url": "https://www.taiwanlottery.com.tw/Lotto/Dailycash/history.aspx",
        "form_prefix": "D539Control_history1",
    },
    Game.BIG_LOTTERY: {
        "url": "https://www.taiwanlottery.com.tw/Lotto/Lotto649/history.aspx",
        "form_prefix": "Lotto649Control_history",
    },
}

GAME_META = {
    Game.GINTSAI_539: {
        "num_max": 39,
    },
    Game.BIG_LOTTERY: {
        "num_max": 49,
    },
}
