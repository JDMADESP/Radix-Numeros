import unittest
from radix_tree import *
from tipo_numeracion import*

class test_pnn(unittest.TestCase):
    def test_numbers(self):
        number_tree = create_tree()
        assert "Razon social: AT&T COMERCIALIZACION MOVIL, S. DE R.L. DE C.V., Tipo Red: MOVIL, Poblacion: TLAXCALA DE XICOHTENCATL" == number_tree.search("2463025555")
        assert "Razon social: AT&T COMERCIALIZACION MOVIL, S. DE R.L. DE C.V., Tipo Red: MOVIL, Poblacion: CHILPANCINGO DE LOS BRAVO" == number_tree.search("7472617821")
        assert "Razon social: AT&T COMERCIALIZACION MOVIL, S. DE R.L. DE C.V., Tipo Red: MOVIL, Poblacion: IXTLAN DEL RIO" == number_tree.search("3241795643")
        assert "Razon social: AT&T COMERCIALIZACION MOVIL, S. DE R.L. DE C.V., Tipo Red: MOVIL, Poblacion: GUASAVE" == number_tree.search("6873045647")
        assert "Razon social: AT&T COMERCIALIZACION MOVIL, S. DE R.L. DE C.V., Tipo Red: MOVIL, Poblacion: CORTAZAR" == number_tree.search("4111795674")
        assert "Razon social: AT&T COMERCIALIZACION MOVIL, S. DE R.L. DE C.V., Tipo Red: MOVIL, Poblacion: COSAMALOAPAN" == number_tree.search("2881734568")
        assert "You did not enter a valid phone number" == number_tree.search("2834568")
        assert "You did not enter a valid phone number" == number_tree.search("30594696A8")


if __name__ == '__main__':
    unittest.main()
