print(sum(abs(sum(__import__("math").sin((__import__("math").floor((4*(n-2)+1)**0.5)%4)*(__import__("math").pi/2))for n in range(2,i+1))//1)+abs(sum(__import__("math").cos((__import__("math").floor((4*(n-2)+1)**0.5)%4)*(__import__("math").pi/2))for n in range(2,i+1))//1
)for i in[int(__import__("sys").stdin.readline().strip())]))
