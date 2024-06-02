class Myclass:
    def __init__(self,**kwargs):
        self.name = kwargs.get('name','defalt_name')
        self.id = kwargs.get('id',0)
        self.sex = kwargs.get('sex','male')
        self.items=kwargs.get('items',[0,0,0])
    
    def __str__(self):
        if self.name=="Niteesh":
            return f"Name:{self.name}\nId:{self.id}\nSex:{self.sex}\n{str(self.items)}"
        if self.items is not None:
            #way 1 --> return f"Items:{self.items}"
            #way 2 -->return "\n".join(str(i) for i in self.items)
            '''way 3 --> list=[f"{index}:{i}" for index,i in enumerate(self.items)]
            return "\n".join(list)'''
            #way 4 -->return self.items   ---> str(self.items) ---> then works
            #way 5 -->return self.items[0] ---> str(self.items) ---> then works
            return f"{self.name}:{str(self.id)}:{str(self.sex)}"
    

object=Myclass(name="Niteesh",id=2526644,sex="Male")
print(object)
object=Myclass(items=[1,2,3,4])
print(object)
print(str([1,2,3,4]))


