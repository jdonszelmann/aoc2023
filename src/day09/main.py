
(lambda p,d:print(
    sum(d(h.split(),0,d) for h in p),
    sum(d(h.split(),1,d) for h in p),
))(
    open("data.in").read().split("\n"),
    lambda h,b,f:int(h[b-1])+(any(h)and[1,-1][b]*f([int(b)-int(a)for a,b in zip(h,h[1:])],b,f))
)

