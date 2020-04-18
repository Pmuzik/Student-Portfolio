#Creates a randomly generated password based on random words inspired by Dot.Hack
'''''
import random
area1 = list of area 1 names
area2 = list of area 2 names
area3 = list of area 3 names
password = ''

def generate_pass():
    randomly select a name from area1
    add name to password
    randomly select a name from area2
    add name to password
    randomly select a name from area3
    add name to password
    (password = password+area)
    return password

----has not been added yet----
def add_num():
    select random number between 0-99
    cast number to string
    concatenate with '#'
     add '#'+'random number' to password

ask user if they want to generate a new password or exit
if yes
    generate_pass()
    ask if they want to add a number
    if yes
        add_num()
        print new password
        loop back to query
    if no
        print new password
        loop back to query
'''
import random

area1 = ['Buzzing', 'Elegant', 'Forgotten', 'Essential', 'Screaming', 'Chasing',
         'Creeping', 'Dancing', 'Hidden', 'Wealthy', 'Peaceful', 'Submissive', 'Great',
         'Blurry', 'Gallant', 'Lazy', 'Sneering', 'Pulsating', 'Delicious', 'Setting',
         'Disputing', 'Crying', 'Coiling', 'Rising', 'Choosing', 'Heartless', 'Entwined',
         'Endless', 'Sacred', 'Upfront', 'Fly-Away', 'Heavenly', 'Truthful', 'Halberd',
         'Warm', 'Rough-Song', 'Unseeing', 'Harvesting', 'Croaking', 'Overjoyed',
         'Graceful', 'Paling', 'Agonizing', 'Piling', 'Restful', 'Wandering', 'Unknowing',
         'Obstructed', 'Saddened', 'Counting', 'Dreaming', 'Decadent', 'Playing', 'Beloved',
         'Fattening', 'Unending', 'Roaring', "Spring's", 'Concealed', 'Protected', 'Closed',
         'Freezing', 'Immovable', 'Dawning', 'Starting', 'Courageous', 'Your', 'Immaculate',
         'Digging', 'Wronged', 'Cleaning', 'Trivial', 'Newborn', 'Assertive', 'Corpulent',
         'Abhorrent', 'Emergent', 'Vile', 'Novel', 'Scraping', 'Last', 'Listless', "Hornet's",
         "Ripping", "Soft", "Tired", 'Blasphemous', 'Burdened', 'My', 'Unknown', 'Deviant',
         'Raining', 'Another', 'Lone', 'First', 'Obscure', 'Belligerent', 'Bent-Blade', 'Sordid',
         'Alchemical', 'Hectored', 'Waking', 'Overripe', 'Abrupt', 'Undead', 'Painted', 'Sanctuary',
         'Deleted', 'Benign', 'Linked', 'Overwrought', 'Benighted', 'Assuaged', 'Feckless', 'Benevolent',
         'Bright', 'Unassigned', 'Eternal', 'Cacophonous','Egregious', 'Inverted', 'Elite', 'Soaring',
         'Matronly', 'Patriarchal', 'Matriarchal', 'Jovian', 'Eclectic', 'Asinine', 'Abbreviated',
         'Branded', 'Royal', 'Mischievous', 'Uninitiated', "Low", "Electric", "Unorthodox", 'Blessed',
         "Starlet's", "Magister's", 'Unsheathed', 'Embattled', 'Full']

