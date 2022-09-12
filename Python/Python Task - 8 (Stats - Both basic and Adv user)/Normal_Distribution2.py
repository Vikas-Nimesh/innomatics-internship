from math import erf

def cdf(mean, std, x):
    return  0.5 * (1 + erf((x - mean) / (std * (2 ** 0.5))))

if __name__ == "__main__":
    mean, std = list(map(float, input().split(' ')))
    q1 = float(input().strip())
    q2 = float(input().strip())
    
    print(round((1-cdf(mean, std, q1))*100, 2))
    print(round((1-cdf(mean, std, q2))*100, 2))
    print(round(cdf(mean, std, q2)*100, 2))