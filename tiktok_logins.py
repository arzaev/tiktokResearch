import requests
from boter.work import go


class Login:
    def __init__(self, proxy=True,
                 item_proxy='127.0.0.1:8080',
                 type_proxy='https',
                 user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
                 verify=False, timeout=10):
        self.user_agent = user_agent
        self.session = requests.Session()
        self.item_proxy = item_proxy
        self.type_proxy = type_proxy
        if type_proxy == 'socks5':
            self.proxies = {
                'http': 'socks5://{}'.format(item_proxy),
                'https': 'socks5://{}'.format(item_proxy)
            }
        else:
            if '@' in item_proxy:
                self.proxies = {'http': 'http://{}'.format(item_proxy),
                                'https': 'https://{}'.format(item_proxy)}
            else:
                self.proxies = {'http': item_proxy, 'https': item_proxy}
        self.verify = verify
        self.timeout = timeout
        self.list = []
        self.proxies = None

    def start(self, login, full):
        url = 'https://www.tiktok.com/@{}?'.format(login)
        headers = {
            'Host': 'www.tiktok.com',
            'User-Agent': self.user_agent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Upgrade-Insecure-Requests': '1',
            'Connection': 'close'
        }
        r = self.session.get(url, headers=headers, verify=False, proxies=self.proxies)
        url = 'https://www.tiktok.com/@{}?'.format(login)
        headers = {
            'Host': 'www.tiktok.com',
            'User-Agent': self.user_agent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Upgrade-Insecure-Requests': '1',
            'Connection': 'close'
        }
        r = self.session.get(url, headers=headers, verify=False, proxies=self.proxies)
        # print(r.text)
        # with open('index.html', 'w', encoding='utf-8') as f:
        #     f.write(str(r.text))
        print(r.status_code)
        # following = r.text.split(' Following, 0 Likes')[0].split(' ')[-1]
        # if int(following) < 100:
        #     self.list.append(login)

        if 'and vids you can find here' in r.text:
            print(True)
        else:
            print(False)
            with open('norm.txt', 'a') as f:
                f.write(str(login) + '\n')
        # if 'page.verify_page_load' in r.text:
        #     print("\n\n\n\nSTOP\n\n")
        # if r.status_code == 200:
        #     pass
        # else:
        #     with open('norm.txt', 'a') as f:
        #         f.write(str(login) + '\n')


with open('input.txt', 'r') as f:
    logins = f.read().split('\n')

# with open('tmp_file.txt', 'r') as f:
#     tmp_logins = f.read().split('\n')
#
#
# count = 0
for i in logins:
    login = Login()
    l = i.split(':')[1]
    print(l)
    login.start(l, i)
    # count += 1


# go(start, logins, 1)
