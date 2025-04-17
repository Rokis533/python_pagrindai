# from models.irasas import Irasas
from models.pajamos import Pajamos, Irasas
from models.islaidos import Islaidos
from object_saving import load_from_file, save_to_file


def run():
    irasas = Irasas(10,4)
    save_to_file("test.pkl" ,irasas)
    print(irasas)


run()