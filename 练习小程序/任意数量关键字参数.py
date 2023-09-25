def make_pizza(size,**materials):
    size=int(size)
    print("You just ordered a %d inches pizza with these:"%size)
    for i,j in materials.items():
        print(type(i))
        print("%d unit of %s"%(j,i))
make_pizza(15,water=4,ash=1,pepper=8,gold=8)