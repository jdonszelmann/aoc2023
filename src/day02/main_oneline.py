

print(__import__("functools").reduce(lambda a,v:
    (lambda m:(a[0]+int(v[0].split(" ")[1])if m[0]<=12 and m[1]<=13 and m[2]<=14 else a[0],m[0]*m[1]*m[2]+a[1]))(
        [max(v)for v in[[int(c.split(" ")[1])for c in v[1].replace(";",",").split(",")if c.split(" ")[2][0]==l]for l in"rgb"]]
    ),
    [g.split(":")for g in open("data.in").readlines()],
    (0,0)
))
