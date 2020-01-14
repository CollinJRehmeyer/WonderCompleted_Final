'''
Created on Jan 10, 2020

@author: rehme
'''
import random
import datetime

def generate():
    
    
    leaders = ["George Washington", "Harun al-Rashid", "Ashurbanipal", "Maria Theresa", "Montezuma",
               "Nebuchadnezzar II", "Pedro II", "Hagios Theodora", "Dido", "Boudicca", "Wu Zetian",
               "Harald Bluetooth", "Ramesses II", "Elizabeth", "Selassie", "Napoleon", "Bismarck",
               "Alexander", "Atilla", "Pachacuti", "Ghandi", "Gajah Mada", "Hiawatha", "Oda Nobunaga",
               "Sejong", "Pacal", "Genghis Khan", "Ahmad al-Mansur", "William", "Suleiman", "Darius",
               "Casimir III", "Kamehameha", "Maria I", "Caesar", "Catherine", "Pocatello",
               "Ramkhamhaeng", "Askia", "Isabella", "Gustavus Adolphus", "Enrico Dandolo", "Shaka"]
    

    wonders = ["Great Library", "Mausoleum of Halicarnassus", "Pyramids", "Statue of Zeus", "Stonehenge",
               "Temple of Artemis", "Colossus", "Great Lighthouse", "Great Wall", "Hanging Gardens",
               "Oracle", "Parthenon", "Petra", "Terracotta Army", "Alhambra", "Angkor Wat", "Borobudur",
               "Chichen Itza", "Great Mosque of Djenne", "Hagia Sophia", "Machu Picchu", "Notre Dame",
               "Forbidden Palace", "Globe Theatre", "Himeji Castle", "Leaning Tower of Pisa", "Porcelain Tower",
               "Red Fort", "Sistine Chapel", "Taj Mahal", "Uffizi", "Big Ben", "Brandenburg Gate", "Louvre",
               "Broadway", "Eiffel Tower", "Kremlin", "Neushwanstein", "Prora", "Statue of Liberty",
               "Cristo Redentor", "Great Firewall", "Pentagon", "Sydney Opera House", "CN Tower",
               "Hubble Space Telescope", "International Space Station", "United Nations"]

    
    
    random.seed(datetime.time())
    leader = random.randint(0, len(leaders) - 1)
    wonder = random.randint(0, len(wonders) - 1)
    
    farawayland = random.randint(0,1)
    
    theLeader = leaders[leader]
    theWonder = wonders[wonder]
    
    if farawayland == 1:
        return theWonder + " has been built in a faraway land!"
    else:
        return theLeader + " has completed " + theWonder
    
    
    