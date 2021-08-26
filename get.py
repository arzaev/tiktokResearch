with open('input.txt', 'r') as f:
    file = f.read().split('\n')

for i in file:
    with open('out.txt', 'a') as f:
        f.write(i.split(':')[1] + '\n')