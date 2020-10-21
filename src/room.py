# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, item, l_count=0):
        self.name = name
        self.description = description
        self.item = item
        self.l_count = l_count
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
