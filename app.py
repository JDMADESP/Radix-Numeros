import csv
from radix_tree import *
from flask import Flask, render_template, request, jsonify, make_response


created_tree = None

app = Flask(__name__)
app.json.sort_keys = False



@app.route("/", methods=["GET", "POST"])
async def index():
  if request.method == "POST":
    global created_tree
    if request.is_json: ##Get JSON Terms and ASYNCHRONOUS
      data = request.get_json()
      if not data:
        return jsonify({"error":"Incorrect Data"})
      numbers_test = data["Numbers"]
      if not numbers_test:
        return jsonify({"error":"Incorrect Numbers Data"})
      return_list = []
      for num in numbers_test:
        info_of_number = created_tree.search(num)
        return_list.append(info_of_number)
      return jsonify({"Numbers":return_list})
  else:
    new_tree = create_tree()
    created_tree = new_tree
    return jsonify({"Success":"Tree Created"})


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
        

def create_tree():
    number_tree = Radix_tree()
    list_of_csv = list_csv('pnn.csv')
    for line in list_of_csv:
        new_numeracion = tipo_numeracion(line)
        number_tree.insert(new_numeracion)
    return number_tree