locals().update({'math':__import__("math")})or print(sum(abs(round(sum(math.sin((math.floor((4*(n-2)+1)**0.5)%4)*(math.pi/2))for n in range(2,i+1))))+abs(round(sum(math.cos((math.floor((4*(n-2)+1)**0.5)%4)*(math.pi/2))for n in range(2,i+1))))for i in[int(__import__("sys").stdin.readline().strip())]))
