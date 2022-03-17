# DO NOT REMOVE
from deck import print_card, draw_card, print_header, draw_starting_hand, print_end_turn_status, print_end_game_status

print_header('YOUR TURN')
user_value = draw_starting_hand()
reply = ''
if user_value < 21:
     reply = input("You have {}. Hit (y/n)? {}".format(user_value, ''))
    
while reply == 'y' and user_value < 21:
    user_anothervalue = draw_card()
    user_value = user_value + user_anothervalue
    if user_value < 21:
        reply = input("You have {}. Hit (y/n)? {}".format(user_value, ''))
print_end_turn_status(user_value)

print_header('DEALER TURN')
dealer_value = draw_starting_hand()
while dealer_value <= 17:
    dealer_anothervalue = draw_card()
    dealer_value = dealer_value + dealer_anothervalue
print_end_turn_status(dealer_value)

print_end_game_status(user_value, dealer_value)


    




