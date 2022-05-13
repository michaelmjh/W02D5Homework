class Bar:

    def __init__(self, name, till, rooms):
        self.name = name
        self.till = till
        self.rooms = rooms

    
    def increase_till(self, room):
        self.till += room.entry_fee

    def check_in_guest(self, room, guest):
        if room.check_space_available() and guest.check_can_afford_entry(room):
            room.add_guest(guest)
            self.increase_till(room)
            guest.pay_entry(room)
            
    def check_out_guest(self, room, guest):
        room.remove_guest(guest)