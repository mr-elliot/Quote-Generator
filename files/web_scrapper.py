from bs4 import BeautifulSoup
import requests as req


def ScrapIt():
    lt = []
    for j in range(1, 17):      # to get each pages number
        urlx = "https://www.brainyquote.com/topics/technology-quotes" + f"_{j}"
        resp = req.get(urlx)
        soup = BeautifulSoup(resp.text, 'html.parser')

        for i in range(1, 61):      # to get quotes form each page
            txt = soup.find('div', id=f'qpos_{j}_{i}')
            quote = txt.find_all('a', title="view quote")
            auth = txt.find('a', title="view author")
            lt.append(f'{quote[-1].text} --{auth.text}')

    return lt
