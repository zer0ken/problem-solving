def solution(numer1, denom1, numer2, denom2):
    import math
    
    denom = denom1 * denom2
    numer = numer1 * denom2 + numer2 * denom1
    gcd = math.gcd(denom, numer)
    return [numer // gcd, denom // gcd]