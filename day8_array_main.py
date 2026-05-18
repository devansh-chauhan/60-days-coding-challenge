nums = [12, 345, 2, 6789, 4444, 98, 1001, 56]
even_count = 0
for num in nums:
    digit_count = len(str(num))   
    if digit_count % 2 == 0:
        even_count += 1

print("User Data:", nums)
print("Numbers with even numbers of digits:", even_count)