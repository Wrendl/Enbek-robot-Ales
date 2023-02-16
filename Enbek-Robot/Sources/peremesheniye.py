import datetime
import sys
import os
from Sources import logger
from pyPythonRPA.Robot import pythonRPA
from Sources.init import address_mapping, position_mapping, contract_type_mapping, logs, regime_type_mapping
import psutil


def peremesheniye(period, credentials, oneC_app):
    oneC_app.start()
    pythonRPA.bySelector(
        [{"title": "Запуск 1С:Предприятия", "class_name": "V8TopLevelFrameTaxiStarter", "backend": "uia"}]).wait_appear(
        20)
    pythonRPA.time.delay(0.3)
    pythonRPA.bySelector(
        [{"title": "Запуск 1С:Предприятия", "class_name": "V8TopLevelFrameTaxiStarter", "backend": "uia"}]).set_focus()

    # TODO Changed
    # ------------------------------------------------------------------------------------------------------------------
    pythonRPA.bySelector(
        [{"title": "Запуск 1С:Предприятия", "class_name": "V8TopLevelFrameTaxiStarter", "backend": "uia"},
        {"ctrl_index": 1}, {"ctrl_index": 1}, {"ctrl_index": 0}, {"ctrl_index": 8}, {"ctrl_index": 0}]).double_click()
    # pythonRPA.bySelector(
        # [{"title": "Запуск 1С:Предприятия", "class_name": "V8TopLevelFrameTaxiStarter", "backend": "uia"},
        #  {"ctrl_index": 4}, {"ctrl_index": 1}, {"ctrl_index": 0}, {"ctrl_index": 8}, {"ctrl_index": 0}]).double_click()
    # a = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"},
    #      {"ctrl_index":4},{"ctrl_index":1},{"ctrl_index":0},{"ctrl_index":8},{"ctrl_index":0}]
    # ------------------------------------------------------------------------------------------------------------------

    pythonRPA.bySelector(
        [{"title": "Доступ к информационной базе", "class_name": "V8NewLocalFrameBaseWnd",
          "backend": "uia"}]).wait_appear(20)
    pythonRPA.time.delay(0.3)
    pythonRPA.bySelector(
        [{"title": "Доступ к информационной базе", "class_name": "V8NewLocalFrameBaseWnd",
          "backend": "uia"}]).set_focus()

    # TODO Changed
    # ------------------------------------------------------------------------------------------------------------------
    pythonRPA.bySelector(
        [{"title": "Доступ к информационной базе", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"},
         {"title": "1С:Предприятие"}, {"ctrl_index": 1}, {"ctrl_index": 1}, {"ctrl_index": 0},
         {"ctrl_index": 2}]).click()
    # pythonRPA.bySelector(
    #     [{"title": "Доступ к информационной базе", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"},
    #      {"ctrl_index": 0}, {"ctrl_index": 4}, {"ctrl_index": 1}, {"ctrl_index": 0}, {"ctrl_index": 2}]).click()
    # ------------------------------------------------------------------------------------------------------------------

    pythonRPA.time.delay(0.3)
    pythonRPA.keyboard.write(credentials["oneC_login"])
    pythonRPA.time.delay(0.3)

    pythonRPA.bySelector(
        [{"title": "Доступ к информационной базе", "class_name": "V8NewLocalFrameBaseWnd",
          "backend": "uia"}]).set_focus()

    # TODO Changed
    # ------------------------------------------------------------------------------------------------------------------
    pythonRPA.bySelector(
        [{"title": "Доступ к информационной базе", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"},
         {"title": "1С:Предприятие"}, {"ctrl_index": 1}, {"ctrl_index": 1}, {"ctrl_index": 0},
         {"ctrl_index": 3}]).click()

    # pythonRPA.bySelector(
    #     [{"title": "Доступ к информационной базе", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"},
    #      {"ctrl_index": 0}, {"ctrl_index": 4}, {"ctrl_index": 1}, {"ctrl_index": 0}, {"ctrl_index": 3}]).click()
    # ------------------------------------------------------------------------------------------------------------------

    pythonRPA.time.delay(0.3)
    pythonRPA.keyboard.write(credentials["oneC_password"])
    pythonRPA.time.delay(0.3)

    # TODO Changed
    # ------------------------------------------------------------------------------------------------------------------
    pythonRPA.bySelector(
        [{"title": "Доступ к информационной базе", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"},
         {"title": "1С:Предприятие"}, {"ctrl_index": 1}, {"ctrl_index": 1}, {"ctrl_index": 0}, {"title": "OK"}]).click()
    # pythonRPA.bySelector(
    #     [{"title": "Доступ к информационной базе", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"},
    #      {"ctrl_index": 0}, {"ctrl_index": 4}, {"ctrl_index": 1}, {"ctrl_index": 0}, {"title": "OK"}]).click()
    # ------------------------------------------------------------------------------------------------------------------

    pythonRPA.bySelector([{"title":"Загрузка конфигурационной информации...","class_name":"V8NewLocalFrameBaseWnd","backend":"uia"},{"title":"1С:Предприятие"},{"ctrl_index":0},{"ctrl_index":0},{"ctrl_index":0},{"title":"Нет"}]).wait_appear(10)
    if pythonRPA.bySelector([{"title":"Загрузка конфигурационной информации...","class_name":"V8NewLocalFrameBaseWnd","backend":"uia"},{"title":"1С:Предприятие"},{"ctrl_index":0},{"ctrl_index":0},{"ctrl_index":0},{"title":"Нет"}]).is_exists() == True:
        pythonRPA.bySelector([{"title": "Загрузка конфигурационной информации...",
                               "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"}, {"title": "1С:Предприятие"},
                              {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"title": "Нет"}]).click()
    pythonRPA.bySelector([{
        "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
        "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1}, {"ctrl_index": 0},
        {"ctrl_index": 1}, {"ctrl_index": 0}, {"title": "Главное меню"},
        {"title": "Кадровый учет"}]).wait_appear(20)
    pythonRPA.time.delay(0.3)
    try:
        pythonRPA.bySelector([{
            "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
            "class_name": "V8TopLevelFrame", "backend": "uia"}]).maximize()
    except:
        pass
    pythonRPA.time.delay(0.3)
    # pythonRPA.keyboard.press('esc')
    okno_zayavki = [{"title":"1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name":"V8TopLevelFrame","backend":"uia"},{"ctrl_index":1},{"ctrl_index":16},{"ctrl_index":0}]
    if pythonRPA.bySelector(okno_zayavki).is_exists():
        pythonRPA.keyboard.press('esc')
    pythonRPA.time.delay(0.3)
    employees_arr = []
    pythonRPA.bySelector([{
        "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
        "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1}, {"ctrl_index": 0},
        {"ctrl_index": 1}, {"ctrl_index": 0}, {"title": "Главное меню"},
        {"title": "Кадровый учет"}]).click()
    pythonRPA.bySelector([{"title":"1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name":"V8TopLevelFrame","backend":"uia"},{"ctrl_index":0},{"title":"Кадровый учет"},{"title":"Кадровые перемещения организаций"}]).wait_appear(5)
    pythonRPA.time.delay(0.3)
    pythonRPA.bySelector([{"title":"1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name":"V8TopLevelFrame","backend":"uia"},{"ctrl_index":0},{"title":"Кадровый учет"},{"title":"Кадровые перемещения организаций"}]).click()
    pythonRPA.bySelector([{
                              "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                              "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1}, {"ctrl_index": 16},
                          {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 1},
                          {"ctrl_index": 0}, {"title": "Установить интервал дат..."}]).wait_appear(20)
    pythonRPA.time.delay(1)
    pythonRPA.bySelector([{
                              "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                              "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1}, {"ctrl_index": 16},
                          {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 1},
                          {"ctrl_index": 0}, {"title": "Установить интервал дат..."}]).click()
    pythonRPA.bySelector(
        [{"title": "Настройка периода", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"}, {"ctrl_index": 0},
         {"ctrl_index": 0}, {"ctrl_index": 0}, {"title": "Интервал"}, {"title": "Интервал"}]).wait_appear(5)
    if pythonRPA.bySelector(
        [{"title": "Настройка периода", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"}, {"ctrl_index": 0},
         {"ctrl_index": 0}, {"ctrl_index": 0}, {"title": "Интервал"}, {"title": "Интервал"}]).is_exists() == False:
        pythonRPA.bySelector([{
            "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
            "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1}, {"ctrl_index": 16},
            {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 1},
            {"ctrl_index": 0}, {"title": "Установить интервал дат..."}]).click()
        pythonRPA.bySelector(
            [{"title": "Настройка периода", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"},
             {"ctrl_index": 0},
             {"ctrl_index": 0}, {"ctrl_index": 0}, {"title": "Интервал"}, {"title": "Интервал"}]).wait_appear(5)
    pythonRPA.time.delay(0.3)
    pythonRPA.keyboard.press("down", 7, 0.3)
    pythonRPA.keyboard.press("tab", 1, 0.3)
    pythonRPA.keyboard.write(str(period["since"]))
    pythonRPA.time.delay(0.3)
    pythonRPA.keyboard.press("tab", 1, 0.3)
    pythonRPA.keyboard.press("down", 7, 0.3)
    pythonRPA.keyboard.press("tab", 1, 0.3)
    pythonRPA.keyboard.write(str(period["till"]))
    pythonRPA.time.delay(0.3)
    pythonRPA.keyboard.press("ctrl+enter")
    pythonRPA.time.delay(3)
    pythonRPA.bySelector([{
        "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
        "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1}, {"ctrl_index": 16},
        {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 1},
        {"ctrl_index": 0}, {"title": "Действия"}]).wait_appear(30)
    pythonRPA.bySelector([{
        "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
        "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1}, {"ctrl_index": 16},
        {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 1},
        {"ctrl_index": 0}, {"title": "Действия"}]).click()
    pythonRPA.bySelector([{
                              "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                              "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 0},
                          {"title": "Действия"}, {"title": "Вывести список..."}]).wait_appear(5)
    pythonRPA.time.delay(0.3)
    pythonRPA.bySelector([{
                              "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                              "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 0},
                          {"title": "Действия"}, {"title": "Вывести список..."}]).click()
    pythonRPA.bySelector(
        [{"title": "Вывести список", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"}, {"ctrl_index": 0},
         {"ctrl_index": 0}, {"ctrl_index": 0}, {"title": "ОК"}]).wait_appear(10)
    pythonRPA.time.delay(0.3)
    pythonRPA.bySelector(
        [{"title": "Вывести список", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"}, {"ctrl_index": 0},
         {"ctrl_index": 0}, {"ctrl_index": 0}, {"title": "ОК"}]).click()
    pythonRPA.bySelector([{
                              "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                              "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1}, {"ctrl_index": 16},
                          {"ctrl_index": 1}, {"ctrl_index": 0}]).wait_appear(10)
    pythonRPA.time.delay(0.3)
    pythonRPA.bySelector([{
                              "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                              "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1}, {"ctrl_index": 16},
                          {"ctrl_index": 1}, {"ctrl_index": 0}]).click()
    pythonRPA.time.delay(0.3)
    pythonRPA.keyboard.press("ctrl+a")
    pythonRPA.time.delay(0.3)
    pythonRPA.keyboard.press("ctrl+c")
    pythonRPA.time.delay(0.5)
    employees_count = len(str(pythonRPA.clipboard.get()).split("\n")) - 1
    employees_list = []
    if employees_count == 0:
        print("end")
    else:
        for employee in str(pythonRPA.clipboard.get()).split("\n"):
            if "Ручная корректировка" in str(employee):
                continue
            elif str(employee).split("	")[5] == "" or len(str(employee).split("	")[5]) == 0:
                continue
            else:
                employees_list.append(str(employee).split("	"))
        pythonRPA.keyboard.press("esc")
        pythonRPA.time.delay(0.5)
        try:
            pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                                      "class_name": "V8TopLevelFrame", "backend": "uia"}]).maximize()
        except:
            pass
        pythonRPA.time.delay(0.5)

        # employees_list = employees_list[3:4]

        for employee in employees_list: #TODO Changed
            cnt = 0
            try:
                if employees_list.index(employee) == 0:
                    pythonRPA.bySelector([{
                        "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                        "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},
                        {"ctrl_index": 0}, {"ctrl_index": 3}, {"ctrl_index": 0}, {"title": "Главное меню"},
                        {"title": "Кадровый учет"}]).click()
                    pythonRPA.bySelector([{
                        "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                        "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 0},
                        {"title": "Кадровый учет"}, {"title": "Сотрудники"}]).wait_appear(5)
                    pythonRPA.time.delay(0.3)
                    pythonRPA.bySelector([{
                        "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                        "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 0},
                        {"title": "Кадровый учет"}, {"title": "Сотрудники"}]).click()
                    pythonRPA.bySelector([{
                        "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                        "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},
                        {"ctrl_index": 16}, {"ctrl_index": 1}, {"ctrl_index": 0}, {"ctrl_index": 0},
                        {"ctrl_index": 0}, {"ctrl_index": 3}, {"ctrl_index": 0}, {"ctrl_index": 0},
                        {"ctrl_index": 0}, {"ctrl_index": 0},
                        {"title": "Головной офис Наименование"}]).wait_appear(180)
                    pythonRPA.time.delay(0.5)
                    pythonRPA.keyboard.press("ctrl+tab")
                    pythonRPA.time.delay(1)
                    pythonRPA.keyboard.press("home")
                    pythonRPA.time.delay(2)
                try:
                    pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для "
                                                    "Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш "
                                                    "Ажар Қанатқызы","class_name": "V8TopLevelFrame", "backend": "uia"}]
                                         ).maximize()
                except Exception as e:
                    print("Can't maximize", e)
                employee_dict = {}
                window_index_1 = 1
                employee_dict["Номер доп соглашения"] = "БН"
                employee_dict["ФИО"] = employee[5]
                # print(employee)
                try_index = 0
                while True:
                    if try_index == 10:
                        break
                    try:
                        pythonRPA.bySelector([{
                    "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                    "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},
                    {"ctrl_index": 16}, {"ctrl_index": window_index_1}, {"ctrl_index": 0}, {"ctrl_index": 0},
                    {"ctrl_index": 0}, {"ctrl_index": 0},
                    {"title": str(employee[5]) + " Сотрудники"}]).double_click()
                        break
                    except:
                        try_index = try_index + 1
                        pythonRPA.time.delay(1)
                        pythonRPA.keyboard.press("pgdown")
                        pythonRPA.time.delay(1)
                pythonRPA.time.delay(0.3)
                try:
                    pythonRPA.bySelector([{
                        "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                        "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},
                        {"ctrl_index": 16}, {"ctrl_index": window_index_1 + 1}, {"ctrl_index": 0},
                        {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 10},
                        {"ctrl_index": 3}, {"ctrl_index": 1}, {"ctrl_index": 2}]).wait_appear(15)

                    pythonRPA.time.delay(0.3)

                    pythonRPA.bySelector([{
                                              "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                                              "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},
                                          {"ctrl_index": 16}, {"ctrl_index": window_index_1 + 1}, {"ctrl_index": 0},
                                          {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 10},
                                          {"ctrl_index": 3}, {"ctrl_index": 1}, {"ctrl_index": 2}]).right_click()
                except:
                    count = 0
                    while True:
                        if count > 10:
                            break
                        try:
                            pythonRPA.keyboard.press("pgdown")
                            pythonRPA.time.delay(1)
                            pythonRPA.bySelector([{
                                "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                                "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},
                                {"ctrl_index": 16}, {"ctrl_index": window_index_1}, {"ctrl_index": 0},
                                {"ctrl_index": 0},
                                {"ctrl_index": 0}, {"ctrl_index": 0},
                                {"title": str(employee[5]) + " Сотрудники"}]).double_click()
                            pythonRPA.bySelector([{
                                "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                                "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},
                                {"ctrl_index": 16}, {"ctrl_index": window_index_1 + 1}, {"ctrl_index": 0},
                                {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 10},
                                {"ctrl_index": 3}, {"ctrl_index": 1}, {"ctrl_index": 2}]).wait_appear(15)
                            pythonRPA.time.delay(0.3)
                            pythonRPA.bySelector([{
                                "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                                "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},
                                {"ctrl_index": 16}, {"ctrl_index": window_index_1 + 1}, {"ctrl_index": 0},
                                {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 10},
                                {"ctrl_index": 3}, {"ctrl_index": 1}, {"ctrl_index": 2}]).right_click()
                            break
                        except:
                            count = count + 1
                            pythonRPA.time.delay(5)
                cnt = 1
                pythonRPA.time.delay(1)
                pythonRPA.keyboard.press("down", 13, 0.3)
                pythonRPA.keyboard.press("enter")
                pythonRPA.bySelector(
                    [{"title": "Вывести список", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"},
                     {"depth_start": 6, "depth_end": 6, "title": "Включить все"}]).wait_appear(5)
                pythonRPA.time.delay(0.3)
                pythonRPA.bySelector(
                    [{"title": "Вывести список", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"},
                     {"depth_start": 6, "depth_end": 6, "title": "Включить все"}]).click()
                pythonRPA.time.delay(0.3)
                pythonRPA.keyboard.press("ctrl+enter")
                pythonRPA.bySelector([{
                                          "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                                          "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},
                                      {"ctrl_index": 16}, {"ctrl_index": window_index_1 + 2}, {"ctrl_index": 0}]).wait_appear(5)
                pythonRPA.time.delay(0.3)
                pythonRPA.bySelector([{
                                          "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                                          "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},
                                      {"ctrl_index": 16}, {"ctrl_index": window_index_1 + 2}, {"ctrl_index": 0}]).click()
                pythonRPA.time.delay(0.3)
                pythonRPA.keyboard.press("ctrl+a")
                pythonRPA.time.delay(0.5)
                pythonRPA.keyboard.press("ctrl+c")
                pythonRPA.time.delay(0.5)
                employee_info = str(pythonRPA.clipboard.get())
                pythonRPA.time.delay(0.3)
                pythonRPA.keyboard.press("esc")
                pythonRPA.time.delay(0.3)
                if employee_info.split("\n")[2].split("	")[6] == employee_info.split("\n")[3].split("	")[6] and employee_info.split("\n")[2].split("	")[1] == employee_info.split("\n")[3].split("	")[1] and employee_info.split("\n")[2].split("	")[7] == employee_info.split("\n")[3].split("	")[7] and employee_info.split("\n")[2].split("	")[8] == employee_info.split("\n")[3].split("	")[8] and employee_info.split("\n")[2].split("	")[9] == employee_info.split("\n")[3].split("	")[9] and employee_info.split("\n")[2].split("	")[10] == employee_info.split("\n")[3].split("	")[10] and "продлен" not in str(employee[9]).lower():
                    pythonRPA.keyboard.press("esc", 1, 0.3)
                    continue
                prodleniye_date_bool = False
                if "продлен" in str(employee[9]).lower():
                    prodleniye_date_bool = True
                name = str(employee_info.split("\n")[2].split("	")[2]).replace("Сотрудник", "").replace("(осн.)", "").strip()
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
                    # employee_dict["Дата окончания действия дополнительного соглашения"] = employee_info.split("\n")[2].split("	")[3].split(".")[0] + "." + employee_info.split("\n")[2].split("	")[3].split(".")[1] + "." + str(int(employee_info.split("\n")[2].split("	")[3].split(".")[2]) + 1)
                else:
                    employee_dict["Дата окончания действия дополнительного соглашения"] = employee_info.split("\n")[3].split("	")[3]
                employee_dict["Табельный номер"] = employee_info.split("\n")[3].split("	")[1]
                employee_dict["Место выполнения работы"] = address_mapping(employee_info.split("\n")[3].split("	")[1])
                if employee_dict["Место выполнения работы"] == {"address": "Не найден в маппинге"}:
                    logs([str(datetime.datetime.now().strftime("%H:%M")), str(employee_dict['ФИО']), '', employee_dict["Табельный номер"],
                          "Нет в списке/Неправильно указан адрес места работы", "Перемещение"])
                    pythonRPA.keyboard.press("esc", 1, 0.3)
                    continue
                employee_dict["Должность"] = position_mapping(employee_info.split("\n")[3].split("	")[8])
                if employee_dict["Должность"] == "Не найден в маппинге":
                    logs([str(datetime.datetime.now().strftime("%H:%M")), str(employee_dict['ФИО']), '', employee_dict["Табельный номер"],
                          "Нет в списке/Неправильно указана должность", "Перемещение"])
                    pythonRPA.keyboard.press("esc", 1, 0.3)
                    continue
                if employee_info.split("\n")[3].split("	")[9] != "":
                    employee_dict["Штатная должность"] = employee_info.split("\n")[3].split("	")[10] + ", " + employee_info.split("\n")[3].split("	")[9]
                else:
                    employee_dict["Штатная должность"] = employee_info.split("\n")[3].split("	")[10]
                pythonRPA.keyboard.press("esc", 1, 0.5)
                pythonRPA.keyboard.press("ctrl+tab")
                pythonRPA.time.delay(0.5)

                cnt = 2

                try:
                    pythonRPA.bySelector([{
                                              "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                                              "class_name": "V8TopLevelFrame", "backend": "uia"}]).maximize()
                except:
                    pass

                pythonRPA.time.delay(0.3)
                pythonRPA.keyboard.press("ctrl+f")
                pythonRPA.bySelector(
                    [{"title": "Поиск", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"}, {"ctrl_index": 0},
                     {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 12}]).wait_appear(10)
                pythonRPA.time.delay(0.3)
                pythonRPA.bySelector(
                    [{"title": "Поиск", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"}, {"ctrl_index": 0},
                     {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 12}]).click()
                pythonRPA.time.delay(0.3)
                pythonRPA.keyboard.press("ctrl+a")
                pythonRPA.time.delay(0.3)
                pythonRPA.keyboard.press("delete")
                pythonRPA.time.delay(0.3)
                pythonRPA.keyboard.write(name + " (осн.)")
                pythonRPA.time.delay(0.3)
                pythonRPA.keyboard.press("ctrl+enter")
                pythonRPA.bySelector([{"title":"1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name":"V8TopLevelFrame","backend":"uia"},{"title":"1С:Предприятие"},{"ctrl_index":0},{"ctrl_index":0},{"ctrl_index":0},{"title":"OK"}]).wait_appear(5)
                if pythonRPA.bySelector([{"title":"1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name":"V8TopLevelFrame","backend":"uia"},{"title":"1С:Предприятие"},{"ctrl_index":0},{"ctrl_index":0},{"ctrl_index":0},{"title":"OK"}]).is_exists():
                    pythonRPA.bySelector([{
                                              "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                                              "class_name": "V8TopLevelFrame", "backend": "uia"},
                                          {"title": "1С:Предприятие"}, {"ctrl_index": 0}, {"ctrl_index": 0},
                                          {"ctrl_index": 0}, {"title": "OK"}]).click()
                    pythonRPA.time.delay(0.5)
                    pythonRPA.keyboard.press("ctrl+f")
                    pythonRPA.bySelector(
                        [{"title": "Поиск", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"},
                         {"ctrl_index": 0},
                         {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 12}]).wait_appear(10)
                    pythonRPA.time.delay(0.3)
                    pythonRPA.bySelector(
                        [{"title": "Поиск", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"},
                         {"ctrl_index": 0},
                         {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 12}]).click()
                    pythonRPA.time.delay(0.3)
                    pythonRPA.keyboard.press("ctrl+a")
                    pythonRPA.time.delay(0.3)
                    pythonRPA.keyboard.press("delete")
                    pythonRPA.time.delay(0.3)
                    pythonRPA.keyboard.write(name)
                    pythonRPA.time.delay(0.3)
                    pythonRPA.keyboard.press("ctrl+enter")

                try:
                    pythonRPA.bySelector([{
                        "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                        "class_name": "V8TopLevelFrame", "backend": "uia"}]).maximize()
                except:
                    pass

                pythonRPA.time.delay(0.5)
                pythonRPA.keyboard.press("enter")

                cnt = 3

                window_index_2 = 3
                if employees_list.index(employee) != 0:
                    window_index_2 = window_index_2 - 1
                pythonRPA.bySelector([{
                    "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                    "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},
                    {"ctrl_index": 16}, {"ctrl_index": window_index_2}, {"ctrl_index": 0}, {"ctrl_index": 0},
                    {"ctrl_index": 0}, {"ctrl_index": 4}, {"ctrl_index": 0}, {"title": "Общее"},
                    {"title": "Трудовой договор"}]).wait_appear(10)
                pythonRPA.time.delay(0.3)
                try:
                    pythonRPA.bySelector([{
                        "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                        "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},
                        {"ctrl_index": 16}, {"ctrl_index": 2}, {"ctrl_index": 0}, {"ctrl_index": 0},
                        {"ctrl_index": 0}, {"ctrl_index": 4}, {"ctrl_index": 0}, {"title": "Общее"},
                        {"ctrl_index": 5}, {"ctrl_index": 16}]).click()
                except:
                    pythonRPA.time.delay(0.5)
                    pythonRPA.keyboard.press("enter")
                    pythonRPA.bySelector([{
                        "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                        "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},
                        {"ctrl_index": 16}, {"ctrl_index": window_index_2}, {"ctrl_index": 0}, {"ctrl_index": 0},
                        {"ctrl_index": 0}, {"ctrl_index": 4}, {"ctrl_index": 0}, {"title": "Общее"},
                        {"title": "Трудовой договор"}]).wait_appear(10)
                    pythonRPA.time.delay(0.3)
                    pythonRPA.bySelector([{
                        "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                        "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},
                        {"ctrl_index": 16}, {"ctrl_index": 2}, {"ctrl_index": 0}, {"ctrl_index": 0},
                        {"ctrl_index": 0}, {"ctrl_index": 4}, {"ctrl_index": 0}, {"title": "Общее"},
                        {"ctrl_index": 5}, {"ctrl_index": 16}]).click()
                pythonRPA.time.delay(0.3)
                pythonRPA.keyboard.press("ctrl+a")
                pythonRPA.time.delay(0.3)
                pythonRPA.keyboard.press("ctrl+c")
                pythonRPA.time.delay(0.5)
                iin = str(pythonRPA.clipboard.get())
                pythonRPA.time.delay(0.3)
                employee_dict["ИИН"] = iin
                pythonRPA.bySelector([{
                    "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                    "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},
                    {"ctrl_index": 16}, {"ctrl_index": 2},{"ctrl_index":0},{"ctrl_index":0},{"ctrl_index":0},{"ctrl_index":4},{"ctrl_index":0},{"ctrl_index":8}]).click()
                pythonRPA.time.delay(0.3)
                pythonRPA.keyboard.press("ctrl+a")
                pythonRPA.time.delay(0.3)
                pythonRPA.keyboard.press("ctrl+c")
                pythonRPA.time.delay(0.5)
                employment_type = str(pythonRPA.clipboard.get())
                pythonRPA.time.delay(0.3)
                if employment_type == "Основное место работы":
                    employee_dict["Вид работы"] = "основная работа"
                else:
                    employee_dict["Вид работы"] = "работа по совместительству"
                pythonRPA.bySelector([{
                    "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                    "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},
                    {"ctrl_index": 16}, {"ctrl_index": 2}, {"ctrl_index": 0}, {"ctrl_index": 0},
                    {"ctrl_index": 0}, {"ctrl_index": 4}, {"ctrl_index": 0}, {"title": "Общее"},
                    {"title": "Трудовой договор"}]).click()
                pythonRPA.bySelector([{
                    "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                    "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},
                    {"ctrl_index": 16}, {"ctrl_index": 2}, {"ctrl_index": 0}, {"ctrl_index": 0},
                    {"ctrl_index": 0}, {"ctrl_index": 4}, {"ctrl_index": 0},
                    {"title": "Трудовой договор"}, {"ctrl_index": 5}, {"ctrl_index": 39}]).wait_appear(10)
                pythonRPA.time.delay(0.3)
                pythonRPA.bySelector([{
                    "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                    "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},
                    {"ctrl_index": 16}, {"ctrl_index": 2}, {"ctrl_index": 0}, {"ctrl_index": 0},
                    {"ctrl_index": 0}, {"ctrl_index": 4}, {"ctrl_index": 0},
                    {"title": "Трудовой договор"}, {"ctrl_index": 5}, {"ctrl_index": 20}]).click()
                pythonRPA.time.delay(0.3)
                pythonRPA.keyboard.press("ctrl+a")
                pythonRPA.time.delay(0.3)
                pythonRPA.keyboard.press("ctrl+c")
                pythonRPA.time.delay(0.5)
                employment_end_date = str(pythonRPA.clipboard.get())
                pythonRPA.time.delay(0.3)
                if prodleniye_date_bool and employee_dict["Дата окончания действия дополнительного соглашения"] != "":
                    employee_dict["Дата окончания действия трудового договора"] = employee_dict["Дата окончания действия дополнительного соглашения"]
                elif employment_end_date[0].isnumeric():
                    employee_dict["Дата окончания действия трудового договора"] = employment_end_date
                    if okonchaniye_dop_soglasheniya_bool == False:
                        employee_dict["Дата окончания действия дополнительного соглашения"] = employment_end_date
                else:
                    employee_dict["Дата окончания действия трудового договора"] = ""
                    if okonchaniye_dop_soglasheniya_bool == False:
                        employee_dict["Дата окончания действия дополнительного соглашения"] = ""
                pythonRPA.bySelector([{
                    "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                    "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},
                    {"ctrl_index": 16}, {"ctrl_index": 2}, {"ctrl_index": 0}, {"ctrl_index": 0},
                    {"ctrl_index": 0}, {"ctrl_index": 4}, {"ctrl_index": 0},
                    {"title": "Трудовой договор"}, {"ctrl_index": 5}, {"ctrl_index": 23}]).click()
                pythonRPA.time.delay(0.3)
                pythonRPA.keyboard.press("ctrl+a")
                pythonRPA.time.delay(0.3)
                pythonRPA.keyboard.press("ctrl+c")
                pythonRPA.time.delay(0.5)
                working_schedule = str(pythonRPA.clipboard.get())
                pythonRPA.time.delay(0.3)
                employee_dict["Режим рабочего времени"] = regime_type_mapping(working_schedule)
                if employee_dict["Режим рабочего времени"] == "Не найден в маппинге":
                    logs([str(datetime.datetime.now().strftime("%H:%M")), str(employee_dict['ФИО']), employee_dict["ИИН"], employee_dict["Табельный номер"],
                          "Нет в списке/Неправильно указан режим рабочего времени", "Перемещение"])
                    pythonRPA.keyboard.press("esc", 1, 0.5)
                    pythonRPA.keyboard.press("ctrl+tab", 1, 0.5)
                    continue
                pythonRPA.time.delay(0.3)
                print(employee_dict)
                employees_arr.append(employee_dict)
                pythonRPA.keyboard.press("esc", 1, 0.5)
                cnt = 2
                pythonRPA.keyboard.press("ctrl+tab", 1, 0.5)
                cnt = 0
            except Exception as e:
                logger.logger.exception(e)
                try:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno)
                    logs([str(datetime.datetime.now().strftime("%H:%M")), '', '', ''
                          "Техническая ошибка", "Перемещение"])
                except:
                    print("without log")

                if cnt == 1:  # Состояние 1 когда открыто инфо employee в перемещениях
                    pythonRPA.time.delay(1)
                    pythonRPA.keyboard.press("esc", 1, 0.5)
                    pythonRPA.time.delay(1)
                if cnt == 2:  # Состояние 2 когда открыт таб "Сотрудники"
                    pythonRPA.time.delay(1)
                    pythonRPA.keyboard.press("ctrl+tab", 1, 0.5)
                    pythonRPA.time.delay(1)
                if cnt == 3:  # Состояние 3 когда открыто инфо employee в табе "Сотрудники"
                    pythonRPA.time.delay(1)
                    pythonRPA.keyboard.press("esc", 1, 0.5)
                    pythonRPA.keyboard.press("ctrl+tab", 1, 0.5)
                    pythonRPA.time.delay(1)

    pythonRPA.keyboard.press("esc", 2, 0.5)
    pythonRPA.bySelector([{
                              "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                              "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 0},
                          {"title": "Закрыть"}]).click()
    pythonRPA.bySelector([{
                              "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                              "class_name": "V8TopLevelFrame", "backend": "uia"},
                          {"depth_start": 5, "depth_end": 5, "title": "Да"}]).wait_appear(5)
    pythonRPA.bySelector([{
                              "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                              "class_name": "V8TopLevelFrame", "backend": "uia"},
                          {"depth_start": 5, "depth_end": 5, "title": "Да"}]).click()
    pythonRPA.time.delay(1)
    print(employees_arr)
    return employees_arr
