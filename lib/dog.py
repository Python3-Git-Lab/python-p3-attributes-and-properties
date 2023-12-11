#!/usr/bin/env python3

from typing import Any


APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self,name,breed = "any"):
        self.name= name
        self.breed= breed
     
     #Name getter
    def get_name(self):
        return self._name
    
    #Breed getter
    def get_breed(self):
        return self._breed
    
    #Name setter
    def set_name(self,name):
        if (isinstance(name, str) and (1<=len(name)<=25)):
            print(f"Name is: {name}")
            self._name= name
        else:
            print("Name must be string between 1 and 25 characters.")
    
    # breed getter
    def set_breed(self, breed):
        if (breed in APPROVED_BREEDS):
            print(f"The breed is: {breed}") 
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")
            
    #Name property
    name = property(get_name, set_name)
    #breed property
    breed = property(get_breed, set_breed)
    

breed1 = Dog(0,"Mastiff")
