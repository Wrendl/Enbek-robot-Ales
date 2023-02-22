import os
import sys
from pyPythonRPA.Robot import pythonRPA
from Sources_new.init import address_mapping, logs, contract_type_mapping, regime_type_mapping, position_mapping


class Priem:

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

        self.auth()

        self.focus_1C()

        # --- Okno zayavki ubrat'---
        if pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1}, {"ctrl_index": 16},
                                 {"ctrl_index": 0}]).is_exists():
            self.time_delay()
            pythonRPA.keyboard.press('esc')

        # --- Enter to Кадровый учет ---
        pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1}, {"ctrl_index": 0},{"ctrl_index": 1}, {"ctrl_index": 0}, {"title": "Главное меню"},
                              {"title": "Кадровый учет"}]).click()
        pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 0},
                              {"title": "Кадровый учет"}, {"title": "Прием на работу в организаций"}]).wait_appear(5)
        pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 0},
                              {"title": "Кадровый учет"}, {"title": "Прием на работу в организаций"}]).click()

        # -- Set date ---
        pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1}, {"ctrl_index": 16},{"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 1},{"ctrl_index": 0},
                              {"title": "Установить интервал дат..."}]).wait_appear(20)
        pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1}, {"ctrl_index": 16},{"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 1},{"ctrl_index": 0},
                              {"title": "Установить интервал дат..."}]).click()
        pythonRPA.bySelector([{"title": "Настройка периода", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"},{"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 0}, {"title": "Интервал"},
                              {"title": "Интервал"}]).wait_appear(15)
        self.time_delay()
        pythonRPA.keyboard.press("down", 7, 0.3)
        pythonRPA.keyboard.press("tab", 1, 0.3)
        pythonRPA.keyboard.write(str(self.since))
        self.time_delay()
        pythonRPA.keyboard.press("tab", 1, 0.3)
        pythonRPA.keyboard.press("down", 7, 0.3)
        pythonRPA.keyboard.press("tab", 1, 0.3)
        pythonRPA.keyboard.write(str(self.till))
        self.time_delay()
        pythonRPA.keyboard.press("ctrl+enter")
        self.time_delay()

        # --- Вывести список ---
        pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1}, {"ctrl_index": 16},{"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 1},{"ctrl_index": 0},
                              {"title": "Действия"}]).wait_appear(30)
        pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1}, {"ctrl_index": 16},{"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 1},{"ctrl_index": 0},
                              {"title": "Действия"}]).click()
        pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 0},
                              {"title": "Действия"}, {"title": "Вывести список..."}]).wait_appear(10)
        self.time_delay()
        pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 0},
                              {"title": "Действия"}, {"title": "Вывести список..."}]).click()
        pythonRPA.bySelector([{"title": "Вывести список", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 0},
                              {"title": "ОК"}]).wait_appear(10)
        self.time_delay()
        pythonRPA.bySelector([{"title": "Вывести список", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 0},
                              {"title": "ОК"}]).click()

        pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1}, {"ctrl_index": 16},{"ctrl_index": 1},
                              {"ctrl_index": 0}]).wait_appear(10)
        self.time_delay()
        pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1}, {"ctrl_index": 16},{"ctrl_index": 1},
                              {"ctrl_index": 0}]).click()

        # --- Copy all data ---
        self.copy_data()
        employees_count = len(str(pythonRPA.clipboard.get()).split("\n")) - 1
        employees_list = []

        # --- If no data return ---
        if employees_count == 0:
            print("0 employees - priem")
            return []

        # --- Add data to employee_list ---
        for employee in str(pythonRPA.clipboard.get()).split("\n"):
            if "Ручная корректировка" in str(employee):
                continue
            else:
                employees_list.append(str(employee).split("	"))
        pythonRPA.keyboard.press("esc")
        self.time_delay()

        self.focus_1C()

        print(len(employees_list))

        # --- Iteration, ---
        for employee in employees_list:
            try:
                # --- Open sotrudniki ---
                if employees_list.index(employee) == 0:
                    self.open_sotrudniki()

                # --- Find employee from list ---
                employee_dict = {'ФИО': employee[5]}
                window_index_1 = 1

                self.find_employee_from_list(window_index_1, employee)

                pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": window_index_1 + 1}, {"ctrl_index": 0}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 11}, {"ctrl_index": 3}, {"ctrl_index": 0},
                                      {"ctrl_index": 2}]).wait_appear(15)

                # ---> Name
                pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": window_index_1 + 1}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 11},{"ctrl_index": 3}, {"ctrl_index": 0},
                                      {"ctrl_index": 2}]).click()
                self.copy_data()
                name = str(pythonRPA.clipboard.get()).replace("Сотрудник", "").replace("(осн.)", "").strip()
                self.time_delay()

                # ---> Табельный номер / Место выполнения работы
                pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": window_index_1 + 1}, {"ctrl_index": 0}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 11}, {"ctrl_index": 3}, {"ctrl_index": 0},
                                      {"ctrl_index": 1}]).click()
                self.copy_data()
                employee_dict["Табельный номер"] = str(pythonRPA.clipboard.get())
                employee_dict["Место выполнения работы"] = address_mapping(employee_dict["Табельный номер"])

                # --- Switch to Sotrudniki tab ---
                pythonRPA.keyboard.press("esc")
                pythonRPA.keyboard.press("ctrl+tab")
                self.time_delay()

                self.focus_1C()
                self.time_delay()

                # --- Find employee in sotrudniki with prefix -> " (осн.)" ---
                pythonRPA.keyboard.press("ctrl+f")
                pythonRPA.bySelector([{"title": "Поиск", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 0},
                                      {"ctrl_index": 12}]).wait_appear(10)
                self.time_delay()
                pythonRPA.bySelector([{"title": "Поиск", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 0},
                                      {"ctrl_index": 12}]).click()
                self.time_delay()
                pythonRPA.keyboard.press("ctrl+a")
                self.time_delay()
                pythonRPA.keyboard.press("delete")
                self.time_delay()
                pythonRPA.keyboard.write(name + " (осн.)")
                self.time_delay()
                pythonRPA.keyboard.press("ctrl+enter")

                # --- Find employee in sotrudniki without prefix, if it didn't find before ---
                ok_button = [{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"},{"title": "1С:Предприятие"}, {"ctrl_index": 0}, {"ctrl_index": 0},{"ctrl_index": 0},{"title": "OK"}]
                pythonRPA.bySelector(ok_button).wait_appear(5)
                if pythonRPA.bySelector(ok_button).is_exists():
                    pythonRPA.bySelector(ok_button).click()
                    self.time_delay()
                    pythonRPA.keyboard.press("ctrl+f")
                    pythonRPA.bySelector([{"title": "Поиск", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"},{"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 0},
                                          {"ctrl_index": 12}]).wait_appear(10)
                    self.time_delay()
                    pythonRPA.bySelector([{"title": "Поиск", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"},{"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 0},
                                          {"ctrl_index": 12}]).click()
                    self.time_delay()
                    pythonRPA.keyboard.press("ctrl+a")
                    self.time_delay()
                    pythonRPA.keyboard.press("delete")
                    self.time_delay()
                    pythonRPA.keyboard.write(name)
                    self.time_delay()
                    pythonRPA.keyboard.press("ctrl+enter")

                pythonRPA.bySelector(ok_button).wait_appear(5)
                if pythonRPA.bySelector(ok_button).is_exists():
                    pythonRPA.bySelector(ok_button).click()
                    self.time_delay()
                    pythonRPA.keyboard.press("ctrl+tab")
                    logs(str(employee_dict['ФИО']), "", "",
                         "Нет в сотрудниках", "Прием")
                    self.time_delay()
                    continue

                # --- Enter sotrudniki card
                self.focus_1C()
                self.time_delay()
                pythonRPA.keyboard.press("enter")
                window_index_2 = 2
                pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": window_index_2}, {"ctrl_index": 0}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 4}, {"ctrl_index": 0},
                                      {"title": "Общее"},{"title": "Трудовой договор"}]).wait_appear(15)
                self.time_delay()

                # ---> Вид работы
                pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": window_index_2}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 4}, {"ctrl_index": 0},
                                      {"ctrl_index": 8}]).click()
                self.copy_data()
                employment_type = str(pythonRPA.clipboard.get())

                if employment_type == "Основное место работы":
                    employee_dict["Вид работы"] = "основная работа"
                else:
                    employee_dict["Вид работы"] = "работа по совместительству"
                self.time_delay()

                # ---> ИИН
                pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": window_index_2}, {"ctrl_index": 0}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 4}, {"ctrl_index": 0}, {"title": "Общее"},{"ctrl_index": 5},
                                      {"ctrl_index": 16}]).click()
                self.copy_data()
                employee_dict["ИИН"] = str(pythonRPA.clipboard.get())

                # ---> Номер договора
                pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": window_index_2}, {"ctrl_index": 0}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 4}, {"ctrl_index": 0}, {"title": "Общее"},
                                      {"title": "Трудовой договор"}]).click()
                pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": window_index_2}, {"ctrl_index": 0}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 4}, {"ctrl_index": 0},
                                      {"title": "Трудовой договор"}, {"ctrl_index": 5}, {"ctrl_index": 39}]).wait_appear(10)
                pythonRPA.time.delay(0.3)
                pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": window_index_2}, {"ctrl_index": 0}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 4}, {"ctrl_index": 0},
                                      {"title": "Трудовой договор"}, {"ctrl_index": 5}, {"ctrl_index": 39}]).click()
                self.copy_data()
                employee_dict["Номер договора"] = str(pythonRPA.clipboard.get())

                # ---> Срок договора
                pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": window_index_2}, {"ctrl_index": 0}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 4}, {"ctrl_index": 0},
                                      {"title": "Трудовой договор"}, {"ctrl_index": 5}, {"ctrl_index": 32}]).click()
                self.copy_data()
                contract_type = str(pythonRPA.clipboard.get())
                self.time_delay()
                employee_dict["Срок договора"] = contract_type_mapping(contract_type)

                if employee_dict["Срок договора"] == "Не найден в маппинге":
                    logs(str(employee_dict['ФИО']), employee_dict["ИИН"], employee_dict["Табельный номер"], "Нет в списке/Неправильно указан срок договора", "Прием")
                    self.time_delay()
                    pythonRPA.keyboard.press("esc")
                    self.time_delay()
                    pythonRPA.keyboard.press("ctrl+tab")
                    continue

                # ---> Дата заключения договора
                pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": window_index_2}, {"ctrl_index": 0}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 4}, {"ctrl_index": 0},
                                      {"title": "Трудовой договор"}, {"ctrl_index": 5}, {"ctrl_index": 18}]).click()
                self.copy_data()
                employee_dict["Дата заключения договора"] = str(pythonRPA.clipboard.get())

                # ---> Дата начала работы
                pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": window_index_2}, {"ctrl_index": 0}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 4}, {"ctrl_index": 0},
                                      {"title": "Трудовой договор"}, {"ctrl_index": 5}, {"ctrl_index": 19}]).click()
                self.copy_data()
                employee_dict["Дата начала работы"] = str(pythonRPA.clipboard.get())

                # ---> Дата окончания действия договора
                pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": window_index_2}, {"ctrl_index": 0}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 4}, {"ctrl_index": 0},
                                      {"title": "Трудовой договор"}, {"ctrl_index": 5}, {"ctrl_index": 20}]).click()
                self.copy_data()
                employment_end_date = str(pythonRPA.clipboard.get())
                pythonRPA.time.delay(0.3)

                if employment_end_date[0].isnumeric():
                    employee_dict["Дата окончания действия договора"] = employment_end_date
                else:
                    employee_dict["Дата окончания действия договора"] = ""

                # ---> Штатная должность
                pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": window_index_2}, {"ctrl_index": 0}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 4}, {"ctrl_index": 0},
                                      {"title": "Трудовой договор"}, {"ctrl_index": 5}, {"ctrl_index": 34}]).click()
                self.copy_data()
                employee_dict["Штатная должность"] = str(pythonRPA.clipboard.get())

                # ---> Режим рабочего времени
                pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": window_index_2}, {"ctrl_index": 0}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 4}, {"ctrl_index": 0},
                                      {"title": "Трудовой договор"}, {"ctrl_index": 5}, {"ctrl_index": 23}]).click()
                self.copy_data()
                working_schedule = str(pythonRPA.clipboard.get())
                employee_dict["Режим рабочего времени"] = regime_type_mapping(working_schedule)

                if employee_dict["Режим рабочего времени"] == "Не найден в маппинге":
                    logs(str(employee_dict['ФИО']), employee_dict["ИИН"], employee_dict["Табельный номер"],
                         "Нет в списке/Неправильно указан режим рабочего времени", "Прием")
                    self.time_delay()
                    pythonRPA.keyboard.press("esc")
                    self.time_delay()
                    pythonRPA.keyboard.press("ctrl+tab")
                    continue

                # ---> Должность
                pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": window_index_2}, {"ctrl_index": 0}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 4}, {"ctrl_index": 0},
                                      {"title": "Трудовой договор"}, {"ctrl_index": 5}, {"ctrl_index": 26}]).click()
                self.copy_data()
                position = str(pythonRPA.clipboard.get())
                self.time_delay()
                employee_dict["Должность"] = position_mapping(position)

                if employee_dict["Должность"] == "Не найден в маппинге":
                    logs(str(employee_dict['ФИО']), employee_dict["ИИН"], employee_dict["Табельный номер"],
                         "Нет в списке/Неправильно указана должность", "Прием")
                    self.time_delay()
                    pythonRPA.keyboard.press("esc")
                    self.time_delay()
                    pythonRPA.keyboard.press("ctrl+tab")
                    continue

                self.time_delay()
                pythonRPA.keyboard.press("esc")
                self.time_delay()
                pythonRPA.keyboard.press("ctrl+tab")

                if employee_dict["Место выполнения работы"] == {"address": "Не найден в маппинге"}:
                    logs(str(employee_dict['ФИО']), employee_dict["ИИН"], employee_dict["Табельный номер"],
                         "Нет в списке/Неправильно указан адрес места работы", "Прием")
                    continue

                print(employee_dict)
                self.employees_arr.append(employee_dict)
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                logs('', '', '', "Техническая ошибка", "Прием")

        # --- Exit from 1C ---
        pythonRPA.keyboard.press("esc", 2, 0.5)
        pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 0},
                              {"title": "Закрыть"}]).click()
        pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"},
                              {"depth_start": 5, "depth_end": 5, "title": "Да"}]).wait_appear(10)
        pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"},
                              {"depth_start": 5, "depth_end": 5, "title": "Да"}]).click()
        self.time_delay(3)

        # --- Return employees arr
        print(self.employees_arr)
        return self.employees_arr

    def get_list(self):
        self.oneC_app.start()

        self.auth()

        self.focus_1C()

        # --- Okno zayavki ubrat'---
        if pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16},
                                 {"ctrl_index": 0}]).is_exists():
            self.time_delay()
            pythonRPA.keyboard.press('esc')

        # --- Enter to Кадровый учет ---
        pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 0}, {"ctrl_index": 1}, {"ctrl_index": 0}, {"title": "Главное меню"},
                              {"title": "Кадровый учет"}]).click()
        pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 0},
                              {"title": "Кадровый учет"}, {"title": "Прием на работу в организаций"}]).wait_appear(5)
        pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 0},
                              {"title": "Кадровый учет"}, {"title": "Прием на работу в организаций"}]).click()

        # -- Set date ---
        pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 1}, {"ctrl_index": 0},
                              {"title": "Установить интервал дат..."}]).wait_appear(20)
        pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 1}, {"ctrl_index": 0},
                              {"title": "Установить интервал дат..."}]).click()
        pythonRPA.bySelector([{"title": "Настройка периода", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"},{"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"title": "Интервал"},
                              {"title": "Интервал"}]).wait_appear(15)
        self.time_delay()
        pythonRPA.keyboard.press("down", 7, 0.3)
        pythonRPA.keyboard.press("tab", 1, 0.3)
        pythonRPA.keyboard.write('01.11.2022')
        self.time_delay()
        pythonRPA.keyboard.press("tab", 1, 0.3)
        pythonRPA.keyboard.press("down", 7, 0.3)
        pythonRPA.keyboard.press("tab", 1, 0.3)
        pythonRPA.keyboard.write('31.12.2022')
        self.time_delay()
        pythonRPA.keyboard.press("ctrl+enter")
        self.time_delay()
        pythonRPA.keyboard.press("home")
        self.time_delay()

        g_arr = []
        prev_name = '23'
        pythonRPA.keyboard.press("down")
        while True:
            pythonRPA.keyboard.press("enter")
            self.time_delay()
            pythonRPA.keyboard.press("right", 2, 0.5)
            self.time_delay()
            self.copy_data()
            name = str(pythonRPA.clipboard.get()).replace("Сотрудник", "").replace("(осн.)", "").strip()
            print(name)
            g_arr.append(name)
            self.time_delay()
            pythonRPA.keyboard.press("esc")
            self.time_delay()
            pythonRPA.keyboard.press("down")
            self.time_delay()

            if name == prev_name:
                break
            prev_name = name

        print(g_arr)

        return g_arr



