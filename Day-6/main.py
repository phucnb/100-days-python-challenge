def turn_right():
    turn_left()
    turn_left()
    turn_left()

def intersection():
    if right_is_clear() and front_is_clear():
        turn_right()
        turn_right()
        if right_is_clear() and front_is_clear():
            return True
        else:
            turn_left()
            turn_left()
            return False
    else:
        return False
while not at_goal():
    if intersection():
        while not is_facing_north():
            turn_left()
        move()
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
            
    
        
     
        
    
    
