from bs4 import BeautifulSoup
import requests as req

# urlx = "https://www.brainyquote.com/topics/technology-quotes"
# resp = req.get(urlx)
# # print(resp.text)
#
# soup = BeautifulSoup(resp.text, 'html.parser')
# dic = soup.find('div', id = 'quotesList')
# d2 = dic.find('div', id = 'qpos_1_1')

# d2 = soup.find('div', id = 'qpos_1_6')
# d3 = d2.find_all('a', title="view quote")
# d4 = d2.find('a', title="view author")
# print(d3[-1].text)
# print(d4.text)
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