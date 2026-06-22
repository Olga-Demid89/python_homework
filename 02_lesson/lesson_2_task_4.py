n = int(input("Введите число:"))


def fizz_buzz(n):
    for x in range(1, n+1):
        if x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        if (x % 3 == 0) and (x % 5 == 0):
            print("FizzBuzz")
        else:
            print(x)


fizz_buzz(n)
