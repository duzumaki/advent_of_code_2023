from collections import defaultdict, deque

f = open("test.txt").read().split(",")

boxes = defaultdict(deque)


def hash(label: str):
    output = 0
    for c in label:
        output += ord(c)
        output *= 17
        output %= 256
    return output


for step in f:
    if "=" in step:
        label, operation = step.split("=")

    elif "-" in step:
        label, operation = step.split("-")
        if not operation:
            operation = "-"

    if operation.isdigit():
        # e.g box 0: [rn 1]
        for i, box in enumerate(boxes[hash(label)]):
            # repacing old lens for label with new lens
            if box[0] == label:
                box[1] = operation
                break
        else:
            boxes[hash(label)].append([label, operation])

    elif operation == "-":
        to_remove = []
        for i, box in enumerate(boxes[hash(label)]):
            if box[0] == label:
                to_remove.append(i)

        for remove in to_remove:
            del boxes[hash(label)][remove]

    if not boxes[hash(label)]:
        del boxes[hash(label)]


FOCUSING_POWER = 0

for box_count, slots in boxes.items():
    current_power_of_box = 0

    for i, slot in enumerate(slots):
        focal_length = int(slot[1])
        current_power_of_box += (box_count+1) * (i + 1) * focal_length

    FOCUSING_POWER += current_power_of_box

print(FOCUSING_POWER)
