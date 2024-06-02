class Myclass:
    def __init__(self,name=None):
        self.name = name
        print(f'inside Myclass:',self.name)

    def __str__(self):
        return self.name
class Mychild(Myclass):
    def __init__(self,name=None):
        super().__init__(name)
        print(f'inside mychild:',self.name)
    def __str__(self):
        return self.name
class SuperChild(Mychild):
    def __init__(self,name=None):
        super().__init__(name)
        print(f'inside superchild:',self.name)

class one:
    def __init__(self,*args,**kw):
        self.args=args
        self.kw=kw
        print(f"args:{args},kw:{kw}")
        print("type of args:",type(args),"\ntype of kw",type(kw))



if __name__ == '__main__':   
    object=Myclass("niteesh")
    print(object)
    child_object=Mychild('sharat')
    print(child_object)
    super_object=SuperChild('mukesh')
    print(super_object)
    object=one(1,2,3,name="niteesh",role="System Engineer")
