from dotenv import load_dotenv
from pyapp.model_connection.model import get_model_lm_from_config_dir
from pyapp.utils.config import find_config
from pathlib import Path
from pyapp.utils.config import get_pyapp_config 
from pyapp.config import get_config
from pyapp.cli.schemas import Config as AppConfig
from app_lm_template.schemas import Config

here = Path(__file__).resolve()
config_dir = find_config(here, "appdeps.toml")
app_config : AppConfig = get_config(config_dir.parent)
env = find_config(here, "appdeps.env")
load_dotenv(env)

model = get_model_lm_from_config_dir(config_dir=config_dir)

config = get_pyapp_config(Config, here)