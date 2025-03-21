import sys
from collections import deque

raw_lines = open(0).read().split('\n')
input_iter = iter(raw_lines)

M, N, O, P, Q, R, S, T, U, V, W = map(int, next(input_iter).split())

left = 0
queue = deque()

box = []
for w in range(W):
    wt = []
    for v in range(V):
        vt = []
        for u in range(U):
            ut = []
            for t in range(T):
                tt = []
                for s in range(S):
                    st = []
                    for r in range(R):
                        rt = []
                        for q in range(Q):
                            qt = []
                            for p in range(P):
                                pt = []
                                for o in range(O):
                                    ot = []
                                    for n in range(N):
                                        tomatoes = list(map(int, next(input_iter).split()))
                                        ot.append(tomatoes)
                                        for m in range(M):
                                            if tomatoes[m] == 0:
                                                left += 1
                                            elif tomatoes[m] == 1:
                                                queue.append((m, n, o, p, q, r, s, t, u, v, w))
                                    pt.append(ot)
                                qt.append(pt)
                            rt.append(qt)
                        st.append(rt)
                    tt.append(st)
                ut.append(tt)
            vt.append(ut)
        wt.append(vt)
    box.append(wt)

deltas = [
#   [m, n, o, p, q, r, s, t, u, v, w]
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
]

timestamp = 0
while queue:
    m, n, o, p, q, r, s, t, u, v, w = queue.popleft()
    timestamp = box[w][v][u][t][s][r][q][p][o][n][m]
    for dm, dn, do, dp, dq, dr, ds, dt, du, dv, dw in deltas:
        nm, nn, no, np, nq, nr, ns, nt, nu, nv, nw = [
            m + dm, n + dn, o + do, p + dp,
            q + dq, r + dr, s + ds, t + dt,
            u + du, v + dv, w + dw
        ]
        
        if any([
            nm < 0, nm >= M, nn < 0, nn >= N,
            no < 0, no >= O, np < 0, np >= P,
            nq < 0, nq >= Q, nr < 0, nr >= R,
            ns < 0, ns >= S, nt < 0, nt >= T,
            nu < 0, nu >= U, nv < 0, nv >= V,
            nw < 0, nw >= W,
        ]):
            continue

        if box[nw][nv][nu][nt][ns][nr][nq][np][no][nn][nm] == 0:
            box[nw][nv][nu][nt][ns][nr][nq][np][no][nn][nm] = timestamp + 1
            left -= 1
            queue.append((nm, nn, no, np, nq, nr, ns, nt, nu, nv, nw))
            
if left:
    sys.stdout.write('-1')
else:
    sys.stdout.write(str(timestamp - 1))