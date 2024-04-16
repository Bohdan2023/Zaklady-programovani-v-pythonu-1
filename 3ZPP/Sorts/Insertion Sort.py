print("Введите числа через пробел:")
user_input = input()
A = list(map(int, user_input.split()))

for j in range(1, len(A)):
    t = A[j] #левая рука в которую складываем числа и сортируем их там
    i = j - 1
    while i >= 0 and t < A[i]:
        A[i + 1] = A[i]
        i = i - 1
    A[i + 1] = t

print(A)