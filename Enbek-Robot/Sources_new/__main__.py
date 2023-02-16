# -*- coding: utf-8 -*-
import agent_initializetion
from Sources.new_enbek.main import start_priem_enbek
from Sources_new.init import credentials, period
from Sources_new.priem import Priem
from pyPythonRPA.Robot import pythonRPA

# --------------------------------- Get Data ---------------------------------
oneC_app = pythonRPA.application(r"C:\Program Files\1cv8\common\1cestart.exe")
root_path = str(__file__).split("Sources")[0].replace("/", "\\")
credentials = credentials()
period = period()

priem = Priem(period, credentials, oneC_app)
priem_list = priem.start()

# priem_list = []
# start_priem_enbek(priem_list)
print("end")
