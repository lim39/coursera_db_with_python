# Information about Class
# Basic Example
class PartyAnimal:
    x=0

    def party(self):
        self.x= self.x + 1
        print("So far", self.x)

an = PartyAnimal()

an.party()      # an -> self
an.party()
an.party()


print("Type",type(an))  
# Type <class '__main__.PartyAnimal'>
print("Dir",dir(an))
# Dir ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
#       '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', 
#       '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', 
#       '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
#       '__str__', '__subclasshook__', '__weakref__', 'party', 'x']