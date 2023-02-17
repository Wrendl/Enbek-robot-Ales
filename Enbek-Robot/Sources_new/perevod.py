import os
import sys
from oneC_func import auth, focus_1C, time_delay, copy_data, open_sotrudniki, find_employee_from_list
from pyPythonRPA.Robot import pythonRPA
from Sources_new.init import address_mapping, logs, contract_type_mapping, regime_type_mapping, position_mapping


class Perevod:

    def __init__(self, period, credentials, oneC_app):
        self.period = period
        self.login = credentials["oneC_login"]
        self.password = credentials["oneC_password"]
        self.oneC_app = oneC_app
        self.since = period["since"]
        self.till = period["till"]

        self.employees_arr = []

    def start(self):
        self.oneC_app.start()

        auth(self.login, self.password)

        focus_1C()

        # --- Okno zayavki ubrat'---
        if pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16},
                                 {"ctrl_index": 0}]).is_exists():
            time_delay()
            pythonRPA.keyboard.press('esc')

        # --- Enter to Кадровый учет ---
        pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 0}, {"ctrl_index": 1}, {"ctrl_index": 0}, {"title": "Главное меню"},
                              {"title": "Кадровый учет"}]).click()

        pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 0},{"title": "Кадровый учет"},
                              {"title": "Кадровые перемещения организаций"}]).wait_appear(5)
        pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 0},{"title": "Кадровый учет"},
                              {"title": "Кадровые перемещения организаций"}]).click()

        # -- Set date ---
        pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 1}, {"ctrl_index": 0},
                              {"title": "Установить интервал дат..."}]).wait_appear(20)
        pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 1}, {"ctrl_index": 0},
                              {"title": "Установить интервал дат..."}]).click()
        pythonRPA.bySelector([{"title": "Настройка периода", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"},{"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"title": "Интервал"},
                              {"title": "Интервал"}]).wait_appear(15)
        time_delay()
        pythonRPA.keyboard.press("down", 7, 0.3)
        pythonRPA.keyboard.press("tab", 1, 0.3)
        pythonRPA.keyboard.write(str(self.since))
        time_delay()
        pythonRPA.keyboard.press("tab", 1, 0.3)
        pythonRPA.keyboard.press("down", 7, 0.3)
        pythonRPA.keyboard.press("tab", 1, 0.3)
        pythonRPA.keyboard.write(str(self.till))
        time_delay()
        pythonRPA.keyboard.press("ctrl+enter")
        time_delay()

        # --- Вывести список ---
        pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 1}, {"ctrl_index": 0},
                              {"title": "Действия"}]).wait_appear(30)
        pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 1}, {"ctrl_index": 0},
                              {"title": "Действия"}]).click()
        pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 0},
                              {"title": "Действия"}, {"title": "Вывести список..."}]).wait_appear(10)
        time_delay()
        pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 0},
                              {"title": "Действия"}, {"title": "Вывести список..."}]).click()
        pythonRPA.bySelector([{"title": "Вывести список", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 0},
                              {"title": "ОК"}]).wait_appear(10)
        time_delay()
        pythonRPA.bySelector([{"title": "Вывести список", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 0},
                              {"title": "ОК"}]).click()

        pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": 1},
                              {"ctrl_index": 0}]).wait_appear(10)
        time_delay()
        pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": 1},
                              {"ctrl_index": 0}]).click()

        # --- Copy all data ---
        copy_data()
        employees_count = len(str(pythonRPA.clipboard.get()).split("\n")) - 1
        employees_list = []

        # --- If no data return ---
        if employees_count == 0:
            print("0 employees - perevod")
            return []

        # --- Add data to employee_list ---
        for employee in str(pythonRPA.clipboard.get()).split("\n"):
            if "Ручная корректировка" in str(employee):
                continue
            else:
                employees_list.append(str(employee).split("	"))
        pythonRPA.keyboard.press("esc")
        time_delay()

        focus_1C()

        print(len(employees_list))

        for employee in employees_list:
            try:
                if employees_list.index(employee) == 0:
                    open_sotrudniki()
                employee_dict = {'ФИО': employee[5],
                                 "Номер доп соглашения": "БН"}
                window_index_1 = 1

                find_employee_from_list(window_index_1, employee)

                pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": window_index_1 + 1}, {"ctrl_index": 0}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 11}, {"ctrl_index": 3}, {"ctrl_index": 0},
                                      {"ctrl_index": 2}]).wait_appear(15)
