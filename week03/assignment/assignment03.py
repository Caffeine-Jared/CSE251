'''
Requirements
1. Write a multithreaded program that calls a local web server. The web server is 
   provided to you. It will return data about the Star Wars movies.
2. You will make 94 calls to the web server, using 94 threads to get the data.
3. Using a new thread each time, obtain a list of the characters, planets, 
   starships, vehicles, and species of the sixth Star Wars movie.
3. Use the provided print_film_details function to print out the data 
   (should look exactly like the "sample_output.txt file).
   
Questions:
1. Is this assignment an IO Bound or CPU Bound problem (see https://stackoverflow.com/questions/868568/what-do-the-terms-cpu-bound-and-i-o-bound-mean)?
    >
2. Review dictionaries (see https://isaaccomputerscience.org/concepts/dsa_datastruct_dictionary). How could a dictionary be used on this assignment to improve performance?
    >
'''


from datetime import datetime, timedelta
import time
import requests
import json
import threading


# Const Values
TOP_API_URL = 'http://127.0.0.1:8790'

# Global Variables
call_count = 0

#TODO create a thread class that uses the 'requests' module
#     to call the server using an URL.
class myThread(threading.Thread):
    def init(self, url):
        threading.Thread.init(self)
        self.url = url

    def run(self):
        response = requests.get(self.url)
        response_dict = json.loads(response.text)
        print(response_dict)
        

def print_film_details(film, chars, planets, starships, vehicles, species):
    '''
    Print out the film details in a formatted way
    '''
    
    def display_names(title, name_list):
        print('')
        print(f'{title}: {len(name_list)}')
        names = sorted([item["name"] for item in name_list])
        print(str(names)[1:-1].replace("'", ""))

    print('-' * 40)
    print(f'Title   : {film["title"]}')
    print(f'Director: {film["director"]}')
    print(f'Producer: {film["producer"]}')
    print(f'Released: {film["release_date"]}')

    display_names('Characters', chars)
    display_names('Planets', planets)
    display_names('Starships', starships)
    display_names('Vehicles', vehicles)
    display_names('Species', species)


def main():
    url = TOP_API_URL + '/films/6'
    film_thread = myThread(url)
    film_thread.start()
    film_thread.join()
    #Start a timer
    begin_time = time.perf_counter()
    
    print('Starting to retrieve data from the server')

    # TODO Using your thread class, retrieve TOP_API_URL to get
    # the list of the urls for each of the categories in the form
    # of a dictionary (open your browser and go to http://127.0.0.1:8790
    # to see the json/dictionary). Note that these categories are for
    # the sixth Star Wars movie.

# def get_urls():
#     urls = []
#     response = requests.get(TOP_API_URL)
#     data = response.json()
#     for key in data.keys():
#         if key in ['characters', 'planets', 'starships', 'vehicles', 'species']:
#             urls.append(data[key])
#     print(urls)
#     return urls

# get_urls()

# def get_categories():
#     urls = get_urls()
#     for url in urls:
#         category_thread = myThread(url)
#         category_thread.start()
#         category_thread.join()
#         print(category_thread)
# get_categories()




# def retrieve_urls():
#     threads = []
#     thread_data = {}
#     response = requests.get(TOP_API_URL)
#     data = response.json()
#     for key in data.keys():
#         if key in ['characters', 'planets', 'starships', 'vehicles', 'species']:
#             url = data[key]
#             thread = myThread(url)
#             thread.start()
#             thread_data[key] = {'thread': thread, 'data': None}
#     for key in thread_data.keys():
#         thread_data[key]['thread'].join()
#         thread_data[key]['data'] = thread_data[key]['thread'].data
#     return thread_data


    # TODO Retrieve details on film 6 by putting a '6' at the end of the film URL.
    # For example, http://127.0.0.1:8790/film/6 gives you all the details of 
    # the sixth movie.

# def retrieve_film_details():
#     film_url = TOP_API_URL + '/film/6'
#     thread = myThread(film_url)
#     thread.start()
#     thread.join()
#     return thread.data

#     # TODO Create a list of threads for each of the categories (characters, planets, starships, vehicles, species)
#     #      and start each of the threads. Note: You will need to use the 'start' method to start the threads.
#     #      See https://docs.python.org/3/library/threading.html#thread-objects for more information.
#     #      You will need to use the 'join' method to wait for all the threads to finish.
#     #      See https://docs.python.org/3/library/threading.html#thread-objects for more information.
# def retrieve_category_details():
#     threads = []
#     thread_data = {}
#     data = retrieve_urls()
#     for key in data.keys():
#         url = data[key]['data']
#         thread = myThread(url)
#         thread.start()
#         thread_data[key] = {'thread': thread, 'data': None}
#     for key in thread_data.keys():
#         thread_data[key]['thread'].join()
#         thread_data[key]['data'] = thread_data[key]['thread'].data
#     for key in thread_data.keys():
#         threads.append(thread_data[key]['thread'])
#         for thread in threads:
#             thread.join()
#     return thread_data

# def retrieve_character_details():
#     threads = []
#     thread_data = {}
#     data = retrieve_category_details()
#     for item in data['characters']['data']:
#         thread = myThread(item)
#         thread.start()
#         thread_data[item] = {'thread': thread, 'data': None}
#     for key in thread_data.keys():
#         thread_data[key]['thread'].join()
#         thread_data[key]['data'] = thread_data[key]['thread'].data
#     for key in thread_data.keys():
#         threads.append(thread_data[key]['thread'])
#         for thread in threads:
#             thread.join()
#     return thread_data


