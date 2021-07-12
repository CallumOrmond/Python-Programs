D = []
A = 1

def test(D,A):
    D.append("1")
    A = 2
    return


test(D,A)

print(D)
print(A)