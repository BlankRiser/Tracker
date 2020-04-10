from jikanpy import Jikan
import requests as requests

obj = Jikan()

schedules = obj.schedule()

# using function to get schedule of the day


def animeSchedule(day):
    tempDay = []
    for i in range(0, len(schedules[day])):
        Detail = {
            'image_url': schedules[day][i]['image_url'],
            'title': schedules[day][i]['title'],
            'MAL_Url': schedules[day][i]['url'],
            'synopsis': schedules[day][i]['synopsis'],
            # 'genre': schedules[day][i]['genres'], needs another loop, as inner elements are also a list
        }
        tempDay.append(Detail)
    return tempDay


# Implementing search using requests with jikan url

url = 'https://api.jikan.moe/v3'

# https://api.jikan.moe/v3/search/manga?q=hunter&limit=2

# mailId= 26
# name = Hunter X Hunter

season = [ 'spring', 'fall', 'winter', 'summer' ]

animeType = [ 'tv', 'ova', 'movie', 'special', 'ona', 'music' ]

mangaType = [ 'manga', 'novel', 'oneshot', 'doujin', 'manhwa', 'manhua' ]

animeStatus = ['airing', 'completed', 'complete', 'to_be_aired', 'tba', 'upcoming']

mangaStatus = ['publishing', 'completed', 'complete', 'to_be_published', 'tbp', 'upcoming']

xRated = ['g', 'pg', 'r17', 'r', 'rx']

animeSearchOrederBy = ['title', 'start_date', 'end_date', 'score', 'type', 'members', 'id', 'episodes', 'rating']

mangaSearchOrederBy = ['title', 'start_date', 'end_date', 'score', 'type', 'members', 'id', 'chapters', 'volumes']

sort = ['ascending', 'asc', 'descending', 'desc']

animeGenre = {'Action': '1', 'Adventure': '2', 'Cars': '3', 'Comedy': '4', 'Dementia': '5', 'Demons': '6', 'Mystery': '7', 'Drama': '8', 'Ecchi': '9', 'Fantasy': '10',
              'Game': '11', 'Hentai': '12', 'Historical': '13', 'Horror': '14', 'Kids': '15', 'Magic': '16', 'Martial Arts': '17', 'Mecha': '18', 'Music': '19', 'Parody': '20', 'Samurai': '21',
              'Romance': '22', 'School': '23', 'Sci Fi': '24', 'Shoujo': '25', 'Shoujo Ai': '26', 'Shounen': '27', 'Shounen Ai': '28', 'Space': '29', 'Sports': '30', 'Super Power': '31', 'Vampire':
              '32', 'Yaoi': '33', 'Yuri': '34', 'Harem': '35', 'Slice Of Life': '36', 'Supernatural': '37', 'Military': '38', 'Police': '39', 'Psychological': '40', 'Thriller': '41', 'Seinen': '42', 'Josei': '43',
              }

mangaGenre = {'Action': '1', 'Adventure': '2', 'Cars': '3', 'Comedy': '4', 'Dementia': '5', 'Demons': '6', 'Mystery': '7', 'Drama': '8', 'Ecchi': '9', 'Fantasy': '10',
              'Game': '11', 'Hentai': '12', 'Historical': '13', 'Horror': '14', 'Kids': '15', 'Magic': '16', 'Martial Arts': '17', 'Mecha': '18', 'Music': '19', 'Parody': '20', 'Samurai': '21',
              'Romance': '22', 'School': '23', 'Sci Fi': '24', 'Shoujo': '25', 'Shoujo Ai': '26', 'Shounen': '27', 'Shounen Ai': '28', 'Space': '29', 'Sports': '30', 'Super Power': '31', 'Vampire': '32',
              'Yaoi': '33', 'Yuri': '34', 'Harem': '35', 'Slice Of Life': '36', 'Supernatural': '37', 'Military': '38', 'Police': '39', 'Psychological': '40', 'Seinen': '41', 'Josei': '42', 'Doujinshi': '43',
              'Gender Bender': '43', 'Thriller': '45'
              }



# Top anime and manga of MAL

topAnimeParam = ['airing', 'upcoming', 'tv', 'movie', 'ova', 'special']
topMangaParam = ['manga', 'novels', 'oneshots', 'doujin', 'manhwa', 'manhua']
page = '1'  # MAL has 50 items in each page, and I am loading only the 1st page

topAnime = requests.get(url+'/top/anime' + '/' + page + '/' + topAnimeParam[3]) # https://api.jikan.moe/v3/top/anime/1/movie
topAnime = topAnime.json()

topManga = requests.get(url + '/top/manga' + '/' + page + '/' + topMangaParam[0]) # https://api.jikan.moe/v3/top/manga/1/manga
topManga = topManga.json()


# Searching manga

def searchManga(name=''):
    # https://api.jikan.moe/v3 /search/anime?q= <Fate/Zero> &page=1 ?rated=r17 &order_by=score &sort=asc &status=completed &genre=39
    search = requests.get(url+'/search/manga?q='+ name +'&page=1'+'&type=manga' )
    mangaResult = search.json()

    results= []
    for i in range(0,len(mangaResult)):
        searchDetail = {
            'image_url' : mangaResult['results'][i]['image_url'],
            'title' : mangaResult['results'][i]['title'],
            'MAL_Url': mangaResult['results'][i]['url'],
            'synopsis': mangaResult['results'][i]['synopsis']
            }
        results.append(searchDetail)
    return results

# Searching manga

def searchAnime(name=''):
    # https://api.jikan.moe/v3 /search/anime?q= <Fate/Zero> &page=1 ?rated=r17 &order_by=score &sort=asc &status=completed &genre=39
    search = requests.get(url+'/search/manga?q='+ name +'&page=1'+'&type=anime' )
    animeResult = search.json()

    results= []
    for i in range(0,len(animeResult)):
        searchDetail = {
            'image_url' : animeResult['results'][i]['image_url'],
            'title' : animeResult['results'][i]['title'],
            'MAL_Url': animeResult['results'][i]['url'],
            'synopsis': animeResult['results'][i]['synopsis']
            }
        results.append(searchDetail)
    return results