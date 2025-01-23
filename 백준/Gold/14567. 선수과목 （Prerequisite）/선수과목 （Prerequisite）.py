import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())

graph = {subject: [] for subject in range(1, N + 1)}
for _ in range(M):
    presubject, subject = map(int, readline().split())
    graph[subject].append(presubject)

    
semesters = {}
def count_semeters(cur):
    if cur in semesters:
        return semesters[cur]
    if not graph[cur]:
        semesters[cur] = 1
        return 1
    max_semester = 0
    for presubject in graph[cur]:
        max_semester = max(max_semester, count_semeters(presubject))
    max_semester += 1
    semesters[cur] = max_semester
    return max_semester

for subject in range(1, N + 1):
    semester = semesters.get(subject, count_semeters(subject))
    sys.stdout.write(f'{semester} ')