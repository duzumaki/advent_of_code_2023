f = open("test.txt", "r")

nums = []


def generate_sequence(nums: list):
    output = []
    for i in range(1, len(nums)):
        output.append(nums[i] - nums[i-1])

    return output


TOTAL = 0

for line in f:
    ends = []
    sequence = [int(num) for num in line.split()]

    ends.append(sequence[-1])

    while not all(n==0 for n in sequence):
        sequence = generate_sequence(sequence)
        ends.append(sequence[-1])
    
    TOTAL += sum(ends)

print(TOTAL)