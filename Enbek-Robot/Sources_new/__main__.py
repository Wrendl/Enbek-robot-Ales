# -*- coding: utf-8 -*-
import agent_initializetion
from Sources.new_enbek.main import start_priem_enbek
from Sources_new.init import credentials, period
from Sources_new.priem import Priem
from Sources_new.perevod import Perevod
from pyPythonRPA.Robot import pythonRPA

# --------------------------------- Get Data ---------------------------------
oneC_app = pythonRPA.application(r"C:\Program Files\1cv8\common\1cestart.exe")
root_path = str(__file__).split("Sources")[0].replace("/", "\\")
credentials = credentials()
period = period()


# --------------------------------- Priem ---------------------------------
priem = Priem(period, credentials, oneC_app)
priem_list = priem.start()
start_priem_enbek(priem_list)


# --------------------------------- Perevod ---------------------------------
perevod = Perevod(period, credentials, oneC_app)
perevod = perevod.start()
print("end")
