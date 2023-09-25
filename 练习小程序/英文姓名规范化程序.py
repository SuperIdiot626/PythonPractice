def normalize(L):
        return (L.lower()).capitalize()

# 测试:
L1 = ['adam', 'LISA', 'barT','SBBitch']
L2 = list(map(normalize, L1))
print(L2)