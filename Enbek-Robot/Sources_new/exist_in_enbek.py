# -*- coding: utf-8 -*-
import time
from init import credentials, period, logs
from pyPythonRPA.Robot import pythonRPA
from Sources_new.priem import Priem
from Sources.new_enbek.enbek import Enbek
from Sources.new_enbek.settings import enbek_login, enbek_password


def search_enbek(list):
    # Start
    enbek = Enbek()
    enbek.start(enbek_login, enbek_password)

    # Search method
    for i in list:
        enbek.find_element('//input[@class="MuiInputBase-input css-mnn31"]').click()
        enbek.find_element('//input[@class="MuiInputBase-input css-mnn31"]').send_keys(enbek.keys.CONTROL + 'a')
        enbek.find_element('//input[@class="MuiInputBase-input css-mnn31"]').send_keys(enbek.keys.BACKSPACE)

        enbek.find_element('//input[@class="MuiInputBase-input css-mnn31"]').send_keys(i)
        enbek.find_element('//span[@class="contraxts2Search_searchField__button__3cYaa"]').click()
        time.sleep(1)
        enbek.find_element('//span[@class="contraxts2Search_searchField__button__3cYaa"]').click()
        time.sleep(1)

        tr = enbek.find_elements('//table[@class="contractsTable_table__sZ6EM"]/tbody/tr')
        logs(i, len(tr), '', '', '')
        print(i, '----', len(tr))
    enbek.quit()


def get_from_1C():
    oneC_app = pythonRPA.application(r"C:\Program Files\1cv8\common\1cestart.exe")
    root_path = str(__file__).split("Sources")[0].replace("/", "\\")
    credentials1 = credentials()
    period1 = period()
    priem = Priem(period1, credentials1, oneC_app)
    g_arr = priem.get_list()
    return g_arr


if __name__ == '__main__':
    list1 = get_from_1C()
    search_enbek(list1)
