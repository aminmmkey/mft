i = 0
limit = 10000
answer = 0

while i < limit:
    i = i + 1
    answer = answer + 1 / (i ** 2)


piii = (answer * 6) ** 0.5
print(piii)
