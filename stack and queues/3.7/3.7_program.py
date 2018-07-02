
from pet_class import *




if __name__ == '__main__':
    pet_cage = pet_handling()
    pet_cage.pet_enqueue(1,"Rotwheeler")
    pet_cage.pet_enqueue(1,"Doberman")
    pet_cage.pet_enqueue(1,"German sheperd")
    pet_cage.pet_enqueue(2,"British Shorthair")
    pet_cage.pet_enqueue(2,"Maine Coon")
    pet_cage.pet_enqueue(2,"Sphynx cat")
    pet_cage.pet_enqueue(2,"Persian cat")
    print "the cage contains :"
    print(pet_cage)
