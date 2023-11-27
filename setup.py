import os
from utils.path import get_pip_path

PIP_PATH = get_pip_path()

## === Install torch with cuda === ##

os.system(f"{PIP_PATH} install torch --index-url https://download.pytorch.org/whl/cu121") # cuda 12.1
os.system("git clone https://github.com/huggingface/transformers.git ./temp/transformers")
os.system(f"cd temp/transformers && {PIP_PATH} install -e .")
os.system(f"{PIP_PATH} install -r requirements.txt")