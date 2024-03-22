import random
logo = '''88          88                       88        88                       88         
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P"                            '''
def print_card(card):
    if card == 11 or card == 1:
        return("""
         _________
        |         |
        |    A    |
        |         |
        |_________|
        """)
    elif card == 1:
        return("""
         _________
        |         |
        |    1    |
        |         |
        |_________|
        """)
    elif card == 3:
        return("""
         _________
        |         |
        |    3    |
        |         |
        |_________|
        """)
    elif card == 4:
        return("""
         _________
        |         |
        |    4    |
        |         |
        |_________|
        """)
    elif card == 5:
        return("""
         _________
        |         |
        |    5    |
        |         |
        |_________|
        """)
    elif card == 6:
        return("""
         _________
        |         |
        |    6    |
        |         |
        |_________|
        """)
    elif card == 7:
        return("""
         _________
        |         |
        |    7    |
        |         |
        |_________|
        """)
    elif card == 8:
        return("""
         _________
        |         |
        |    8    |
        |         |
        |_________|
        """)
    elif card == 9:
        return("""
         _________
        |         |
        |    9    |
        |         |
        |_________|
        """)
    elif card == 10:
        return("""
         ________
        |        |
        |   10   |
        |        |
        |________|
        """)
        