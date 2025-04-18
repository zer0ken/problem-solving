l, s = int(input()), int(input())
if s > l:
    diff = s - l
    if diff <= 20:
        fine = 100
    elif diff <= 30:
        fine = 270
    else:
        fine = 500 
    print(f'You are speeding and your fine is ${fine}.')
else:
    print('Congratulations, you are within the speed limit!')