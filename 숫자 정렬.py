
numbers = [64, 34, 25, 12, 22, 11, 90]

print("정렬 전:", numbers)

n = len(numbers)
for i in range(n):
    for j in range(0, n-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print("정렬 후:", numbers)