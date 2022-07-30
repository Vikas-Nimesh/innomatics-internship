for i in range(int(input())): 
    a = int(input()); A = set(input().split()) 
    b = int(input()); B = set(input().split())
    if(len(A.difference(B))==0):
        print("True")
    else:
        print("False")