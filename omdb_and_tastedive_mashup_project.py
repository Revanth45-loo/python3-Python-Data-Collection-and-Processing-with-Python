#Q1

import requests_with_caching
import json

def get_movies_from_tastedive(movie_name):
    baseurl = "https://tastedive.com/api/similar"
    parameters={}
    parameters['q']=movie_name
    parameters['type']='movies'
    parameters['limit']=5
    tastedive_result=requests_with_caching.get(baseurl, params = parameters)
    return tastedive_result.json()
    
#Q2
    
def extract_movie_titles(movie_dict):
    movie_titles=[]
    for movie in movie_dict['Similar']['Results']:
        print(movie['Name'])
        movie_titles.append(movie['Name'])
    return movie_titles

#Q3

def get_related_titles(movie_list):
    movie_final_list=[]
    for movie in movie_list:
        movie_from_tastedive=get_movies_from_tastedive(movie)
        extract_title=extract_movie_titles(movie_from_tastedive)
        for name in extract_title:
            if name not in movie_final_list:
                movie_final_list.append(name)
    return movie_final_list

#Q4
import requests_with_caching
import json

def get_movie_data(title):
    baseurl="http://www.omdbapi.com/"
    parameters={}
    parameters['t']=title
    parameters['r']='json'
    omdb_result=requests_with_caching.get(baseurl,params=parameters)
    a= json.loads(omdb_result.text)
    return a

#Q5
    
def get_movie_rating(omdb_dict_result):
    rating=0
    if len(omdb_dict_result['Ratings'])>1:
        if omdb_dict_result['Ratings'][1]['Source'] == 'Rotten Tomatoes':
            rating=omdb_dict_result['Ratings'][1]['Value'][:2]
            rating=int(rating)
    else:
        rating=0
    return rating

#Q6

def get_sorted_recommendations(mov_title_list):
    movie_rating_dict={}
    for movie in get_related_titles(mov_title_list):
        mov_rating=get_movie_rating(get_movie_data(movie))
        movie_rating_dict[movie]=mov_rating
    sorted_key_list=sorted(movie_rating_dict,key=lambda movie: (movie_rating_dict[movie],movie),reverse=True)
    return sorted_key_list

    
