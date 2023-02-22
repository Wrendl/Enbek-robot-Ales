import os
import sys
from oneC_func import auth, focus_1C, time_delay, copy_data, open_sotrudniki, find_employee_from_list
from pyPythonRPA.Robot import pythonRPA
from Sources_new.init import address_mapping, logs, contract_type_mapping, regime_type_mapping, position_mapping


class Uvolnenie:

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

        pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 0},
                              {"title": "Кадровый учет"}, {"title": "Увольнения из организаций"}]).wait_appear(5)

        pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 0},
                              {"title": "Кадровый учет"}, {"title": "Увольнения из организаций"}]).click()

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
        pythonRPA.bySelector([{
                                  "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                                  "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},
                              {"ctrl_index": 16}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0},
                              {"ctrl_index": 0}, {"ctrl_index": 1}, {"ctrl_index": 0},
                              {"title": "Действия"}]).wait_appear(30)
        pythonRPA.bySelector([{
                                  "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                                  "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},
                              {"ctrl_index": 16}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0},
                              {"ctrl_index": 0}, {"ctrl_index": 1}, {"ctrl_index": 0},
                              {"title": "Действия"}]).click()
        pythonRPA.bySelector([{
                                  "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                                  "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 0},
                              {"title": "Действия"}, {"title": "Вывести список..."}]).wait_appear(10)
        time_delay()
        pythonRPA.bySelector([{
                                  "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                                  "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 0},
                              {"title": "Действия"}, {"title": "Вывести список..."}]).click()
        pythonRPA.bySelector(
            [{"title": "Вывести список", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"}, {"ctrl_index": 0},
             {"ctrl_index": 0}, {"ctrl_index": 0},
             {"title": "ОК"}]).wait_appear(10)
        time_delay()
        pythonRPA.bySelector(
            [{"title": "Вывести список", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"}, {"ctrl_index": 0},
             {"ctrl_index": 0}, {"ctrl_index": 0},
             {"title": "ОК"}]).click()

        pythonRPA.bySelector([{
                                  "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                                  "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},
                              {"ctrl_index": 16}, {"ctrl_index": 1},
                              {"ctrl_index": 0}]).wait_appear(10)
        time_delay()
        pythonRPA.bySelector([{
                                  "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                                  "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},
                              {"ctrl_index": 16}, {"ctrl_index": 1},
                              {"ctrl_index": 0}]).click()

        # --- Copy all data ---
        copy_data()
        employees_count = len(str(pythonRPA.clipboard.get()).split("\n")) - 1
        employees_list = []

        # --- If no data return ---
        if employees_count == 0:
            print("0 employees - uvolnenie")
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
                employee_dict = {'ФИО': employee[5]}
                window_index_1 = 1

                find_employee_from_list(window_index_1, employee)

                pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": window_index_1 + 1}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 0}, {"title": "Увольнение"}, {"ctrl_index": 2},
                                      {"ctrl_index": 1}, {"ctrl_index": 3}]).wait_appear(15)
                time_delay()
                name = str(pythonRPA.bySelector([{"title":"1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name":"V8TopLevelFrame","backend":"uia"},{"ctrl_index":1},{"ctrl_index":16},{"ctrl_index": window_index_1 + 1},{"ctrl_index":0},{"ctrl_index":0},{"ctrl_index":0},{"title":"Увольнение"},{"ctrl_index":2},{"ctrl_index":1},{"ctrl_index":2}]).texts()[0]).replace("Сотрудник", "").replace("(осн.)", "").strip()

                # --- Дата расторжение ---
                pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": window_index_1 + 1}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 0}, {"title": "Увольнение"}, {"ctrl_index": 2},
                                      {"ctrl_index": 1}, {"ctrl_index": 3}]).click()
                copy_data()
                fired_date = str(pythonRPA.clipboard.get())
                pythonRPA.time.delay(0.3)
                employee_dict["Дата расторжение"] = fired_date

                # --- Причина ---
                pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},{"ctrl_index": 16}, {"ctrl_index": window_index_1 + 1}, {"ctrl_index": 0},{"ctrl_index": 0}, {"ctrl_index": 0}, {"title": "Увольнение"}, {"ctrl_index": 2},
                                      {"ctrl_index": 1}, {"ctrl_index": 8}]).click()
                copy_data()
                fired_reason = str(pythonRPA.clipboard.get())
                pythonRPA.time.delay(0.3)
                employee_dict["Причина"] = delete_contract_type_mapping(fired_reason)
                if employee_dict["Причина"] == "Не найден в маппинге":
                    logs([str(datetime.datetime.now().strftime("%H:%M")), str(employee_dict['ФИО']), '',
                          "Нет в списке/Неправильно указана причина увольнения", "Увольнение"])
                    pythonRPA.keyboard.press("esc", 1, 0.5)
                    continue

                # --- Switch to Sotrudniki tab ---
                pythonRPA.keyboard.press("esc", 1, 0.5)
                pythonRPA.keyboard.press("ctrl+tab")
                time_delay()
                focus_1C()

                # --- Find employee in sotrudniki with prefix -> " (осн.)" ---
                time_delay()
                pythonRPA.keyboard.press("ctrl+f")
                pythonRPA.bySelector([{"title": "Поиск", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"}, {"ctrl_index": 0},
                                      {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 12}]).wait_appear(10)
                time_delay()
                pythonRPA.bySelector([{"title": "Поиск", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"}, {"ctrl_index": 0},
                                      {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 12}]).click()
                time_delay()
                pythonRPA.keyboard.press("ctrl+a")
                time_delay()
                pythonRPA.keyboard.press("delete")
                time_delay()
                pythonRPA.keyboard.write(name + " (осн.)")
                time_delay()
                pythonRPA.keyboard.press("ctrl+enter")
                ok_button = [{
                                 "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                                 "class_name": "V8TopLevelFrame", "backend": "uia"}, {"title": "1С:Предприятие"},
                             {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"title": "OK"}]

                pythonRPA.bySelector(ok_button).wait_appear(5)
                if pythonRPA.bySelector(ok_button).is_exists():
                    pythonRPA.bySelector(ok_button).click()
                    time_delay()
                    pythonRPA.keyboard.press("ctrl+f")
                    pythonRPA.bySelector([{"title": "Поиск", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"},{"ctrl_index": 0},
                                          {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 12}]).wait_appear(10)
                    time_delay()
                    pythonRPA.bySelector([{"title": "Поиск", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"},{"ctrl_index": 0},
                                          {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 12}]).click()
                    time_delay()
                    pythonRPA.keyboard.press("ctrl+a")
                    time_delay()
                    pythonRPA.keyboard.press("delete")
                    time_delay()
                    pythonRPA.keyboard.write(name)
                    time_delay()
                    pythonRPA.keyboard.press("ctrl+enter")
                    time_delay()
                    if pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"},{"title": "1С:Предприятие"}, {"ctrl_index": 0}, {"ctrl_index": 0},{"ctrl_index": 0},
                                             {"title": "OK"}]).is_exists():
                        pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"},{"title": "1С:Предприятие"}, {"ctrl_index": 0}, {"ctrl_index": 0},{"ctrl_index": 0},
                                              {"title": "OK"}]).click()
                        time_delay()
                        logs([str(datetime.datetime.now().strftime("%H:%M")), str(employee_dict['ФИО']), '',
                              "Нет в сотрудниках", "Увольнение"])
                        pythonRPA.time.delay(0.3)
                        pythonRPA.keyboard.press("ctrl+tab", 1, 0.5)
                        continue

                focus_1C()
                pythonRPA.time.delay(0.5)
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
                except Exception as e:
                    logs([str(datetime.datetime.now().strftime("%H:%M")), str(employee_dict['ФИО']), '',
                          "Нет в сотрудниках", "Увольнение"])
                    time_delay()
                    pythonRPA.keyboard.press("ctrl+tab", 1, 0.5)
                    continue
                copy_data()
                iin = str(pythonRPA.clipboard.get())
                time_delay()
                employee_dict["ИИН"] = iin
                time_delay()
                pythonRPA.keyboard.press("esc", 1, 0.5)
                pythonRPA.keyboard.press("ctrl+tab", 1, 0.5)
                print(employee_dict)
                employees_arr.append(employee_dict)

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




