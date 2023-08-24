#Land Draw Odds
#Carrik McNerlin, 13 January 2018

#skip steps to figure out library size if possible
know = str(input('Do you know how many lands are left in your library? [Y] or [N]\n'))
if know.upper() == 'Y':
    remaining_lands = int(input('Alright, good. How many are left then? '))
else:
    print("Alright. No problem; I know it's tough to keep track. Let's do it together :)\n")
    total_lands = int(input("First thing's first, how many lands are in your full library? "))


    lands_out = int(input('How many lands do you have out, in your hand, or in the graveyard/exile currently? '))
    remaining_lands = total_lands - lands_out
    print('You have %d lands left in your library.\n' % remaining_lands)


cards_left = int(input('How many cards do you still have in library? '))
draw_odds = (remaining_lands / cards_left) * 100 #display as percentage


print('You have a %.2f%% chance of drawing a land next.' % (draw_odds))