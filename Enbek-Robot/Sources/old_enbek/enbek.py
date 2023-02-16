import shutil
import glob
import os
import time
import keyboard
from glob import glob
from pyPythonRPA.Robot import pythonRPA
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec, expected_conditions
from selenium.webdriver.support.ui import WebDriverWait, Select
from webdriver_manager.chrome import ChromeDriverManager
import datetime
from Sources.init import logs
import sys
from selenium.webdriver.chrome.options import Options


class Enbek:

    def __init__(self, robot_path, login, psw, psw_ecp, debug=False):
        self.debug = debug
        self.driver = None
        self.driver_data = [login, psw]
        self.robot_path = robot_path
        self.downloads_path = os.path.join(os.environ['USERPROFILE'], "Downloads\\").replace("/", "\\")
        self.temp_path = self.robot_path + "Temp\\Enbek"
        self.path = {"downloads": {"title": "Downloads", "path": self.downloads_path, "dir": self.downloads_path[:-1]},
                     "temp": {"title": "Temp", "path": self.temp_path, "dir": self.temp_path[:-1]},
                     "enbek_files": {"title": "Enbek_files", "path": self.temp_path + "Enbek_files\\",
                                     "dir": self.temp_path + "Enbek_files"}}
        self.url = {
            "login": "https://www.enbek.kz/docs/ru/user",
            "list": "https://www.enbek.kz/ru/cabinet/dogovor/list/good",
            "add": "https://www.enbek.kz/ru/cabinet/dogovor/add",
        }
        # Data containers
        self.anchor = None
        self.path_to_ecp = r"D:\Documents\Desktop\PythonRPA\Robot\ALESRobot\Tools\ecp\GOSTKNCA_825b268fff47b575a0129c3cb85743c345db0db4.p12"
        self.passw = psw_ecp
        print("\t")

    # Files
    def _mkdir(self):
        """Пробегается по self.path, создает их, если не найдены"""
        path = self.path
        for folder in path:
            current_folder = path[folder]["dir"]
            if not os.path.isdir(current_folder):
                os.makedirs(current_folder)

    def _clean(self, var="*", del_sub_dirs=False):
        """Чистит все файлы в self.path"""
        path = self.path
        self._mkdir()
        ignore = ["enbek_files"]
        for folder in path:
            if (var == "*" and folder not in ignore) or var == folder:
                current_folder = path[folder]["path"]
                children = glob.glob(current_folder + "*")
                for child in children:
                    if os.path.isdir(child):
                        print(child, "is a dir")
                        if del_sub_dirs and folder != "temp":
                            shutil.rmtree(child)
                    elif os.path.isfile(child) or os.path.islink(child):
                        print(child, "is a file")
                        os.remove(child)
                if var != "*":
                    break

    # General

    def _sel_wait_el(self, by, selector, sec=60, appear=True):
        """Ожидание элемента появление или изчезновение подается через bool 'appear'"""
        driver = self.driver
        time.sleep(0.3)
        try:
            if appear:
                WebDriverWait(driver, sec).until(ec.presence_of_element_located((by, selector)))
            else:
                WebDriverWait(driver, sec).until_not(ec.presence_of_element_located((by, selector)))
            return True
        except:
            return False
        finally:
            time.sleep(0.2)

    def _sel_init(self):
        """Запуск драйвера и логин в enbek. Объект драйвера создается именно здесь"""
        # Driver init
        try:
            self.driver = webdriver.Chrome(executable_path=r'C:\Users\enbek_kz\.wdm\drivers\chromedriver\win32\102.0.5005.61\chromedriver.exe')
        except Exception as e:
            print(e)
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.switch_to.window(self.driver.current_window_handle)
        driver = self.driver
        driver.get(self.url["list"])
        login = "//input[@placeholder='Логин или E-mail']"
        login_2 = "//input[@placeholder='Логин или Email']"
        try:
            WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, login)))
            driver.find_element(By.XPATH, login).send_keys(self.driver_data[0])
        except:
            WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, login_2)))
            driver.find_element(By.XPATH, login_2).send_keys(self.driver_data[0])
        passw = "//input[@placeholder='Пароль']"
        # passw = "pass"
        driver.find_element(By.XPATH, passw).send_keys(self.driver_data[1])
        driver.find_element(By.XPATH, passw).send_keys(Keys.RETURN)
        driver.get(self.url["list"])

    # create_dogovor
    def _check_iin(self, root, counter=1):
        while counter:
            self._sel_wait_el(By.XPATH,
                              ".//input[@name='IIN']/parent::div/parent::div/div[@class='mdb-ehr-progress' and @style='display: block;']",
                              5)
            self._sel_wait_el(By.XPATH,
                              ".//input[@name='IIN']/parent::div/parent::div/div[@class='mdb-ehr-progress' and @style='display: none;']",
                              5)
            time.sleep(1)
            if counter > 0:
                input_fam = root.find_element(By.XPATH, ".//input[@name='FAM']")
                if len(input_fam.get_attribute("value")) > 1:
                    print(input_fam.get_attribute("value"))
                    return True
            else:
                counter -= 1
        return False

    def _fill_iin(self, root, iin):
        self.anchor.click()

        input_iin = root.find_element(By.XPATH, ".//input[@name='IIN']")
        input_iin.send_keys(iin)
        button_iin = root.find_element(By.XPATH, ".//input[@name='IIN']/parent::div/span/button")
        button_iin.click()
        flag = self._check_iin(root, 2)
        if not flag:
            raise ValueError("Время ожидания истекло: не найден по ИИН")
        print("self._fill_iin > done")

    def _fill_string(self, root, num, dol):
        self.anchor.click()

        input_num = root.find_element(By.XPATH, ".//input[@name='numDogovor']")
        input_num.send_keys(num)

        input_dol = root.find_element(By.XPATH, ".//input[@name='shtatDolj']")
        input_dol.send_keys(dol)

        print("self._fill_string > done")

    def _fill_select(self, root, srok, vid):
        self.anchor.click()

        select_srok = Select(root.find_element(By.XPATH, ".//select[@name='dContractCate']"))
        select_srok.select_by_visible_text(srok)

        select_vid = Select(root.find_element(By.XPATH, ".//select[@name='partTime']"))
        select_vid.select_by_visible_text(vid)

        print("self._fill_select > done")

    def _fill_date(self, root, dogovor, nachalo, konec=""):
        self.anchor.click()

        input_dogovor = root.find_element(By.XPATH, ".//input[@name='dateZakDogovor']")
        input_dogovor.click()
        input_dogovor.send_keys(dogovor)
        self.anchor.click()

        input_nachalo = root.find_element(By.XPATH, ".//input[@name='dateBegDogovor']")
        input_nachalo.click()
        input_nachalo.send_keys(nachalo)
        self.anchor.click()

        if len(konec):
            input_konec = root.find_element(By.XPATH, ".//input[@name='dateEndDogovor']")
            input_konec.click()
            input_konec.send_keys(konec)
            self.anchor.click()

        print("self._fill_date > done")

    def _fill_dol(self, root, dol):
        driver = self.driver
        self.anchor.click()

        span_dogovor = root.find_element(By.XPATH,
                                         ".//label[text()='Должность ']/parent::div//span[@class='selection']")
        span_dogovor.click()

        root_dogovor = driver.find_element(By.XPATH,
                                           "//span[@class='select2-container select2-container--default select2-container--open']")

        input_dogovor = root_dogovor.find_element(By.XPATH, ".//input[@class='select2-search__field']")

        input_dogovor.send_keys(dol)

        if self._sel_wait_el(By.XPATH,
                             ".//li[@class='select2-results__option select2-results__option--highlighted' and text()='" + dol + "']",
                             sec=5):
            li_dogovor = driver.find_element(By.XPATH,
                                             ".//li[@class='select2-results__option select2-results__option--highlighted' and text()='" + dol + "']")
        elif self._sel_wait_el(By.XPATH, ".//li[@class='select2-results__option' and text()='" + dol + "']", sec=5):
            li_dogovor = driver.find_element(By.XPATH,
                                             ".//li[@class='select2-results__option' and text()='" + dol + "']")
        else:
            raise ValueError("Время ожидания истекло: Должность не найдена")
        li_dogovor.click()
        if not self._sel_wait_el(By.CSS_SELECTOR, "span.select2-container--open input.select2-search__field",
                                 appear=False):
            raise ValueError("Время ожидания истекло: Должность не выбрана")

        print("self._fill_dol > done")

    def _fill_adres(self, root, obl, center, adres, nas_punkt):
        driver = self.driver
        self.anchor.click()

        button_obl = root.find_element(By.XPATH, ".//Button[text()='Выбрать']")
        button_obl.click()

        self._sel_wait_el(By.XPATH, ".//div[@class='modal-content' and //h4[text()='Справочник регионов']]")
        root_adres = driver.find_element(By.XPATH,
                                         ".//div[@class='modal-content' and //h4[text()='Справочник регионов']]")

        li_obl = root_adres.find_element(By.XPATH, ".//li[span[text()='" + obl + "']]")
        li_obl.click()

        time.sleep(1)
        self._sel_wait_el(By.XPATH, ".//li[span[text()='" + center + "']]")
        li_center = root_adres.find_element(By.XPATH, ".//li[span[text()='" + center + "']]")
        li_center.click()

        button_adres = root_adres.find_element(By.XPATH, ".//button[text()='Выбор']")
        button_adres.click()

        try:
            button_otmena = root_adres.find_element(By.XPATH, ".//button[text()='Отмена']")
            button_otmena.click()
        except:
            pass

        if not self._sel_wait_el(By.XPATH, ".//div[@class='modal-content' and //h4[text()='Справочник регионов']]",
                                 appear=False):
            raise ValueError("Время ожидания истекло: Адрес не выбран")

        input_adres = root.find_element(By.XPATH, ".//input[@name='workPlace']")
        input_adres.send_keys(adres)

        span_nas_punkt = root.find_element(By.XPATH,
                                           ".//label[text()='Населённый пункт ']/parent::div//span[@class='selection']")
        span_nas_punkt.click()

        root_nas = driver.find_element(By.XPATH,
                                       "//span[@class='select2-container select2-container--default select2-container--open']")
        input_nas_punkt = root_nas.find_element(By.XPATH, ".//input[@class='select2-search__field']")
        input_nas_punkt.send_keys(nas_punkt)

        if self._sel_wait_el(By.XPATH,
                             ".//li[@class='select2-results__option select2-results__option--highlighted' and text()='" + nas_punkt + "']",
                             sec=5):
            li_nas = driver.find_element(By.XPATH,
                                         ".//li[@class='select2-results__option select2-results__option--highlighted' and text()='" + nas_punkt + "']")
        elif self._sel_wait_el(By.XPATH, ".//li[@class='select2-results__option' and text()='" + nas_punkt + "']",
                               sec=5):
            li_nas = driver.find_element(By.XPATH,
                                         ".//li[@class='select2-results__option' and text()='" + nas_punkt + "']")
        else:
            raise ValueError("Время ожидания истекло: Должность не найдена")
        li_nas.click()
        if not self._sel_wait_el(By.CSS_SELECTOR, "span.select2-container--open input.select2-search__field",
                                 appear=False):
            raise ValueError("Время ожидания истекло: Должность не выбрана")

        print("self._fill_adres > done")

    def _fill_rezhim(self, root, rezhim, stavka=False):
        self.anchor.click()

        select_rezhim = Select(root.find_element(By.XPATH, ".//select[@name='workingHours']"))
        select_rezhim.select_by_visible_text(rezhim)

        if stavka:
            self._sel_wait_el(By.XPATH, ".//input[@name='tariffRate']")
            input_stavka = root.find_element(By.XPATH, ".//input[@name='tariffRate']")
            input_stavka.send_keys(stavka)

        print("self._fill_rejim > done")

    def _fill_dog(self, data):
        driver = self.driver
        driver.get(self.url["add"])
        if self._sel_wait_el(By.XPATH, "//h3[text()='Добавление договора']"):
            self.anchor = driver.find_element(By.XPATH, "//h3[text()='Добавление договора']")
            root = driver.find_element(By.CSS_SELECTOR, ".content")

            iin_iin = data["ИИН"]
            self._fill_iin(root, iin_iin)

            string_num = data["Номер договора"]
            string_dol = data["Штатная должность"].strip()
            self._fill_string(root, string_num, string_dol)

            select_srok = data["Срок договора"]
            select_vid = data["Вид работы"]
            self._fill_select(root, select_srok, select_vid)

            rezhim = data["Режим рабочего времени"].split(", ")
            rezhim_rezhim = rezhim[0]
            rezhim_stavka = rezhim[1] if len(rezhim) > 1 else False
            self._fill_rezhim(root, rezhim_rezhim, rezhim_stavka)

            date_dogovor = data["Дата заключения договора"]
            date_nachalo = data["Дата начала работы"]
            date_konec = data["Дата окончания действия договора"] if (
                    "на определенный срок не менее одного года" in select_srok or "на время выполнения сезонной работы" in select_srok) else ""
            self._fill_date(root, date_dogovor, date_nachalo, date_konec)

            dol_dol = data["Должность"]
            self._fill_dol(root, dol_dol)

            select_country = Select(root.find_element(By.XPATH, ".//select[@name='workPlaceCountry']"))
            select_country.select_by_visible_text('Казахстан')

            adres_adres = ""
            adres_obl = data["Место выполнения работы"]["obl"]
            adres_center = data["Место выполнения работы"]["city"]
            nas_punkt = data["Место выполнения работы"]["nas_punkt"]
            try:
                adres_adres = data["Место выполнения работы"]["street"]
            except:
                adres_adres = data["Место выполнения работы"]["nas_punkt"]
            self._fill_adres(root, adres_obl, adres_center, adres_adres, nas_punkt)

            # select_military = Select(root.find_element(By.XPATH, ".//select[@name='army']"))
            # select_military.select_by_visible_text(data["Военная обязанность"])

            submit = root.find_element(By.XPATH, ".//input[@value='Сохранить']")
            submit.click()
        else:
            raise ValueError("Время ожидания истекло: https://www.enbek.kz/ru/cabinet/dogovor/add")
        print("self._fill_dog > done")


    def _search_iin_create(self, root, iin):
        self.anchor.click()

        input_iin = root.find_element(By.XPATH, ".//input[@name='iin']")
        input_iin.send_keys(iin)
        button_iin = root.find_element(By.XPATH,
                                       './/button[@type="submit" and text()="Найти"]')
        button_iin.click()

        if self._sel_wait_el(By.XPATH, '//strong[text()="Пусто..." ]', 3):
            return False
        else:
            return True

    def _check_dogovor_create(self, data):
        driver = self.driver
        driver.get(self.url["list"])
        if self._sel_wait_el(By.XPATH, "//a[text()[contains(., 'Добавить')]]"):
            self.anchor = driver.find_element(By.XPATH, '//strong[text()="Договоры"]')
            root = driver.find_element(By.CSS_SELECTOR, ".content")

            iin_iin = data["ИИН"]
            iin_exist = self._search_iin_create(root, iin_iin)
            print(iin_exist)
        else:
            raise ValueError("Время ожидания истекло: https://www.enbek.kz/ru/cabinet/dogovor/list")
        print("self._check_dogovor > done")
        return iin_exist

    def _to_ecp_priem(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, '//button[text()="Подписать договор и отправить"]')))

        driver.find_element(By.XPATH, '//button[text()="Подписать договор и отправить"]').click()

    # Public
    def create_dogovor(self, data):
        if not self.driver:
            self._sel_init()

        iin_exist = self._check_dogovor_create(data)
        if not iin_exist:
            self._fill_dog(data)
            time.sleep(3)

            self._to_ecp_priem()

            self._apply_dogovor()

            logs([str(datetime.datetime.now().strftime("%H:%M")), str(data["ИИН"]), "Внесён",
                  "Ok", "Прием"])
        else:
            logs([str(datetime.datetime.now().strftime("%H:%M")), str(data["ИИН"]), "Был внесён",
                  "Ok", "Прием"])
        time.sleep(3)



    def _search_iin_create1(self, root, iin, driver):
        self.anchor.click()

        input_iin = root.find_element(By.XPATH, ".//input[@name='iin']")
        input_iin.send_keys(iin)
        button_iin = root.find_element(By.XPATH,
                                       './/button[@type="submit" and text()="Найти"]')
        button_iin.click()

        dog = driver.find_element_by_class_name("item-list")
        dog_i = dog.find_element_by_xpath('div/div/a')
        link = dog_i.get_attribute('href')
        print(link)
        dog_i.click()

        dop_dr = self.driver
        dop_dr.get(link)
        dop = WebDriverWait(dop_dr, 3).until(ec.presence_of_element_located((By.LINK_TEXT, 'Добавить доп. соглашение')))
        link1 = dop.get_attribute('href')
        print(link1)
        dop.click()
        return link1

    def _check_dop_sogl(self, data):
        driver = self.driver
        driver.get(self.url["list"])
        if self._sel_wait_el(By.XPATH, "//a[text()[contains(., 'Добавить')]]"):
            self.anchor = driver.find_element(By.XPATH, '//strong[text()="Договоры"]')
            root = driver.find_element(By.CSS_SELECTOR, ".content")

            iin_iin = data["ИИН"]
            link = self._search_iin_create1(root, iin_iin, driver)
            print("self._check_dogovor > done")
            return link
        else:
            print("self._check_dogovor > done")
            raise ValueError("Время ожидания истекло: https://www.enbek.kz/ru/cabinet/dogovor/list")

    def _data_append(self, data, link):
        root = self.driver
        root.get(link)
        no_dop_sogl = root.find_element_by_xpath('//input[@name="numDogovor"]')
        no_dop_sogl.send_keys(data["Номер доп соглашения"])

        select_rezhim = Select(root.find_element(By.XPATH, "//select[@name='workingHours']"))
        select_rezhim.select_by_visible_text(data["Режим рабочего времени"])

        date_nachalo_dop_sogl = root.find_element_by_xpath("//input[@name='dateBegDogovor']")
        date_nachalo_dop_sogl.click()
        date_nachalo_dop_sogl.send_keys(data["Дата начала действия доп соглашения"])

        date_zakl_dop_sogl = root.find_element_by_xpath("//input[@name='dateZakDogovor']")
        date_zakl_dop_sogl.click()
        date_zakl_dop_sogl.send_keys(data["Дата заключения дополнительного соглашения"])

        # data['Срок договора']
        if len(data["Дата окончания действия дополнительного соглашения"]) != 0:
            if datetime.datetime.strptime(data["Дата окончания действия дополнительного соглашения"], "%d.%m.%Y") - datetime.datetime.strptime(data["Дата начала действия доп соглашения"], "%d.%m.%Y") >= datetime.timedelta(days=365):
                select_srok = Select(root.find_element(By.XPATH, "//select[@name='srokdop']"))
                select_srok.select_by_visible_text(data['Срок договора'])
                select_srok = data['Срок договора']
            else:
                select_srok = Select(root.find_element(By.XPATH, "//select[@name='srokdop']"))
                select_srok.select_by_visible_text("на неопределенный срок")
                select_srok = "на неопределенный срок"
        else:
            select_srok = Select(root.find_element(By.XPATH, "//select[@name='srokdop']"))
            select_srok.select_by_visible_text("на неопределенный срок")
            select_srok = "на неопределенный срок"

        select_vid = Select(root.find_element(By.XPATH, ".//select[@name='partTime']"))
        select_vid.select_by_visible_text(data["Вид работы"])

        date_konec = data["Дата окончания действия трудового договора"] if (
                "на определенный срок не менее одного года" in select_srok or "на время выполнения сезонной работы" in select_srok) else ""

        if len(date_konec):
            input_konec = root.find_element(By.XPATH, ".//input[@name='endDateTD']")
            input_konec.click()
            input_konec.send_keys(date_konec)

        date_dop_konec = data["Дата окончания действия дополнительного соглашения"] if (
                "на определенный срок не менее одного года" in select_srok or "на время выполнения сезонной работы" in select_srok) else ""

        if len(date_dop_konec) and date_dop_konec != "None" and date_dop_konec != "":
            input_dop_konec = root.find_element(By.XPATH, ".//input[@name='dateEndDogovor']")
            input_dop_konec.click()
            input_dop_konec.send_keys(date_dop_konec)

        dol = data['Должность']
        span_dogovor = root.find_element(By.XPATH,"//span[@class='selection']")
        span_dogovor = span_dogovor.find_element(By.XPATH, 'span')
        span_dogovor.click()
        root_dogovor = root.find_element(By.XPATH,"//span[@class='select2-container select2-container--default select2-container--open']")
        input_dogovor = root_dogovor.find_element(By.XPATH, ".//input[@class='select2-search__field']")
        input_dogovor.send_keys(dol)
        if self._sel_wait_el(By.XPATH,
                             "//li[@class='select2-results__option select2-results__option--highlighted' and text()='" + dol + "']",
                             sec=5):
            li_dogovor = root.find_element(By.XPATH,
                                             "//li[@class='select2-results__option select2-results__option--highlighted' and text()='" + dol + "']")
        elif self._sel_wait_el(By.XPATH, "//li[@class='select2-results__option' and text()='" + dol + "']", sec=5):
            li_dogovor = root.find_element(By.XPATH,
                                             "//li[@class='select2-results__option' and text()='" + dol + "']")
        else:
            raise ValueError("Время ожидания истекло: Должность не найдена")
        li_dogovor.click()
        if not self._sel_wait_el(By.CSS_SELECTOR, "span.select2-container--open input.select2-search__field",
                                 appear=False):
            raise ValueError("Время ожидания истекло: Должность не выбрана")

        # data['Штатная должность']
        input_dol = root.find_element(By.XPATH, "//input[@name='shtatDolj']")
        input_dol.send_keys(data['Штатная должность'])

        # data['Место выполнения работы']
        adres = ""
        obl = data["Место выполнения работы"]["obl"]
        center = data["Место выполнения работы"]["city"]
        nas_punkt = data["Место выполнения работы"]["nas_punkt"]
        try:
            adres = data["Место выполнения работы"]["street"]
        except:
            adres = data["Место выполнения работы"]["nas_punkt"]
        select_country = Select(root.find_element(By.XPATH, "//select[@name='workPlaceCountry']"))
        select_country.select_by_visible_text('Казахстан')
        button_obl = root.find_element(By.XPATH, "//Button[text()='Выбрать']")
        button_obl.click()

        self._sel_wait_el(By.XPATH, "//div[@class='modal-content' and //h4[text()='Справочник регионов']]")
        root_adres = root.find_element(By.XPATH,
                                         ".//div[@class='modal-content' and //h4[text()='Справочник регионов']]")
        li_obl = root_adres.find_element(By.XPATH, ".//li[span[text()='" + obl + "']]")
        li_obl.click()
        self._sel_wait_el(By.XPATH, "//li[span[text()='" + center + "']]")
        time.sleep(1)
        li_center = root_adres.find_element(By.XPATH, "//li[span[text()='" + center + "']]")
        time.sleep(1)
        li_center.click()

        button_adres = root_adres.find_element(By.XPATH, ".//button[text()='Выбор']")
        button_adres.click()

        try:
            button_otmena = root_adres.find_element(By.XPATH, ".//button[text()='Отмена']")
            button_otmena.click()
        except:
            pass

        if not self._sel_wait_el(By.XPATH, "//div[@class='modal-content' and //h4[text()='Справочник регионов']]",
                                 appear=False):
            raise ValueError("Время ожидания истекло: Адрес не выбран")

        input_adres = root.find_element(By.XPATH, "//input[@name='workPlace']")
        input_adres.send_keys(adres)

        span_nas = root.find_element(By.XPATH, ".//label[text()='Населённый пункт ']/parent::div//span[@class='selection']")
        span_nas = span_nas.find_element(By.XPATH, 'span')
        span_nas.click()
        root_dogovor = root.find_element(By.XPATH,
                                         "//span[@class='select2-container select2-container--default select2-container--open']")
        input_dogovor = root_dogovor.find_element(By.XPATH, ".//input[@class='select2-search__field']")
        center = nas_punkt
        input_dogovor.send_keys(center)

        if self._sel_wait_el(By.XPATH,
                             "//li[@class='select2-results__option select2-results__option--highlighted' and text()='" + center + "']",
                             sec=5):
            li_center = root.find_element(By.XPATH,
                                             "//li[@class='select2-results__option select2-results__option--highlighted' and text()='" + center + "']")
        elif self._sel_wait_el(By.XPATH, "//li[@class='select2-results__option' and text()='" + center + "']", sec=5):
            li_center = root.find_element(By.XPATH,
                                             "//li[@class='select2-results__option' and text()='" + center + "']")
        else:
            raise ValueError("Время ожидания истекло: Должность не найдена")
        li_center.click()

        apply = root.find_element(By.XPATH, "//input[@value='Сохранить']")
        apply.click()

    def _to_ecp_peremew(self):
        driver = self.driver
        WebDriverWait(driver, 3).until(
            ec.presence_of_element_located((By.XPATH, '//strong[text()="Социальные отпуска"]')))

        deystvie = driver.find_element(By.XPATH, '//table[thead[tr[th[text()="№ Дополнительного соглашения"]]]]')
        deystvie = deystvie.find_element(By.XPATH, 'tbody/tr[last()]/td[7]/div/button')
        deystvie.click()

        WebDriverWait(driver, 3).until(
            ec.presence_of_element_located((By.XPATH, '//a[text()="Отправить"]')))

        otpravit_arr = driver.find_elements(By.XPATH, '//a[text()="Отправить"]')
        for otpravit in otpravit_arr:
            try:
                driver.execute_script("arguments[0].click();", otpravit)
            except:
                pass

    def create_dop_sogl(self, data):
        if not self.driver:
            self._sel_init()

        link = self._check_dop_sogl(data)

        self._data_append(data, link)

        try:
            self._to_ecp_peremew()
            self._apply_dogovor()
            logs([str(datetime.datetime.now().strftime("%H:%M")), str(data["ИИН"]), "Внесён",
                  "Ok", "Перемещение"])
        except:
            logs([str(datetime.datetime.now().strftime("%H:%M")), str(data["ИИН"]), "Был внесён",
                  "Ok", "Перемещение"])

    def _search_iin_create2(self, root, iin, driver):
        self.anchor.click()
        print('do_iin')
        input_iin = root.find_element(By.XPATH, ".//input[@name='iin']")
        input_iin.send_keys(iin)
        button_iin = root.find_element(By.XPATH,
                                       './/button[@type="submit" and text()="Найти"]')
        button_iin.click()
        try:
            dog = driver.find_element_by_class_name("item-list")
            dog_i = dog.find_element_by_xpath('div/div/a')
            link = dog_i.get_attribute('href')
            print(link)
            dog_i.click()
            print(2)

            dop_dr = self.driver
            dop_dr.get(link)
            time.sleep(2)
            rast = WebDriverWait(dop_dr, 3).until(ec.presence_of_element_located((By.XPATH, "//button[text()='Расторгнуть']")))
            # rast = dop_dr.find_element(By.XPATH, "//button[text()='Расторгнуть']")
            rast.click()
            return dop_dr
        except:
            return "already"

    def _check_del_dog(self, data):
        driver = self.driver
        driver.get(self.url["list"])
        if self._sel_wait_el(By.XPATH, "//a[text()[contains(., 'Добавить')]]"):
            self.anchor = driver.find_element(By.XPATH, '//strong[text()="Договоры"]')
            root = driver.find_element(By.CSS_SELECTOR, ".content")

            iin_iin = data["ИИН"]
            driver_common = self._search_iin_create2(root, iin_iin, driver)
            print("self._check_dogovor > done")
            return driver_common
        else:
            print("self._check_dogovor > done")
            raise ValueError("Время ожидания истекло: https://www.enbek.kz/ru/cabinet/dogovor/list")

    def _data_append_del(self, data, root):
        date_rast_dog = WebDriverWait(root, 3).until(ec.presence_of_element_located((By.XPATH, "//input[@name='dateCutDogovor']")))
        date_rast_dog.click()
        root.execute_script('document.getElementsByName("dateCutDogovor")[0].removeAttribute("readonly")')
        date_rast_dog.send_keys(data["Дата расторжение"])
        prichina = root.find_element(By.XPATH, "//div[@class='prich']/div/span/span/span")
        prichina.click()
        prich = data["Причина"]
        if prich == "Достижение работником пенсионного возраста":
            prich = "Достижение работником пенсионного возраста, установленного" + "\u00A0" + "пунктом 1 статьи 11" + "\u00A0" + "Закона Республики Казахстан «О пенсионном обеспечении в Республике Казахстан», с правом ежегодного продления срока трудового договора по взаимному согласию сторон"
        input_prichina = root.find_element(By.XPATH, ".//input[@class='select2-search__field']")
        input_prichina.send_keys(prich)
        print(3)
        if self._sel_wait_el(By.XPATH,
                             "//li[@class='select2-results__option select2-results__option--highlighted' and text()='" + prich + "']",
                             sec=5):
            li_prichina = root.find_element(By.XPATH,
                                           "//li[@class='select2-results__option select2-results__option--highlighted' and text()='" + prich + "']")
        elif self._sel_wait_el(By.XPATH, "//li[@class='select2-results__option' and text()='" + prich + "']", sec=5):
            li_prichina = root.find_element(By.XPATH,
                                           "//li[@class='select2-results__option' and text()='" + prich + "']")
        else:
            raise ValueError("Время ожидания истекло: Должность не найдена")
        li_prichina.click()
        if not self._sel_wait_el(By.CSS_SELECTOR, "span.select2-container--open input.select2-search__field",
                                 appear=False):
            raise ValueError("Время ожидания истекло: Должность не выбрана")

        submit = root.find_element(By.XPATH, "//button[text()='Расторгнуть']")
        logs([str(datetime.datetime.now().strftime("%H:%M")), str(data["ИИН"]), "Внесён",
              "Ok", "Увольнение"])
        submit.click()

    def terminate_dog(self, data):
        if not self.driver:
            self._sel_init()

        driver = self._check_del_dog(data)

        if driver == "already":
            logs([str(datetime.datetime.now().strftime("%H:%M")), str(data["ИИН"]), "Не внесён",
                  "Был уже удален в enbek.kz", "Увольнение"])
        else:
            self._data_append_del(data, driver)

            self._apply_dogovor()

    def _apply_dogovor(self):
        passw = self.passw
        driver = self.driver
        time.sleep(2)
        apply_button = driver.find_element(By.XPATH, "//button[text()='OK']")
        apply_button.click()
        pythonRPA.bySelector([{"class_name":"Chrome_WidgetWin_1","backend":"uia"},{"backend":"uia"},{"title":"Имя файла:"}]).wait_appear(30)
        time.sleep(1)
        # print(self.path_to_ecp)
        keyboard.write(self.path_to_ecp)
        time.sleep(1)
        keyboard.press('enter')
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.NAME, "ecpPassword")))
        time.sleep(1)
        # print(passw)
        keyboard.write(passw)
        time.sleep(2)
        # driver.find_element(By.XPATH, '//div[@class="modal-footer"]/button').click()
        # driver.find_element(By.XPATH, '//div[@class="modal-footer"]/button').click()
        # keyboard.press('enter')
        ok_buttons = driver.find_elements(By.XPATH, '//div[@class="modal-footer"]/button[contains(text(), "OK")]')
        for ok_button in ok_buttons:
            try:
                driver.execute_script("arguments[0].click();", ok_button)
            except:
                pass
        time.sleep(10)

    def quit(self):
        if self.driver:
            self.driver.quit()

    def _search_iin_create_otpusk(self, root, iin, driver):
        self.anchor.click()

        input_iin = root.find_element(By.XPATH, ".//input[@name='iin']")
        input_iin.send_keys(iin)
        button_iin = root.find_element(By.XPATH,
                                       './/button[@type="submit" and text()="Найти"]')
        button_iin.click()

        dog = driver.find_element_by_class_name("item-list")
        dog_i = dog.find_element_by_xpath('div/div/a')
        link = dog_i.get_attribute('href')
        print(link)
        dog_i.click()

        dop_dr = self.driver
        dop_dr.get(link)
        # dop = WebDriverWait(dop_dr, 3).until(ec.presence_of_element_located((By.LINK_TEXT, 'Добавить доп. соглашение')))
        otpusk = WebDriverWait(dop_dr, 3).until(ec.presence_of_element_located((By.XPATH, '//a[text()="Добавить соц. отпуск"]')))
        link1 = otpusk.get_attribute('href')
        print(link1)
        otpusk.click()
        return link1

    def _check_otpusk(self, data):
        driver = self.driver
        driver.get(self.url["list"])
        if self._sel_wait_el(By.XPATH, "//a[text()[contains(., 'Добавить')]]"):
            self.anchor = driver.find_element(By.XPATH, '//strong[text()="Договоры"]')
            root = driver.find_element(By.CSS_SELECTOR, ".content")

            iin_iin = data["ИИН"]
            link = self._search_iin_create_otpusk(root, iin_iin, driver)
            print("self._check_dogovor > done")
            return link
        else:
            print("self._check_dogovor > done")
            raise ValueError("Время ожидания истекло: https://www.enbek.kz/ru/cabinet/dogovor/list")

    def _data_append_otpusk(self, data, link):
        root = self.driver
        root.get(link)

        WebDriverWait(root, 2).until(ec.presence_of_element_located((By.XPATH, '//h3[text()="Добавление социального отпуска"]')))

        tip_otpuska = root.find_element(By.XPATH, '//span[@title="Выберите тип отпуска"]')
        tip_otpuska.click()

        tip = data["Тип отпуска"]
        if self._sel_wait_el(By.XPATH,
                             "//li[@class='select2-results__option select2-results__option--highlighted' and text()='" + tip + "']",
                             sec=5):
            li_otpusk = root.find_element(By.XPATH,
                                             "//li[@class='select2-results__option select2-results__option--highlighted' and text()='" + tip + "']")
        elif self._sel_wait_el(By.XPATH, "//li[@class='select2-results__option' and text()='" + tip + "']", sec=5):
            li_otpusk = root.find_element(By.XPATH,
                                             "//li[@class='select2-results__option' and text()='" + tip + "']")
        else:
            raise ValueError("Время ожидания истекло: Должность не найдена")
        li_otpusk.click()

        ne_rabotal_s = root.find_element(By.XPATH, '//input[@name="beginDate"]')
        ne_rabotal_s.send_keys(data["Дата с"])

        ne_rabotal_po = root.find_element(By.XPATH, '//input[@name="endDate"]')
        ne_rabotal_po.send_keys(data["Дата по"])

        try:
            no_tabelya = root.find_element(By.XPATH, '//input[@name="sheetNumber"]')
            no_tabelya.send_keys(data["Номер табеля"])
        except:
            print("Другой тип отпуска")

        try:
            first_date = root.find_element(By.XPATH, '//input[@name="workDate"]')
            first_date.send_keys(data["Дата по"])
        except:
            print("Другой тип отпуска")

        apply = root.find_element(By.XPATH, '//input[@value="Сохранить"]')

        apply.click()

    def _to_ecp_otpusk(self):
        driver = self.driver
        WebDriverWait(driver, 3).until(
            ec.presence_of_element_located((By.XPATH, '//strong[text()="Социальные отпуска"]')))

        deystvie = driver.find_element(By.XPATH, '//table[thead[tr[th[text()="Тип отпуска"]]]]')
        deystvie = deystvie.find_element(By.XPATH, 'tbody/tr[last()]/td[7]/div/button')
        deystvie.click()

        WebDriverWait(driver, 3).until(
            ec.presence_of_element_located((By.XPATH, '//a[text()="Отправить"]')))
        otpravit = driver.find_element(By.XPATH, '//a[text()="Отправить"]')
        otpravit.click()

    def to_otpusk(self, data):
        if not self.driver:
            self._sel_init()

        link = self._check_otpusk(data)

        self._data_append_otpusk(data, link)

        self._to_ecp_otpusk()

        self._apply_dogovor()

        logs([str(datetime.datetime.now().strftime("%H:%M")), str(data["ИИН"]), "Внесён",
              "Ok", "Отпускные"])
