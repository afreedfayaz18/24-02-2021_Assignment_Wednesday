def countDigit(n):
    if n == 0:
        return 0
    return 1 + countDigit(n // 10)
n =int(input("Enter the Number :"))
print("Number of digits : % d" % (countDigit(n)))
 