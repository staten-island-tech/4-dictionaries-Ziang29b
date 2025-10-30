apple = {"price":"2 dollar","size" : "about 3 inches", "color": "green, red or yellow"}
banana = {"price": "2 dollar", "size": "6 or 7 inches", "color" : "yellow or green"}
giant_baguette_pillow = {"rice" : "222 dollars", "size": "10 feet long 1 feet 6 inches wide", "color": "baguette colored"}
stuff = {"apple":apple,"banana":banana, "giant_baguette_pillow":giant_baguette_pillow }
user_input = input("what do you want: ")
if user_input in stuff:      
    print (stuff[user_input])
else:
    print ("we no have")