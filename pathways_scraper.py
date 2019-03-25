import json
from urllib.request import urlopen

from bs4 import BeautifulSoup
from pyvt import Timetable

TERM = '201909'
URL = 'https://banweb.banner.vt.edu/ssb/prod/HZSKVTSC.P_DispRequest'

soup = BeautifulSoup(urlopen(URL), 'html.parser')
areas = soup.find('select', {'name': 'CORE_CODE'}).find_all('option')
areas = [area['value'] for area in areas]
areas.remove('AR%')
areas_dict = {area: set() for area in areas}

timetable = Timetable()

for area in areas:
    sections = timetable.cle_lookup(area, TERM, open_only=False)
    for s in sections:
        if s.credits == '* Additional Times *':
            continue
        string = '{}|{}|{}'.format(s.code, s.name, s.credits)
        areas_dict[area].add(string)
    areas_dict[area] = list(areas_dict[area])
    areas_dict[area].sort()

print(json.dumps(areas_dict))
