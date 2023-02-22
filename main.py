import film_player.media_player as mp
import film_player.films_worker as fw
import os

player = mp.Player()
print(player.play())
print(player.change_quality)

# print(os.getcwd())
# os.chdir('film_player')
# os.mkdir('film_storage')
# os.chdir('film_storage')
# for i in range(65, 91):
#     os.mkdir(chr(i))
# os.chdir('../..')
# print(os.getcwd())

film = fw.Film()
film.give_info()
film.open_trailer()
film.upload_file()
print(film.get_film_address())