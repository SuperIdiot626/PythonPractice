owls=5
squirrels=1

O0=4
S0=4
Ot= 0.5*O0+0.3*S0
St=-0.4*O0+1.3*S0
i=0
while i<100:
    Ot= 0.5*O0+0.3*S0
    St=-0.4*O0+1.3*S0
    O0=Ot
    S0=St
    print(O0,S0,i)
    i=i+1