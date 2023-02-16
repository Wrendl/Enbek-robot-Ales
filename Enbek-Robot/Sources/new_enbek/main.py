# coding=utf8
import datetime
from Sources.init import logs
from Sources.new_enbek.enbek import Enbek, TDData
from Sources.new_enbek.init import update_perevod


def start_uvol_enbek(uvol_arr):
    enbek = Enbek()
    for uvol in uvol_arr:
        try:
            enbek.delete_td(uvol)
            logs([str(datetime.datetime.now().strftime("%H:%M")), str(uvol["ФИО"]), str(uvol["ИИН"]),
                  "---", "Внесён", "Увольнение"])
        except Exception as e:
            logs([str(datetime.datetime.now().strftime("%H:%M")), str(uvol["ФИО"]), str(uvol["ИИН"]),
                  "Ошибка в enbek.kz", "Увольнение"])
            print('Ошибка в увольнении сотрудника - ', str(e))
            print(uvol)
        # input()
    enbek.quit()


def start_priem_enbek(priem_arr):
    enbek = Enbek()
    for priem in priem_arr:
        try:
            priem_new = TDData(priem)
            enbek.add_td(priem_new)
            logs([str(datetime.datetime.now().strftime("%H:%M")), str(priem["ФИО"]), str(priem["ИИН"]), str(priem["Табельный номер"]), "Внесён", "Прием"])
        except Exception as e:
            logs([str(datetime.datetime.now().strftime("%H:%M")), str(priem["ФИО"]), str(priem["ИИН"]), str(priem["Табельный номер"]), "Ошибка в enbek.kz", "Прием"])
            print('Ошибка в приеме сотрудника - ', str(e))
            print(priem)
            print('---------------------------------------')

    enbek.quit()


def start_perevod_enbek(perevod_arr):
    enbek = Enbek()
    for perevod in perevod_arr:
        try:
            perevod_new = update_perevod(perevod)
            enbek.dop_soglashenie(perevod_new)
            logs([str(datetime.datetime.now().strftime("%H:%M")), str(perevod["ФИО"]), str(perevod["ИИН"]), str(perevod["Табельный номер"]), "Внесён",
                  "Перемещении"])
        except Exception as e:
            logs([str(datetime.datetime.now().strftime("%H:%M")), str(perevod["ФИО"]), str(perevod["Табельный номер"]), str(perevod["ИИН"]),
                  "Ошибка в enbek.kz", "Перемещении"])
            print('Ошибка в перемещении сотрудника - ', str(e))
            print(perevod)
    enbek.quit()