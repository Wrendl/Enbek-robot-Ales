import time

from pyPythonRPA.Robot import pythonRPA
import datetime
from Sources.init import delete_contract_type_mapping, logs
import psutil
import os
import sys


def uvolneniye(period, credentials, oneC_app):
    oneC_app.start()
    pythonRPA.bySelector(
        [{"title": "Запуск 1С:Предприятия", "class_name": "V8TopLevelFrameTaxiStarter", "backend": "uia"}]).wait_appear(20)
    pythonRPA.time.delay(0.3)
    pythonRPA.bySelector(
        [{"title": "Запуск 1С:Предприятия", "class_name": "V8TopLevelFrameTaxiStarter", "backend": "uia"}]).set_focus()
    # TODO Changed
    # ------------------------------------------------------------------------------------------------------------------
    pythonRPA.bySelector(
        [{"title": "Запуск 1С:Предприятия", "class_name": "V8TopLevelFrameTaxiStarter", "backend": "uia"},
        {"ctrl_index": 1}, {"ctrl_index": 1}, {"ctrl_index": 0}, {"ctrl_index": 8}, {"ctrl_index": 0}]).double_click()
    # pythonRPA.bySelector(
    #     [{"title": "Запуск 1С:Предприятия", "class_name": "V8TopLevelFrameTaxiStarter", "backend": "uia"},
    #      {"ctrl_index": 4}, {"ctrl_index": 1}, {"ctrl_index": 0}, {"ctrl_index": 8}, {"ctrl_index": 0}]).double_click()
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

    pythonRPA.bySelector(
        [{"title": "Загрузка конфигурационной информации...", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"},
         {"title": "1С:Предприятие"}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0},
         {"title": "Нет"}]).wait_appear(10)
    if pythonRPA.bySelector([{"title": "Загрузка конфигурационной информации...",
                              "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"}, {"title": "1С:Предприятие"},
                             {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0},
                             {"title": "Нет"}]).is_exists() == True:
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
    pythonRPA.bySelector([{"title":"1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name":"V8TopLevelFrame","backend":"uia"},{"ctrl_index":0},{"title":"Кадровый учет"},{"title":"Увольнения из организаций"}]).wait_appear(5)
    pythonRPA.time.delay(0.3)
    pythonRPA.bySelector([{"title":"1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name":"V8TopLevelFrame","backend":"uia"},{"ctrl_index":0},{"title":"Кадровый учет"},{"title":"Увольнения из организаций"}]).click()
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
                employee_dict["ФИО"] = employee[5]
                # print(employee)
                window_index_1 = 1
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
                pythonRPA.bySelector([{"title":"1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name":"V8TopLevelFrame","backend":"uia"},{"ctrl_index":1},{"ctrl_index":16},{"ctrl_index": window_index_1 + 1},{"ctrl_index":0},{"ctrl_index":0},{"ctrl_index":0},{"title":"Увольнение"},{"ctrl_index":2},{"ctrl_index":1},{"ctrl_index":3}]).wait_appear(15)
                pythonRPA.time.delay(0.3)
                # name = str(pythonRPA.bySelector([{"title":"1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name":"V8TopLevelFrame","backend":"uia"},{"ctrl_index":1},{"ctrl_index":16},{"ctrl_index": window_index_1 + 1},{"ctrl_index":0},{"ctrl_index":0},{"ctrl_index":0},{"title":"Увольнение"},{"ctrl_index":2},{"ctrl_index":1},{"ctrl_index":2}]).texts()[0]).replace("Сотрудник", "").replace("(осн.)", "").strip()
                try:
                    name = str(pythonRPA.bySelector([{"title":"1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name":"V8TopLevelFrame","backend":"uia"},{"ctrl_index":1},{"ctrl_index":16},{"ctrl_index": window_index_1 + 1},{"ctrl_index":0},{"ctrl_index":0},{"ctrl_index":0},{"title":"Увольнение"},{"ctrl_index":2},{"ctrl_index":1},{"ctrl_index":2}]).texts()[0]).replace("Сотрудник", "").replace("(осн.)", "").strip()
                except:
                    pythonRPA.bySelector([{"title":"1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name":"V8TopLevelFrame","backend":"uia"},{"ctrl_index":1},{"ctrl_index":16},{"ctrl_index": window_index_1 + 1},{"ctrl_index":0},{"ctrl_index":0},{"ctrl_index":0},{"title":"Увольнение"},{"ctrl_index":2},{"ctrl_index":1},{"ctrl_index":2}]).click()
                    pythonRPA.time.delay(0.3)
                    pythonRPA.keyboard.press("ctrl+a")
                    pythonRPA.time.delay(0.3)
                    pythonRPA.keyboard.press("ctrl+c")
                    pythonRPA.time.delay(0.5)
                    name = str(pythonRPA.clipboard.get()).replace("Сотрудник", "").replace("(осн.)", "").strip()
                    pythonRPA.time.delay(0.3)
                pythonRPA.bySelector([{"title":"1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name":"V8TopLevelFrame","backend":"uia"},{"ctrl_index":1},{"ctrl_index":16},{"ctrl_index": window_index_1 + 1},{"ctrl_index":0},{"ctrl_index":0},{"ctrl_index":0},{"title":"Увольнение"},{"ctrl_index":2},{"ctrl_index":1},{"ctrl_index":3}]).click()
                pythonRPA.time.delay(0.3)
                pythonRPA.keyboard.press("ctrl+a")
                pythonRPA.time.delay(0.3)
                pythonRPA.keyboard.press("ctrl+c")
                pythonRPA.time.delay(0.5)
                fired_date = str(pythonRPA.clipboard.get())
                pythonRPA.time.delay(0.3)
                employee_dict["Дата расторжение"] = fired_date
                pythonRPA.bySelector([{"title":"1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name":"V8TopLevelFrame","backend":"uia"},{"ctrl_index":1},{"ctrl_index":16},{"ctrl_index": window_index_1 + 1},{"ctrl_index":0},{"ctrl_index":0},{"ctrl_index":0},{"title":"Увольнение"},{"ctrl_index":2},{"ctrl_index":1},{"ctrl_index":8}]).click()
                pythonRPA.time.delay(0.3)
                pythonRPA.keyboard.press("ctrl+a")
                pythonRPA.time.delay(0.3)
                pythonRPA.keyboard.press("ctrl+c")
                pythonRPA.time.delay(0.5)
                fired_reason = str(pythonRPA.clipboard.get())
                pythonRPA.time.delay(0.3)
                employee_dict["Причина"] = delete_contract_type_mapping(fired_reason)
                if employee_dict["Причина"] == "Не найден в маппинге":
                    logs([str(datetime.datetime.now().strftime("%H:%M")), str(employee_dict['ФИО']), '',
                         "Нет в списке/Неправильно указана причина увольнения", "Увольнение"])
                    pythonRPA.keyboard.press("esc", 1, 0.5)
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
                pythonRPA.bySelector([{
                                          "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                                          "class_name": "V8TopLevelFrame", "backend": "uia"},
                                      {"title": "1С:Предприятие"}, {"ctrl_index": 0}, {"ctrl_index": 0},
                                      {"ctrl_index": 0}, {"title": "OK"}]).wait_appear(5)
                if pythonRPA.bySelector([{
                                             "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                                             "class_name": "V8TopLevelFrame", "backend": "uia"},
                                         {"title": "1С:Предприятие"}, {"ctrl_index": 0}, {"ctrl_index": 0},
                                         {"ctrl_index": 0}, {"title": "OK"}]).is_exists():
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
                    pythonRPA.time.delay(0.5)
                    if pythonRPA.bySelector([{
                        "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                        "class_name": "V8TopLevelFrame", "backend": "uia"},
                        {"title": "1С:Предприятие"}, {"ctrl_index": 0}, {"ctrl_index": 0},
                        {"ctrl_index": 0}, {"title": "OK"}]).is_exists():
                        pythonRPA.bySelector([{
                            "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                            "class_name": "V8TopLevelFrame", "backend": "uia"},
                            {"title": "1С:Предприятие"}, {"ctrl_index": 0}, {"ctrl_index": 0},
                            {"ctrl_index": 0}, {"title": "OK"}]).click()
                        pythonRPA.time.delay(0.5)
                        logs([str(datetime.datetime.now().strftime("%H:%M")), str(employee_dict['ФИО']), '',
                             "Нет в сотрудниках", "Увольнение"])
                        pythonRPA.time.delay(0.3)
                        pythonRPA.keyboard.press("ctrl+tab", 1, 0.5)
                        continue

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
                except Exception as e:
                    logs([str(datetime.datetime.now().strftime("%H:%M")), str(employee_dict['ФИО']), '',
                          "Нет в сотрудниках", "Увольнение"])
                    pythonRPA.time.delay(0.3)
                    pythonRPA.keyboard.press("ctrl+tab", 1, 0.5)
                    continue
                pythonRPA.time.delay(0.3)
                pythonRPA.keyboard.press("ctrl+a")
                pythonRPA.time.delay(0.3)
                pythonRPA.keyboard.press("ctrl+c")
                pythonRPA.time.delay(0.5)
                iin = str(pythonRPA.clipboard.get())
                pythonRPA.time.delay(0.3)
                employee_dict["ИИН"] = iin
                pythonRPA.time.delay(0.3)
                pythonRPA.keyboard.press("esc", 1, 0.5)
                pythonRPA.keyboard.press("ctrl+tab", 1, 0.5)
                print(employee_dict)
                employees_arr.append(employee_dict)
            except:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                try:
                    logs([str(datetime.datetime.now().strftime("%H:%M")), '', '', "Техническая ошибка",
                          "Увольнение"])
                except:
                    print("without log")
    pythonRPA.keyboard.press("esc", 2, 0.5)
    pythonRPA.bySelector([{"title":"1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name":"V8TopLevelFrame","backend":"uia"},{"ctrl_index":0},{"title":"Закрыть"}]).click()
    pythonRPA.bySelector([{"title":"1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name":"V8TopLevelFrame","backend":"uia"},{"depth_start": 5, "depth_end": 5, "title":"Да"}]).wait_appear(5)
    pythonRPA.bySelector([{"title":"1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы","class_name":"V8TopLevelFrame","backend":"uia"},{"depth_start": 5, "depth_end": 5, "title":"Да"}]).click()
    pythonRPA.time.delay(1)
    print(employees_arr)
    return employees_arr
