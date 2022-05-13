class Guest:

    def __init__(self, name, wallet, favourite_song):
        self.name = name
        self.wallet = wallet
        self.favourite_song = favourite_song

    def check_can_afford_entry(self, room):
        if self.wallet >= room.entry_fee:
            return True
        else:
            return False

    def pay_entry(self, room):
        self.wallet -= room.entry_fee

    def react_to_song(self, songs):
        if self.favourite_song in songs:
            return ("Woohoo")