n = int(input("Enter n:"))
with open("fizzbuzz_output.txt", "w") as file:
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            result = "FizzBuzz"            
        elif i % 3 == 0 :
            result = "Fizz"
        elif i % 5 == 0:
            result = "Buzz"
        else:
            result = str(i)
        
        print(result)
        file.write(result + "\n")
print("Output saved to fizzbuzz_output.txt")