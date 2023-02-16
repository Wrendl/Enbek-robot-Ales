"""CORE 19.11.21"""
import ctypes
import glob
import json
import os
import pathlib
import shutil
import urllib3
import win32clipboard
from pywinauto import Application
from pywinauto.timings import wait_until_passes
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.switch_to import SwitchTo
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
urllib3.disable_warnings(RuntimeWarning)
if ctypes.windll.user32.GetKeyboardLayout(0) != 67699721:
    raise ValueError("Смените раскладку на ENG")
D_TIMEOUT = 10


class Path:

    @staticmethod
    def glob(path: str, recursive=False):
        return glob.glob(pathname=path, recursive=recursive)

    @staticmethod
    def copy(src: str, dst: str, follow_symlinks=True):
        src = str(pathlib.Path(src).absolute().resolve())
        dst = str(pathlib.Path(dst).absolute().resolve())
        return shutil.copy(src=src, dst=dst, follow_symlinks=follow_symlinks)

    @staticmethod
    def move(src: str, dst: str):
        src = str(pathlib.Path(src).absolute().resolve())
        dst = str(pathlib.Path(dst).absolute().resolve())
        return shutil.move(src=src, dst=dst)

    @staticmethod
    def cwd():
        return str(pathlib.Path.cwd().resolve())

    @staticmethod
    def home():
        return str(pathlib.Path.home().resolve())

    @staticmethod
    def name(path: str):
        path = str(pathlib.Path(path).resolve())
        return str(os.path.basename(path))

    @staticmethod
    def parent(path: str):
        path = pathlib.Path(path).absolute().resolve()
        return str(path.parent)

    @staticmethod
    def absolute(path: str):
        path = pathlib.Path(path).absolute().resolve()
        return str(path)

    @staticmethod
    def rmfile(path: str):
        path = pathlib.Path(path).absolute().resolve()
        path.unlink()

    @staticmethod
    def rmdir(path: str):
        path = pathlib.Path(path).absolute().resolve()
        path.rmdir()

    @staticmethod
    def rmtree(path: str, ignore_errors=False, onerror=None):
        path = str(pathlib.Path(path).absolute().resolve())
        shutil.rmtree(path=path, ignore_errors=ignore_errors, onerror=onerror)

    @staticmethod
    def mkdir(path: str, parents=True, exist_ok=True):
        path = pathlib.Path(path).absolute().resolve()
        path.mkdir(parents=parents, exist_ok=exist_ok)
        return str(path)

    @staticmethod
    def isdir(path: str):
        path = pathlib.Path(path).absolute().resolve()
        return path.is_dir()

    @staticmethod
    def isfile(path: str):
        path = pathlib.Path(path).absolute().resolve()
        return path.is_file()

    @staticmethod
    def join(a: str, *paths: str):
        a = pathlib.Path(a).absolute().resolve()
        return os.path.join(str(a), *paths)

    @staticmethod
    def unpack(src: str, dst: str = None):
        src = str(pathlib.Path(src).absolute().resolve())
        dst = str(pathlib.Path(dst).absolute().resolve()) if dst else dst
        shutil.unpack_archive(src, dst)

    @staticmethod
    def downloaded(path: str, timeout=D_TIMEOUT):
        while timeout:
            sleep(1)
            timeout -= 1
            if len(Path.glob(path)):
                sleep(1)
                return Path.glob(path)[0]
        return None

    @staticmethod
    def clean(path: str):
        path = str(pathlib.Path(path).absolute().resolve())
        Path.rmtree(path)
        Path.mkdir(path)
        return path

    @staticmethod
    def compare(src: str, dst: str):
        src = str(pathlib.Path(src).absolute().resolve())
        dst = str(pathlib.Path(dst).absolute().resolve())
        if src != dst:
            return False
        else:
            return True


class Json:

    @staticmethod
    def read(path):
        with open(path, 'r', encoding='utf-8') as fp:
            data = json.load(fp)
        return data

    @staticmethod
    def write(path, data):
        with open(path, 'w+', encoding='utf-8') as fp:
            json.dump(data, fp, ensure_ascii=False)


