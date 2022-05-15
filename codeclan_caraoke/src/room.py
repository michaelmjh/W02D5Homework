class Room:

    def __init__(self, name, capacity, entry_fee):
        self.name = name
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.guests = []
        self.songs = []

# Functionality for adding guests to rooms
    def check_space_available(self):
        if len(self.guests) < self.capacity:
            return True
        else: 
            return False

    def check_already_checked_in(self, guest):
        if guest in self.guests:
            return True
        else:
            return False

    def add_guest(self, guest):
        self.guests.append(guest)

    def remove_guest(self, guest):
        self.guests.remove(guest)

#Functionality for adding songs to playlist
    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        if len(self.songs) > 0:
            self.songs.remove(song)
