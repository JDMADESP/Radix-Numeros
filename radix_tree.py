

class Node:
    def __init__(self):
        self.children = [None] * 10
        self.is_end_of_SERIE = False
        self.dict_of_ranges = {}

class Radix_tree:
    def __init__(self):
        self.root = Node()
    
    def insert(self, numeracion_node): ##Important NIR, SERIE, Inicial - Numeracion Final
        ####First organize first six values of phone number into three
        NIR = numeracion_node.NIR
        SERIE = numeracion_node.SERIE
        first_six_numbers = NIR + SERIE
        curr_node = self.root
        for num in first_six_numbers:
            if curr_node[int(num)] is None:
                curr_node[int(num)] = Node()
            curr_node = curr_node(int(num))
        ###Now organize values in range values, add to list and set list as 
        ##Key value in leaf node with dictionary
        initial_value = int(numeracion_node.NUM_INICIAL)
        final_value = int(numeracion_node.NUM_FINAL)
        list_of_range = []
        list_of_range[0] = initial_value
        list_of_range[1] = final_value
        curr_node.is_end_of_SERIE = True
        curr_node.dict_of_ranges[list_of_range] = numeracion_node


    def search(self, num):
        if (len(num) != 10):
            return "You did not enter a valid phone number"
        if (num.isdigit() == False):
            return "You did not enter a valid phone number"
        first_six = num[0] + num[1] + num[2] + num[3] + num[4] + num[5]
        last_four = num[6] + num[7] + num[8] + num[9]
        curr_node = self.root
        for path in first_six:
            if curr_node[int(path)] == None:
                return "Phone number not in database"
            curr_node = curr_node[int(path)]
        if (curr_node.is_end_of_SERIE == False):
            return "Something wrong with tree"
        for keys in curr_node.dict_of_ranges:
            initial = int(keys[0])
            final = int(keys[1])
            if initial <= last_four <= final:
                numeracion = curr_node.dict_of_ranges[keys]
                return f"Razon social: {numeracion.razon_social}, Tipo Red: {numeracion.tipo_red}"