# def retrieve_planet_details():
#     threads = []
#     thread_data = {}
#     data = retrieve_category_details()
#     for item in data['planets']['data']:
#         thread = myThread(item)
#         thread.start()
#         thread_data[item] = {'thread': thread, 'data': None}
#     for key in thread_data.keys():
#         thread_data[key]['thread'].join()
#         thread_data[key]['data'] = thread_data[key]['thread'].data
#     for key in thread_data.keys():
#         threads.append(thread_data[key]['thread'])
#         for thread in threads:
#             thread.join()
#     return thread_data


# def retrieve_starship_details():
#     threads = []
#     thread_data = {}
#     data = retrieve_category_details()
#     for item in data['starships']['data']:
#         thread = myThread(item)
#         thread.start()
#         thread_data[item] = {'thread': thread, 'data': None}
#     for key in thread_data.keys():
#         thread_data[key]['thread'].join()
#         thread_data[key]['data'] = thread_data[key]['thread'].data
#     for key in thread_data.keys():
#         threads.append(thread_data[key]['thread'])
#         for thread in threads:
#             thread.join()
#     return thread_data


# def retrieve_vehicle_details():
#     threads = []
#     thread_data = {}
#     data = retrieve_category_details()
#     for item in data['vehicles']['data']:
#         thread = myThread(item)
#         thread.start()
#         thread_data[item] = {'thread': thread, 'data': None}
#     for key in thread_data.keys():
#         thread_data[key]['thread'].join()
#         thread_data[key]['data'] = thread_data[key]['thread'].data
#     for key in thread_data.keys():
#         threads.append(thread_data[key]['thread'])
#         for thread in threads:
#             thread.join()
#     return thread_data


# def retrieve_species_details():
#     threads = []
#     thread_data = {}
#     data = retrieve_category_details()
#     for item in data['species']['data']:
#         thread = myThread(item)
#         thread.start()
#         thread_data[item] = {'thread': thread, 'data': None}
#     for key in thread_data.keys():
#         thread_data[key]['thread'].join()
#         thread_data[key]['data'] = thread_data[key]['thread'].data
#     for key in thread_data.keys():
#         threads.append(thread_data[key]['thread'])
#         for thread in threads:
#             thread.join()
#     return thread_data

# def display_film_details(film_details):
#     print('Film Details')
#     print('============')
#     for key in film_details.keys():
#         print(f'{key}: {film_details[key]}')

# def display_category_details(category_details):
#     print('Category Details')
#     print('================')
#     for key in category_details.keys():
#         print(f'{key}: {category_details[key]}')

# def display_character_details(character_details):
#     print('Character Details')
#     print('=================')
#     for key in character_details.keys():
#         print(f'{key}: {character_details[key]}')

# def display_planet_details(planet_details):
#     print('Planet Details')
#     print('==============')
#     for key in planet_details.keys():
#         print(f'{key}: {planet_details[key]}')

# def display_starship_details(starship_details):
#     print('Starship Details')
#     print('================')
#     for key in starship_details.keys():
#         print(f'{key}: {starship_details[key]}')

# def display_vehicle_details(vehicle_details):
#     print('Vehicle Details')
#     print('===============')
#     for key in vehicle_details.keys():
#         print(f'{key}: {vehicle_details[key]}')

# def display_species_details(species_details):
#     print('Species Details')
#     print('===============')
#     for key in species_details.keys():
#         print(f'{key}: {species_details[key]}')

# def display_all_details(film_details, category_details, character_details, planet_details, starship_details, vehicle_details, species_details):
#     retrieve_planet_details()
#     retrieve_category_details()
#     retrieve_character_details()
#     retrieve_starship_details()
#     retrieve_vehicle_details()
#     retrieve_species_details()
    
#     display_film_details(film_details)
#     display_category_details(category_details)
#     display_character_details(character_details)
#     display_planet_details(planet_details)
#     display_starship_details(starship_details)
#     display_vehicle_details(vehicle_details)
#     display_species_details(species_details)


# display_all_details(retrieve_film_details(), retrieve_category_details(), retrieve_character_details(), retrieve_planet_details(), retrieve_starship_details(), retrieve_vehicle_details(), retrieve_species_details())


#     # TODO Wait for all the threads to finish. Note: You will need to use the 'join' method to wait for all the threads to finish.
#     #      See https://docs.python.org/3/library/threading.html#thread-objects for more information.


#     # TODO Get the data from each of the threads and put them in a list.
#     #      Note: You will need to use the 'join' method to wait for all the threads to finish.


    
#     # Iterate over each of the keys in the sixth film details and get the data
#     # for each of the categories (might want to create function to do this)

#     # TODO Call the display function



# print(f'There were {call_count} calls to the server')
# total_time = time.perf_counter() - begin_time
# total_time_str = "{:.2f}".format(total_time)
# print(f'Total time = {total_time_str} sec')
    
#     # If you do have a slow computer, then put a comment in your code about why you are changing
#     # the total_time limit. Note: 90+ seconds means that you are not doing multithreading
# assert total_time < 15, "Unless you have a super slow computer, it should not take more than 15 seconds to get all the data."

# assert call_count == 94, "It should take exactly 94 threads to get all the data"
    

if __name__ == "__main__":
    main()