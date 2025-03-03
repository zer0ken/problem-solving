def main():
    answer = list(map(int, input()))
    guess = list(map(int, input()))
    
    strikes = set()
    step = 1
    while answer != guess:
        has_ball = False
        for i in range(4):
            if guess[i] == answer[i]:
                strikes.add(i)
                continue
            if guess[i] in answer:
                has_ball = True
            else:
                guess[i] = (guess[i] + 1) % 10
                while guess[i] in guess[:i] + guess[i+1:]:
                    guess[i] = (guess[i] + 1) % 10
        if has_ball:
            new_guess = list(guess)
            for i in range(4):
                if i in strikes:
                    continue
                j = (i + 1) % 4
                while j in strikes:
                    j = (j + 1) % 4
                new_guess[j] = guess[i]
            guess = new_guess
        step += 1
    print(step)


if __name__ == '__main__':
    main()