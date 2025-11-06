stuff=[ 
                {
                "price":"2 dollar",
               "size" : "about 3 inches", 
               "name": "apple"
               },
               {
                "price": "2 dollar",
                "size": "6 or 7 inches",
                "name" : "banana"
                },
                {
                "price" : "222 dollars", 
                 "size": "10 feet long 1 feet 6 inches wide", 
                 "name": "giant baguette pillow"
                }
                ]

shopping = True 
while shopping:
        user_input = input("what do you want, banana apple or giant baguette pillow: ").lower()
        if user_input in [item["name"] for item in stuff]:
             for item in stuff:
                if item["name"] == user_input:
                    print(item)


        else: 
            print("we no have")
        user_input = input ("are you still shopping?").lower()
        if user_input in ["yea" , "yes", "yeah", "yep" , "yuh"]:
            print ("okay enjoy your shopping")
        else: 
            print ("cashier is up front")
            break 