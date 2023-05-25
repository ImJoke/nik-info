import argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

form = [
     "Nama Pemilih",
     "Nomor Induk Kependudukan (NIK)",
     "Nomor Kartu Keluarga (NKK)",
     "Tempat Pemungutan Suara (TPS)"
]

def main(nik: list|str):
        chrome_options = Options()
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://cekdptonline.kpu.go.id/")

        for ni in nik:
            input_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="text"].form-control')))
            input_field.clear()
            input_field.send_keys(ni)

            buttons = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Pencarian"]')))
            buttons.click()

            result_elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//p[@data-v-6caa6b6a and @class="mb-2 text-xl-left"] | //h2[@data-v-6caa6b6a and @class="mb-2"]')))# and @class="mb-2 text-xl-left"]')))

            for f, i in zip(form, result_elements):
                if len(result_elements) == 4:
                    print(f"{f} : \x1b[0;32m{i.text}\033[0m")

                elif len(result_elements) == 1:
                    print(f"\x1b[1;31m{i.text}\033[0m")

                else:
                    print('\x1b[0;32m'+''.join([f"{ord(i):X}" for i in f"{i.text} - {ni[0]}"]))
                    print("\x1b[1;31mBUG : Please submit issue to https://github.com/ImJoke/nik-info\033[0m")
            print()


            buttons = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Kembali"]')))
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
