import requests
from bs4 import BeautifulSoup
import pandas as pd

url ='https://movies.yahoo.com.tw/movie_thisweek.html'
r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')

movies = soup.find_all("div",class_='release_info_text')
movie_infos = []

for movie in movies:
    movie_info = {}
    movie_info['ch_name'] = movie.find('div',class_='release_movie_name').a.text.strip()
    movie_info['en_name'] = movie.find('div',class_='en').a.text.strip()
    movie_info['release_date'] = movie.find('div',class_='release_movie_time').text.replace('上映日期：\n',"").strip()
    movie_info['exciting'] = movie.find('div',class_='leveltext').span.text.strip()
    movie_infos.append(movie_info)

movie_df=pd.DataFrame(movie_infos)
print(movie_df)
