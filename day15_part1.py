f = open("test.txt").read().split(",")


current_value = 0

def hash(step: str):
    output = 0
    for c in step:
        output += ord(c)
        output *= 17
        output %= 256
    return output
    


for step in f:
    current_value += hash(step)


print(current_value)