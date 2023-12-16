

(lambda w,i,j,p:print(__import__("functools").reduce(lambda a,v:a*w(p(v[0]),p(v[1])),zip(*i),1),w(p(j(i[0])),p(j(i[1])))))(lambda t,r:sum(h*(t-h)>r for h in range(t)),[open("data.in").readlines()[m].split()[1:]for m in[0,1]],lambda i:"".join(i),lambda i:int(i.replace(" ","")))
(m:=__import__("math")),(d:=[x.strip().split()for x in open("data.in").readlines()]),(s:=lambda t,d:t-2*int((t-m.sqrt(t*t-4*d))/2)-1),print(m.prod(s(int(d[0][i]),int(d[1][i]))for i in range(1, len(d[0]))), s(int("".join(d[0][1:])), int("".join(d[1][1:]))))