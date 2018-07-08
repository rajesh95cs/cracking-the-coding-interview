
import sys
sys.path.append("../")
from queue import *

import datetime



class pet:
    def __init__(self,type,name,time):
        self.type = type
        self.name = name
        self.time = time
    def __gt__(self,other):
        return self.time > other.time
    def __str__(self):
        out = "{type : "
        if self.type == 1:
            out += "dog"
        if self.type == 2:
            out += "cat"
        out += ", breed : "
        out += str(self.name)
        out += ", time : "+ str(self.time) + "}"
        return out

class pet_handling:
    def __init__(self):
        self.dog_queue = Queue()
        self.cat_queue = Queue()

    def __str__(self):
        out = "the dog cage queue contains : \n"
        out += self.dog_queue.__str__()
        out += "\nthe cat cage queue contains : \n"
        out += str(self.cat_queue)
        return out

    def pet_enqueue(self,type,name):
        time = datetime.datetime.now()
        p1 = pet(type,name,time)
        if type == 1:
            self.dog_queue.enqueue(p1)
        if type == 2:
            self.cat_queue.enqueue(p1)

    def dequeue_any(self):
        if (self.dog_queue.front_element()>self.cat_queue.front_element()):
            return self.cat_queue.dequeue()
        else :
            return self.dog_queue.dequeue()

    def dequeue_dog(self):
        return self.dog_queue.dequeue()

    def dequeue_cat(self):
        return self.cat_queue.dequeue()
