# Creating Movie class
class Movie:
    '''Movie class developed by vamsi for python practice purpose'''
    def __init__(self,title,hero,heroin):
        self.title=title
        self.hero=hero
        self.heroin=heroin
    def info(self):
        print('Movie name:',self.title)
        print('Hero name:',self.hero)
        print('Heroin name:',self.heroin)
#Creating multiple movie objects and adding those objects to list
list_of_movies=[]
while True:
    title=input("Enter Movie Name:")
    hero=input("Enter Hero Name:")
    heroin=input("Enter Heroin Name:")
    m=Movie(title,hero,heroin)
    list_of_movies.append(m)
    print("Movie details added successfully")
    option=input("Do You want to add another movie details[Yes/No]:").strip()
    if option.lower()=='no':
        break
print("All Movie information")
print('#'*40)
# Accessing list objects one by one
for movie in list_of_movies:
    movie.info()
    print('-'*30) # to print blank line




