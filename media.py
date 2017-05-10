
import webbrowser
from PIL import Image
import urllib
import json


class Movie():
    '''This class provides a way to store movie info'''

    # Value for the OMDB API to get Rotten Tomato Rating
    ROTTEN_TOMATO = 1

    def __init__(self, title, storyline, poster_image,
                 youtube_trailer):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer
        self.rating = self.get_rating(title)

    '''This function uses the omdb api and the title in the class
    to find the ratings. The Rotten Tomato rating is then extracted from
    the ratings.'''
    def get_rating(self, title):
        url = "http://www.omdbapi.com/?apikey=ee9ee471&t="
        url += title.replace(" ", "+")
        # Receives the JSON response from the API
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        return data['Ratings'][self.ROTTEN_TOMATO]['Value']

    '''Opens the youtube website of the video'''
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    '''Using the default Image program, the function opens the file'''
    def show_poster(self):
        image = Image.open(self.poster_image_url)
        image.show()

    '''Returns the title and storyline'''
    def get_description(self):
        desc = "Title: %s\nStoryline: %s" % (self.title, self.storyline)
        return desc
