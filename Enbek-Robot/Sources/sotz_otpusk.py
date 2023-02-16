import datetime
import sys
import os
from pyPythonRPA.Robot import pythonRPA
from Sources.init import logs, vacation_mapping
import psutil


def sotz_otpusk(period, credentials, oneC_app):
    oneC_app.start()
    pythonRPA.bySelector(
        [{"title": "Запуск 1С:Предприятия", "class_name": "V8TopLevelFrameTaxiStarter", "backend": "uia"}]).wait_appear(20)
    pythonRPA.time.delay(0.3)
    pythonRPA.bySelector(
        [{"title": "Запуск 1С:Предприятия", "class_name": "V8TopLevelFrameTaxiStarter", "backend": "uia"}]).set_focus()
    # TODO Changed
    # ------------------------------------------------------------------------------------------------------------------
    # pythonRPA.bySelector(
    #     [{"title": "Запуск 1С:Предприятия", "class_name": "V8TopLevelFrameTaxiStarter", "backend": "uia"},
    #     {"ctrl_index": 1}, {"ctrl_index": 1}, {"ctrl_index": 0}, {"ctrl_index": 8}, {"ctrl_index": 0}]).double_click()
    pythonRPA.bySelector(
        [{"title": "Запуск 1С:Предприятия", "class_name": "V8TopLevelFrameTaxiStarter", "backend": "uia"},
         {"ctrl_index": 4}, {"ctrl_index": 1}, {"ctrl_index": 0}, {"ctrl_index": 8}, {"ctrl_index": 0}]).double_click()
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
    # pythonRPA.bySelector(
    #     [{"title": "Доступ к информационной базе", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"},
    #      {"title": "1С:Предприятие"}, {"ctrl_index": 1}, {"ctrl_index": 1}, {"ctrl_index": 0},
    #      {"ctrl_index": 2}]).click()
    pythonRPA.bySelector(
        [{"title":"Доступ к информационной базе","class_name":"V8NewLocalFrameBaseWnd","backend":"uia"},
         {"ctrl_index":0},{"ctrl_index":4},{"ctrl_index":1},{"ctrl_index":0},{"ctrl_index":2}]).click()
    # ------------------------------------------------------------------------------------------------------------------

    pythonRPA.time.delay(0.3)
    pythonRPA.keyboard.write(credentials["oneC_login"])
    pythonRPA.time.delay(0.3)

    pythonRPA.bySelector(
        [{"title": "Доступ к информационной базе", "class_name": "V8NewLocalFrameBaseWnd",
          "backend": "uia"}]).set_focus()

    # TODO Changed
    # ------------------------------------------------------------------------------------------------------------------
    # pythonRPA.bySelector(
    #     [{"title": "Доступ к информационной базе", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"},
    #      {"title": "1С:Предприятие"}, {"ctrl_index": 1}, {"ctrl_index": 1}, {"ctrl_index": 0},
    #      {"ctrl_index": 3}]).click()
    pythonRPA.bySelector(
        [{"title":"Доступ к информационной базе","class_name":"V8NewLocalFrameBaseWnd","backend":"uia"},
         {"ctrl_index":0},{"ctrl_index":4},{"ctrl_index":1},{"ctrl_index":0},{"ctrl_index":3}]).click()
    # ------------------------------------------------------------------------------------------------------------------

    pythonRPA.time.delay(0.3)
    pythonRPA.keyboard.write(credentials["oneC_password"])
    pythonRPA.time.delay(0.3)

    # TODO Changed
    # ------------------------------------------------------------------------------------------------------------------
    # pythonRPA.bySelector(
    #     [{"title": "Доступ к информационной базе", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"},
    #      {"title": "1С:Предприятие"}, {"ctrl_index": 1}, {"ctrl_index": 1}, {"ctrl_index": 0}, {"title": "OK"}]).click()
    pythonRPA.bySelector(
        [{"title":"Доступ к информационной базе","class_name":"V8NewLocalFrameBaseWnd","backend":"uia"},
         {"ctrl_index":0},{"ctrl_index":4},{"ctrl_index":1},{"ctrl_index":0}, {"title": "OK"}]).click()
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
    okno_zayavki = [{
                        "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                        "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1}, {"ctrl_index": 16},
                    {"ctrl_index": 0}]
    if pythonRPA.bySelector(okno_zayavki).is_exists():
        pythonRPA.keyboard.press('esc')
    pythonRPA.time.delay(0.3)
    employees_arr = []
    pythonRPA.bySelector([{
        "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
        "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1}, {"ctrl_index": 0},
        {"ctrl_index": 1}, {"ctrl_index": 0}, {"title": "Главное меню"},
        {"title": "Кадровый учет"}]).click()
    pythonRPA.bySelector([{"title":"1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name":"V8TopLevelFrame","backend":"uia"},{"ctrl_index":0},{"title":"Кадровый учет"},{"title":"Отпуска"}]).wait_appear(5)
    pythonRPA.time.delay(0.3)
    pythonRPA.bySelector([{"title":"1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name":"V8TopLevelFrame","backend":"uia"},{"ctrl_index":0},{"title":"Кадровый учет"},{"title":"Отпуска"}]).click()
    pythonRPA.time.delay(0.3)
    pythonRPA.keyboard.press("down", 2, 0.3)
    pythonRPA.keyboard.press("enter")
    pythonRPA.bySelector([{
                              "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                              "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1}, {"ctrl_index": 16},
                          {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0},
                          {"ctrl_index": 0}, {"title": "Установить интервал дат..."}]).wait_appear(20)
    pythonRPA.time.delay(1)
    pythonRPA.bySelector([{
                              "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                              "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1}, {"ctrl_index": 16},
                          {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0},
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
            {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0},
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
        {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0},
        {"ctrl_index": 0}, {"title": "Действия"}]).wait_appear(30)
    pythonRPA.bySelector([{
        "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
        "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1}, {"ctrl_index": 16},
        {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0},
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
            elif "по уходу" in str(employee).split("	")[7] or "беременн" in str(employee).split("	")[7] or "удоче" in str(employee).split("	")[7] or "усынов" in str(employee).split("	")[7] or "рождением" in str(employee).split("	")[7]:
                employees_list.append(str(employee).split("	"))
            else:
                continue
        pythonRPA.keyboard.press("esc")
        pythonRPA.time.delay(0.5)
        try:
            pythonRPA.bySelector([{"title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                                      "class_name": "V8TopLevelFrame", "backend": "uia"}]).maximize()
        except:
            pass
        pythonRPA.time.delay(0.5)
        for employee in employees_list:
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
                employee_dict = {}
                window_index_1 = 1
                print(employee)
                try_index = 0
                while True:
                    if try_index == 10:
                        break
                    try:
                        pythonRPA.bySelector([{
                    "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                    "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},
                    {"ctrl_index": 16}, {"ctrl_index": window_index_1}, {"ctrl_index": 0}, {"ctrl_index": 0},
                    {"ctrl_index": 0}, {"ctrl_index": 1},
                    {"title": str(employee[5]) + " Сотрудники"}]).double_click()
                        break
                    except:
                        try_index = try_index + 1
                        pythonRPA.time.delay(1)
                        pythonRPA.keyboard.press("pgdown")
                        pythonRPA.time.delay(1)
                pythonRPA.bySelector([{
                    "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                    "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},
                    {"ctrl_index": 16}, {"ctrl_index": window_index_1 + 1}, {"ctrl_index": 0}, {"ctrl_index": 0},
                    {"ctrl_index": 0}, {"ctrl_index": 11}, {"ctrl_index": 2}, {"ctrl_index": 0},
                    {"ctrl_index": 2}]).wait_appear(15)
                pythonRPA.time.delay(0.3)
                name = str(pythonRPA.bySelector([{
                    "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                    "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},
                    {"ctrl_index": 16}, {"ctrl_index": window_index_1 + 1}, {"ctrl_index": 0},
                    {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 11},
                    {"ctrl_index": 2}, {"ctrl_index": 0}, {"ctrl_index": 2}]).texts()[
                               0]).replace("Сотрудник", "").replace("(осн.)", "").strip()
                pythonRPA.bySelector([{
                                          "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                                          "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},
                                      {"ctrl_index": 16}, {"ctrl_index": window_index_1 + 1}, {"ctrl_index": 0},
                                      {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 11},
                                      {"ctrl_index": 2}, {"ctrl_index": 0}, {"ctrl_index": 2}]).right_click()
                pythonRPA.time.delay(0.5)
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
                print(employee_info)
                pythonRPA.time.delay(0.3)
                pythonRPA.keyboard.press("esc")
                pythonRPA.time.delay(0.3)
                # if employee_info.split("\n")[2].split("	")[6] == employee_info.split("\n")[3].split("	")[6] and employee_info.split("\n")[2].split("	")[7] == employee_info.split("\n")[3].split("	")[7] and employee_info.split("\n")[2].split("	")[8] == employee_info.split("\n")[3].split("	")[8] and employee_info.split("\n")[2].split("	")[1] == employee_info.split("\n")[3].split("	")[1] and employee_info.split("\n")[2].split("	")[9] == employee_info.split("\n")[3].split("	")[9]:
                #     pythonRPA.keyboard.press("esc", 1, 0.3)
                #     continue
                employee_dict["Номер табеля"] = employee_info.split("\n")[2].split("	")[1]
                employee_dict["Дата с"] = employee_info.split("\n")[3].split("	")[4]
                employee_dict["Дата по"] = employee_info.split("\n")[3].split("	")[5]
                if "беременн" in str(employee[7]) or "усынов" in str(employee[7]) or "удоче" in str(employee[7]) or "рождением" in str(employee[7]):
                    employee_dict["Тип отпуска"] = vacation_mapping("беременн")
                elif "по уходу" in str(employee[7]):
                    employee_dict["Тип отпуска"] = vacation_mapping("по уходу")
                if employee_dict["Тип отпуска"] == "Не найден в маппинге":
                    logs([str(datetime.datetime.now().strftime("%H:%M")), str(name), "Не внесён",
                          "Тип отпуска неправильный", "Отпускные"])
                    pythonRPA.keyboard.press("esc", 1, 0.3)
                    continue
                pythonRPA.keyboard.press("esc", 1, 0.5)
                pythonRPA.keyboard.press("ctrl+tab")
                pythonRPA.time.delay(0.5)
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
                    {"title": "Трудовой договор"}, {"ctrl_index": 5}, {"ctrl_index": 19}]).click()
                pythonRPA.time.delay(0.3)
                pythonRPA.keyboard.press("ctrl+a")
                pythonRPA.time.delay(0.3)
                pythonRPA.keyboard.press("ctrl+c")
                pythonRPA.time.delay(0.5)
                employment_end_date = str(pythonRPA.clipboard.get())
                pythonRPA.time.delay(0.3)
                print(employee_dict)
                employees_arr.append(employee_dict)
                pythonRPA.keyboard.press("esc", 1, 0.5)
                pythonRPA.keyboard.press("ctrl+tab", 1, 0.5)
            except:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                try:
                    logs([str(datetime.datetime.now().strftime("%H:%M")), str(employee[5]), "Не внесён",
                          str(exc_type) + " " + str(fname) + " " + str(exc_tb.tb_lineno), "Отпускные"])
                except:
                    print("without log")
                # PROCNAME = "1cv8.exe"
                # for proc in psutil.process_iter():
                #     # check whether the process name matches
                #     if proc.name() == PROCNAME:
                #         proc.kill()
                # pythonRPA.bySelector([{
                #                           "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                #                           "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 0},
                #                       {"title": "Закрыть"}]).click()
                # pythonRPA.bySelector([{
                #                           "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                #                           "class_name": "V8TopLevelFrame", "backend": "uia"},
                #                       {"depth_start": 5, "depth_end": 5, "title": "Да"}]).wait_appear(5)
                # pythonRPA.bySelector([{
                #                           "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                #                           "class_name": "V8TopLevelFrame", "backend": "uia"},
                #                       {"depth_start": 5, "depth_end": 5, "title": "Да"}]).click()
                # pythonRPA.time.delay(1)
                # oneC_app.start()
                # pythonRPA.bySelector(
                #     [{"title": "Запуск 1С:Предприятия", "class_name": "V8TopLevelFrameTaxiStarter", "backend": "uia"},
                #      {"ctrl_index": 1}, {"ctrl_index": 1}, {"ctrl_index": 0}, {"ctrl_index": 8},
                #      {"ctrl_index": 0}]).wait_appear(20)
                # pythonRPA.time.delay(0.3)
                # pythonRPA.bySelector(
                #     [{"title": "Запуск 1С:Предприятия", "class_name": "V8TopLevelFrameTaxiStarter", "backend": "uia"},
                #      {"ctrl_index": 1}, {"ctrl_index": 1}, {"ctrl_index": 0}, {"ctrl_index": 8},
                #      {"ctrl_index": 0}]).double_click()
                # pythonRPA.bySelector(
                #     [{"title": "Доступ к информационной базе", "class_name": "V8NewLocalFrameBaseWnd",
                #       "backend": "uia"},
                #      {"title": "1С:Предприятие"}, {"ctrl_index": 1}, {"ctrl_index": 1}, {"ctrl_index": 0},
                #      {"ctrl_index": 3}]).wait_appear(20)
                # pythonRPA.time.delay(0.3)
                # pythonRPA.bySelector(
                #     [{"title": "Доступ к информационной базе", "class_name": "V8NewLocalFrameBaseWnd",
                #       "backend": "uia"},
                #      {"title": "1С:Предприятие"}, {"ctrl_index": 1}, {"ctrl_index": 1}, {"ctrl_index": 0},
                #      {"ctrl_index": 2}]).click()
                # pythonRPA.time.delay(0.3)
                # pythonRPA.keyboard.write(credentials["oneC_login"])
                # pythonRPA.time.delay(0.3)
                # pythonRPA.bySelector(
                #     [{"title": "Доступ к информационной базе", "class_name": "V8NewLocalFrameBaseWnd",
                #       "backend": "uia"},
                #      {"title": "1С:Предприятие"}, {"ctrl_index": 1}, {"ctrl_index": 1}, {"ctrl_index": 0},
                #      {"ctrl_index": 3}]).click()
                # pythonRPA.time.delay(0.3)
                # pythonRPA.keyboard.write(credentials["oneC_password"])
                # pythonRPA.time.delay(0.3)
                # pythonRPA.bySelector(
                #     [{"title": "Доступ к информационной базе", "class_name": "V8NewLocalFrameBaseWnd",
                #       "backend": "uia"},
                #      {"title": "1С:Предприятие"}, {"ctrl_index": 1}, {"ctrl_index": 1}, {"ctrl_index": 0},
                #      {"title": "OK"}]).click()
                # pythonRPA.bySelector([{
                #     "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                #     "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1}, {"ctrl_index": 0},
                #     {"ctrl_index": 1}, {"ctrl_index": 0}, {"title": "Главное меню"},
                #     {"title": "Кадровый учет"}]).wait_appear(20)
                # pythonRPA.time.delay(0.3)
                # try:
                #     pythonRPA.bySelector([{
                #         "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                #         "class_name": "V8TopLevelFrame", "backend": "uia"}]).maximize()
                # except:
                #     pass
                # pythonRPA.time.delay(0.3)
                # pythonRPA.bySelector([{
                #     "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                #     "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1}, {"ctrl_index": 0},
                #     {"ctrl_index": 1}, {"ctrl_index": 0}, {"title": "Главное меню"},
                #     {"title": "Кадровый учет"}]).click()
                # pythonRPA.bySelector([{
                #                           "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                #                           "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 0},
                #                       {"title": "Кадровый учет"},
                #                       {"title": "Кадровые перемещения организаций"}]).wait_appear(5)
                # pythonRPA.time.delay(0.3)
                # pythonRPA.bySelector([{
                #                           "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                #                           "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 0},
                #                       {"title": "Кадровый учет"},
                #                       {"title": "Кадровые перемещения организаций"}]).click()
                # pythonRPA.bySelector([{
                #     "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                #     "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1}, {"ctrl_index": 16},
                #     {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 1},
                #     {"ctrl_index": 0}, {"title": "Установить интервал дат..."}]).wait_appear(20)
                # pythonRPA.time.delay(0.3)
                # pythonRPA.bySelector([{
                #     "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                #     "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1}, {"ctrl_index": 16},
                #     {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 1},
                #     {"ctrl_index": 0}, {"title": "Установить интервал дат..."}]).click()
                # pythonRPA.bySelector(
                #     [{"title": "Настройка периода", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"},
                #      {"ctrl_index": 0},
                #      {"ctrl_index": 0}, {"ctrl_index": 0}, {"title": "Интервал"}, {"title": "Интервал"}]).wait_appear(
                #     10)
                # pythonRPA.time.delay(0.3)
                # pythonRPA.keyboard.press("down", 7, 0.3)
                # pythonRPA.keyboard.press("tab", 1, 0.3)
                # pythonRPA.keyboard.write(str(period["since"]))
                # pythonRPA.time.delay(0.3)
                # pythonRPA.keyboard.press("tab", 1, 0.3)
                # pythonRPA.keyboard.press("down", 7, 0.3)
                # pythonRPA.keyboard.press("tab", 1, 0.3)
                # pythonRPA.keyboard.write(str(period["till"]))
                # pythonRPA.time.delay(0.3)
                # pythonRPA.keyboard.press("ctrl+enter")
                # pythonRPA.time.delay(0.5)
                # try:
                #     pythonRPA.bySelector([{
                #                               "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                #                               "class_name": "V8TopLevelFrame", "backend": "uia"}]).maximize()
                # except:
                #     pass
                # pythonRPA.time.delay(0.5)
                # pythonRPA.bySelector([{
                #     "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                #     "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},
                #     {"ctrl_index": 0}, {"ctrl_index": 3}, {"ctrl_index": 0}, {"title": "Главное меню"},
                #     {"title": "Кадровый учет"}]).click()
                # pythonRPA.bySelector([{
                #     "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                #     "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 0},
                #     {"title": "Кадровый учет"}, {"title": "Сотрудники"}]).wait_appear(5)
                # pythonRPA.time.delay(0.3)
                # pythonRPA.bySelector([{
                #     "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                #     "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 0},
                #     {"title": "Кадровый учет"}, {"title": "Сотрудники"}]).click()
                # pythonRPA.bySelector([{
                #     "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                #     "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1},
                #     {"ctrl_index": 16}, {"ctrl_index": 1}, {"ctrl_index": 0}, {"ctrl_index": 0},
                #     {"ctrl_index": 0}, {"ctrl_index": 3}, {"ctrl_index": 0}, {"ctrl_index": 0},
                #     {"ctrl_index": 0}, {"ctrl_index": 0},
                #     {"title": "Головной офис Наименование"}]).wait_appear(180)
                # pythonRPA.time.delay(0.5)
                # pythonRPA.keyboard.press("ctrl+tab")
                # pythonRPA.time.delay(1)
                # pythonRPA.keyboard.press("home")
                # pythonRPA.time.delay(2)
    pythonRPA.keyboard.press("esc", 2, 0.5)
    # PROCNAME = "1cv8.exe"
    # for proc in psutil.process_iter():
    #     # check whether the process name matches
    #     if proc.name() == PROCNAME:
    #         proc.kill()
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
