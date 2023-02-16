import datetime
from time import sleep

import keyboard
import pyautogui

from Sources.init import logs
from Sources.new_enbek.init import fill_contractCate, fill_workingHours, fill_workplace
from Sources.new_enbek.pythonrpa_mini import App, Path, Json, JsonData, Web
from Sources.new_enbek.settings import enbek_login, enbek_password, driver_path, eds_password, eds_path
from Sources.new_enbek.enbek_maps import *


class TDData(JsonData):
    map_dContractCate = map_dContractCate
    map_partTime = map_partTime
    map_uozcodprof = map_uozcodprof
    map_workPlaceCountry = map_workPlaceCountry
    map_uoz_caption = map_uoz_caption
    map_cato = map_cato
    map_workingHours = map_workingHours
    map_army = map_army
    location_mapping = location_mapping

    def __init__(self, data):
        super().__init__()
        self.IIN = data['ИИН']  # * ИИН
        self.numDogovor = data['Номер договора']  # * Номер договора
        contractCate_value = fill_contractCate(data['Дата заключения договора'], data['Дата окончания действия договора'])
        self.dContractCate = self.map_dContractCate[contractCate_value]  # + Срок договора
        self.dateZakDogovor = data['Дата заключения договора']  # * Дата заключения договора
        self.dateBegDogovor = data['Дата начала работы'] # * Дата начала работы
        self.dateEndDogovor = data['Дата окончания действия договора']  # - Дата окончания действия договора
        self.partTime = self.map_partTime['default_value']  # + Вид работы
        self.remoteWork = False  # * Дистанционная работа
        self.uozcodprof = str(data['Должность']).upper()  # + НКЗ Должность
        self.shtatDolj = str(data['Штатная должность'])  # * Должность
        self.workPlaceCountry = self.map_workPlaceCountry["default_value"]  # + Страна места работы
        workplace_values = fill_workplace(data['Место выполнения работы'])
        self.uoz_caption = workplace_values['obl']  # + Город или область # TODO
        self.cato = workplace_values['city'].upper()  # + Район города или населённый пункт области # TODO
        self.nas_punkt = workplace_values['nas_punkt'].upper()
        self.workPlace = workplace_values['street']  # * Место выполнения работы
        self.workingHours = data['Режим рабочего времени']  # + Режим рабочего времени
        self.army = self.map_army["default_value"]  # + Военная обязанность


