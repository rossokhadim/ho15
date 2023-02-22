import webbrowser
import os
class Film:
    title = 'Crazy, Stupid, Love'
    description = "A middle-aged husband's life changes dramatically when his wife asks him for a divorce.\nHe seeks to rediscover his manhood with the help of a newfound friend, Jacob, learning to pick up girls at bars."
    directors = ['Glenn Ficarra', 'John Requa']
    IMDb_RATING = 7.4
    year = 2011
    trailer = 'https://www.imdb.com/video/vi3722091801/'

    def give_info(self):
        print(f'Title: {self.title}, \nDescription: {self.description}, \nDirectors: {self.directors},  \nIMDb_RATING = {self.IMDb_RATING},  \nyear = {self.year},  \nTrailer: {self.trailer}')

    def open_trailer(self):
        webbrowser.open_new(self.trailer)

    def upload_file(self):
        number = 1
        while number != 0:
            print('What do you want?(write number) \n1.Create a file \n0.Stop ')
            number = int(input())
            if number == 0: break
            print("Write letter of folder")
            letter = input()
            os.chdir('film_player/film_storage')
            os.chdir(letter)
            print("Write name of film")
            name = input()
            new_file = open(name+'.txt', 'w')
            new_file.close()
            os.chdir('../../../')

    def get_film_address(self):
        print('Write name of film(without .txt)')
        film_name = input()
        os.chdir('film_player/film_storage')
        for dir in os.listdir():
            os.chdir(dir)
            for file in os.listdir():
                if str(file) == film_name + '.txt':
                    return os.getcwd()+"\\"+film_name+'.txt'
            os.chdir('../')
        os.chdir('../../')