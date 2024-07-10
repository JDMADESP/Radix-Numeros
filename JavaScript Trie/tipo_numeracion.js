

// import Papa from 'papaparse';
import RadixTree from './radix_tree.js'

class numeracion{
    constructor(csv_list){
        self.clave_censal = csv_list[0]
        self.poblacion = csv_list[1]
        self.municipio = csv_list[2]
        self.estado = csv_list[3]
        self.presuscripcion = csv_list[4]
        self.region = csv_list[5]
        self.ASL = csv_list[6]
        self.NIR = csv_list[7]
        self.SERIE = csv_list[8]
        self.NUM_INICIAL = csv_list[9]
        self.NUM_FINAL = csv_list[10]
        self.ocupacion = csv_list[11]
        self.tipo_red = csv_list[12]
        self.modalidad = csv_list[13]
        self.razon_social = csv_list[14]
        self.fecha_asignacion = csv_list[15]
        self.fecha_consolidacion = csv_list[16]
        self.fecha_migracion = csv_list[17]
        self.NIR_anterior = csv_list[18]
    }
}
