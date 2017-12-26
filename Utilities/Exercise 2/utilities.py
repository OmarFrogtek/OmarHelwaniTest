def create_OrderId(): 

     # This function creates random orders that follow the given template. 

    import random

    order = ""

    for i in range (0,8):    
        order = order + str(random.choice("0123456789abcdef"))

    order = order + "-"

    for i in range (0,4):    
        order = order + str(random.choice("0123456789abcdef"))

    order = order + "-"

    for i in range (0,4):    
        order = order + str(random.choice("0123456789abcdef"))

    order = order + "-"

    for i in range (0,4):    
        order = order + str(random.choice("0123456789abcdef"))

    order = order + "-"

    for i in range (0,12):    
        order = order + str(random.choice("0123456789abcdef"))

    return order