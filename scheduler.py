import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time
from room_generator import GenerateRoom
import random
import datetime
import uuid

# Function to generate a random schedule
def generate_schedule():
    now = datetime.datetime.now()
    hours = [8, 12, 18]  # Possible hours
    chosen_hour = random.choice(hours)  # Choose a random hour
    if chosen_hour < now.hour:
        # Schedule is for tomorrow
        schedule = datetime.datetime.combine(now.date() + datetime.timedelta(days=1),
                                              datetime.time(hour=chosen_hour))
    else:
        # Schedule is for today
        schedule = datetime.datetime.combine(now.date(),
                                              datetime.time(hour=chosen_hour))
    return schedule

# Use a service account
cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)

# Get a reference to the Firestore database
db = firestore.client()

while True:
    roomID = str(uuid.uuid4())
    # Create a new room document with a new room ID
    generate_room = GenerateRoom()
    roomCategory = generate_room.generate_room()
    roomName = roomCategory+ ' Meet Up'
    
    # Generate a new schedule
    new_schedule = generate_schedule()
    new_room_ref = db.collection('Rooms').document(roomID)
    new_room_ref.set(       
            {
                'roomName': roomName,
                'roomCategory': roomCategory,
                'roomSchedule': new_schedule,
                'roomParticipants': [],
                'chatContents': [
                ]
            })
    # Wait for 2 hours
    time.sleep(7200)
 
