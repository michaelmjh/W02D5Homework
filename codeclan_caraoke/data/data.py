from src.bar import Bar
from src.guest import Guest
from src.room import Room
from src.song import Song

song_1 = Song('long tall sally', 'little richard')
song_2 = Song('im so excited', 'ponter sisters')

guest_1 = Guest('michael', 10, song_1)
guest_2 = Guest('ian', 3, song_2)
guest_3 = Guest('josh', 10, song_1)
guest_4 = Guest('gillian', 10, song_2)
guest_5 = Guest('iain', 10, song_1)
guest_6 = Guest('ally', 10, song_2)
guest_7 = Guest('kieran', 10, song_2)

guest_list = [guest_1, guest_2, guest_3, guest_4, guest_5, guest_6, guest_7]

room_1 = Room('oldies', 5, 5)
room_2 = Room('rock', 10, 10)
        
rooms = [room_1, room_2]

bar_1 = Bar('ccc', 100, rooms)