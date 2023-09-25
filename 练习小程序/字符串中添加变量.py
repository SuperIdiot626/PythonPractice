class Tiger(object):
        def __init__(self,name='dachong'):
                self.name=name
                self.color='orange'
                self.weight='500'
        def eat(self):
                print('the tiger is eating')

a=Tiger()
b='***LISA is a pig***'
c={1,2,3,4,5,6,7,8}
d=7.10
e=f"{a}{b}{c}{d}"
print(e)
#<__main__.Tiger object at 0x000002829F387520>***LISA is a pig***{1, 2, 3, 4, 5, 6, 7, 8}7.1