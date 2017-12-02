print(sum(max(x)-min(x)for x in[[*map(int,y.strip().split("\t"))]for y in __import__("sys").stdin.readlines()]))
