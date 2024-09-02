import requests
import os
import subprocess
import random
import re
import threading
import urllib.request
import argparse
import sys
from time import time

output_file = 'proxy.txt'
os.system('cls' if os.name == 'nt' else 'clear')

if os.path.isfile(output_file):
    os.remove(output_file)
    print(f"File 'proxy.txt' telah dihapus.")

print(f"Otw Download\n")

proxy_urls = [
'https://api.proxyscrape.com/v2/?request=displayproxies',
'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt', 
'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt', 
'https://raw.githubusercontent.com/yuceltoluyag/GoodProxy/main/raw.txt', 
'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt', 
'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt', 
'https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt', 
'https://proxyspace.pro/http.txt', 
'https://api.proxyscrape.com/?request=displayproxies&proxytype=http',
'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt', 
'http://worm.rip/http.txt', 
'http://worm.rip/https.txt', 
'https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt', 
'https://raw.githubusercontent.com/mallisc5/master/proxy-list-raw.txt', 
'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt', 
'https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt', 
'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt', 
'https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/free.txt', 
'https://raw.githubusercontent.com/HyperBeats/proxy-list/main/https.txt', 
'https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/http.txt', 
'https://raw.githubusercontent.com/caliphdev/Proxy-List/master/http.txt', 
'https://raw.githubusercontent.com/proxylist-to/proxy-list/main/http.txt', 
'https://raw.githubusercontent.com/zloi-user/hideip.me/main/https.txt', 
'https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt', 
'https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/https.txt', 
'https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt', 
'https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/http/data.txt', 
'https://raw.githubusercontent.com/tuanminpay/live-proxy/master/http.txt', 
'https://raw.githubusercontent.com/casals-ar/proxy-list/main/https'
'https://raw.githubusercontent.com/casals-ar/proxy-list/main/http'
'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt', 
'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt', 
'https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt', 
'https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt', 
'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt', 
'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/https_proxies.txt', 
'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt', 
'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt', 
'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt', 
'http://freeproxylist-daily.blogspot.com/2013/05/usa-proxy-list-2013-05-15-0111-am-gmt8.html'
'http://freeproxylist-daily.blogspot.com/2013/05/usa-proxy-list-2013-05-13-812-gmt7.html'
'http://www.cybersyndrome.net/pla5.html'
'http://vipprox.blogspot.com/2013_06_01_archive.html'
'http://vipprox.blogspot.com/2013/05/us-proxy-servers-74_24.html'
'http://vipprox.blogspot.com/p/blog-page_7.html'
'http://vipprox.blogspot.com/2013/05/us-proxy-servers-199_20.html'
'http://vipprox.blogspot.com/2013_02_01_archive.html'
'http://alexa.lr2b.com/proxylist.txt', 
'http://vipprox.blogspot.com/2013_03_01_archive.html'
'http://browse.feedreader.com/c/Proxy_Server_List-1/449196260'
'http://browse.feedreader.com/c/Proxy_Server_List-1/449196258'
'http://sock5us.blogspot.com/2013/06/01-07-13-free-proxy-server-list.html'
'http://browse.feedreader.com/c/Proxy_Server_List-1/449196251'
'http://free-ssh.blogspot.com/feeds/posts/default', 
'http://browse.feedreader.com/c/Proxy_Server_List-1/449196259'
'http://sockproxy.blogspot.com/2013/04/11-04-13-socks-45.html'
'http://proxyfirenet.blogspot.com/'
'https://www.javatpoint.com/proxy-server-list', 
'https://openproxy.space/list/http'
'http://proxydb.net/'
'http://olaf4snow.com/public/proxy.txt', 
'http://westdollar.narod.ru/proxy.htm'
'https://openproxy.space/list/socks4'
'https://openproxy.space/list/socks5'
'http://tomoney.narod.ru/help/proxi.htm'
'http://sergei-m.narod.ru/proxy.htm'
'http://rammstein.narod.ru/proxy.html'
'http://greenrain.bos.ru/R_Stuff/Proxy.htm'
'http://inav.chat.ru/ftp/proxy.txt', 
'http://johnstudio0.tripod.com/index1.htm'
'http://atomintersoft.com/transparent_proxy_list', 
'http://atomintersoft.com/anonymous_proxy_list', 
'http://atomintersoft.com/high_anonymity_elite_proxy_list', 
'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt', 
'https://raw.githubusercontent.com/yuceltoluyag/GoodProxy/main/raw.txt', 
'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt', 
'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt', 
'https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt', 
'https://proxyspace.pro/http.txt', 
'https://api.proxyscrape.com/?request=displayproxies&proxytype=http',
'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt', 
'http://worm.rip/http.txt', 
'http://worm.rip/https.txt', 
'http://alexa.lr2b.com/proxylist.txt', 
'https://api.openproxylist.xyz/http.txt', 
'http://rootjazz.com/proxies/proxies.txt', 
'https://multiproxy.org/txt_all/proxy.txt', 
'https://proxy-spider.com/api/proxies.example.txt', 
'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt', 
'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt', 
'https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt', 
'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt', 
'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt', 
'https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt', 
'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all',
'https://www.proxydocker.com/en/proxylist/download?email=noshare&country=all&city=all&port=all&type=all&anonymity=all&state=all&need=all',
'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=anonymous',
'http://alexa.lr2b.com/proxylist.txt', 
'https://api.openproxylist.xyz/http.txt', 
'http://rootjazz.com/proxies/proxies.txt', 
'https://multiproxy.org/txt_all/proxy.txt', 
'https://proxy-spider.com/api/proxies.example.txt', 
'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt', 
'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt', 
'https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt', 
'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt', 
'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt', 
'https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt', 
'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all',
'https://www.proxydocker.com/en/proxylist/download?email=noshare&country=all&city=all&port=all&type=all&anonymity=all&state=all&need=all',
'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=anonymous',
"https://www.proxy-list.download/api/v1/get?type=http",
"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
'https://github.com/Tsprnay/Proxy-lists/raw/master/proxies/http.txt', 
'https://github.com/Tsprnay/Proxy-lists/raw/master/proxies/https.txt', 
'https://github.com/proxy4parsing/proxy-list/raw/main/http.txt', 
'https://github.com/vakhov/fresh-proxy-list/raw/master/http.txt', 
'https://github.com/vakhov/fresh-proxy-list/raw/master/https.txt', 
'https://github.com/TuanMinPay/live-proxy/raw/master/http.txt', 
'https://github.com/yemixzy/proxy-list/raw/main/proxies/unchecked.txt', 
'https://github.com/andigwandi/free-proxy/raw/main/proxy_list.txt', 
'https://github.com/elliottophellia/yakumo/raw/master/results/http/global/http_checked.txt', 
'https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt', 
'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt', 
'https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt', 
'https://api.openproxylist.xyz/http.txt', 
'https://proxy-spider.com/api/proxies.example.txt', 
'https://naawy.com/api/public/proxylist/getList/?proxyType=http&format=txt', 
'https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt', 
'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt', 
'https://github.com/BlackCage/Proxy-Scraper-and-Verifier/raw/main/Proxies/Not_Processed/proxies.txt', 
'https://raw.githubusercontent.com/elliottophellia/yakumo/master/results/http/global/http_checked.txt', 
'https://github.com/hookzof/socks5_list/raw/master/proxy.txt', 
'https://github.com/vakhov/fresh-proxy-list/raw/master/socks5.txt', 
'https://github.com/ALIILAPRO/Proxy/raw/main/socks5.txt', 
'https://github.com/casals-ar/proxy-list/raw/main/socks5',
'https://github.com/monosans/proxy-list/raw/main/proxies/socks5.txt', 
'https://github.com/Zaeem20/FREE_PROXIES_LIST/raw/master/socks5.txt', 
'https://github.com/vakhov/fresh-proxy-list/raw/master/socks5.txt', 
'https://github.com/MyZest/update-live-socks5/raw/master/liveSocks5.txt', 
'https://github.com/ObcbO/getproxy/raw/master/file/socks5.txt', 
]

