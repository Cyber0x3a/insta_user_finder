import random
import requests
import threading
from datamuse import Datamuse
print("TOOL >> INSTAGRAM USERNAME FINDER")
api = Datamuse()
id = input("CHAT 🔜 ")
token = input("Token 🔜 ")

def insta(random_user):
    url = requests.post('https://www.instagram.com/accounts/web_create_ajax/attempt/', headers={
        'Host': 'www.instagram.com',
        'content-length': '85',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
        'sec-ch-ua-mobile': '?0',
        'x-instagram-ajax': '81f3a3c9dfe2',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'x-requested-with': 'XMLHttpRequest',
        'x-asbd-id': '198387',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36',
        'x-csrftoken': 'jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
        'sec-ch-ua-platform': '"Linux"',
        'origin': 'https://www.instagram.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.instagram.com/accounts/emailsignup/',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-IQ,en;q=0.9',
        'cookie': 'csrftoken=jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv; mid=YtsQ1gABAAEszHB5wT9VqccwQIUL; ig_did=227CCCC2-3675-4A04-8DA5-BA3195B46425; ig_nrcb=1'
    }, data=f'email=aakmnnsjskksmsnsn%40gmail.com&username={random_user}&first_name=&opt_into_one_tap=false')
    if '{"message":"feedback_required","spam":true,"feedback_title":"Try Again Later","feedback_message":"We limit how often you can do certain things on Instagram to protect our community. Tell us if you think we made a mistake.","feedback_url":"repute/report_problem/scraping/","feedback_appeal_label":"Tell us","feedback_ignore_label":"OK","feedback_action":"report_problem","status":"fail"}' in url.text:
        print(f'ERROR: Try Again Later: {random_user}')
    elif '"errors": {"username":' in url.text or '"code": "username_is_taken"' in url.text:
        pass
    else:
        print(f'Good User: {random_user}')
        good = f"USERNAME>> {random_user}"
        requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={good}')



def random_words():
    while True:
        ran1 = 'qwertyuiopasdfghjklzxvcbnm'
        v1 = ''.join(random.choice(ran1) for _ in range(2))
        results = api.words(sp=v1+'*', max=5)
        words = [item['word'] for item in results]
        rand_word = random.choice(words)
        while len(rand_word) < 5:
            rand_word = random.choice(words)
        rand_word = rand_word.replace(' ','')
        insta(rand_word)

Threads = []
for t in range(600):
    x = threading.Thread(target=random_words)
    x.start()
    Threads.append(x)
for Th in Threads:
    Th.join(timeout=0)
