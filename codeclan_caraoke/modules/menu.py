from src.bar import Bar
from src.guest import Guest
from data.data import *

def menu_display_start_menu():
    print("Options:")
    print("1. Check-in guest")
    print("2. Show checked-in guests")
    print("q. Quit")

def menu_select_room():
    menu_display_room_selection()
    return menu_get_menu_selection()

def menu_display_room_selection():
    print("Choose a room:")
    for room in bar_1.rooms:
        print(f"{bar_1.rooms.index(room) + 1}: {room.name.title()}")
    
def menu_select_guest():
    menu_display_guest_selection()
    return menu_get_menu_selection()

def menu_display_guest_selection():
    print("Choose a guest:")
    for guest in guest_list:
        print(f"{guest_list.index(guest) + 1}: {guest.name.title()}")

def menu_get_menu_selection():
    user_input = input("Enter a option: ")
    print()
    return user_input

def menu_checked_in_guests(room):
    for guest in bar_1.rooms[room]:
        print(f"{guest.index() + 1}: {guest.name}")