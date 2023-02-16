# -*- coding: utf-8 -*-
import time

import agent_initializetion
from pyPythonRPA.Robot import pythonRPA
# from Sources.mail import send_mail
from Sources.new_enbek.main import start_priem_enbek, start_uvol_enbek, start_perevod_enbek
from Sources.init import credentials, period
from Sources.priem import priem
from Sources.peremesheniye import peremesheniye
from Sources.uvolneniye import uvolneniye

# time.sleep(30)



oneC_app = pythonRPA.application(r"C:\Program Files\1cv8\common\1cestart.exe")
credentials = credentials()
period = period()

root_path = str(__file__).split("Sources")[0].replace("/", "\\")
login = credentials["enbek_login"]
psw = credentials["enbek_password"]
psw_ecp = credentials["ecp_password"]

# try:
# priem_arr = priem(period, credentials, oneC_app)
# start_priem_enbek(priem_arr)
# except:
#     print('priem error')

# try:
uvol_arr = uvolneniye(period, credentials, oneC_app)
# start_uvol_enbek(uvol_arr)
# except:
#     print('uvol error')

# try:
# pereme_arr = peremesheniye(period, credentials, oneC_app)
# start_perevod_enbek(pereme_arr)
# except:
#     print('perevod error')

# send_mail()
# '''
# [{'ФИО': 'Әлдибек Д.М.', 'Дата расторжение': '03.10.2022', 'Причина': 'По инициативе работника', 'ИИН': '780329300070'}, {'ФИО': 'Дуисбеков Т.Ж.', 'Дата расторжение': '12.10.2022', 'Причина': 'Достижение работником пенсионного возраста', 'ИИН': '590929301941'}, {'ФИО': 'Әміров Б.М.', 'Дата расторжение': '14.10.2022', 'Причина': 'По инициативе работника', 'ИИН': '960225300200'}, {'ФИО': 'Бакун Е.В.', 'Дата расторжение': '16.10.2022', 'Причина': 'Достижение работником пенсионного возраста', 'ИИН': '590915300709'}, {'ФИО': 'Елемесов К.Е.', 'Дата расторжение': '17.10.2022', 'Причина': 'По инициативе работника', 'ИИН': '850207300458'}, {'ФИО': 'Ахметов К.К.', 'Дата расторжение': '17.10.2022', 'Причина': 'По инициативе работника', 'ИИН': '730518301195'}, {'ФИО': 'Нуров Е.Б.', 'Дата расторжение': '18.10.2022', 'Причина': 'По инициативе работника', 'ИИН': '871003300267'}, {'ФИО': 'Меналимов С.С.', 'Дата расторжение': '19.10.2022', 'Причина': 'Достижение работником пенсионного возраста', 'ИИН': '590918301703'}, {'ФИО': 'Филатова И.М.', 'Дата расторжение': '22.10.2022', 'Причина': 'Достижение работником пенсионного возраста', 'ИИН': '620321402235'}, {'ФИО': 'Амангельдинов Ж.С.', 'Дата расторжение': '31.10.2022', 'Причина': 'По инициативе работника', 'ИИН': '930323301996'}]
# '''
print('end')
