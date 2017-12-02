print(sum(int(a)for k in[__import__("sys").stdin.readline().strip()]for a,b in zip(k,k[1:]+k[:1])if a==b))
