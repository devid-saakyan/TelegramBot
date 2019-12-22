import requests
from bs4 import BeautifulSoup
import datetime

base_url_tennis = 'https://www.liveresult.ru/tennis/'
base_url_football = 'https://www.liveresult.ru/football/England/Premier-League/scheduled/'

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrodiv78.0.3904.70 Safari/537.36'}

def get_html(url,headers):
    if url:
        r = requests.get(url,headers=headers)
        html = r.text
        return html

def tennis_parse_tennis(base_url):
    data_matches_online =[]
    soup = BeautifulSoup(base_url, 'lxml')
    #print(soup)
    div = soup.find('div', class_="matches-live")
    divs = div.find_all('div', class_="live-group-data live-group-static")
    #print(divs)
    team1 = div.find_all('div', class_="tennis-teams-team team1")
    team2 = div.find_all('div', class_="tennis-teams-team team2")
    for i in range(len(divs)):
        match = divs[i].find('div', class_="live-match-row live-match-data")
        #print(match)
        if match is not None:
            time = match.find('time', class_="time").text.strip()
            team1[i] = match.find('div', class_="tennis-teams-team team1")
            team2[i] = match.find('div', class_="tennis-teams-team team2")
            team1_score = team1[i].find('div', class_="team-score").text.strip().replace('  ','').replace('\n/',' ')
            team2_score = team2[i].find('div', class_="team-score").text.strip().replace('  ','').replace('\n/',' ')
            try:
                team1_name = team1[i].find('div', class_="players win").text.strip().replace('  ','').replace('\n/',' ')
            except AttributeError:
                team1_name = team1[i].find('div', class_="players").text.strip().replace('  ','').replace('\n/',' ')
            try:
                team2_name = team2[i].find('div', class_="players win").text.strip().replace('  ','').replace('\n/',' ')
            except AttributeError:
                team2_name = team2[i].find('div', class_="players").text.strip().replace('  ','').replace('\n/',' ')
            data_matches_online.append([time.strip(),team1_name.strip(),team1_score.strip(),team2_score.strip(),team2_name.strip()])

    return (data_matches_online)
#tennis_parse_tennis(get_html(base_url_tennis, headers))

def football_parser(base_url):
    data_matches_online=[]
    soup = BeautifulSoup(base_url,'lxml')
    table = soup.find('div', class_='matches-list')
    matches = table.find_all('a', class_='matches-list-match')
    for i in range(len(matches)):
        match = matches[i].find('div', class_='match-details')

        time = match.find('span', class_='match-time-time')
        date = match.find('span', class_='match-time-date')
        time = str(time.text).strip()
        date = str(date.text).strip()

        teams = match.find('span', class_='match-title')
        team1 = teams.find('span', class_='team team1')
        team2 = teams.find('span', class_='team team2')
        team1 = str(team1.text).strip()
        team2 = str(team2.text).strip()

        tour = matches[i].find('span', class_='match-cat')
        tour = str(tour.text).strip()
        date = time + ' ' + date
        date = datetime.datetime.strptime(date, '%H:%M %d.%m.%Y')
        data_matches_online.append([team1, team2, date, time, tour])
    return data_matches_online

def get_main_tennis():
    url = 'https://www.liveresult.ru/tennis/'
    r = tennis_parse_tennis(get_html(url, headers))
    return r

def get_main_football():
    url = 'https://www.liveresult.ru/football/England/Premier-League/scheduled/'
    r = football_parser(get_html(url, headers))
    return r

get_main_football()
#soccer_parse_tennis(base_url_tennis,headers)
