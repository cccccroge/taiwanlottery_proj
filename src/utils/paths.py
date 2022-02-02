from pathlib import Path
import os.path

ROOT_FOLDER = Path(__file__).parent.parent.parent
DATA_FOLDER = os.path.join(ROOT_FOLDER, "data")
SCRAPY_FOLDER = os.path.join(ROOT_FOLDER, "src", "scrapy_proj")

ASSET_FOLDER = os.path.join(ROOT_FOLDER, "asset")
KV_FOLDER = os.path.join(ROOT_FOLDER, "src", "kv")
