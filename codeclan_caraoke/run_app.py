from src.bar import Bar
from src.guest import Guest
from src.room import Room
from src.song import Song
from modules.menu import *

user_input = "w"

while user_input != "q":
    menu_display_start_menu()
    user_input = menu_get_menu_selection()
    
    if user_input == "1":
        room = int(menu_select_room()) - 1
        guest = int(menu_select_guest()) - 1

        bar_1.check_in_guest(bar_1.rooms[room], guest_list[guest])
    
    elif user_input == "2":
        room = int(menu_select_room()) - 1

        menu_checked_in_guests(room)





