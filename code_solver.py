import itertools

def generate_all_combinations(colors, length):
    """Generates a list of all the possible sequence that the code could be. With no duplicate colors in the code"""
    return list(itertools.product(colors, repeat=length))


def calculate_feedback(secret_code, guess):
    """function to give feedback as to color or position of the sequence"""
    correct_color_and_position = 0
    correct_color_only = 0
    
    secret_code_counts = {}
    guess_counts = {}
    
    for i in range(len(secret_code)):
        if secret_code[i] == guess[i]:  
            correct_color_and_position += 1
        else:
            secret_code_counts[secret_code[i]] = secret_code_counts.get(secret_code[i], 0) + 1
            guess_counts[guess[i]] = guess_counts.get(guess[i], 0) + 1
            
    for color in guess_counts:
        if color in secret_code_counts:
            correct_color_only += min(secret_code_counts[color], guess_counts[color])
    
    return correct_color_and_position, correct_color_only


def guess_secret_code(possible_codes):
    """function is guessing the first code in the possible codes"""
    return possible_codes[0]


def remove_inconsistent_codes(possible_codes, guess, feedback):
    """function colculates the feedback of all codes and removes the inconsistent codes"""
    consistent_codes = []
    for code in possible_codes:
        if calculate_feedback(code, guess) == feedback:
            consistent_codes.append(code)
    return consistent_codes


def mastermind(colors, length, secret_code):
    """function that runs the mastermind solver"""
    possible_codes = generate_all_combinations(colors, length)
    guesses = 0
    
    while True:
        guess = guess_secret_code(possible_codes)
        feedback = calculate_feedback(secret_code, guess)
        guesses += 1
        print(f"Guess #{guesses}: {guess}, Feedback: {feedback}")
        
        if feedback == (length, 0):
            print(f"The secret code is {guess}")
            break
        
        possible_codes = remove_inconsistent_codes(possible_codes, guess, feedback)
        
        if guesses >= 10:
            print("Maximum number of guesses reached. The secret code is still unknown.")
            break


colors = ['R', 'Y', 'P', 'O', 'W', 'T', 'B', 'G']
length = 4
secret_code = ['G', 'B', 'R', 'W']

mastermind(colors, length, secret_code)


"""This program's main purpose is to remove all the possible inconsistent codes,
 then makes a guess and again removes other inconsistent code. 
 Until the actual code is got"""
