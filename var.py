import os
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")

def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list

class Var:
    API_ID = int(os.getenv("API_ID", "29495557"))
    API_HASH = os.getenv("API_HASH", "e5efba8eba82bd702ce0740c2cfa6281")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "5502966020:AAGxzBFjhjhB-hSujb4HI3QDWqLOrUtZ3UI")
    sudo = os.getenv("SUDO", "5526165514 5778117994")
    SUDO = []
    if sudo:
        SUDO = make_int(sudo)
