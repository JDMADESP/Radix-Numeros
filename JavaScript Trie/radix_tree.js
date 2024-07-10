//npm run dev to run React site

class Node{
    constructor(){
        this.children = {};
        this.is_END_of_SERIE = false;
        this.info = [];
    }
}

class EndNode{
    constructor(start_val, end_val, info){
        this.start_val = start_val;
        this.end_val = end_val;
        this.information = info;
    }
}

class Radix_tree{
    constructor(){
        this.root = new Node();
    }

    insert(numeracion_node) {
        let NIR = numeracion_node.NIR;
        let SERIE = numeracion_node.SERIE;
        let first_six_numbers = NIR + SERIE;
        let curr_node = this.root;
        for (const num in first_six_numbers){
            if (!curr_node.children[num]){
                curr_node.children[num] = new Node();
            }
            curr_node = curr_node.children[num];
        }
        let start_val = Number(numeracion_node.NUM_INICIAL);
        let end_val = Number(numeracion_node.NUM_FINAL);
        let information = numeracion_node;
        let newEndNode = new EndNode(start_val, end_val, information);
        curr_node.info.push(newEndNode);
    }

    search(num) {
        if (num.length != 10){
            return "You did not enter a valid phone number";
        }
        if (isNaN(num)){
            return "You did not enter a valid phone number";
        }
        let first_six = num.slice(0, 6);
        let last_four = num.slice(6, 10);
        curr_node = self.root;
        for (val in first_six){
            if (!curr_node.children[val]){
                return "Phone Number not in Database";
            }
            curr_node = curr_node.children[val];
        }
        if (curr_node.is_END_of_SERIE == false){
            return "Something wrong with the tree";
        }
        for (childNode in curr_node.info){
            if (childNode.start_val <= Number(last_four) && Number(last_four) <= childNode.end_val){
                let numeracion = childNode.information;
                return `Razon social: ${numeracion.razon_social}, Tipo Red: ${numeracion.tipo_red}, Poblacion: ${numeracion.poblacion}`
            }
        }
        return "Phone number not in Database"
    }
}

export default Radix_tree