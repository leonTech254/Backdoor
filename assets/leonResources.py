
class color:
    black="\033[1;30;20m"
    red="\033[1;31;20m"
    green="\033[1;32;20m"
    yellow="\033[1;33;20m"
    blue="\033[1;34;20m"
    purple="\033[1;35;20m"
    cyan="\033[1;36;20m"
    white="\033[1;37;20m"
    stopcolor="\033[38;2;255;255;255m"
class banner:
    def leonBanner():
        brand=f"""
        {color.yellow}
         _    ___ ___  _  _ _____ ___ ___  ___ ___ ___ _   _ ___ ___ _______   __
        | |  | __/ _ \| \| |_   _| __/ _ \/ __| __/ __| | | | _ \_ _|_   _\ \ / /
        | |__| _| (_) | .` | | | | _| (_) \__ \ _| (__| |_| |   /| |  | |  \ V / {color.green}
        |____|___\___/|_|\_| |_| |___\__\_\___/___\___|\___/|_|_\___| |_|   |_|  
        {color.cyan}
         ____  _                     _____               _             
        |  _ \| |__   ___  _ __   __|_   _| __ __ _  ___| | _____ _ __ 
        | |_) | '_ \ / _ \| '_ \ / _ \| || '__/ _` |/ __| |/ / _ \ '__|
        |  __/| | | | (_) | | | |  __/| || | | (_| | (__|   <  __/ |   
        |_|   |_| |_|\___/|_| |_|\___||_||_|  \__,_|\___|_|\_\___|_| 
    
 
        {color.green}
        ________________________________________________________________________
        |                                                                      |{color.red}
        |   [@]:Created by:{color.yellow} Leon Martin                                        |{color.red}
        |   [@]:Email:martinleontech23@gmail.com,martin@leonteqsecurity.com    |
        |   [@]:Whatsapp:+254719531573                                         |
        |   [@]:Website:https://leonteqsecurity.com                            |
        |   [@]:Github Account:https://github.com/leonTech254                  |{color.green}
        |                                                                      |
        |______________________________________________________________________|
        """
        print(brand)
class custom_output:
    def info(string,selectedColor):
        print(f"{selectedColor}{string} {color.green}")
    def error(string):
        print(f"{color.red}[!] {string} {color.green} \n")
        


class user_input():
    def useruput(userInput):
        u=input(f"{color.yellow}[?]{userInput} {color.white}")
        return u