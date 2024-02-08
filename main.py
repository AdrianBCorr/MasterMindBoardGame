import random

COLOR_LIST = ["G", "B", "R", "Y", "P", "O", "W", "T"] #color list
#G->Green B->Blue R->Red Y->Yellow P->Pink O->Orange W->White T->Teal

def comp_seq():
    """function is for the computer to create a sequence"""
    sequence = set()
    for _ in range(10):
        sequence.add(random.choice(COLOR_LIST))
        if len(sequence) == 4:
            break
    #print(sequence)
    return list(sequence)

def user_guess():
    """function is used to prompt the user is guess a sequence and to arrange the sequence in a list"""
    guess = input("Guess: ").upper()
    user_input = []
    for i in guess:
        user_input += i
    #print(user_input)
    return user_input

def check_seq(sequence, user_input):
    """function used to check the code and user's answer and repond to the code"""
    correct_chr = 0
    for i in sequence:
        if i in user_input:
            correct_chr += 1
    
    reply = [] #this list is used to hint the user about the code 
    # (+) -> correct color, correct position
    # (-) -> correct color, wrong position
    for i in range(len(user_input)):
        if sequence[i] == user_input[i]:
            correct_chr -= 1
            reply += '+'
        
    for i in range(correct_chr):
        reply += '-'
    
    print(f"{user_input} {reply}")

seq = comp_seq()
chances = 10
game = True
print(f"Welcome to Master Mind:\n{COLOR_LIST}\nwhere G->Green B->Blue R->Red Y->Yellow P->Pink O->Orange W->White T->Teal")
print("Guess four colors\nfor hints after each turn\n('+' -> correct color, correct position)\n('-' -> correct color, wrong position")
print(COLOR_LIST)
while(game):
    chances -= 1
    user = user_guess()
    check_seq(seq, user)
    if chances < 1:
        game = False
        print(f"You Lost!\nThe sequence is {seq}")
    elif user == seq:
        print(f"You Won in {10 - chances} tries!!!")
        game = False
    
