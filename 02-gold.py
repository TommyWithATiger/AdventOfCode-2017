print(sum(a//b for x in[[*map(int,y.strip().split("\t"))]for y in __import__("sys").stdin.readlines()]for a in x for b in x if a%b<1>0!=a-b))
