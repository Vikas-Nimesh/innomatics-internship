class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        list1 = list(str(n))
        int_list = []
        for i in list1:
            int_list.append(int(i))
            
        mul_result = 1
        sum_result = sum(int_list)
        for x in int_list:
            mul_result = mul_result * x
        return mul_result - sum_result
        