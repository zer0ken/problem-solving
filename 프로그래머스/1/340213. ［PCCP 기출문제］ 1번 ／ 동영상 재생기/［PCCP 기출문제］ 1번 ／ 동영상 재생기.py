def parse(mmss):
    m, s = map(int, mmss.split(':'))
    return 60 * m + s


def to_str(s):
    m = s // 60
    return f'{m:02}:{s%60:02}'


def solution(video_len, pos, op_start, op_end, commands):
    total = parse(video_len)
    cur = parse(pos)
    op = (parse(op_start), parse(op_end))
    
    for command in commands:
        if op[0] <= cur <= op[1]:
            cur = op[1]
        if command == 'prev':
            cur = max(0, cur - 10)
        else:
            cur = min(total, cur + 10)
        if op[0] <= cur <= op[1]:
            cur = op[1]
    return to_str(cur)