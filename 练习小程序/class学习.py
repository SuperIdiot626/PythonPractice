class Tiger(object):
        def __init__(self,name='dachong'):
                self.name=name
                self.color='orange'
                self.weight='500'
        def eat(self):
                print('the tiger is eating')

class Lion(object):
        def __init__(self,name='xinba'):
                self.name=name
                self.color='yellow'
                self.weight='300'
        def eat(self):
                print('the lion is eating')
        def hunt(self):
                print('the lion is hunting')  

class TigerLion(Tiger,Lion):
        def __init__(self,name='zzz'):
                self.name=name
                self.color='flower'
                self.weight='400'
        def sex(self):
                print('nasty~')

a=TigerLion()
print(a.name)
a.eat()
a.hunt()
a.sex()