class Container:
    def __init__(self):
        pass

    def __call__(self, data: dict = None):
        if data:
            for key in data:
                self.__dict__[key] = data[key]
            return self
        else:
            return self.__dict__


class JsonData(Container):

    def __init__(self, path: str = None):
        super().__init__()
        if path:
            self.read(path)

    def read(self, json_path: str):
        data = Json.read(json_path)
        for key in data:
            self.__dict__[key] = data[key]
        return self

    def write(self, json_path: str):
        Json.write(json_path, self.__dict__)
        return self


class Clipboard:

    @staticmethod
    def get(timing_before=0.3):
        sleep(timing_before)
        win32clipboard.OpenClipboard()
        result = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
        win32clipboard.CloseClipboard()
        return result

    @staticmethod
    def set(text: str, timing_before=0.3, timing_after=0.3):
        def set_(text_):
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, text_)
            win32clipboard.CloseClipboard()

        sleep(timing_before)
        set_(text)
        n = 100
        while Clipboard.get(timing_before=0) != text and n:
            n -= 1
            sleep(0.1)
        if n == 0:
            raise ValueError('Значение не присвоено')
        sleep(timing_after)


class Web:
    options = ChromeOptions
    keys = Keys
    path = Path
    by = By
    ec = ec
    ac = ActionChains

    def __init__(self, driver_path=None, download_path=None, user_data_dir=None, options=None, debug=False):
        default_driver_path = r"C:\Portable\PyCharmPortable\App\Chromium\chromedriver.exe"
        self.driver_path = driver_path if driver_path is not None else default_driver_path
        self.download_path = download_path if download_path is not None else os.path.join(pathlib.Path.home(),
                                                                                          'Downloads')
        if options:
            self.options = options
        else:
            self.options = ChromeOptions()
            self.options.add_experimental_option("excludeSwitches", ["enable-logging", "enable-automation"])
            self.options.add_experimental_option("useAutomationExtension", False)
            self.options.add_experimental_option("prefs", {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
                "profile.default_content_settings.popups": 0,
                "download.default_directory": self.download_path,
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": False,
                "profile.content_settings.exceptions.automatic_downloads.*.setting": 1
            })
            self.options.add_argument("--start-maximized")
            self.options.add_argument("--no-sandbox")
            self.options.add_argument("--disable-dev-shm-usage")
            self.options.add_argument("--disable-print-preview")
            self.options.add_argument("--disable-extensions")
            self.options.add_argument("--disable-notifications")
            self.options.add_argument("--ignore-ssl-errors=yes")
            self.options.add_argument("--ignore-certificate-errors")
        if user_data_dir:
            self.options.add_argument(f"user-data-dir={user_data_dir}")
        self.debug = debug

        if driver_path == '':
            self.webdriver = webdriver.Chrome(ChromeDriverManager().install(), options=self.options)
        else:
            self.webdriver = webdriver.Chrome(self.driver_path, options=self.options)
        self.switch_to = SwitchTo(self.webdriver)

    # ? Native

    def get(self, url: any):
        return self.webdriver.get(url)

    def back(self):
        return self.webdriver.back()

    def forward(self):
        return self.webdriver.forward()

    def close(self):
        return self.webdriver.close()

    def quit(self):
        return self.webdriver.quit()

    def maximize_window(self):
        return self.webdriver.maximize_window()

    def minimize_window(self):
        return self.webdriver.minimize_window()

    def execute_script(self, script: any, *args: any):
        return self.webdriver.execute_script(script, *args)

    def execute_async_script(self, script: any, *args: any):
        return self.webdriver.execute_async_script(script, *args)

    def save_screenshot(self, filename: str):
        return self.webdriver.save_screenshot(filename)

    def title(self):
        return self.webdriver.title

    def current_url(self):
        return self.webdriver.current_url

    def window_handles(self):
        return self.webdriver.window_handles

    def current_window_handle(self):
        return self.webdriver.current_window_handle

    # ? Extended

    def alert(self, text='', timeout=D_TIMEOUT):
        try:
            WebDriverWait(self.webdriver, timeout).until(ec.alert_is_present(), text)
            self.webdriver.switch_to.alert.accept()
            return True
        except TimeoutException:
            return False

    def focus(self, index=-1, frame=None, f_index=0):
        self.webdriver.switch_to.window(self.window_handles()[index])
        if frame:
            self.webdriver.switch_to.frame(self.find_elements(frame)[f_index].webobject)

    def find_element(self, selector, by='xpath', timeout=D_TIMEOUT, until_not=False, event=None):
        if event is None:
            event = ec.presence_of_element_located
        if timeout:
            self.wait_element(selector, by, timeout, until_not, event)
        webobject = self.webdriver.find_element(by, selector)
        el = WebElement(driver=self.webdriver, webobject=webobject, selector=selector, by=by, debug=self.debug)
        return el

    def find_elements(self, selector, by='xpath', timeout=D_TIMEOUT, until_not=False, event=None):
        if event is None:
            event = ec.presence_of_element_located
        if timeout:
            self.wait_element(selector, by, timeout, until_not, event)
        webobjects = self.webdriver.find_elements(by, selector)
        els = []
        for each in webobjects:
            els.append(WebElement(driver=self.webdriver, webobject=each, selector=selector, by=by, debug=self.debug))
        return els

    def wait_element(self, selector, by='xpath', timeout=D_TIMEOUT, until_not=False, event=None):
        if event is None:
            event = ec.presence_of_element_located
        try:
            if until_not:
                WebDriverWait(self.webdriver, timeout).until_not(event((by, selector)))
            else:
                WebDriverWait(self.webdriver, timeout).until(event((by, selector)))
            flag = True
        except Exception as e:
            if self.debug:
                print(e)
            flag = False
        if self.debug:
            print(selector, "appeared:", flag)
        return flag


