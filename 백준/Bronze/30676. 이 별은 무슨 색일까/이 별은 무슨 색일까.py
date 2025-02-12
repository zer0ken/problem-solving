colors = [
    (620, 781, 'Red'),
    (590, 620, 'Orange'),
    (570, 590, 'Yellow'),
    (495, 570, 'Green'),
    (450, 495, 'Blue'),
    (425, 450, 'Indigo'),
    (380, 425, 'Violet'),
]
lambda_ = int(input())
for l, r, c in colors:
    if l <= lambda_ < r:
        print(c)
        exit(0)