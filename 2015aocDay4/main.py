import hashlib

input = "bgvyzdsv"
test_input = "pqrstuv"


def check_result(test):
    check = hashlib.md5(test.encode()).hexdigest()
    to_check = check[0:6]
    if to_check == "000000":
        return True
    else:
        return False
i = 1
current = input + str(i)
print(current)
while not check_result(current):
    current = input + str(i)

    i = i + 1

print("done")
print(i - 1)





