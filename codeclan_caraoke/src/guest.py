class Guest:

    def __init__(self, name, wallet, favourite_song):
        self.name = name
        self.wallet = wallet
        self.favourite_song = favourite_song

    def check_can_afford_entry(self):
        if self.wallet > 5:
            return True
        else:
            return False

    def pay_entry(self):
        self.wallet -= 5

    def react_to_song(self, song):
        if song == self.favourite_song:
            return ("Woohoo")