import random

class GenerateRoom:
    room_categories = ["Design", "Programming", "Business", "Investment", "Games", "Sports", "Music", "Movie"]
    
    @staticmethod
    def generate_room():
        room_category = random.choice(GenerateRoom.room_categories)
        return room_category
