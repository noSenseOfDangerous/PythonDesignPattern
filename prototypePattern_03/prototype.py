from collections import OrderedDict
import copy
class Book:
    def __init__(self,name,authors,price,**rest):
        self.name=name
        self.authors=authors
        self.price=price
        self.__dict__.update(rest)
    def __str__(self):
        mylist=[]
        ordered=OrderedDict(sorted(self.__dict__.items()))
        for i in ordered.keys():
            mylist.append('{}: {}'.format(i,ordered[i]))
            if i=="price":
                mylist.append('$')
            mylist.append('\n')
        return ''.join(mylist)
class Prototype:
    def __init__(self):
        self.objects=dict()
    def register(self,identifier,obj):
        self.objects[identifier]=obj
    def unregister(self,identifier):
        del self.objects[identifier]
    def clone(self,identifier,**attr):
        found=self.objects.get(identifier)
        if not found:
            raise ValueError('Incorrect object identifier {}'.format(identifier))
        obj=copy.deepcopy(found)
        obj.__dict__.update(attr)
        return obj

