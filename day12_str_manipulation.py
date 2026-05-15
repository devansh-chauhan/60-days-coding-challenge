text = input("Enter a string:")
rev = ""
for i in range(len(text)-1, -1, -1):
    rev += text[i]

print("Original String:", text)
print("Reversed String:", rev)

# Space Complexity Analysis
# Original string uses O(n) space
# Reversed string also uses O(n) extra space
# Therefore overall extra space complexity is O(n)