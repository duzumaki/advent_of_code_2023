from collections import defaultdict, deque
from dataclasses import dataclass, field
from pprint import pprint

f = open("test.txt").read().splitlines()



@dataclass
class Module:
    state: str = "off"
    memory: list = field(default_factory=dict)
    dest: list = field(default_factory=list)
    type: str = None

graph = defaultdict(Module)

conjuctions = []

for line in f:
    src, dest = line.split("->")
    src = src.replace(" ", "")
    dest = dest.replace(" ", "").split(",")
    type = src[0]

    if src == "broadcaster":
        graph[src].dest.extend(dest)
    else:
        graph[src[1:]].type = type
        graph[src[1:]].dest = dest

    if type == "&":
        conjuctions.append((src[1:], dest))
    

for module, info in graph.items():
    for conjuction_name, conjuction_dest in conjuctions:
        if conjuction_name in info.dest:
            graph[conjuction_name].memory[module] = info.state


low = 0
high = 0
for _ in range(1000):
    q = deque([("broadcaster", dest, "low") for dest in graph["broadcaster"].dest])
    low += 1

    while q:
        src, dest, pulse = q.popleft()

        if pulse == "low":
            low += 1
        else:
            high += 1

        if dest not in graph:
            continue

        module = graph[dest]

        if module.type == "%":
            if pulse == "low":
                module.state = "on" if module.state == "off" else "off"
                pulse_to_send = "high" if module.state == "on" else "low"

                for d in module.dest:
                    q.append((dest, d, pulse_to_send))

        elif module.type == "&":
            module.memory[src] = pulse

            pulses = module.memory.values()
            all_high = all(pulse == "high" for pulse in pulses)
            pulse_to_send = "low" if all_high else "high"

            for d in module.dest:
                q.append((dest, d, pulse_to_send))

print(low * high)
