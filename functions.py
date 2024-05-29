def choises(number):

    if number=="r" or number ==1:
        return """
   _________
  |   |  |  \__
  /¨¨¨¨===  |  |
 /    ___/__|__|
|    /         |
 \____ROCK_____/"""
    elif number== "p" or number==2:
        return """
    __ __ __
   |  |  |  |__
   |¨¨|¨¨|¨¨|  |
__ |¨¨|¨¨|¨¨|¨¨|
\ \|  |  |  |¨¨|
|  \__         |
|              |
 \____PAPER____/
""" 
    elif number == "s" or number==3:
        return """
 __       __
 \  \   /  /
  \  \ /  /
   \  V  /__ __
  /¨¨¨¨===  |  |
 /    ___/__|__|
|    /         |
 \__SCISSORS___/
"""
    else: 
        return "check that you have spelled correctly"



        # if user == "r" and ai ==1: 
        #         print("IT'S A TIE!")
        #         ties+=1
        # elif user == "p" and ai ==2: 
        #         print("IT'S A TIE!")
        #         ties+=1
        # elif user == "s" and ai ==3: 
        #         print("IT'S A TIE!")
        #         ties+=1

        # elif user == "r" and ai ==2: 
        #         print("AI WON!")
        #         losses+=1

        # elif user == "p" and ai ==1: 
        #         print("YOU WON!")
        #         wins+=1

        # elif user == "s" and ai ==2: 
        #         print("YOU WON!")
        #         wins+=1

        # elif user == "p" and ai ==3: 
        #         print("AI WON!")
        #         losses+=1

        # elif user == "r" and ai ==3: 
        #         print("YOU WON!")
        #         wins+=1

        # elif user == "s" and ai ==1: 
        #         print("AI WON!")
        #         losses+=1