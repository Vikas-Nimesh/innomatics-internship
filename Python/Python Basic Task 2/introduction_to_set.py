def average(array):
    my_set = set(array)
    total_number = len(my_set)
    sum_of_number = sum(my_set)
    average_of_set = sum_of_number/total_number
    return average_of_set
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)