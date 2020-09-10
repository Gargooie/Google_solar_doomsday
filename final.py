x = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]

def solution(l):
    array = sorted(l, key=lambda l:[int(y) for y in l.split('.')])
    return array

print(solution(x))
