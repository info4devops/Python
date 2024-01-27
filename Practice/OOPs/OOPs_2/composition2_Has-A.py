# Accessing members of one class from other class
#1. By Composition(Has-A relationship)

class SportsNews:
  def sportsInfo(self):
    print('Sports Info')
    print('\tSports Information')

class MovieNews:
  def movieInfo(self):
    print('Movie Info')
    print('\tMovie Information')
    
class PoliticalNews:
  def politicalInfo(self):
    print('Sports Info')
    print('\tSports Information')
    
class VNews:
  
  def __init__(self): # passing methods as instance variable
    self.sports=SportsNews()
    self.movies=MovieNews()
    self.political=PoliticalNews()
  def getTotalNews(self):
    print('Welcome to VNews')
    self.sports.sportsInfo()
    self.movies.movieInfo()
    self.political.politicalInfo()

v=VNews()
v.getTotalNews()