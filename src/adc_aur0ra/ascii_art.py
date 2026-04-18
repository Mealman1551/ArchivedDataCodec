# ADC Archiver Aurora ASCII Art Module
# (c) 2026 Mealman1551


import platform
from .constants import TEAL, BLUE, LIGHT_GREEN, reset


def get_linux_banner():
    return rf"""{TEAL}
    _    ____   ____      _             _     _                
   / \  |  _ \ / ___|    / \   _ __ ___| |__ (_)_   _____ _ __ 
  / _ \ | | | | |       / _ \ | '__/ __| '_ \| \ \ / / _ \ '__|
 / ___ \| |_| | |___   / ___ \| | | (__| | | | |\ V /  __/ |   
/_/   \_\____/ \____| /_/   \_\_|  \___|_| |_|_| \_/ \___|_|   
                                                               
  __              _     _                  
 / _| ___  _ __  | |   (_)_ __  _   ___  __
| |_ / _ \| '__| | |   | | '_ \| | | \ \/ /
|  _| (_) | |    | |___| | | | | |_| |>  < 
|_|  \___/|_|    |_____|_|_| |_|\__,_/_/\_\  
    {reset}"""


def get_windows_banner():
    return rf"""{BLUE}
    _    ____   ____      _             _     _
   / \  |  _ \ / ___|    / \   _ __ ___| |__ (_)_   _____ _ __
  / _ \ | | | | |       / _ \ | '__/ __| '_ \| \ \ / / _ \ '__|
 / ___ \| |_| | |___   / ___ \| | | (__| | | | |\ V /  __/ |
/_/   \_\____/ \____| /_/   \_\_|  \___|_| |_|_| \_/ \___|_|

  __             __        ___           _
 / _| ___  _ __  \ \      / (_)_ __   __| | _____      _____
| |_ / _ \| '__|  \ \ /\ / /| | '_ \ / _` |/ _ \ \ /\ / / __|
|  _| (_) | |      \ V  V / | | | | | (_| | (_) \ V  V /\__ \
|_|  \___/|_|       \_/\_/  |_|_| |_|\__,_|\___/ \_/\_/ |___/               
    {reset}"""


def get_other_os_banner():
    return rf"""{LIGHT_GREEN}
    _    ____   ____      _             _     _
   / \  |  _ \ / ___|    / \   _ __ ___| |__ (_)_   _____ _ __
  / _ \ | | | | |       / _ \ | '__/ __| '_ \| \ \ / / _ \ '__|
 / ___ \| |_| | |___   / ___ \| | | (__| | | | |\ V /  __/ |
/_/   \_\____/ \____| /_/   \_\_|  \___|_| |_|_| \_/ \___|_|

  __                    _   _                  ___  ____
 / _| ___  _ __    ___ | |_| |__   ___ _ __   / _ \/ ___|
| |_ / _ \| '__|  / _ \| __| '_ \ / _ \ '__| | | | \___ \
|  _| (_) | |    | (_) | |_| | | |  __/ |    | |_| |___) |
|_|  \___/|_|     \___/ \__|_| |_|\___|_|     \___/|____/
    {reset}"""


def print_banner():
    opr = platform.system().lower()

    if opr in ["linux"]:
        print(get_linux_banner())
    elif opr in ["windows"]:
        print(get_windows_banner())
    else:
        print(get_other_os_banner())


def get_info_banner(dev, name, opr):

    from .constants import RED, PURPLE, GREEN, YELLOW, ORANGE, BOLD, ITALIC, TEAL, reset

    return f"""
             {RED}####{reset}        {PURPLE}%%%%%%%%%%%{reset}         {GREEN}********{reset}  
            {RED}######{reset}       {PURPLE}%%%%%%%%%%%{reset}      {GREEN}*************{reset}
           {RED}### ###{reset}      {PURPLE}%%%%      %%%%{reset}   {GREEN}****      ****{reset}
          {RED}###  ###{reset}      {PURPLE}%%%       %%%%{reset}  {GREEN}****           {reset}
         {RED}###   ####{reset}     {PURPLE}%%%       %%%%{reset}  {GREEN}***            {reset}
        {RED}###    ####{reset}     {PURPLE}%%%      %%%%{reset}   {GREEN}****            {reset}
       {RED}#############{reset}    {PURPLE}%%%      %%%%{reset}   {GREEN}****       ***{reset}  
      {RED}####       ###{reset}   {PURPLE}%%%%%%%%%%%%{reset}      {GREEN}************{reset}   
     {RED}####        ####{reset}  {PURPLE}%%%%%%%%%{reset}          {GREEN}*******{reset}  

        | ADC Archiver {TEAL}Aurora{reset} | Version: 2026.04.1 |

        
        GitHub page: https://github.com/Mealman1551/ArchivedDataCodec
        Webpage: https://mealman1551.github.io/adc.html

        ---------

        You are hosting ADC on: {ORANGE}{dev}{reset}
        You are using ADC as: {ORANGE}{name}{reset}
        You are using ADC on: {ORANGE}{opr}{reset}

        (c) 2026 Mealman1551
        """