def download_and_save_proxies(url, output_file):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(output_file, 'a') as file:
                file.write(response.text)
                print(f"Collecting: {url}")
        else:
            print(f"failed: {url}")
    except Exception as e:
        print(f"failed: {url}")

open(output_file, 'w').close()

class Proxy:
    def __init__(self, method, proxy):
        if method.lower() not in ["http", "https"]:
            raise NotImplementedError("Only HTTP and HTTPS are supported")
        self.method = method.lower()
        self.proxy = proxy

    def is_valid(self):
        return re.match(r"\d{1,3}(?:\.\d{1,3}){3}(?::\d{1,5})?$", self.proxy)

    def check(self, site, timeout, user_agent):
        url = self.method + "://" + self.proxy
        proxy_support = urllib.request.ProxyHandler({self.method: url})
        opener = urllib.request.build_opener(proxy_support)
        urllib.request.install_opener(opener)
        req = urllib.request.Request(self.method + "://" + site)
        req.add_header("User-Agent", user_agent)
        try:
            start_time = time()
            urllib.request.urlopen(req, timeout=timeout)
            end_time = time()
            time_taken = end_time - start_time
            return True, time_taken, None
        except Exception as e:
            return False, 0, e

    def __str__(self):
        return self.proxy

def verbose_print(verbose, message):
    if verbose:
        print(message)

