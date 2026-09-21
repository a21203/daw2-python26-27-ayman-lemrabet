# tipos de datos

x = 3

print(x, type(x))
print(x + 1)
print(x - 1)
print(x * 2)
print(x ** 2)  # exponente

# mas ejemplos
x += 1
print(x)

x *= 2
print(x)

# tipos float
y = 2.5

print(y, type(y))
print(y, y + 1, y + 2, y ** 2)

#booleans
t, f=True, False
print(t, type(t))
print(t and f) #and
print(t or f)
ptint(not t)
print(t != f)
print(t or f)
print(not t or f)
#string
hello = 'hello'
world = 'world'
print(hello)
print(hello, len(hello))
hw = hello + '' + world
print(hw))

hw12= '{} {} {}' .format(hello, world, 'world') #formateo de cadenas
print(hw12)
#mas funciones de cades
s="hello"
print(s.capitalize()) #may
print(s.upper())
print(s.rjust(7))
print(s.center(7))
print(s.replace('l', '(ell)'))
print('           world'.strip())
