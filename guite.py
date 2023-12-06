#CS5001
#Fall 2023
#Final Project
#Herry Li & Nengjui Yu

#demo version gui, used blackjack

from tkinter import *
from PIL import Image, ImageTk
from blackjack import Blackjack
import random

root = Tk()
root.title('Black Jack')
root.geometry('1200x800')
root.iconbitmap('PNG-cards-1.3/Northeastern_University.jpg')
root.configure(background='green')


# Define global game
game = None

#make img fit to frame
def resize_cards(card: str):
    our_card_img = Image.open(card)
    resized = our_card_img.resize((150, 218))
    new_image = ImageTk.PhotoImage(resized)
    return new_image

#adjust filenames
def convert_card(card: dict) -> str:
    suit = card['suit'].lower()
    rank = str(card['rank']).lower()
    image = f'PNG-cards-1.3/{rank}_of_{suit}.png'
    return image

#update hand values
#used in hit, stand
def update_hand_values():
    player_hand = game.calculate_hand_value(game.player_hand)
    dealer_hand = game.calculate_hand_value(game.player_hand)

    player_hand_value.set(f'Player Hand Value: {player_hand}')
    dealer_hand_value.set(f'Dealer Hand Value: **')

    if player_hand > 21:
        result = 'You bust! You lose'
        show_result_popup(result)
    elif dealer_hand > 21:
        result = f'Dealer has {dealer_hand} \nYou win'
        show_result_popup(result)

# Start game
def shuffle():

    #create game
    global game  # Access the global game variable
    game = Blackjack()
    game.start_game()

    #frames
    #first two cards fixed
    #show only husky cards for dealer except first card
    dealer_frame.config(text='Dealer')
    player_frame.config(text='Player')
    update_hand_values()

    dealer_hand = game.dealer_hand
    player_hand = game.player_hand

    player_card1 = convert_card(player_hand[0])
    player_card2 = convert_card(player_hand[1])
    player_image1 = resize_cards(player_card1)
    player_image2 = resize_cards(player_card2)

    card1 = 'PNG-cards-1.3/Northeastern_University.jpg' #husky card
    #dealer randomly shows a card in first round
    num = random.randint(0, 1)
    dealer_image1 = resize_cards(convert_card(dealer_hand[num]))
    dealer_image2 = resize_cards(card1)

    
    #configurations
    dealer_labels[0].config(image=dealer_image1)
    dealer_labels[0].image = dealer_image1  

    player_labels[0].config(image=player_image1)
    player_labels[0].image = player_image1  

    dealer_labels[1].config(image=dealer_image2)
    dealer_labels[1].image = dealer_image2  

    player_labels[1].config(image=player_image2)
    player_labels[1].image = player_image2  
    
    #toggle if game started
    start_button.config(text='Restart Game', command=restart_game)

#resets images to empty
#used in game restart
def reset_hand_images():
    for label in dealer_labels:
        label.config(image='')
        label.image = ''

    for label in player_labels:
        label.config(image='')
        label.image = ''

#restart the game
def restart_game():
    global game
    game = None
    reset_hand_images()
    shuffle()

# Hit function
def hit():
    global game
    game.hit()

    player_hand = game.player_hand
    dealer_hand = game.dealer_hand

    # Get the last card, resize
    player_card = convert_card(player_hand[-1])  
    player_image = resize_cards(player_card)
    
    dealer_card = convert_card(dealer_hand[-1])  
    dealer_image = resize_cards(dealer_card)

    card1 = 'PNG-cards-1.3/Northeastern_University.jpg' #husky card
    common_image = resize_cards(card1)

    # Find the next empty label in player_labels
    next_player_label_index = -1
    next_dealer_label_index = -1

    #player and dealer have same # of cards
    #record index
    for index, _ in enumerate(player_labels):
        if _.cget('image') == '':
            next_player_label_index = index
            next_dealer_label_index = index
            break  

    if next_player_label_index != -1:
        player_labels[next_player_label_index].config(image=player_image)
        player_labels[next_player_label_index].image = player_image
        
    # Dealer, show a common image for all cards except the first card
    if next_dealer_label_index != -1:
        if next_dealer_label_index > 0:
            dealer_labels[next_dealer_label_index].config(image=common_image)
            dealer_labels[next_dealer_label_index].image = common_image
        else:
            # Show the first card of the dealer's hand
            dealer_labels[next_dealer_label_index].config(image=dealer_image)
            dealer_labels[next_dealer_label_index].image = dealer_image

    update_hand_values()


#stand function
def stand():
    global game
    player_hand_value = game.calculate_hand_value(game.player_hand)
    dealer_hand_value = game.calculate_hand_value(game.dealer_hand)

    #dealer has to hit until 17
    #5 cards max
    while dealer_hand_value < 17 and len(game.dealer_hand) < 6:
        dealer_hand_value = game.calculate_hand_value(game.dealer_hand)
        game.deal_card(game.dealer_hand)

    result = game.who_wins(player_hand_value, dealer_hand_value)
    show_result_popup(result)

#pop up win if stand
def show_result_popup(result):
    result_popup = Toplevel(root)
    result_popup.title('Game Result')

    result_label = Label(result_popup, text=result, font=("Helvetica", 16))
    result_label.pack(padx=20, pady=20)

    ok_button = Button(result_popup, text='OK', font=("Helvetica", 14), command=result_popup.destroy)
    ok_button.pack(pady=20)

    
# frames
my_frame = Frame(root, bg='green')
my_frame.pack(pady=20)

dealer_frame = LabelFrame(my_frame, text='Dealer', bd=0)
dealer_frame.pack(padx=20, ipadx=20)

player_frame = LabelFrame(my_frame, text='Player', bd=0)
player_frame.pack(ipadx=20, pady=10)

value_frame = Frame(my_frame, bg='green')
value_frame.pack(pady=20)

# labels
dealer_labels = []
player_labels = []

for i in range(5):
    dealer_label = Label(dealer_frame, text='')
    dealer_label.grid(pady=20, row=0, column=i, padx=10)
    dealer_labels.append(dealer_label)

    player_label = Label(player_frame, text='')
    player_label.grid(pady=20, row=1, column=i, padx=10)
    player_labels.append(player_label)

# Hand value labels
player_hand_value = StringVar()
player_hand_label = Label(value_frame, textvariable=player_hand_value, font=("Helvetica", 12), bg='green', fg='white')
player_hand_label.grid(row=0, column=0, padx=10)

dealer_hand_value = StringVar()
dealer_hand_label = Label(value_frame, textvariable=player_hand_value, font=("Helvetica", 12), bg='green', fg='white')
dealer_hand_label.grid(row=0, column=0, padx=10)


# buttons
start_button = Button(value_frame, text='Start Game', font=("Helvetica", 14), command=shuffle)
start_button.grid(row=0, column=2, pady=20)

hit_button = Button(value_frame, text='Hit', font=("Helvetica", 14), command=hit)
hit_button.grid(row=0, column=3, pady=20)

stand_button = Button(value_frame, text='Stand', font=("Helvetica", 14), command=stand)
stand_button.grid(row=0, column=4, pady=20)


# Run the Tkinter main loop
root.mainloop()
