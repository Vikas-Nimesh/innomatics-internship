# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
x = list(map(float, input().split()[:n]))
y = list(map(float, input().split()[:n]))

mu = lambda arr: sum(arr)/len(arr)
mu_diff = lambda arr: list(map(lambda i: i - mu(arr), arr))
std = lambda arr: (sum(list(map(lambda i: i**2, mu_diff(arr))))/ len(arr))**.5
P_corr = lambda m, n: sum(list(map(lambda i, j: i*j , mu_diff(m), mu_diff(n))))/ (len(m)*std(m)*std(n))

print(round(P_corr(x, y), 3))