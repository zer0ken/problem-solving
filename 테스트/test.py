def main():
    import sys

    S, BADS, K = sys.stdin.read().split()
    K = int(K)
    BADS = {chr(97 + i): int(is_bad == '0') for i, is_bad in enumerate(BADS)}

    suffixes = sorted([S[i:] for i in range(len(S))])
    previous_good_str = ''
    good_str_count = 0
    for suffix in suffixes:
        bad_count = 0
        is_on_new_path = 0
        for i in range(len(suffix)):
            bad_count += BADS[suffix[i]]
            if bad_count > K:
                i -= 1
                break
            
            if not is_on_new_path and (
                i >= len(previous_good_str) or
                suffix[i] != previous_good_str[i]
            ):
                is_on_new_path = 1

            if is_on_new_path:
                good_str_count += 1
        
        previous_good_str = suffix[:i+1]
    
    sys.stdout.write(str(good_str_count))


main()