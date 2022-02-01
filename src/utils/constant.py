from enum import Enum


class Game(Enum):
    GINTSAI_539 = "今彩539"
    BIG_LOTTERY = "大樂透"


CRAWLING_META = {
    Game.GINTSAI_539: {
        "url": "https://www.taiwanlottery.com.tw/Lotto/Dailycash/history.aspx",
        "form_prefix": "D539",
    },
    Game.BIG_LOTTERY: {
        "url": "https://www.taiwanlottery.com.tw/Lotto/Lotto649/history.aspx",
        "form_prefix": "Lotto649",
    },
}