class WebElement:
    class IsSelect:
        def __init__(self, webelement):
            self.__select = Select(webelement)
            self.options = self.__select.options
            self.all_selected_options = self.__select.all_selected_options
            self.is_multiple = self.__select.is_multiple

        # Related

        def select_by_index(self, index, delay_before=0, delay_after=0):
            sleep(delay_before)
            self.__select.select_by_index(index)
            sleep(delay_after)

        def select_by_value(self, value, delay_before=0, delay_after=0):
            sleep(delay_before)
            self.__select.select_by_value(value)
            sleep(delay_after)

        def select_by_visible_text(self, text, delay_before=0, delay_after=0):
            sleep(delay_before)
            self.__select.select_by_visible_text(text)
            sleep(delay_after)

        def deselect_by_index(self, index, delay_before=0, delay_after=0):
            sleep(delay_before)
            self.__select.deselect_by_index(index)
            sleep(delay_after)

        def deselect_by_value(self, value, delay_before=0, delay_after=0):
            sleep(delay_before)
            self.__select.deselect_by_value(value)
            sleep(delay_after)

        def deselect_by_visible_text(self, text, delay_before=0, delay_after=0):
            sleep(delay_before)
            self.__select.deselect_by_visible_text(text)
            sleep(delay_after)

        def deselect_all(self, delay_before=0, delay_after=0):
            sleep(delay_before)
            self.__select.deselect_all()
            sleep(delay_after)

    def __init__(self, driver, webobject, selector, by='xpath', debug=False):
        self.webdriver = driver
        self.webobject = webobject
        self.selector = selector
        self.by = by
        if webobject.tag_name.lower() == "select":
            self.is_select = self.IsSelect(self.webobject)
        self.debug = debug

    # ? Related

    def find_element(self, selector, by='xpath', timeout=D_TIMEOUT, until_not=False, event=None):
        if event is None:
            event = ec.presence_of_element_located
        if selector[0] != '.':
            raise ValueError("Дочерний селектор должен начинаться с '.'")
        if timeout:
            self.wait_element(selector, by, timeout, until_not, event)
        webobject = self.webobject.find_element(by, selector)
        el = WebElement(driver=self.webdriver, webobject=webobject, selector=selector, by=by, debug=self.debug)
        return el

    def find_elements(self, selector, by='xpath', timeout=D_TIMEOUT, until_not=False, event=None):
        if event is None:
            event = ec.presence_of_element_located
        if selector[0] != '.':
            raise ValueError("Дочерний селектор должен начинаться с '.'")
        if timeout:
            self.wait_element(selector, by, timeout, until_not, event)
        webobjects = self.webobject.find_elements(by, selector)
        els = []
        for each in webobjects:
            els.append(WebElement(driver=self.webdriver, webobject=each, selector=selector, by=by, debug=self.debug))
        return els

    def wait_element(self, selector, by='xpath', timeout=D_TIMEOUT, until_not=False, event=None, exc=True):
        if selector[0] == '.':
            selector = f'{self.selector}{selector[1:]}'
        else:
            selector = f'{self.selector}{selector}'
            if exc:
                raise ValueError("Дочерний селектор должен начинаться с '.'")

        if event is None:
            event = ec.presence_of_element_located
        try:
            if until_not:
                WebDriverWait(self.webdriver, timeout).until_not(event((by, selector)))
            else:
                WebDriverWait(self.webdriver, timeout).until(event((by, selector)))
            flag = True
        except Exception as e:
            if self.debug:
                print(e)
            flag = False
        if self.debug:
            print(selector, "appeared:", flag)
        return flag

    # ? Actions

    def click(self, delay_before=0, delay_after=0, scroll=True):
        sleep(delay_before)
        if scroll:
            self.scroll()
        self.webobject.click()
        sleep(delay_after)
        return self

    def double_click(self, delay_before=0, delay_after=0, scroll=True):
        sleep(delay_before)
        if scroll:
            self.scroll()
        ac = ActionChains(self.webdriver)
        ac.double_click(self.webobject).perform()
        sleep(delay_after)
        return self

    def scroll(self, delay_before=0, delay_after=0):
        sleep(delay_before)
        try:
            ac = ActionChains(self.webdriver)
            ac.move_to_element(self.webobject).perform()
        except (Exception,):
            pass
        sleep(delay_after)
        return self

    def send_keys(self, *args, delay_before=0, delay_after=0, clear=False):
        sleep(delay_before)
        if clear:
            self.webobject.clear()
        self.webobject.send_keys(*args)
        sleep(delay_after)
        return self

    def get_attribute(self, name, delay_before=0, delay_after=0):
        sleep(delay_before)
        value = self.webobject.get_attribute(name)
        sleep(delay_after)
        return value

    def get_text(self, delay_before=0, delay_after=0):
        sleep(delay_before)
        value = self.webobject.text
        sleep(delay_after)
        return str(value)

    def clear(self, delay_before=0, delay_after=0):
        sleep(delay_before)
        self.webobject.clear()
        sleep(delay_after)
        return self


