import os
import pickle
from datetime import datetime

settings_dir = os.path.expanduser("~/.clientmanager")
if not os.path.exists(settings_dir):
    os.mkdir(settings_dir)

computers = [
    ("Computer 27", "192.168.10.215"),
    ("Computer 04", "192.168.10.89"),
    ("Computer 03", "192.168.10.133"),
    ("Computer 02", "192.168.10.99"),
    ("Computer 01", "192.168.10.27"),
    ("Computer 09", "192.168.10.78"),
    ("Computer 10", "192.168.10.242"),
    ("Computer 12", "192.168.10.62"),
    ("Computer 11", "192.168.10.217"),
    ("Computer 17", "192.168.10.129"),
    ("Computer 18", "192.168.10.221"),
    ("Computer 19", "192.168.10.197"),
    ("Computer 26", "192.168.10.104"),
    ("Computer 25", "192.168.10.144"),
    ("Computer 28", "192.168.10.205"),
    ("Computer 32", "192.168.10.120"),
    ("Computer 31", "192.168.10.24"),
    ("Computer 30", "192.168.10.166"),
    ("Computer 29", "192.168.10.70"),
    ("Computer 23", "192.168.10.45"),
    ("Computer 22", "192.168.10.180"),
    ("Computer 21", "192.168.10.235"),
    ("Computer 16", "192.168.10.80"),
    ("Computer 20", "192.168.10.196"),
    ("Computer 14", "192.168.10.94"),
    ("Computer 07", "192.168.10.128"),
    ("Computer 08", "192.168.10.186"),
    ("Computer 06", "192.168.10.226"),
    ("Computer 05", "192.168.10.239"),
    ("Computer 24", "192.168.10.250"),
    ("Computer 13", "192.168.10.117"),
    ("Computer 15", "192.168.10.112"),
#    ("Manager computer", "192.168.10.32"),
]

computers.sort(key=lambda x:x[0])

sessions = {
    "Online session": ("online", (30,60,), 2),
    "Offline session": ("student", (60,120), 1),
}


#---------------------------------
# Accounting
#---------------------------------
# This is the accounting logic. You may overwrite everything, even the functions
# inside the module settings_customize -- don't make changes here

max_daily_credits = 120

class NoMoreCredits(Exception):
    pass

def get_account_filename():
    return os.path.join(settings_dir, "{dtm:s}".format(dtm=datetime.now().strftime("%Y-%m-%d")))

def get_accounting_dict():
    filename = get_account_filename()
    if os.path.exists(filename):
        f = open(filename)
        return pickle.load(f)
    else:
        return {}

def save_accounting_dict(accounting):
    f = open(get_account_filename(), "w")
    pickle.dump(accounting, f)

def save_usage(person, credits, force=False):
    accounting = get_accounting_dict()
    used_credits = accounting.get(person, 0) + credits
    if (used_credits <= max_daily_credits) or force:
        accounting[person] = used_credits
        save_accounting_dict(accounting)
        return max_daily_credits - used_credits
    else:
        raise NoMoreCredits

