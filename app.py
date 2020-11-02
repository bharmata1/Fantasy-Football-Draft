# Creates a new empty populatable list of your fantasy football team
draft_list = []


def show_help():
    print("This is a snake formatted full PPR Fantasy Football draft!")
    print("You will have a maximum of 10 total selections and can start building your team now. Good Luck!")
    print("""
Enter 'STOP' to stop adding players to your team.
Enter 'HELP' for these tips.
Enter 'DONE' to display your team.
""")
    
    

def add_to_list(player):
    # Adds the player to the users team
    draft_list.append(player)
    # Lets user know the pick was successful and tells them how many total players they have drafted
    print("Selection successful! Your team has a total of {} players.".format(len(draft_list)))    


def show_list():
    print("Here's your team:")
    for player in draft_list:
        print(player)
    
show_help()
while True:
    new_player = input("> ")
    
    
    if new_player == 'STOP':
        break
    elif new_player == 'HELP':
        show_help()
        continue
    elif new_player == 'DONE':
            show_list()
            continue
   
    add_to_list(new_player)
    
show_list()