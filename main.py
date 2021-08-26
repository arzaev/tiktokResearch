

s = 'TeenyMoonU'

# with open('tmp.txt', 'r', encoding='utf-8') as f:
    # some = f.read().split('\n')

# s = '{} ❤️ my photos here 𝐦𝐞𝐞𝐭𝐨𝐧𝐥𝐲𝐦𝐞.𝐜𝐨𝐦'

list = []
count = 0
for i in range(600):
    # list.append(s + str(count))

    with open('file.txt', 'a', encoding='utf-8') as f:
        # f.write(s.format(some[count]) + '\n')
        f.write(s + str(count) + '\n')
    count += 1