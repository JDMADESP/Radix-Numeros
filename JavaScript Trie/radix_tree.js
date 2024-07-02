

class Node{
    constructor(){
        this.children = {};
        this.is_END_of_SERIE = false;
        this.phone_ranges = {}
    }
}

class Radix_tree{
    constructor(){
        this.root = Node();
    }

    insert(numeracion_node) {
        let NIR = numeracion_node.NIR
        let SERIE = numeracion_node.SERIE
        first_six_numbers = NIR + SERIE
    }
}