def check(file, timeout, method, site, verbose, random_user_agent):
    proxies = []
    with open(file, "r") as f:
        for line in f:
            proxies.append(Proxy(method, line.replace("\n", "")))

    print(f"Checking {len(proxies)} Proxy")
    proxies = filter(lambda x: x.is_valid(), proxies)
    valid_proxies = []
    user_agent = random.choice(user_agents)

    def check_proxy(proxy, user_agent):
        new_user_agent = user_agent
        if random_user_agent:
            new_user_agent = random.choice(user_agents)
        valid, time_taken, error = proxy.check(site, timeout, new_user_agent)
        message = {
            True: f"{proxy} are valid, took {time_taken} seconds",
            False: f"{proxy} are invalid: {repr(error)}",
        }[valid]
        verbose_print(verbose, message)
        valid_proxies.extend([proxy] if valid else [])

    threads = []
    for proxy in proxies:
        t = threading.Thread(target=check_proxy, args=(proxy, user_agent))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    with open(file, "w") as f:
        for proxy in valid_proxies:
            f.write(str(proxy) + "\n")

    print(f"Found {len(valid_proxies)} valid Proxies")


def verbose_print(verbose, message):
    if verbose:
        print(message)

for url in proxy_urls:
    download_and_save_proxies(url, output_file)
    
with open('proxy.txt', 'r') as ceki:
    jumlh = sum(1 for line in ceki)
    
print(f"\n{jumlh} Proxy has been SCRAPED, do you want to check Y/N: ", end="")
choice = input().strip().lower()

if choice == 'y' or choice == 'Y':
    user_agents = [
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
      "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15",
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36",
     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
     "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
     "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9",
     "Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4",
     "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
     "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240",
     "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
     "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
     "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
     "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
     "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
     "Mozilla/5.0 (Linux; Android 12; V2120 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36"
    ]
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--timeout", type=int, default=20, help="Dismiss the proxy after -t seconds")
    parser.add_argument("-p", "--proxy", default="http", help="Check HTTPS or HTTP proxies")
    parser.add_argument("-s", "--site", default="https://google.com/", help="Check with specific website like google.com")
    parser.add_argument("-v", "--verbose", action="store_true", help="Increase output verbosity")
    parser.add_argument("-r", "--random_agent", action="store_true", help="Use a random user agent per proxy")
    
    args = parser.parse_args()
    check(file=output_file, timeout=args.timeout, method=args.proxy, site=args.site, verbose=args.verbose, random_user_agent=args.random_agent)
    sys.exit(0)
else:
    print(f"Terima Kasih, Telah Menggunakan Script Saya!.\n")
