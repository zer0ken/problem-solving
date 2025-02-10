def main():
    import sys

    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N, K = map(int, readline().split())
    bottles = N
    purchased = 0
    
    counter = [N]
    while True:
        i = 0
        while i < len(counter):
            merged = counter[i] // 2
            left = counter[i] % 2
            if not merged:
                break
            bottles = bottles - counter[i] + left + merged
            counter[i] = left
            if i == len(counter) - 1:
                counter.append(merged)
            else:
                counter[i+1] += merged
            i += 1
        if bottles <= K:
            break
        bottles += 1
        purchased += 1
        counter[0] += 1

    write(str(purchased))


if __name__ == '__main__':
    main()