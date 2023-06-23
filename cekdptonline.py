from pathlib import Path
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

def main(nik: list):
        nik = validator(nik)

        if nik:
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

                result_elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//p[@class="mb-2 text-xl-left"] | //h2[@class="mb-2"]')))

                for f, i in zip(form, result_elements):
                    if len(result_elements) == 4:
                        print(f"{f} : \x1b[0;32m{i.text}\033[0m")

                    elif len(result_elements) == 1:
                        print(f"\x1b[1;31m{i.text}\033[0m")

                    else:
                        print('\x1b[0;32m'+''.join([f"{ord(i):X}" for i in f"{i.text} - {ni}"]))
                        print("\x1b[1;31mBUG : Please submit issue to https://github.com/ImJoke/nik-info\033[0m")
                print()

                buttons = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Kembali"]')))
                buttons.click()

            driver.quit()
        

def validator(nik: list): # Just to be able to enter nik into cekdptonline
    niks = [i for i in nik if 5 < len(i) < 17]

    if len(nik) != len(niks):
        print(f"Invalid NIKs : {','.join(i[0] for i in nik if not (5 < len(i[0]) < 17))}")
    return niks

def parserList(listData: list) -> list:
    return [x for i in listData for x in i.replace(',', ' ').split()]

def checkPath(fileName: str) -> bool:
    thisFileLST = __file__.replace('\\', '/').rsplit('/', maxsplit=1)
    fileNameLST = str(Path(fileName).absolute()).replace('\\', '/').rsplit('/', maxsplit=1)

    return Path(fileName).is_file() and thisFileLST[0].lower() == fileNameLST[0].lower()

def fileLoader(filePath: str):
    for i in filePath:
        if checkPath(i):
            with open(i, 'r') as file:
                main(file.read().replace(',', ' ').split())
        else:
            print("Invalid path!")

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
