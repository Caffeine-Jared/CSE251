"""
Course: CSE 251
Lesson Week: 02 - Team Activity
File: team02.py
Author: Brother Comeau (modified by Brother Foushee)

Purpose: Playing Card API calls

Instructions:

- Review instructions in Canvas.

"""

from datetime import datetime, timedelta
import threading
import requests
import json
deck_id = '5lc1xs96ns03'
url = f'https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=1'
# https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1

class Request_thread(threading.Thread):

    def __init__(self, url):
        # Call the Thread class's init function
        threading.Thread.__init__(self)
        self.url = url
        self.response = {}

    def run(self):
        response = requests.get(self.url)
        # Check the status code to see if the request succeeded.
        if response.status_code == 200:
            self.response = response.json()
        else:
            print('RESPONSE = ', response.status_code)

class Deck:

    def __init__(self, deck_id):
        self.id = deck_id
        self.reshuffle()
        self.remaining = 52


    def reshuffle(self):
        # TODO - add call to reshuffle
        t1 = Request_thread(f'https://deckofcardsapi.com/api/deck/{self.id}/shuffle/')
        t1.start()
        t1.join()
        pass

    def draw_card(self):
        # TODO add call to get a card
        t2 = Request_thread(f'https://deckofcardsapi.com/api/deck/{self.id}/draw/?count=2')
        t2.start()
        t2.join()
        if t2.response != {}:
            self.remaining = t2.response['remaining']
            return t2.response['cards'][0]['code']
        else:
            return 'something went wrong'
            

    def cards_remaining(self):
        return self.remaining


    def draw_endless(self):
        if self.remaining <= 0:
            self.reshuffle()
        return self.draw_card()


if __name__ == '__main__':

    # TODO - run the program team_get_deck_id.py and insert
    #        the deck ID here.  You only need to run the 
    #        team_get_deck_id.py program once. You can have
    #        multiple decks if you need them

    deck_id = '5lc1xs96ns03'

    # Test Code >>>>>
    deck = Deck(deck_id)
    for i in range(55):
        card = deck.draw_endless()
        print(i, card, flush=True)
    print()
    # <<<<<<<<<<<<<<<<<<

