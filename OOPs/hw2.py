class Employee:
    def __init__(self,id):
        self.id=id
        self.name = ''
        self.manager = None

    def get_manager_hierarchy(self):
        hierarchy = [self.name]
        if(self.manager is not None):
            hierarchy += self.manager.get_manager_hierarchy()
        return hierarchy

e1=Employee(1)
e1.name='ABC'

e2=Employee(2)
e2.name='DEF'
e1.manager=e2

e3=Employee(3)
e3.name='GHI'
e2.manager=e3

print(e1.get_manager_hierarchy())

#abc - def - ghi

