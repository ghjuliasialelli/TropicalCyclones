# Script to scrape names from http://ibtracs.unca.edu/

from itertools import chain
import requests
import re
from tqdm import tqdm
import pandas as pd

def scrape(save = False) :

    pattern = r'\<td\>\s([A-Z]+)\<\/td\>'

    all_names = []
    for letter in tqdm(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']) : 
        url = 'http://ibtracs.unca.edu/index.php?name=Letter-{}'.format(letter)
        response = requests.get(url)
        text = response.content.decode('utf-8')
        names = re.findall(pattern, text)
        all_names.append(names)
    all_names = list(chain(*all_names))
    all_names = [name.title() for name in all_names]
    if save : pd.DataFrame(all_names, columns=['Names']).to_excel('IBTRACS-names.xlsx', index=False)