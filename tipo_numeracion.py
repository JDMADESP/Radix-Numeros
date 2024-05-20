import csv
from radix_tree import *


class tipo_numeracion:
    def __init__(self, lista_valores):
        self.clave_censal = lista_valores[0]
        self.poblacion = lista_valores[1]
        self.municipio = lista_valores[2]
        self.estado = lista_valores[3]
        self.presuscripcion = lista_valores[4]
        self.region = lista_valores[5]
        self.ASL = lista_valores[6]
        self.NIR = lista_valores[7]
        self.SERIE = lista_valores[8]
        self.NUM_INICIAL = lista_valores[9]
        self.NUM_FINAL = lista_valores[10]
        self.ocupacion = lista_valores[11]
        self.tipo_red = lista_valores[12]
        self.modalidad = lista_valores[13]
        self.razon_social = lista_valores[14]
        self.fecha_asignacion = lista_valores[15]
        self.fecha_consolidacion = lista_valores[16]
        self.fecha_migracion = lista_valores[17]
        self.NIR_anterior = lista_valores[18]
        


def list_csv(filename):
    my_list = []
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file) ##.reader uses dialect for preset parameters of what it expects file to be
        ##by default it expects values to be separated by a comma
        next(csv_reader) ##Skips first row
        for row in csv_reader:
            my_list.append(row)
        return my_list
        

number_tree = Radix_tree()
list_of_csv = list_csv('pnn.csv')
for line in list_of_csv:
    new_numeracion = tipo_numeracion(line)
    number_tree.insert(new_numeracion)

A = "2463025555" #AT&T COMERCIALIZACION MOVIL, S. DE R.L. DE C.V., MOVIL (661)
B = "7472617821" #AT&T COMERCIALIZACION MOVIL, S. DE R.L. DE C.V., MOVIL (419)
C = "3241795643" #AT&T COMERCIALIZACION MOVIL, S. DE R.L. DE C.V., MOVIL (33457)
D = "6873045647" #AT&T COMERCIALIZACION MOVIL, S. DE R.L. DE C.V., MOVIL (45000)
E =  "4111795674" #AT&T COMERCIALIZACION MOVIL, S. DE R.L. DE C.V., MOVIL (163589)
assert "Razon social: AT&T COMERCIALIZACION MOVIL, S. DE R.L. DE C.V., Tipo Red: MOVIL, Poblacion: TLAXCALA DE XICOHTENCATL" == number_tree.search(A)
assert "Razon social: AT&T COMERCIALIZACION MOVIL, S. DE R.L. DE C.V., Tipo Red: MOVIL, Poblacion: CHILPANCINGO DE LOS BRAVO" == number_tree.search(B)
assert "Razon social: AT&T COMERCIALIZACION MOVIL, S. DE R.L. DE C.V., Tipo Red: MOVIL, Poblacion: IXTLAN DEL RIO" == number_tree.search(C)
assert "Razon social: AT&T COMERCIALIZACION MOVIL, S. DE R.L. DE C.V., Tipo Red: MOVIL, Poblacion: GUASAVE" == number_tree.search(D)
assert "Razon social: AT&T COMERCIALIZACION MOVIL, S. DE R.L. DE C.V., Tipo Red: MOVIL, Poblacion: CORTAZAR" == number_tree.search(E)
print("Passed all tests")