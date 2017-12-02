print(sum(int(a)for k in[__import__("sys").stdin.readline().strip()]for a,b in zip(k,k[len(k)//2:]+k[:len(k)//2])if a==b))
