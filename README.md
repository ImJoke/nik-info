# Install
```sh
git clone --depth=1 https://github.com/ImJoke/nik-info
cd nik-info
pip install -r requirements.txt
```
# Usage
#### Using `-n` or `--nik` flag
```sh
python cekdptonline.py -n <nik>
```
#### Using `-f` or `--file` flag
```sh
python cekdptonline.py -f <file path>
```
# Example
#### Using `-n` flag
```sh
python cekdptonline.py -n 1234567891234567,1234567891234567,1234567891234567,...
```
```sh
python cekdptonline.py -n "1234567891234567 1234567891234567 1234567891234567 ..."
```
```sh
python cekdptonline.py -n "1234567891234567,1234567891234567,1234567891234567,..."
```
```sh
python cekdptonline.py -n "1234567891234567, 1234567891234567, 1234567891234567, ..."
```
#### Using `-f` flag
```sh
python cekdptonline.py -f path_1,path_2,path_3,...
```
```sh
python cekdptonline.py -f "path_1 path_2 path_3 ..."
```
```sh
python cekdptonline.py -f "path_1,path_2,path_3,..."
```
```sh
python cekdptonline.py -f "path_1, path_2, path_3, ..."
```
# Help output
```sh
$ python cekdptonline.py -h
usage: cekdptonline.py [-h] (-n NIK [NIK ...] | -f FILE [FILE ...])

Get NIK information using NIK values from a file.

options:
  -h, --help            show this help message and exit
  -n NIK [NIK ...], --nik NIK [NIK ...]
                        Nomor Induk Kependudukan
  -f FILE [FILE ...], --file FILE [FILE ...]
                        Path to the file containing NIK values
```
# Note
Try to combine this tool with the [nik-parser](https://github.com/ImJoke/nik-parser "nik-parser") tool
# Tested on
- Windows 11 + Python ≥ 3.x.x + chrome
# References
- [kpu.go.id](https://cekdptonline.kpu.go.id "cekdptonline")
