import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

INC = 1

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_experimental_option('prefs', {
        'geolocation': True,
        "profile.managed_default_content_settings.images": 2,
    })

    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.delete_all_cookies()

    for i in range(2005, 2010):
        for j in range(0, 13, INC):
            if j != 0 and j != 12:
                # use_date is used to complete the URL
                use_date = f"from={i}-{j if j >= 10 else '0' + str(j)}" \
                           f"-01&to={i}-{j + INC if j + INC >= 10 else '0' + str(j + INC)}-01"
                print(use_date)

                driver.get(f"http://dati.retecivica.bz.it/services/POLLNET_REMARKS?format=csv&{use_date}&STAT_ID=69")
                time.sleep(0.1)

            if j == 12:
                use_date = f"from={i}-12-01&to={i + 1}-01-01"
                print(use_date)

                driver.get(f"http://dati.retecivica.bz.it/services/POLLNET_REMARKS?format=csv&{use_date}&STAT_ID=69")
                time.sleep(0.1)

        time.sleep(2)

    driver.quit()
