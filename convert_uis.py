#  coding: utf-8
import os


def convert(path: str):
    # Não é mais necessário converter os arquivos .ui para .py pois agora
    # carregamos o layout direto dos arquivos .ui. Vou deixar para referência

    # Telas
    files = [x for x in os.listdir(path) if x.endswith(".ui")]
    for file in files:
        print("Convertendo " + file)
        os.system(f"pyuic5 {path}/{file} -o {path}/{file.replace('.ui', '.py')}")


if __name__ == '__main__':
    convert("qt_uis/screens/raw_screens")
    convert("qt_uis/widgets/raw_widgets")