class App:
    class Keys:
        CANCEL = '{VK_CANCEL}'  # ^break
        HELP = '{VK_HELP}'
        BACKSPACE = '{BACKSPACE}'
        BACK_SPACE = BACKSPACE
        TAB = '{VK_TAB}'
        CLEAR = '{VK_CLEAR}'
        RETURN = '{VK_RETURN}'
        ENTER = '{ENTER}'
        SHIFT = '{VK_LSHIFT}'
        LEFT_SHIFT = SHIFT
        CONTROL = '{VK_CONTROL}'
        LEFT_CONTROL = CONTROL
        ALT = '{VK_MENU}'
        LEFT_ALT = ALT
        PAUSE = '{VK_PAUSE}'
        ESCAPE = '{VK_ESCAPE}'
        SPACE = '{VK_SPACE}'
        PAGE_UP = '{PGUP}'
        PAGE_DOWN = '{PGDN}'
        END = '{VK_END}'
        HOME = '{VK_HOME}'
        LEFT = '{VK_LEFT}'
        ARROW_LEFT = LEFT
        UP = '{VK_UP}'
        ARROW_UP = UP
        RIGHT = '{VK_RIGHT}'
        ARROW_RIGHT = RIGHT
        DOWN = '{VK_DOWN}'
        ARROW_DOWN = DOWN
        INSERT = '{VK_INSERT}'
        DELETE = '{VK_DELETE}'

        NUMPAD0 = '{VK_NUMPAD0}'  # number pad keys
        NUMPAD1 = '{VK_NUMPAD1}'
        NUMPAD2 = '{VK_NUMPAD2}'
        NUMPAD3 = '{VK_NUMPAD3}'
        NUMPAD4 = '{VK_NUMPAD4}'
        NUMPAD5 = '{VK_NUMPAD5}'
        NUMPAD6 = '{VK_NUMPAD6}'
        NUMPAD7 = '{VK_NUMPAD7}'
        NUMPAD8 = '{VK_NUMPAD8}'
        NUMPAD9 = '{VK_NUMPAD9}'
        MULTIPLY = '{VK_MULTIPLY}'
        ADD = '{VK_ADD}'
        SEPARATOR = '{VK_SEPARATOR}'
        SUBTRACT = '{VK_SUBTRACT}'
        DECIMAL = '{VK_DECIMAL}'
        DIVIDE = '{VK_DIVIDE}'

        F1 = '{VK_F1}'  # function  keys
        F2 = '{VK_F2}'
        F3 = '{VK_F3}'
        F4 = '{VK_F4}'
        F5 = '{VK_F5}'
        F6 = '{VK_F6}'
        F7 = '{VK_F7}'
        F8 = '{VK_F8}'
        F9 = '{VK_F9}'
        F10 = '{VK_F10}'
        F11 = '{VK_F11}'
        F12 = '{VK_F12}'

        COMMAND = CONTROL

    def __init__(self):
        self.keys = self.Keys
        self.application = Application(backend='uia', allow_magic_lookup=True)

    # ? Application

    def execute(self, path: str, param: str = None):
        if not Path.isfile(path):
            raise ValueError(f'execute file not found: {path}')
        cmd = path if param is None else f'{path} "{param}"'
        self.application.start(cmd)

    # ? Search

    def __find(self, selector, timeout):

        # * callable
        def connect():
            connect_ = {'class_name': selector[0]['class_name'], 'control_type': selector[0]['control_type']}
            self.application.connect(**connect_)
            windows_ = self.application.windows(**selector[0])
            if not len(windows_):
                raise
            for each in windows_:
                if each.element_info.rectangle.left is None:
                    raise
            return windows_

        def find(window_):
            elements_ = window_.descendants(**selector[1])
            if not len(elements_):
                raise
            for each in elements_:
                if each.element_info.rectangle.left is None:
                    raise
            return elements_

        # * windows
        if 'list_index' in selector[0]:
            window_list_index = selector[0]["list_index"]
            del selector[0]["list_index"]
        else:
            window_list_index = None

        windows = wait_until_passes(timeout, 0.5, connect)
        window = windows[0] if window_list_index is None else windows[window_list_index]

        # * elements
        if len(selector) > 1:
            if 'list_index' in selector[1]:
                element_list_index = selector[1]["list_index"]
                del selector[1]["list_index"]
            else:
                element_list_index = None
            elements = wait_until_passes(timeout, 0.5, find, (Exception,), window)
            element = elements[0] if element_list_index is None else elements[element_list_index]

            return elements if element_list_index is None else element
        else:
            return windows if window_list_index is None else window

    def find_element(self, selector: list, timeout=D_TIMEOUT):
        # * copy
        selector_copy = [dict(el) for el in selector]

        element = self.__find(selector_copy, timeout)
        return element

    def find_elements(self, selector: list, timeout=D_TIMEOUT):
        # * copy
        selector_copy = [dict(el) for el in selector]

        if len(selector_copy) == 1:
            if 'list_index' in selector_copy[0]:
                del selector_copy[0]["list_index"]
        else:
            if 'list_index' in selector_copy[1]:
                del selector_copy[1]["list_index"]
        elements = self.__find(selector_copy, timeout)
        return elements

    def wait_element(self, selector: list, timeout=D_TIMEOUT, until_not=False):
        # * copy
        selector_copy = [dict(el) for el in selector]

        while timeout >= 0:
            try:
                element = self.__find(selector_copy, timeout=1 if timeout > 1 else timeout)
            except (Exception,):
                element = None
            timeout -= 1
            if until_not:
                if element is None:
                    return True
                else:
                    timeout -= 1
            else:
                if element is None:
                    timeout -= 1
                else:
                    return True
        return False
