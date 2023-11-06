#  coding: utf-8
import os


def convert():
    # Não é mais necessário converter os arquivos .ui para .py pois agora
    # carregamos o layout direto dos arquivos .ui. Vou deixar para referência
    files = [x for x in os.listdir("screens/raw_screens") if x.endswith(".ui")]
    for file in files:
        print("Convertendo " + file)
        os.system(f"pyuic5 screens/raw_screens/{file} -o screens/raw_screens/{file.replace('.ui', '.py')}")


if __name__ == '__main__':
    convert()
