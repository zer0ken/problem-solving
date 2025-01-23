def solution(ineq, eq, n, m):
    condition = ineq + eq
    if condition == '>=':
        result = n >= m
    if condition == '<=':
        result = n <= m
    if condition == '>!':
        result = n > m
    if condition == '<!':
        result = n < m
    return 1 if result else 0