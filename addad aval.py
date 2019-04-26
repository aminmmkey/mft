number = eval(input())
i = 0
is_prime = True
while i < number - 1:
    i = i + 1
    num = number / i
    if not num % i == 0:
        is_prime = False



print(is_prime)