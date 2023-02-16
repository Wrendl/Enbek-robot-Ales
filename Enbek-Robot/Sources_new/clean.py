import psutil

for proc in psutil.process_iter():
    if proc.name() == "chrome.exe" or proc.name() == "chromedriver.exe":
        proc.kill()