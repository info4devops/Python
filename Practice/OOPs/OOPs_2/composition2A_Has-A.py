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
  
  def __init__(self,sports,movies,politics): # passing variables as instance variable
    self.sports=sports
    self.movies=movies
    self.political=politics
  def getTotalNews(self):
    print('Welcome to VNews')
    self.sports.sportsInfo()
    self.movies.movieInfo()
    self.political.politicalInfo()

sports=SportsNews() #self.sports=sports and sports=SportsNews() means self.sports= SportsNews()

movies=MovieNews()
politics=PoliticalNews()
v=VNews(sports,movies,politics)
v.getTotalNews()