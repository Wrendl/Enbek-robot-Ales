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

        # --- Iteration, ---
        for employee in employees_list:
            try:
                # --- Open sotrudniki ---
                if employees_list.index(employee) == 0:
                    open_sotrudniki()
                focus_1C()

                # --- Find employee from list ---
                employee_dict = {'ФИО': employee[5],
                                 "Номер доп соглашения": "БН"}
                window_index_1 = 1

                find_employee_from_list(window_index_1, employee)
                time_delay()

                # --- Взять все данные с карточки для сверки пред должности ---
                try:
                    pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": window_index_1 + 1}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 10},{"ctrl_index": 3}, {"ctrl_index": 1},
                                          {"ctrl_index": 2}]).wait_appear(15)
                    time_delay()
                    pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": window_index_1 + 1}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 10},{"ctrl_index": 3}, {"ctrl_index": 1},
                                          {"ctrl_index": 2}]).right_click()
                except Exception as e:
                    count = 0
                    while True:
                        if count > 10:
                            break
                        try:
                            pythonRPA.keyboard.press("pgdown")
                            time_delay()
                            pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": window_index_1}, {"ctrl_index": 0},{"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 0},
                                                  {"title": str(employee[5]) + " Сотрудники"}]).double_click()
                            pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": window_index_1 + 1}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 10},{"ctrl_index": 3}, {"ctrl_index": 1},
                                                  {"ctrl_index": 2}]).wait_appear(15)
                            time_delay()
                            pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": window_index_1 + 1}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 10},{"ctrl_index": 3}, {"ctrl_index": 1},
                                                  {"ctrl_index": 2}]).right_click()
                            break
                        except Exception as e:
                            count = count + 1
                            time_delay(5)
                time_delay(2)
                pythonRPA.keyboard.press("down", 13, 0.3)
                pythonRPA.keyboard.press("enter")
                pythonRPA.bySelector([{"title": "Вывести список", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"},
                                      {"depth_start": 6, "depth_end": 6, "title": "Включить все"}]).wait_appear(5)
                time_delay()
                pythonRPA.bySelector([{"title": "Вывести список", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"},
                                      {"depth_start": 6, "depth_end": 6, "title": "Включить все"}]).click()
                time_delay()
                pythonRPA.keyboard.press("ctrl+enter")
                pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": window_index_1 + 2},
                                      {"ctrl_index": 0}]).wait_appear(5)
                time_delay()
                pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": window_index_1 + 2},
                                      {"ctrl_index": 0}]).click()
                copy_data()
                employee_info = str(pythonRPA.clipboard.get())
                time_delay()
                pythonRPA.keyboard.press("esc")
                time_delay()

                # --- Проверяет продлен ли данное доп согл ---
                if employee_info.split("\n")[2].split("	")[6] == employee_info.split("\n")[3].split("	")[6] and \
                        employee_info.split("\n")[2].split("	")[1] == employee_info.split("\n")[3].split("	")[1] and \
                        employee_info.split("\n")[2].split("	")[7] == employee_info.split("\n")[3].split("	")[7] and \
                        employee_info.split("\n")[2].split("	")[8] == employee_info.split("\n")[3].split("	")[8] and \
                        employee_info.split("\n")[2].split("	")[9] == employee_info.split("\n")[3].split("	")[9] and \
                        employee_info.split("\n")[2].split("	")[10] == employee_info.split("\n")[3].split("	")[
                    10] and "продлен" not in str(employee[9]).lower():
                    pythonRPA.keyboard.press("esc", 1, 0.3)
                    continue
                prodleniye_date_bool = False
                if "продлен" in str(employee[9]).lower():
                    prodleniye_date_bool = True
                name = str(employee_info.split("\n")[2].split("	")[2]).replace("Сотрудник", "").replace("(осн.)", "").strip()

                # --- Дата начала действия доп соглашения, Дата заключения дополнительного соглашения, Срок договора ---
                employee_dict["Дата начала действия доп соглашения"] = employee_info.split("\n")[2].split("	")[3]
                employee_dict["Дата заключения дополнительного соглашения"] = employee_info.split("\n")[2].split("	")[3]
                employee_dict["Срок договора"] = contract_type_mapping(employee_info.split("\n")[3].split("	")[6])

                if employee_dict["Срок договора"] == "Не найден в маппинге":
                    logs([str(datetime.datetime.now().strftime("%H:%M")), str(employee_dict['ФИО']), '', '',
                          "Нет в списке/Неправильно указан срок договора", "Перемещение"])
                    pythonRPA.keyboard.press("esc", 1, 0.3)
                    continue

                okonchaniye_dop_soglasheniya_bool = True
                if employee_info.split("\n")[3].split("	")[3] == "" and employee_info.split("\n")[3].split("	")[6] == "На определенный срок":
                    okonchaniye_dop_soglasheniya_bool = False
                else:
                    employee_dict["Дата окончания действия дополнительного соглашения"] = \
                    employee_info.split("\n")[3].split("	")[3]

                # --- Табельный номер, Место выполнения работы ---
                employee_dict["Табельный номер"] = employee_info.split("\n")[3].split("	")[1]
                employee_dict["Место выполнения работы"] = address_mapping(employee_info.split("\n")[3].split("	")[1])

                if employee_dict["Место выполнения работы"] == {"address": "Не найден в маппинге"}:
                    logs([str(datetime.datetime.now().strftime("%H:%M")), str(employee_dict['ФИО']), '',
                          employee_dict["Табельный номер"],
                          "Нет в списке/Неправильно указан адрес места работы", "Перемещение"])
                    pythonRPA.keyboard.press("esc", 1, 0.3)
                    continue

                # --- Должность, Штатная должность ---
                employee_dict["Должность"] = position_mapping(employee_info.split("\n")[3].split("	")[8])
                if employee_dict["Должность"] == "Не найден в маппинге":
                    logs([str(datetime.datetime.now().strftime("%H:%M")), str(employee_dict['ФИО']), '',
                          employee_dict["Табельный номер"],
                          "Нет в списке/Неправильно указана должность", "Перемещение"])
                    pythonRPA.keyboard.press("esc", 1, 0.3)
                    continue

                if employee_info.split("\n")[3].split("	")[9] != "":
                    employee_dict["Штатная должность"] = employee_info.split("\n")[3].split("	")[10] + ", " + \
                                                         employee_info.split("\n")[3].split("	")[9]
                else:
                    employee_dict["Штатная должность"] = employee_info.split("\n")[3].split("	")[10]

                # --- Switch to Sotrudniki tab ---
                pythonRPA.keyboard.press("esc", 1, 0.5)
                pythonRPA.keyboard.press("ctrl+tab")
                time_delay()
                focus_1C()
                time_delay()

                # --- Find employee in sotrudniki with prefix -> " (осн.)" ---
                pythonRPA.keyboard.press("ctrl+f")
                pythonRPA.bySelector(
                    [{"title": "Поиск", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"}, {"ctrl_index": 0},
                     {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 12}]).wait_appear(10)
                time_delay()
                pythonRPA.bySelector(
                    [{"title": "Поиск", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"}, {"ctrl_index": 0},
                     {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 12}]).click()
                time_delay()
                pythonRPA.keyboard.press("ctrl+a")
                time_delay()
                pythonRPA.keyboard.press("delete")
                time_delay()
                pythonRPA.keyboard.write(name + " (осн.)")
                time_delay()
                pythonRPA.keyboard.press("ctrl+enter")

                # --- Find employee in sotrudniki without prefix, if it didn't find before ---
                ok_button = [{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"title": "1С:Предприятие"},{"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"title": "OK"}]

                pythonRPA.bySelector(ok_button).wait_appear(5)
                if pythonRPA.bySelector(ok_button).is_exists():
                    pythonRPA.bySelector(ok_button).click()
                    time_delay()
                    pythonRPA.keyboard.press("ctrl+f")
                    pythonRPA.bySelector([{"title": "Поиск", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"},{"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 0},
                                          {"ctrl_index": 12}]).wait_appear(10)
                    time_delay()
                    pythonRPA.bySelector([{"title": "Поиск", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"},{"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 0},
                                          {"ctrl_index": 12}]).click()
                    time_delay()
                    pythonRPA.keyboard.press("ctrl+a")
                    time_delay()
                    pythonRPA.keyboard.press("delete")
                    time_delay()
                    pythonRPA.keyboard.write(name)
                    time_delay()
                    pythonRPA.keyboard.press("ctrl+enter")

                # --- Enter sotrudniki card ---
                focus_1C()
                time_delay()
                pythonRPA.keyboard.press("enter")

                window_index_2 = 3
                if employees_list.index(employee) != 0:
                    window_index_2 = window_index_2 - 1
                pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": window_index_2}, {"ctrl_index": 0}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 4}, {"ctrl_index": 0}, {"title": "Общее"},
                                      {"title": "Трудовой договор"}]).wait_appear(10)
                time_delay()
                try:
                    pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": 2}, {"ctrl_index": 0}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 4}, {"ctrl_index": 0}, {"title": "Общее"},{"ctrl_index": 5},
                                          {"ctrl_index": 16}]).click()
                except:
                    time_delay()
                    pythonRPA.keyboard.press("enter")
                    pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": window_index_2}, {"ctrl_index": 0}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 4}, {"ctrl_index": 0}, {"title": "Общее"},
                                          {"title": "Трудовой договор"}]).wait_appear(10)
                    time_delay()
                    pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": 2}, {"ctrl_index": 0}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 4}, {"ctrl_index": 0}, {"title": "Общее"},
                                          {"ctrl_index": 5}, {"ctrl_index": 16}]).click()
                copy_data()

                # --- ИИН ---
                iin = str(pythonRPA.clipboard.get())
                pythonRPA.time.delay(0.3)
                employee_dict["ИИН"] = iin

                # --- Вид работы ---
                pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": 2}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0},{"ctrl_index": 4}, {"ctrl_index": 0},
                                      {"ctrl_index": 8}]).click()
                copy_data()
                employment_type = str(pythonRPA.clipboard.get())
                pythonRPA.time.delay(0.3)
                if employment_type == "Основное место работы":
                    employee_dict["Вид работы"] = "основная работа"
                else:
                    employee_dict["Вид работы"] = "работа по совместительству"
                pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": 2}, {"ctrl_index": 0}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 4}, {"ctrl_index": 0}, {"title": "Общее"},
                                      {"title": "Трудовой договор"}]).click()
                pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": 2}, {"ctrl_index": 0}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 4}, {"ctrl_index": 0},
                                      {"title": "Трудовой договор"}, {"ctrl_index": 5}, {"ctrl_index": 39}]).wait_appear(10)
                time_delay()

                # --- Дата окончания действия дополнительного соглашения ---
                pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": 2}, {"ctrl_index": 0}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 4}, {"ctrl_index": 0},
                                      {"title": "Трудовой договор"}, {"ctrl_index": 5}, {"ctrl_index": 20}]).click()
                copy_data()
                employment_end_date = str(pythonRPA.clipboard.get())
                time_delay()
                if prodleniye_date_bool and employee_dict["Дата окончания действия дополнительного соглашения"] != "":
                    employee_dict["Дата окончания действия трудового договора"] = employee_dict[
                        "Дата окончания действия дополнительного соглашения"]
                elif employment_end_date[0].isnumeric():
                    employee_dict["Дата окончания действия трудового договора"] = employment_end_date
                    if okonchaniye_dop_soglasheniya_bool == False:
                        employee_dict["Дата окончания действия дополнительного соглашения"] = employment_end_date
                else:
                    employee_dict["Дата окончания действия трудового договора"] = ""
                    if okonchaniye_dop_soglasheniya_bool == False:
                        employee_dict["Дата окончания действия дополнительного соглашения"] = ""

                # --- Режим рабочего времени ---
                pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": 2}, {"ctrl_index": 0}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 4}, {"ctrl_index": 0},
                                      {"title": "Трудовой договор"}, {"ctrl_index": 5}, {"ctrl_index": 23}]).click()
                copy_data()
                working_schedule = str(pythonRPA.clipboard.get())
                time_delay()
                employee_dict["Режим рабочего времени"] = regime_type_mapping(working_schedule)
                if employee_dict["Режим рабочего времени"] == "Не найден в маппинге":
                    logs([str(datetime.datetime.now().strftime("%H:%M")), str(employee_dict['ФИО']), employee_dict["ИИН"],
                          employee_dict["Табельный номер"],
                          "Нет в списке/Неправильно указан режим рабочего времени", "Перемещение"])
                    pythonRPA.keyboard.press("esc", 1, 0.5)
                    pythonRPA.keyboard.press("ctrl+tab", 1, 0.5)
                    continue
                time_delay()
                print(employee_dict)
                employees_arr.append(employee_dict)
                pythonRPA.keyboard.press("esc", 1, 0.5)
                pythonRPA.keyboard.press("ctrl+tab", 1, 0.5)

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
                              {"depth_start": 5, "depth_end": 5, "title": "Да"}]).wait_appear(5)
        pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"},
                              {"depth_start": 5, "depth_end": 5, "title": "Да"}]).click()

        # --- Return employees arr
        print(employees_arr)
        return employees_arr




