# f = open("guru99.txt", "w+")

with open('missing_solutions.md', 'r') as f:
    lines = f.readlines()
    count = 0
    for line in lines:
        if line.startswith('-'): continue
        count += 1
        # if count > 2: continue
        with open(f'{line.rstrip()}.py', "w+"):
            print(count, line.rstrip())

    