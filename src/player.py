# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:

    def __init__(self, room):
        self.room = room
        self.inv = []

    def get(self, item):
        self.inv.append(item)

    def drop(self, index):
        del self.inv[index]
