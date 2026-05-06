numbers = [5, 3, 7, 9, 2, 4, 1, 8, 6]
sum = 0
for num in numbers:
    sum += num
print("Sum:", sum)

max = numbers[0]
for num in numbers:
    if num > max:
        max = num
print("Maximum:", max)

min = numbers[0]
for num in numbers:
    if num < min:
        min = num
print("Minimum:", min)

freq = {}
for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print("Frequency:", freq)

rev = []
for i in range(len(numbers) -1, -1, -1):
    rev.append(numbers[i])
print("Reversed list:", rev)
