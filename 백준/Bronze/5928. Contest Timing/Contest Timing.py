D, H, M = map(int, input().split())
diff = (D - 11)*24*60 + (H-11)*60 + (M-11)
print('-1' if diff < 0 else diff)