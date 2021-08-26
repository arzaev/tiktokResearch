
import random


with open('proxy.txt', 'r') as f:
    proxies = f.read().split('\n')


with open('input.txt', 'r') as f:
    logins = f.read().split('\n')

list = []
count = 0
for i in logins:
    sp = ''
    if ':' in i:
        sp = ':'
    elif ';' in i:
        sp = ';'
    login = i.split(sp)[0]
    password = i.split(sp)[1]

    proxy = proxies[count].split(':')[0] + ':' + proxies[count].split(':')[1]
    login_proxy = proxies[count].split(':')[2]
    password_proxy = proxies[count].split(':')[3]

    # main_string = login + ':' + login + ':' + password + ':' + proxies[count] + '' + ':' + ':' + ':1'
    main_string = login + ':' + login + ':' + password + ':' + proxy + '' + ':' + login_proxy + ':' + password_proxy + ':1'
    list.append(main_string)
    count += 1

with open('out.txt', 'a') as f:
    f.write("\n".join(list))