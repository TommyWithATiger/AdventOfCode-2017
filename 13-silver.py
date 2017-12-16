print(sum((a%(2*b-2)<1)*a*b for a,b in[map(int,line.strip().split(":"))for line in __import__("sys").stdin.readlines()]))
