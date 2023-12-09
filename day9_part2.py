f = open("test.txt", "r")

nums = []


def generate_sequence(nums: list):
    output = []
    for i in range(1, len(nums)):
        output.append(nums[i] - nums[i - 1])

    return output


TOTAL = 0

for line in f:
    starts = []
    sequence = [int(num) for num in line.split()]

    starts.append(sequence[0])

    while not all(n == 0 for n in sequence):
        sequence = generate_sequence(sequence)
        starts.append(sequence[0])


    total = 0
    for i in range(len(starts) - 1, -1, -1):
        next_ = starts[i] - total
        total = next_
    TOTAL += total

