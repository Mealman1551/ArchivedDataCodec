# ADC Archiver 1.5.0 - ASCII Art Module
# (c) 2026 Mealman1551


import platform
from libadc.constants import TEAL, BLUE, LIGHT_GREEN, reset, VERSION, VERSION_CODENAME


def get_linux_banner():
    return rf"""{TEAL}
    _   ___   ___     _          _    _             
   /_\ |   \ / __|   /_\  _ _ __| |_ (_)_ _____ _ _
  / _ \| |) | (__   / _ \| '_/ _| ' \| \ V / -_) '_|
 /_/_\_\___/ \___| /_/ \_\_| \__|_||_|_|\_/\___|_|
  / _|___ _ _  | |  (_)_ _ _  ___ __
 |  _/ _ \ '_| | |__| | ' \ || \ \ /
 |_| \___/_|   |____|_|_||_\_,_/_\_\
    {reset}"""


def get_windows_banner():
    return rf"""{BLUE}
    _   ___   ___     _          _    _             
   /_\ |   \ / __|   /_\  _ _ __| |_ (_)_ _____ _ _
  / _ \| |) | (__   / _ \| '_/ _| ' \| \ V / -_) '_|
 /_/_\_\___/ \___| /_/ \_\_| \__|_||_|_|\_/\___|_|
  / _|___ _ _  \ \    / (_)_ _  __| |_____ __ _____ 
 |  _/ _ \ '_|  \ \/\/ /| | ' \/ _` / _ \ V  V (_-<
 |_| \___/_|     \_/\_/ |_|_||_\__,_\___/\_/\_//__/
    {reset}"""


def get_other_os_banner():
    return rf"""{LIGHT_GREEN}
    _   ___   ___     _          _    _             
   /_\ |   \ / __|   /_\  _ _ __| |_ (_)_ _____ _ _
  / _ \| |) | (__   / _ \| '_/ _| ' \| \ V / -_) '_|
 /_/_\_\___/ \___| /_/ \_\_| \__|_||_|_|\_/\___|_|
  / _|___ _ _   ___| |_| |_  ___ _ _   ___ ___
 |  _/ _ \ '_| / _ \  _| ' \/ -_) '_| / _ (_-<
 |_| \___/_|   \___/\__|_||_\___|_|   \___/__/
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

    from libadc.constants import RED, PURPLE, GREEN, YELLOW, ORANGE, BOLD, ITALIC, reset

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

        | ADC Archiver | Version: {VERSION} ({VERSION_CODENAME}) |

        
        GitHub page: https://github.com/Mealman1551/ArchivedDataCodec
        Webpage: https://mealman1551.github.io/adc.html
        
        
        ---------

        You are hosting ADC on: {ORANGE}{dev}{reset}
        You are using ADC as: {ORANGE}{name}{reset}
        You are using ADC on: {ORANGE}{opr}{reset}

        (c) 2026 Mealman1551
        """
