import hashlib

input = 'ckczppom'

number = 0

while True:
    a = input + str(number)
    result = hashlib.md5(a.encode()).hexdigest()
    if result[0:6] == "000000":
        break
    number = number + 1

print(number)

