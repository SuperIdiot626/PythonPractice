def make_pizza(size,*materials):
    size=int(size)
    print(type(materials))
    print("You just ordered a %d inches pizza with these:"%size)
    for i in materials:
        print("-"+i)
make_pizza(15,'water','ash','pepper')