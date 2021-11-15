def rod(s):

    rings = []
    for i in range(0,len(s),2):
        rings.append(s[i:i+2])

    rods = {i:set() for i in range(10)}

    for r in rings:
        rod = int(r[1])
        rods[rod].add(r[0])

    rst = 0
    for r in rods:
        ring_on_rod = rods[r]
        if "B" in ring_on_rod and "G" in ring_on_rod and "R" in ring_on_rod:
            rst += 1

    return rst



r = "B2R5G2R2"
print(rod(r))