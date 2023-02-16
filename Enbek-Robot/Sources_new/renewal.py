import time
from Sources.new_enbek.enbek import Enbek
from Sources.new_enbek.settings import enbek_login, enbek_password

# Start
enbek = Enbek()
enbek.start(enbek_login, enbek_password)

# Search method
enbek.find_element('//div[text()="Расширенный поиск"]').click()
enbek.find_element('//div[div[text()="Статус"]]/div[2]/div/input').click()
enbek.find_element('//li[label[text()="Просроченный"]]').click()
enbek.find_element('//button[text()="Поиск"]').click()

for _ in range(17):
    enbek.find_element('//td[@class="contractsTable_pixelGamingContractNumber__3OFq9"]').click()
    # enbek.find_element('//tbody/tr[2]/td[@class="contractsTable_pixelGamingContractNumber__3OFq9"]').click()
    enbek.find_element('//button[text()="Пролонгировать"]').click()
    enbek.find_element('//input[@name="dcontractDateCode"]').click()
    enbek.find_element('//li[label[text()="На неопределенный срок"]]').click()
    enbek.eds_sign()
    enbek.find_element('//button[text()="Назад"]').click()
