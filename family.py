class Mgm:
    """ Base Class """

    def walk(self):
        print("Walk - MGM", id(self))


class Mgf:
    """ Base Class """

    def walk(self):
        print("Walk - MGF", id(self))


class Pgm:
    """ Base Class """

    def walk(self):
        print("Walk - PGM", id(self))


class Pgf:
    """ Base Class """

    def walk(self):
        print("Walk - PGF", id(self))


class Dad(Pgm, Pgf):
    """ Derived class """

    def walk(self):
        print("Walk - Dad", id(self))


class Mom(Mgm, Mgf):
    """ Derived class """

    def walk(self):
        print("Walk - Mom", id(self))

    """ 
    def __init__(self):
        print("Object created successfully")
    
    def __del__(self):
        print("Object destroyed successfully")
    """


class Infant(Mom, Dad):
    """ Derived class """
    "This is documentation __doc__"

    def walk(self):
        print("Walk - Infant", id(self))
        Pgm.walk(self)


Baby = Infant()
# help(Baby)
Mother = Mom()
# Mother.walk()
# print("id of Mother is: ", id(Mother))

Baby.walk()

new = Baby + 1
