num1, st1, num2, st2 = (set(input().split()) for i in range(4))
new_set = st1.symmetric_difference(st2)
empty_set = set()
for i in new_set:
    empty_set.add(int(i))
for i in sorted(empty_set):
    print(i)