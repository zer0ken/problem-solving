import re
input()
s = input()
print(sum(map(int, re.split('[.|:#]', s))))