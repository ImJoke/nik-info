import argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main(nik: list|str):
    chrome_options = Options()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://cekdptonline.kpu.go.id/")
    info_dict = {}

    for n, i in enumerate(nik, 1):
        input_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="text"].form-control')))
        input_field.clear()
        input_field.send_keys(i)

        buttons = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Pencarian"]')))
        buttons.click()

        result_elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//p[@class="list-item-heading mb-1 color-theme-1 mb-1" or @class="mb-2 text-xl-left" or @class="list-item-heading mb-1 color-theme-1 mb-1 text-xl-left"]')))
        for i in range(0, len(result_elements), 2):
            key = result_elements[i].text
            value = result_elements[i + 1].text
            info_dict[key] = value

        print(f"{n}. ", end='')
        for key, value in info_dict.items():
            print(f"{key} : {value}")
        print()

        buttons = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Kembali"]')))
        buttons.click()

    driver.quit()

def parserList(listData: list) -> list:
    return [i.replace(',', ' ').split() for i in listData]

def fileLoader(filePath: str):
    for i in filePath:
        with open(i[0], 'r') as file:
            main(file.read().replace(',', ' ').split())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get NIK information using NIK values from a file.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-n", "--nik", nargs='+', type=str, help="Nomor Induk Kependudukan")
    group.add_argument("-f", "--file", nargs='+', type=str, help="Path to the file containing NIK values")
    args = parser.parse_args()

    if args.nik:
        main(parserList(args.nik))

    elif args.file:
        fileLoader(parserList(args.file))