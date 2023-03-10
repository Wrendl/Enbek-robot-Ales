# -*- coding: utf-8 -*-
from Sources.new_enbek.enbek import Enbek, TDData
from Sources.init import logs
import datetime

from Sources.new_enbek.init import update_perevod

priem_arr_ekonomist = {'ФИО': 'Еркебаева С.Н.', 'Табельный номер': 'Але-4293', 'Место выполнения работы': {'obl': 'Г.АЛМАТЫ', 'city': 'Медеуский район', 'nas_punkt': 'Медеуский район', 'street': 'пр.Достык, 7'}, 'Вид работы': 'основная работа', 'ИИН': '770317400554', 'Номер договора': '46-2022', 'Срок договора': 'на определенный срок не менее одного года', 'Дата заключения договора': '01.12.2022', 'Дата начала работы': '01.12.2022', 'Дата окончания действия договора': '01.12.2023', 'Штатная должность': 'Ведущий экономист', 'Режим рабочего времени': 'Нормальное', 'Должность': 'Экономист'}


'''
Ошибка в приеме сотрудника -  Message: no such element: Unable to locate element: {"method":"xpath","selector":"//li[contains(.,"Работа по месту нахождения работодателя")]"}
  (Session info: chrome=107.0.5304.121)

{'ФИО': 'Нұрсеит А.М.', 'Табельный номер': 'Кск-3074', 'Место выполнения работы': {'obl': 'Г.АЛМАТЫ', 'city': 'Бостандыкский район', 'nas_punkt': 'Бостандыкский район', 'street': 'м-он Нурлы Тау, ул.Гульнафис Баязитовой, сооружение 21'}, 'Вид работы': 'основная работа', 'ИИН': '010521500453', 'Номер договора': '05-2022', 'Срок договора': 'на определенный срок не менее одного года', 'Дата заключения договора': '22.12.2022', 'Дата начала работы': '19.12.2022', 'Дата окончания действия договора': '19.12.2023', 'Штатная должность': 'Инженер по релейной защите', 'Режим рабочего времени': 'Нормальное', 'Должность': 'Инженер по релейной защите и автоматике'}
---------------------------------------
Ошибка в приеме сотрудника -  Message: no such element: Unable to locate element: {"method":"xpath","selector":"//label[text()="ЭКОНОМИСТ"]"}
  (Session info: chrome=107.0.5304.121)

{'ФИО': 'Отарбаева С.Ш.', 'Табельный номер': 'Але-4294', 'Место выполнения работы': {'obl': 'Г.АЛМАТЫ', 'city': 'Медеуский район', 'nas_punkt': 'Медеуский район', 'street': 'пр.Достык, 7'}, 'Вид работы': 'основная работа', 'ИИН': '990410450066', 'Номер договора': '47-2022', 'Срок договора': 'на время замещения временно отсутствующего работника', 'Дата заключения договора': '19.12.2022', 'Дата начала работы': '19.12.2022', 'Дата окончания действия договора': '', 'Штатная должность': 'Ведущий экономист', 'Режим рабочего времени': 'Нормальное', 'Должность': 'Экономист'}
---------------------------------------
Ошибка в приеме сотрудника -  Message: no such element: Unable to locate element: {"method":"xpath","selector":"//li[contains(.,"Работа по месту нахождения работодателя")]"}
  (Session info: chrome=107.0.5304.121)

{'ФИО': 'Жұмабеков Е.С.', 'Табельный номер': 'ТЦ2-8492', 'Место выполнения работы': {'obl': 'Г.АЛМАТЫ', 'city': 'Алатауский район', 'nas_punkt': 'Алатауский район', 'street': 'м-он Алгабас, ул.7, дом 130'}, 'Вид работы': 'основная работа', 'ИИН': '021223500765', 'Номер договора': '95-2022', 'Срок договора': 'на определенный срок не менее одного года', 'Дата заключения договора': '20.12.2022', 'Дата начала работы': '20.12.2022', 'Дата окончания действия договора': '20.12.2023', 'Штатная должность': 'Машинист-обходчик по турбинному оборудованию', 'Режим рабочего времени': 'Нормальное', 'Должность': 'Машинист-обходчик по турбинному оборудованию'}
---------------------------------------
Ошибка в приеме сотрудника -  Message: no such element: Unable to locate element: {"method":"xpath","selector":"//li[contains(.,"АЛМАТИHСКАЯ ОБЛАСТЬ")]"}
  (Session info: chrome=107.0.5304.121)

{'ФИО': 'Альсеитов М.К.', 'Табельный номер': 'Кпч-0273', 'Место выполнения работы': {'obl': 'АЛМАТИHСКАЯ ОБЛАСТЬ', 'city': 'Капчагай Г.А.', 'nas_punkt': 'г.Капчагай', 'street': 'г.Капчагай'}, 'Вид работы': 'основная работа', 'ИИН': '681219301913', 'Номер договора': '10-2022', 'Срок договора': 'на определенный срок не менее одного года', 'Дата заключения договора': '13.12.2022', 'Дата начала работы': '13.12.2022', 'Дата окончания действия договора': '13.12.2023', 'Штатная должность': 'Водитель автомобиля', 'Режим рабочего времени': 'Нормальное', 'Должность': 'Водитель автомобиля'}
---------------------------------------
Ошибка в приеме сотрудника -  Message: no such element: Unable to locate element: {"method":"xpath","selector":"//li[contains(.,"АЛМАТИHСКАЯ ОБЛАСТЬ")]"}
  (Session info: chrome=107.0.5304.121)

{'ФИО': 'Сатыбаев А.К.', 'Табельный номер': 'Кпч-0274', 'Место выполнения работы': {'obl': 'АЛМАТИHСКАЯ ОБЛАСТЬ', 'city': 'Капчагай Г.А.', 'nas_punkt': 'г.Капчагай', 'street': 'г.Капчагай'}, 'Вид работы': 'основная работа', 'ИИН': '020701501085', 'Номер договора': '11-2022', 'Срок договора': 'на определенный срок не менее одного года', 'Дата заключения договора': '20.12.2022', 'Дата начала работы': '20.12.2022', 'Дата окончания действия договора': '20.12.2023', 'Штатная должность': 'Водитель автомобиля', 'Режим рабочего времени': 'Нормальное', 'Должность': 'Водитель автомобиля'}

'''

