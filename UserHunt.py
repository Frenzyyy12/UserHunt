# userhunt.py

import os
import requests
import json
from colorama import init, Fore, Style

init(autoreset=True)

sites = {
    "GitHub": "https://github.com/{}",
    "Instagram": "https://instagram.com/{}",
    "Twitter": "https://twitter.com/{}",
    "Reddit": "https://reddit.com/u/{}",
    "TikTok": "https://tiktok.com/@{}",
    "Pinterest": "https://pinterest.com/{}",
    "Snapchat": "https://www.snapchat.com/add/{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "Twitch": "https://www.twitch.tv/{}",
    "Steam": "https://steamcommunity.com/id/{}"
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_username(username):
    results = {}
    for site, url in sites.items():
        try:
            full_url = url.format(username)
            res = requests.get(full_url, timeout=5)
            if res.status_code == 200:
                results[site] = (True, "FOUND")
            else:
                results[site] = (False, "NOT FOUND")
        except Exception:
            results[site] = (False, "ERROR")
    return results

def save_results(username, results):
    folder = "results"
    if not os.path.exists(folder):
        os.makedirs(folder)
    filepath = os.path.join(folder, f"{username}.txt")
    output = {
        "author": "Frenzyy",
        "username": username,
        "results": {k: v[1] for k, v in results.items()}
    }
    with open(filepath, "w") as f:
        json.dump(output, f, indent=4)

def print_ascii_banner():
    clear_screen()
    banner = f"""
{Fore.RED}

     ,*-~"`^"*u_                                _u*"^`"~-*,
  p!^       /  jPw                            w9j \        ^!p
w^.._      /      "\_                      _/"     \        _.^w
     *_   /          \_      _    _      _/ {Fore.YELLOW}Made by{Style.RESET_ALL}{Fore.RED} \     _* 
       q /           / \q   ( `--` )   p/ \  {Style.RESET_ALL}{Fore.YELLOW}Frenzyy{Style.RESET_ALL}{Fore.RED} \   p
       jj5****._    /    ^\_) {Fore.LIGHTCYAN_EX}o  o{Style.RESET_ALL} {Fore.RED}(_/^    \    _.****6jj
                *_ /      "==) ;; (=="      \ _*
                 `/.w***,   /(    )\   ,***w.\"
                  ^ ilmk ^c/ )    ( \c^      ^
                          'V')_)(_('V'
                              `` ``{Style.RESET_ALL}
{Fore.RED}             [ Usernames Cross Plateforms Hunter ]{Style.RESET_ALL}
"""
    print(banner)

def main():
    print_ascii_banner()
    username = input(Fore.YELLOW + "Enter username to check: " + Style.RESET_ALL).strip()
    if not username:
        print(Fore.RED + "Invalid input. Exiting." + Style.RESET_ALL)
        return
    results = check_username(username)
    save_results(username, results)
    print()
    for site, (found, status) in results.items():
        color = Fore.GREEN if found else (Fore.RED if status == "NOT FOUND" else Fore.MAGENTA)
        print(f"[{Fore.WHITE}{site}{Style.RESET_ALL}] {color}{status}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
