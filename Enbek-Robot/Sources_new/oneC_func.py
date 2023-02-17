
from pyPythonRPA.Robot import pythonRPA


def time_delay(time=0.5):
    pythonRPA.time.delay(time)


def focus_1C():
    try:
        pythonRPA.bySelector([{
                                  "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                                  "class_name": "V8TopLevelFrame",
                                  "backend": "uia"}]).wait_appear(15)
        pythonRPA.bySelector([{
                                  "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                                  "class_name": "V8TopLevelFrame",
                                  "backend": "uia"}]).set_focus()
        pythonRPA.bySelector([{
                                  "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                                  "class_name": "V8TopLevelFrame",
                                  "backend": "uia"}]).maximize()
    except:
        pass


def copy_data():
    time_delay()
    pythonRPA.keyboard.press("ctrl+a")
    time_delay()
    pythonRPA.keyboard.press("ctrl+c")
    time_delay()


def auth(login, password):
    pythonRPA.bySelector([{"title": "Запуск 1С:Предприятия", "class_name": "V8TopLevelFrameTaxiStarter",
                           "backend": "uia"}]).wait_appear(20)

    # --- Into Ales base ---
    time_delay()
    pythonRPA.bySelector([{"title": "Запуск 1С:Предприятия", "class_name": "V8TopLevelFrameTaxiStarter",
                           "backend": "uia"}]).set_focus()

    pythonRPA.bySelector(
        [{"title": "Запуск 1С:Предприятия", "class_name": "V8TopLevelFrameTaxiStarter", "backend": "uia"},
         {"ctrl_index": 1}, {"ctrl_index": 1}, {"ctrl_index": 0}, {"ctrl_index": 8},
         {"ctrl_index": 0}]).double_click()

    pythonRPA.bySelector([{"title": "Доступ к информационной базе", "class_name": "V8NewLocalFrameBaseWnd",
                           "backend": "uia"}]).wait_appear(20)

    # --- Auth ---
    time_delay()
    pythonRPA.bySelector([{"title": "Доступ к информационной базе", "class_name": "V8NewLocalFrameBaseWnd",
                           "backend": "uia"}]).set_focus()

    pythonRPA.bySelector(
        [{"title": "Доступ к информационной базе", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"},
         {"title": "1С:Предприятие"}, {"ctrl_index": 1}, {"ctrl_index": 1}, {"ctrl_index": 0},
         {"ctrl_index": 2}]).click()
    time_delay()
    pythonRPA.keyboard.write(login)

    time_delay()
    pythonRPA.bySelector(
        [{"title": "Доступ к информационной базе", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"},
         {"title": "1С:Предприятие"}, {"ctrl_index": 1}, {"ctrl_index": 1}, {"ctrl_index": 0},
         {"ctrl_index": 3}]).click()
    time_delay()
    pythonRPA.keyboard.write(password)

    time_delay()
    pythonRPA.bySelector(
        [{"title": "Доступ к информационной базе", "class_name": "V8NewLocalFrameBaseWnd", "backend": "uia"},
         {"title": "1С:Предприятие"}, {"ctrl_index": 1}, {"ctrl_index": 1}, {"ctrl_index": 0},
         {"title": "OK"}]).click()


def open_sotrudniki():
    pythonRPA.bySelector([{
                              "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                              "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1}, {"ctrl_index": 0},
                          {"ctrl_index": 3}, {"ctrl_index": 0},
                          {"title": "Главное меню"}, {"title": "Кадровый учет"}]).click()
    pythonRPA.bySelector([{
                              "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                              "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 0},
                          {"title": "Кадровый учет"}, {"title": "Сотрудники"}]).wait_appear(10)
    time_delay(1)
    pythonRPA.bySelector([{
                              "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                              "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 0},
                          {"title": "Кадровый учет"}, {"title": "Сотрудники"}]).click()
    pythonRPA.bySelector([{
                              "title": "1С:Предприятие - Управление производственным предприятием для Казахстана, редакция 1.0 / АлЭС / Основная рабочая база / Төрепаш Ажар Қанатқызы",
                              "class_name": "V8TopLevelFrame", "backend": "uia"}, {"ctrl_index": 1}, {"ctrl_index": 16},
                          {"ctrl_index": 1}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 3},
                          {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0}, {"ctrl_index": 0},
                          {"title": "Головной офис Наименование"}]).wait_appear(180)
    time_delay()
    pythonRPA.keyboard.press("ctrl+tab")
    time_delay()
    pythonRPA.keyboard.press("home")
    time_delay()


def find_employee_from_list(window_index_1, employee):
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