uvol_arr1 = [
{'ФИО': 'Қалдыбек Ә.Б.', 'Дата расторжение': '30.11.2022', 'Причина': 'По инициативе работника', 'ИИН': '990407300651'},
{'ФИО': 'Бухарбеков Е.К.', 'Дата расторжение': '06.12.2022', 'Причина': 'По инициативе работника', 'ИИН': '731102300594'},
{'ФИО': 'Нурбаев Е.Ж.', 'Дата расторжение': '09.12.2022', 'Причина': 'По инициативе работника', 'ИИН': '860926303126'},
{'ФИО': 'Шерипова А.М.', 'Дата расторжение': '09.12.2022', 'Причина': 'По инициативе работника', 'ИИН': '990322400100'}
]


def start_priem_enbek(priem_arr):
    enbek = Enbek()
    for priem in priem_arr:
        try:
            priem_new = TDData(priem)
            enbek.add_td(priem_new)
            logs([str(datetime.datetime.now().strftime("%H:%M")), str(priem["ФИО"]), str(priem["ИИН"]), "Внесён", "Прием"])
        except Exception as e:
            logs([str(datetime.datetime.now().strftime("%H:%M")), str(priem["ФИО"]), str(priem["ИИН"]), "Ошибка в enbek.kz", "Прием"])
            print('Ошибка в приеме сотрудника - ', str(e))
            print(priem)
    enbek.quit()


def start_uvol_enbek(uvol_arr):
    enbek = Enbek()
    for uvol in uvol_arr:
        try:
            enbek.delete_td(uvol)
        except Exception as e:
            logs([str(datetime.datetime.now().strftime("%H:%M")), str(uvol["ФИО"]), str(uvol["ИИН"]),
                  "Ошибка в enbek.kz", "Увольнение"])
            print('Ошибка в увольнении сотрудника - ' + str(e))
            print(uvol)
    enbek.quit()


def start_perevod_enbek(perevod_arr):
    enbek = Enbek()
    for perevod in perevod_arr:
        try:
            perevod_new = update_perevod(perevod)
            enbek.dop_soglashenie(perevod_new)
            logs([str(datetime.datetime.now().strftime("%H:%M")), str(perevod["ФИО"]), str(perevod["ИИН"]), "Внесён",
                  "Перемещении"])
        except Exception as e:
            logs([str(datetime.datetime.now().strftime("%H:%M")), str(perevod["ФИО"]), str(perevod["ИИН"]),
                  "Ошибка в enbek.kz", "Перемещении"])
            print('Ошибка в перемещении сотрудника - ')
            print(perevod)
    enbek.quit()


# start_priem_enbek(arr[12:])
start_uvol_enbek(uvol_arr1)
# start_perevod_enbek(perevod_01_01_06[31:])
# print(len(perevod_01_01_06))
# cnt = 0
# for i in perevod_01_01_06:
#     if i['ФИО'] == 'Авезов Д.Н.':
#         print(cnt)
#     cnt+=1
