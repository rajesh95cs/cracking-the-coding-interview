class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        try:
            return self.items.pop()
        except IndexError:
            print "queue is empty"

    def size(self):
        return len(self.items)

    def front_element(self):
        try:
            return self.items[len(self.items)-1]
        except IndexError:
            print "queue is empty"

    def rear_element(self):
        try:
            return self.items[0]
        except IndexError:
            print "queue is empty"

    def __str__(self):
        out = ""
        for item in reversed(self.items):
           out += "\n"
           out += str(item)
        return out


if __name__ == '__main__':
    queue = Queue()
    queue.dequeue()
