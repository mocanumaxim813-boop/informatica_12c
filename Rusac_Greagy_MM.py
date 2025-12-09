V = float(input("Dati volumul maxim al rucsacului: "))
n = int(input("Dati nr de obiecte: "))

preturi = []
volume = []

for i in range(n):
    p = float(input(f"Dati pretul obiectului {i+1}: "))
    v = float(input(f"Dati volumul obiectului {i+1}: "))
    preturi.append(p)
    volume.append(v)

items = []
for i in range(n):
    v = volume[i]
    p = preturi[i]
    if v == 0:
        ratio = float('inf') if p > 0 else 0.0
    else:
        ratio = p / v
    items.append({'index': i, 'p': p, 'v': v, 'ratio': ratio})

items.sort(key=lambda it: it['ratio'], reverse=True)

x = [0.0] * n
vt = 0.0
pt = 0.0

for it in items:
    if vt >= V:
        break
    i = it['index']
    vi = it['v']
    pi = it['p']
    if vi == 0:
        if pi > 0:
            x[i] = 1.0
            pt += pi
        continue
    if vt + vi <= V + 1e-12:
        x[i] = 1.0
        vt += vi
        pt += pi
    else:
        remain = V - vt
        if remain > 0:
            frac = remain / vi
            x[i] = frac
            vt += vi * frac
            pt += pi * frac
        break

print()
print(f"Pretul total al obiectelor din rucsac este {pt:.4f}")
print(f"Volumul ocupat este {vt:.4f} din {V}")
print("In rucsac s-au introdus:")

for i in range(n):
    if x[i] > 0:
        taken_vol = volume[i] * x[i]
        taken_price = preturi[i] * x[i]
        print(f"Obiectul {i+1}: fractiune={x[i]:.4f}, volum_luat={taken_vol:.4f}, pret_contribuit={taken_price:.4f}")