area2 = ["Wrath's", "Swift", "Black", "Ruined", "Honor", "Marble", "Military",
         "Aster's", "Bustling", "Vain", "Daybreak's", "Kourin's", "Humbling", "Heretic's",
         "Dusk's", "Sunshine's", "Nirvana's", "Cupola", "Friend's", "Forbidden", "Idling",
         "Returning", "Cupid's", "Fortune's", "Mourning", "Medium's", "Leading", "Tragedy's",
         "Cursed", "Obsessive", "Season's", "Advice's", "Failing", "Unlimited", "Past's",
         "Eternity's", "Gray", "Gambler's", "Destiny's", "Love's", "Superior", "Starting",
         "Joyous", "Corpse's", "Blazing", "Discord's", "Red-Plum's", "Boomer's", "Engaging",
         "Chicken's", "Samurai's", "Maid's", "Chrome", "Journey's", "Coffee",
         "Purple", "Bewitching", "Peach", "Mecha", "Slumbering", "Rusting", "Hammered", "Peddler's",
         "Mathematic", "Unborn", "Loving", "Canned", "Gary's", "Sour", "Hazardous", "Warring",
         "Sprite's", "Labyrinth's", "Minotaur's", "Sister's", "Tripling", "Stalking", "Leaden",
         'Cyan', 'Ceramic', 'August', 'Golden', 'Red', "Tearing", "Unforeseen", "Elysian",
         'Chitinous', 'Mean', "Brother's", 'Dormant', "Spider's", 'Bleached', 'Blotted', "Crustacean's",
         'Favorite', "King's", "Handmaiden's", 'Bare', 'Feline', 'Ursine', 'Fevered', 'Bovine',
         "Tyrant's", 'Canine', '_from_', 'World', 'Burg_of_', 'Key_of_', "Sen's", 'Demon', 'Bellicose',
         'Little', 'Depths_of_', "Try-Hard's", 'Ruins_of_', 'Big', 'Wide', 'Rushed', "Era's", 'Sonic',
         'Bastardized', 'Dangerous', 'Mismanaged', 'House_of_', 'Stymied', 'Approaching', 'Egress_of_',
         'Midnight', "Duke's", 'Stalwart', 'Duchy_of_', 'Aggregate', 'Haggard', "Cartographer's", 'Solo',
         'Rambling', "Sentry's", "Fourth", 'Ordained', 'Excommunicated', "Solicitor's", 'Dragon', 'Regalia']

area3 = ["Two-Wings", "Phoenix", "Hand-Song", "Pure-Bred", "Fast-Horse", "Belladonna", "Bum",
         "Generation", "Nemesis", "Alga-Grass", "Old-World", "Princess", "Phantom", "Paradise",
         "Masquerade", "Holy-Ground", "Bulwark", "Camellia", "Freedom", "1000Oaks", "In-Laws",
         "Slacker", "Drunkard", "Exile", "Empire", "Metal-Doll", "Weed-Eater", "Night-Moon",
         "Tiny-Beast", "Footsteps", "Wicker", "Gate", "Offerings", "Pilgrim", "Venom-Fang",
         "March", "Ocean", "Fountain", "Life-Boat", "Bodhi-Tree", "Snow-Lamp", "Cathedral",
         "Puddle", "Tide-Road", "Frog-Lake", "Blue-Cloud", "Scud", "Gold-Bird", "Dark-Tree",
         "Vagabond", "Pinwheel", "Evergreen", "Malt-Town", "Ignorance", "Globe", "Snow-Caps",
         "Foot-Stone", "Twin-Rocks", "Holy-Relic", "Cat's-Eye", "Whiplash", "Crawl-Tree", "Fortune",
         "Resort", "Cassiopeia", "Shadow", "Dead-Wood", "Radiation", "Berserker", "Daydream", "Titans",
         "Long-Tail", "Syndrome", "Algorithm", "Swans", "Orphans", "Breeze", "Vault", "Vector",
         "Twin-Peaks", "Story", 'Pagoda', 'Shower', "Doom", "Tangent", "Fields", 'Uproar',
         'Call', 'Croquis', 'Lock-Box', 'Coup-de-grace', 'Four-Pillars', 'Square', 'Arena', 'Calling',
         'Second', 'Favor', 'Quest', 'Chest', 'Banquet', 'Pitch', 'Achilles', 'Thucydides', 'Damocles',
         'Asylum', 'Regression', 'Giants', 'First-Flame', 'Fortress', 'Parish', 'Noir', 'Sunflower', 'Glory',
         'Firmament', 'South-Paw', 'Aquarius', 'Pisces', 'Libra', 'Gemini', 'Cancer', 'Sonic', 'Sagittarius',
         'Leo', 'Aries', 'Taurus', 'Virgo', 'Scorpio', 'Capricorn', 'Tails', 'Knuckles', 'Kite', 'Chateau',
         'Dynamic_Array', 'Rubric', 'Mandrake', 'Buzzard', 'Wisdom', 'Guard', 'Son', 'Daughter',
         'Thicket-CLearer', 'Garlic-Field', 'Tarot']


def generate_pass():
    password = ''
    password = password + random.choice(area1) + random.choice(area2) + random.choice(area3)
    return password


print(generate_pass())