class Enbek(Web):

    def __init__(self):
        super().__init__(driver_path=driver_path)
        self.driver_check = False

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def start(self, login, password):
        self.get('https://hr.enbek.kz/')

        self.find_element('//div[@class="greenBtn mob"]/a[contains(.,"Вход")]').click()

        self.wait_element('//input[@name="email"]')
        self.find_element('//input[@name="email"]').send_keys(login)

        self.wait_element('//input[@name="password"]')
        self.find_element('//input[@name="password"]').send_keys(password)

        self.find_element('//button[@class="button-primary"]').click()

        sleep(4)
        # if self.find_element('//button[contains(.,"ok")]'):
        #     try:
        #         self.find_element('//button[contains(.,"ok")]').click()
        #     except:
        #         self.get('https://hr.enbek.kz/')
        #         self.find_element('//div[@class="greenBtn mob"]/a[contains(.,"Вход")]').click()
        #
        #         self.wait_element('//input[@name="email"]')
        #         self.find_element('//input[@name="email"]').send_keys(login)
        #
        #         self.wait_element('//input[@name="password"]')
        #         self.find_element('//input[@name="password"]').send_keys(password)
        #
        #         self.find_element('//button[@class="button-primary"]').click()
        #         self.find_element('//button[contains(.,"ok")]').click()

        self.wait_element('//div/p[contains(.,"Я - работодатель")]', timeout=45, event=self.ec.element_to_be_clickable)
        self.find_element('//div/p[contains(.,"Я - работодатель")]').click()

        self.wait_element('//a/p[contains(.,"Трудовые договоры")]', event=self.ec.element_to_be_clickable)
        self.find_element('//a/p[contains(.,"Трудовые договоры")]').click()

        self.driver_check = True

    def add_td(self, data):

        if not self.driver_check:
            self.start(enbek_login, enbek_password)
        else:
            self.get('https://hr.enbek.kz/contracts')

        self.wait_element('//button[contains(.,"Зарегистрировать трудовой договор")]',

                          event=self.ec.element_to_be_clickable)
        self.find_element('//button[contains(.,"Зарегистрировать трудовой договор")]').click()

        # * Дата подписания договора
        sleep(1)
        self.wait_element('//input[@name="registerDate"]', event=self.ec.element_to_be_clickable)
        self.find_element('//input[@name="registerDate"]').send_keys(self.keys.HOME)
        sleep(1)
        self.find_element('//input[@name="registerDate"]').send_keys(data.dateZakDogovor)
        self.wait_element('//input[@name="registerDate"]', event=self.ec.text_to_be_present_in_element)
        sleep(1)

        # * ИИН
        self.find_element('//input[@name="iin"]').send_keys(data.IIN)

        # * Дата начала работы
        sleep(1)
        self.wait_element('//input[@name="dateFrom"]', event=self.ec.element_to_be_clickable)
        self.find_element('//input[@name="dateFrom"]').send_keys(self.keys.HOME)
        sleep(1)
        self.find_element('//input[@name="dateFrom"]').send_keys(data.dateBegDogovor)
        self.wait_element('//input[@name="dateFrom"]', event=self.ec.text_to_be_present_in_element)
        sleep(1)

        # * ФИО
        self.find_element('//button[contains(.,"Найти")]').click()
        self.wait_element('//input[@name="fullName"]', event=self.ec.text_to_be_present_in_element)
        sleep(1)

        # * НОМЕР ТД
        self.find_element('//input[@name="contractNumber"]').send_keys(data.numDogovor)
        self.wait_element('//input[@name="contractNumber"]', event=self.ec.text_to_be_present_in_element)
        sleep(1)

        # * Срок действия трудового договора
        self.find_element('//input[@name="dcontractDateCode"]').click()
        self.wait_element(f'//li[contains(.,"{data.dContractCate}")]', event=self.ec.element_to_be_clickable)
        sleep(1)
        self.find_element(f'//li[contains(.,"{data.dContractCate}")]').click()
        self.wait_element('//input[@name="dcontractDateCode"]', event=self.ec.text_to_be_present_in_element)

        # * Дата окончания действия договора
        try:
            self.wait_element('//input[@name="dateTo"]', event=self.ec.element_to_be_clickable)
            self.find_element('//input[@name="dateTo"]').send_keys(self.keys.HOME)
            sleep(1)
            # self.find_element('//input[@name="dateTo"]').send_keys(self.keys.HOME + data.dateEndDogovor)
            self.find_element('//input[@name="dateTo"]').send_keys(data.dateEndDogovor)
            self.wait_element('//input[@name="dateTo"]', event=self.ec.text_to_be_present_in_element)
            sleep(1)
        except:
            pass

        # * Должность по НКЗ
        self.find_element('//div[contains(.,"Должность по НКЗ") and @class="style_field__1t95V  "]//div/div/input') \
            .click()
        value_ = data.uozcodprof.upper()
        self.find_element('//div[contains(.,"Должность по НКЗ") and @class="style_field__1t95V  "]//div/div/input') \
            .send_keys(value_)
        self.wait_element(f'//label[text()="{value_}"]', event=self.ec.element_to_be_clickable)
        # sleep(1)
        # element = self.find_element(f'//label[text()="{value_}"]')
        # self.execute_script("arguments[0].scrollIntoView(true);", element)
        self.find_element(f'//label[text()="{value_}"]').click()
        self.wait_element('//div[contains(.,"Должность по НКЗ") and @class="style_field__1t95V  "]//div/div/input',
                          event=self.ec.text_to_be_present_in_element)

        # * Должность
        self.find_element('//div[@class="style_wrapper__3TatY"]/div[@class="style_field__5OP8h"]/input') \
            .click()
        self.find_element('//div[@class="style_wrapper__3TatY"]/div[@class="style_field__5OP8h"]/input') \
            .send_keys(data.shtatDolj)
        self.wait_element('//div[@class="style_wrapper__3TatY"]/div[@class="style_field__5OP8h"]/input',
                          event=self.ec.text_to_be_present_in_element)
        sleep(1)

        # * Вид работы
        self.find_element('//input[@name="dpartTimeCode"]').click()
        self.wait_element(f'//li[contains(.,"{data.partTime}")]', event=self.ec.element_to_be_clickable)
        self.find_element(f'//li[contains(.,"{data.partTime}")]').click()
        self.wait_element('//input[@name="dpartTimeCode"]', event=self.ec.text_to_be_present_in_element)
        sleep(1)

        # * Режим рабочего времени workingHours
        self.find_element('//input[@name="dworkingHoursCode"]').click()
        self.wait_element(f'//li[contains(.,"{data.workingHours}")]', event=self.ec.element_to_be_clickable)
        self.find_element(f'//li[contains(.,"{data.workingHours}")]').click()
        self.wait_element('//input[@name="dworkingHoursCode"]', event=self.ec.text_to_be_present_in_element)
        sleep(1)
        # * Тарифная ставка
        # self.find_element('//input[@name="tariffRate"]')

        # * Форма занятости
        self.find_element('//input[@name="dremoteWorkCode"]').click()
        self.wait_element('//li[contains(.,"Работа по месту нахождения работодателя")]',
                          event=self.ec.element_to_be_clickable)
        self.find_element('//li[contains(.,"Работа по месту нахождения работодателя")]').click()
        self.wait_element('//input[@name="dremoteWorkCode"]', event=self.ec.text_to_be_present_in_element)
        sleep(1)
        self.find_element('//input[@name="dremoteWorkCode"]').click()
        self.wait_element('//li[contains(.,"Работа по месту нахождения работодателя")]',
                          event=self.ec.element_to_be_clickable)
        self.find_element('//li[contains(.,"Работа по месту нахождения работодателя")]').click()
        self.wait_element('//input[@name="dremoteWorkCode"]', event=self.ec.text_to_be_present_in_element)
        sleep(1)

        # * СТРАНА МЕСТА работы
        self.find_element('//input[@name="dcountryCode"]').click()
        sleep(1)
        self.wait_element(f'//li[contains(.,"{data.workPlaceCountry}")]', event=self.ec.element_to_be_clickable)
        self.find_element(f'//li[contains(.,"{data.workPlaceCountry}")]').click()
        self.wait_element('//input[@name="dcountryCode"]', event=self.ec.text_to_be_present_in_element)
        sleep(2)

        # * Регион места работы
        self.find_element('//input[@name="ddistrictCode"]').click()
        sleep(1)
        self.wait_element(f'//li[contains(.,"{data.uoz_caption}")]', event=self.ec.element_to_be_clickable)
        self.find_element(f'//li[contains(.,"{data.uoz_caption}")]').click()
        self.wait_element('//input[@name="ddistrictCode"]', event=self.ec.text_to_be_present_in_element)
        sleep(1)

        # * район места работы
        self.find_element('//input[@name="dregionCode"]').click()
        sleep(1)
        self.wait_element(f'//li[contains(.,"{data.cato}")]', event=self.ec.element_to_be_clickable)
        self.find_element(f'//li[contains(.,"{data.cato}")]').click()
        self.wait_element('//input[@name="dregionCode"]', event=self.ec.text_to_be_present_in_element)
        sleep(1)

        # * населенный пункт
        try:
            self.find_element('//input[@name="dlocalityCode"]').click()
            sleep(1)
            self.find_element(f'//li[contains(.,"{data.nas_punkt}")]').click()
            self.wait_element('//input[@name="dlocalityCode"]', event=self.ec.text_to_be_present_in_element)
            sleep(1)
        except:
            pass

        # * адрес места работы
        self.find_element('//input[@name="workingPlace"]').send_keys(data.workPlace)

        self.eds_sign()

    def delete_td(self, data):

        if not self.driver_check:
            self.start(enbek_login, enbek_password)
        else:
            self.get('https://hr.enbek.kz/contracts')

        try:
            self.find_and_check(data)
        except:
            logs([str(datetime.datetime.now().strftime("%H:%M")), str(data["ФИО"]), str(data["ИИН"]), "Нет в enbek.kz",
                  "Увольнение"])
            return

        sleep(3)
        if len(self.find_elements('//span[contains(.,"Расторгнутый")]')) > 0:
            logs([str(datetime.datetime.now().strftime("%H:%M")), str(data["ФИО"]), str(data["ИИН"]), "Был расторгнут",
                  "Увольнение"])
            return
        # * кнопка расторгнуть
        self.wait_element('//button[contains(.,"Расторгнуть")]', event=self.ec.element_to_be_clickable)
        self.find_element('//button[contains(.,"Расторгнуть")]').click()
        sleep(2)

        # * кнопка все равно расторгнуть
        self.wait_element('//button[contains(.,"Понятно, все равно расторгнуть")]',
                          event=self.ec.element_to_be_clickable)
        self.find_element('//button[contains(.,"Понятно, все равно расторгнуть")]').click()

        # * Причина расторжения договора
        self.find_element('//input[@name="terminationReason"]').click()
        self.find_element('//input[@name="terminationReason"]').send_keys(data['Причина'])
        self.wait_element('//li[contains(.,"' + data['Причина'] +'")]', event=self.ec.element_to_be_clickable)
        self.find_element('//li[contains(.,"' + data['Причина'] +'")]').click()
        self.wait_element('//input[@name="terminationReason"]', event=self.ec.text_to_be_present_in_element)

        # * Дата расторжения договора
        sleep(2)
        self.wait_element('//input[@name="terminationDate"]', event=self.ec.element_to_be_clickable)
        self.find_element('//input[@name="terminationDate"]').send_keys(self.keys.HOME)
        sleep(2)
        self.find_element('//input[@name="terminationDate"]').send_keys(data['Дата расторжение'])
        self.wait_element('//input[@name="terminationDate"]', event=self.ec.text_to_be_present_in_element)

        self.eds_sign()

    def eds_sign(self):
        self.find_element('//button[contains(.,"одписать ЭЦП")]').click()
        sleep(2)

        selector_ = [{"title": "Открыть файл", "class_name": "SunAwtDialog", "control_type": "Window", "list_index": 0}]
        App().find_element(selector_).type_keys(eds_path)
        sleep(2)
        App().find_element(selector_).set_focus()
        sleep(2)
        App().find_element(selector_).type_keys('{ENTER}')
        sleep(2)

        selector_ = [{"title": "Формирование ЭЦП в формате XML", "class_name": "SunAwtDialog", "control_type": "Window",
                      "list_index": 0}]
        App().wait_element(selector_, timeout=10)
        sleep(2)
        App().find_element(selector_).type_keys(eds_password + '{ENTER}' + '{ENTER}')
        sleep(2)
        App().find_element(selector_).type_keys('{ENTER}')
        sleep(2)

    def find_and_check(self, data):

        # * поиск по иин
        sleep(2)
        self.find_element('//input[@class="MuiInputBase-input css-mnn31"]').send_keys(data['ИИН'])
        sleep(3)
        # self.find_element('//span[@class="contraxts2Search_searchField__button__3cYaa"]').click()
        self.find_element('//span[contains(.,"Найти")]').click()
        sleep(3)
        self.wait_element('//table', event=self.ec.element_to_be_clickable)
        sleep(3)
        self.find_element('//td[@class="contractsTable_pixelGamingContractNumber__226ny"]').click()

    def dop_soglashenie(self, data):

        # try:
        #     sleep(2)
        #     alert = self.switch_to.alert
        #     alert.accept()
        # except:
        #     pass

        if not self.driver_check:
            self.start(enbek_login, enbek_password)
        else:
            self.get('https://hr.enbek.kz/contracts')

        self.find_and_check(data)

        # * Создать допсоглашение
        self.find_elements('//button[contains(.,"Создать допсоглашение")]')[0].click()
        sleep(2)

        # * номер допсоглашения
        self.find_element('//input[@name="contractNum"]').send_keys(data['номер допсоглашения'])
        self.wait_element('//input[@name="contractNum"]', event=self.ec.text_to_be_present_in_element)
        sleep(2)

        # * Дата заключения доп.соглашения
        self.wait_element('//input[@name="registerDate"]', event=self.ec.element_to_be_clickable)
        self.find_element('//input[@name="registerDate"]').send_keys(self.keys.HOME)
        sleep(2)
        self.find_element('//input[@name="registerDate"]').send_keys(data['Дата заключения доп.соглашения'])
        self.wait_element('//input[@name="registerDate"]', event=self.ec.text_to_be_present_in_element)
        sleep(2)

        # * Дата начала действия доп.соглашения
        self.wait_element('//input[@name="dateFrom"]', event=self.ec.element_to_be_clickable)
        self.find_element('//input[@name="dateFrom"]').send_keys(self.keys.HOME)
        sleep(2)
        self.find_element('//input[@name="dateFrom"]').send_keys(data['Дата начала действия доп.соглашения'])
        self.wait_element('//input[@name="dateFrom"]', event=self.ec.text_to_be_present_in_element)
        sleep(2)

        # * кнопка выбрать
        self.find_element('//button[contains(.,"Выбрать")]').click()
        sleep(2)

        # * Изменения срока трудового договора
        #contractTerm_selector_ = '//label[@for="contractTerm"]'
        #self.find_element(contractTerm_selector_).click()
        self.find_element('//label[@for="contractTerm"]').click()

        # * Изменение должности
        contractPosition_selector_ = '//label[@for="contractPosition"]'
        self.find_element(contractPosition_selector_).click()

        # * Изменение режима рабочего времени
        contractWorkingHours_selector_ = '//label[@for="contractWorkingHours"]'
        self.find_element(contractWorkingHours_selector_).click()

        # * Изменение вида работ
        contractJobType_selector_ = '//label[@for="contractJobType"]'
        self.find_element(contractJobType_selector_).click()

        # * Изменение места выполнения работы
        contractJobLocation_selector_ = '//label[@for="contractJobLocation"]'
        self.find_element(contractJobLocation_selector_).click()

        # * кнопка продоллжить
        self.find_element(' //button[contains(.,"Продолжить")]').click()

        # ! изменение срока трудового договора
        # * Срок действия трудового договора
        self.find_element('//input[@name="dcontractDateCode"]').click()
        self.wait_element('//li[contains(.,"'+'На неопределенный срок'+'")]', event=self.ec.element_to_be_clickable)
        self.find_element('//li[contains(.,"'+'На неопределенный срок'+'")]').click()
        self.wait_element('//input[@name="dcontractDateCode"]', event=self.ec.text_to_be_present_in_element)
        sleep(2)

        # * Дата окончания действия договора
        # if data['Срок договора'] != 'на неопределенный срок'
        # self.wait_element('//input[@name="contractEndDate"]', event=self.ec.element_to_be_clickable)
        # self.find_element('//input[@name="contractEndDate"]').send_keys(self.keys.HOME)
        # sleep(2)
        # self.find_element('//input[@name="contractEndDate"]').send_keys(data['Дата окончания действия дополнительного соглашения'])
        # self.wait_element('//input[@name="contractEndDate"]', event=self.ec.text_to_be_present_in_element)
        # sleep(2)

        # self.find_element('//input[@name="contractEndDate"]').send_keys(self.keys.HOME)
        # sleep(2)
        # self.find_element('//input[@name="contractEndDate"]').send_keys('11.07.2023')

        # ! Изменение режима рабочего времени
        # * Режим рабочего времени
        self.find_element('//input[@name="dworkingHoursCode"]').click()
        self.wait_element('//li[contains(.,"'+data['Режим рабочего времени']+'")]', event=self.ec.element_to_be_clickable)
        self.find_element('//li[contains(.,"'+data['Режим рабочего времени']+'")]').click()
        self.wait_element('//input[@name="dworkingHoursCode"]', event=self.ec.text_to_be_present_in_element)
        sleep(2)

        # * Тарифная ставка
        #self.find_element('//input[@name="tariffRate"]').send_keys()

        # ! Изменение должности
        # * Должность по НКЗ
        # self.find_element('//input[@name="dpositionCode"]').click()
        # self.wait_element('//li[contains(.,"' + data['НКЗ'] +'")]',
        #                   self.ec.element_to_be_clickable)
        # self.find_element('//li[contains(.,"' + data['НКЗ'] + '")]').click()
        # self.wait_element('//input[@name="dpositionCode"]', event=self.ec.text_to_be_present_in_element)

        self.find_element('//div[contains(.,"Должность по НКЗ") and @class="style_field__1t95V  "]//div/div/input') \
            .click()
        self.find_element('//div[contains(.,"Должность по НКЗ") and @class="style_field__1t95V  "]//div/div/input') \
            .send_keys(data['НКЗ'].upper())
        self.wait_element(f'//li[contains(.,"'+data['НКЗ'].upper()+'")]', event=self.ec.element_to_be_clickable)
        sleep(2)
        self.find_element(f'//li[contains(.,"'+data['НКЗ'].upper()+'")]').click()
        self.wait_element('//div[contains(.,"Должность по НКЗ") and @class="style_field__1t95V  "]//div/div/input',
                          event=self.ec.text_to_be_present_in_element)
        sleep(2)

        # * Должность
        self.find_element('//div[@class="style_wrapper__3TatY"]/div[@class="style_field__5OP8h"]/input') \
            .send_keys(data['Должность'])
        self.wait_element('//div[@class="style_wrapper__3TatY"]/div[@class="style_field__5OP8h"]/input',
                          event=self.ec.text_to_be_present_in_element)
        sleep(2)

        #
        # # * Должность
        # self.find_element('//div[@class="style_wrapper__3TatY"]/div[@class="style_field__5OP8h"]/input') \
        #     .send_keys({data['Должность']})
        # self.wait_element('//div[@class="style_wrapper__3TatY"]/div[@class="style_field__5OP8h"]/input',
        #                   event=self.ec.text_to_be_present_in_element)

        # ! Изменение вида работ
        # * Вид работы
        self.find_element('//input[@name="dpartTimeCode"]').click()
        self.wait_element('//li[contains(.,"Основная работа")]', event=self.ec.element_to_be_clickable)
        self.find_element('//li[contains(.,"Основная работа")]').click()
        self.wait_element('//input[@name="dpartTimeCode"]', event=self.ec.text_to_be_present_in_element)
        sleep(2)

        # ! Изменение места выполнения работы
        # * Форма занятости
        self.find_element('//input[@name="dremoteWorkCode"]').click()
        self.wait_element('//li[contains(.,"Работа по месту нахождения работодателя")]',
                          event=self.ec.element_to_be_clickable)
        self.find_element('//li[contains(.,"Работа по месту нахождения работодателя")]').click()
        self.wait_element('//input[@name="dremoteWorkCode"]', event=self.ec.text_to_be_present_in_element)
        sleep(2)

        # * СТРАНА МЕСТА работы
        self.find_element('//input[@name="dcountryCode"]').click()
        sleep(1)
        self.wait_element('//li[contains(.,"КАЗАХСТАН")]', event=self.ec.element_to_be_clickable)
        self.find_element('//li[contains(.,"КАЗАХСТАН")]').click()
        self.wait_element('//input[@name="dcountryCode"]', event=self.ec.text_to_be_present_in_element)
        sleep(2)

        # * Регион места работы
        self.find_element('//input[@name="ddistrictCode"]').click()
        sleep(1)
        self.wait_element('//li[contains(.,"'+data['Регион'].upper()+'")]', event=self.ec.element_to_be_clickable)
        self.find_element('//li[contains(.,"'+data['Регион'].upper()+'")]').click()
        self.wait_element('//input[@name="ddistrictCode"]', event=self.ec.text_to_be_present_in_element)

        # * район места работы
        self.find_element('//input[@name="dregionCode"]').click()
        sleep(1)
        self.wait_element('//li[contains(.,"'+data['район'].upper()+'")]', event=self.ec.element_to_be_clickable)
        self.find_element('//li[contains(.,"'+data['район'].upper()+'")]').click()
        self.wait_element('//input[@name="dregionCode"]', event=self.ec.text_to_be_present_in_element)
        sleep(2)

        # * населенный пункт
        # self.find_element('//input[@name="dlocalityCode"]').send_keys(data.cato)
        try:
            self.find_element('//input[@name="dlocalityCode"]').click()
            sleep(1)
            self.find_element(f'//li[contains(.,"'+data['Населенный пункт']+'")]').click()
            self.wait_element('//input[@name="dlocalityCode"]', event=self.ec.text_to_be_present_in_element)
            sleep(1)
        except:
            pass

        # * адрес места работы
        self.find_element('//input[@name="workingPlace"]').send_keys(data['адрес'])

        # input()
        self.eds_sign()


if __name__ == '__main__':
    # data = dict
    # path = Path.join(serialisation_path, 'enbek_rastorzhenie.json')
    # lst = Json.read(path)
    #
    # for i in lst:
    #     data = PriemEnbek().fill(i['Табельный номер'])
    #     print(data)
    data = {
        'ИИН': '910929451081',
        'Номер трудового договора': '86',
        'номер допсоглашения': '1',
        'Дата заключения доп.соглашения': '01.07.2022',
        'Дата начала действия доп.соглашения': '02.07.2022'
    }

    Enbek().dop_soglashenie(data)


