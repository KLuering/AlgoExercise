def nth_perfect_number():
    n = int(input("Enter a positive integer n: "))
    i = 10
    count = 0
    while True:
        if sum(map(int, str(i))) == 10:
            count += 1
            if count == n:
                return i
        i += 1

# Call the function
print(nth_perfect_number())
