"""
Installs everything necessary for this package
"""

import platform
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[0])) 
sys.path.append(str(Path(__file__).resolve().parents[1])) 
sys.path.append(str(Path(__file__).resolve().parents[2])) 
sys.path.append(str(Path(__file__).resolve().parents[3])) 
sys.path.append(str(Path(__file__).resolve().parents[4])) 

from vizpip_env.lib.pyUtil import *
from vizpip_env.installer import install_package
    

def install():
    if platform.system() == "Windows":
        install_package("sdlOpengl_win")


if __name__ == "__main__":
    install()