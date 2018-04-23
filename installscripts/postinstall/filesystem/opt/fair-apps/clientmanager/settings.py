import os
import pickle
from datetime import datetime

ETH = "eth0"
IP_STARTING_WITH = "192.168.10"

settings_dir = os.path.expanduser("~/.clientmanager")
if not os.path.exists(settings_dir):
    os.mkdir(settings_dir)

computers = [
    ("1", "192.168.10.20"),
]

# session_name = (username, (minutes,), credits_per_minute)
sessions = {
    "Online session": ("online", (30,60,), 2),
    "Offline session": ("student", (60,120), 1),
}

logfile=open(os.path.expanduser("~/Desktop/clientmanager.log"), "a")


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
    if used_credits <= max_daily_credits or force:
        accounting[person] = used_credits
        save_accounting_dict(accounting)
        return max_daily_credits - used_credits
    else:
        raise NoMoreCredits

#---------------------------------
# Customized settings
#---------------------------------
# Customized settings are imported here, hence everything in that module will
# overwrite variables, function definitions etc. from this module.

try:
    from settings_customize import * #@UnusedWildImport
except ImportError:
    pass
