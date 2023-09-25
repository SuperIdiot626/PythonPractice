def step():
    n=1
    print('step %d'%n)
    while 1:
        yield
        n=n+1
        print('step %d'%n)
        
        
y=step()

while 1:
    next(y)
    print('please enter your code:')
    z=input()