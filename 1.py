import sys

print('task 1')

x=3.251
y=0.325
z=0.466*y * (10*x ** (4))

try:
	x = float(input('input x: '))
	y = float(input('input y: '))

except ValueError:
	print('You should input numbers!')
	sys.exit()

print (z)
