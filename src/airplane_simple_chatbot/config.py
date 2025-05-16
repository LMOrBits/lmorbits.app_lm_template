from pyapp.model_connection.model import get_model_lm_from_config_dir
from pyapp.utils.config import find_config
from pathlib import Path
from pyapp.utils.config import get_pyapp_config 
from airplane_simple_chatbot.schemas import Config

here = Path(__file__).resolve()
config_dir = find_config(here, "appdeps.toml")
model = get_model_lm_from_config_dir(config_dir=config_dir)

config = get_pyapp_config(Config, here)