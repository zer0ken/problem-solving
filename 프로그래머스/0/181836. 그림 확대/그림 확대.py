def solution(picture, k):
    image = []
    for row in picture:
        new_row = ''.join(cha*k for cha in row)
        for _ in range(k):
            image.append(new_row)
    return image