a, b = map(int, input().split())
c, d = map(int, input().split())

max_value = 0
max_rotation = 0

rotation = 0
value = a / c + b / d
if max_value < value:
    max_value = value
    max_rotation = rotation
    
rotation = 1
value = c / d + a / b
if max_value < value:
    max_value = value
    max_rotation = rotation
    
rotation = 2
value = d / b + c / a
if max_value < value:
    max_value = value
    max_rotation = rotation
    
rotation = 3
value = b / a + d / c
if max_value < value:
    max_value = value
    max_rotation = rotation

print(max_rotation)