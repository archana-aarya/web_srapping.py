# from bs4 import BeautifulSoup
# import requests,json
# import pprint
# movie_link="https://www.imdb.com/india/top-rated-indian-movies/"
# url=requests.get(movie_link)
# print(url)
# beauti=BeautifulSoup(url.text,"html.parser")
# print(beauti)

# def scrape_top_list():
#     main_div=beauti.find("div",class_="lister")
#     tbody=main_div.find("tbody",class_="lister-list")
#     trs=tbody.find_all("tr")
    

#     movie_ranks=[]
#     movie_name=[]
#     year=[]
#     movie_url=[]
#     rating=[]
#     top_indian_movies=[]

#     # tr=0
#     # while tr<len(trs):
#     for tr in trs:
#         movies_details={}
#         position_of_movie=tr.find("td",class_="titleColumn").get_text().strip()
#         movie_rank= " "
#         for i in position_of_movie:
#             if "." not in i:
#                 movie_rank+=i
#                 # tr+=1
#             else:
#                 break
#         movie_ranks.append(movie_rank)

#         tittle=tr.find("td",class_="titleColumn").a.get_text()
#         movie_name.append(tittle)
#         year_of_movie=tr.find("td",class_="titleColumn").span.get_text()
#         year.append(year_of_movie)

#         IMdb_=tr.find("td",class_="ratingColumn imdbRating").strong.get_text()
#         rating.append(IMdb_)

#         link=tr.find("td",class_="titleColumn").a["href"]
#         movie_link="https://www.imdb.com"+link
#         movie_url.append (movie_link)
#         movies_details["name of movie"]= tittle
#         movies_details["year"]=int(year_of_movie[1:5])
#         movies_details["position_movie"]=int(movie_rank)
#         movies_details["url"]=movie_link
#         movies_details["rating"]=float(IMdb_)
#         top_indian_movies.append(movies_details)

#     return top_indian_movies

# movies_data=scrape_top_list()

# with open("task_1.json","w+")as data:
#     json.dump(movies_data,data,indent=4)
# pprint.pprint(scrape_top_list())


            #  OR








import requests,os,pprint
import json
from bs4 import BeautifulSoup

url= "https://www.imdb.com/india/top-rated-indian-movies/"
r = requests.get(url)
# print(r)
soup = BeautifulSoup(r.text,"html.parser")
# print(soup)

def scrap_movies():
    

    details_list = []
    lister_table = soup.find("div",class_="lister")
    tbody_data = lister_table.find("tbody",class_="lister-list")
    t= tbody_data.findAll("tr")


    for tr in t:
        deatils_dict = {"movies_name":"","year":"","position":"","rating":"","url":""}

        position = tr.find("td",class_="titleColumn").text
        stars=""
        for exact_position in position:
            if "."!=exact_position:
                stars+=exact_position
            else:
                break
            
        
        movies_name = tr.find("td",class_="titleColumn").a.text
        year = tr.find("td",class_="titleColumn").span.text
        
        rating = tr.find("td",class_="ratingColumn").strong.text
        url=tr.find('td',class_="titleColumn").a["href"]
        movies_url="https://www.imdb.com/"+url
    
        deatils_dict["movies_name"]=movies_name
        deatils_dict["year"]=year[1:-1]
        deatils_dict["position"]=int(stars.strip())
        deatils_dict["rating"]=rating
        deatils_dict["url"]=movies_url
        
        details_list.append(deatils_dict.copy())
    
    return details_list


movies_data=scrap_movies()


if os.path.exists("web_task1.json"):
    pass
else:
    with open("web_task1.json","w+") as file:
        json.dump(movies_data,file,indent=4)

pprint.pprint(scrap_movies())