raw_scores = input()

score = {'A': 0, 'B': 0}
win_by_2 = False

for c in raw_scores:
    if c in ('A', 'B'):
        cur = c
    else:
        score[cur] += int(c)
        
        if not win_by_2:
            if score[cur] >= 11:
                break
        elif cur == 'A' and score['A'] >= score['B'] + 2:
            break
        elif cur == 'B' and score['B'] >= score['A'] + 2:
            break
        
        if score['A'] == score['B'] == 10:
            win_by_2 = True
        
print(cur)