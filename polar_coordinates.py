import cmath
from cmath import phase

c = input("Enter a complex number (in the form a+bj): ").strip()
z = phase(complex(c))
print(z)

r, phi = cmath.polar(complex(c))

print(r)

print(phi)