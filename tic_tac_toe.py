"""
Student: Mark Hammer
Instructor: Bro. Parrish
Course: CSE 210
Semester: Spring 2022
Assignment: Tic-Tac-Toe Game
"""
# Import section
import os
import platform

# Define main function
def main():
    # Clear terminal with clear_term function
    clear_term()
   
    # Print welcome message and a blank line
    print(f"Hello and welcome to the Tic-Tac-Toe game!")
    print()

    # Create the board then displey the board followed by a blank line
    squares = create_squares()
    create_board(squares)

    # Default variable
    player = "x"
    turn = 1

    # Play the game
    while not winner(squares):
        # Asks player to move
        get_move(player, squares)

        # Figure out whose turn is next
        player = next_turn(player)

        # Display the board
        create_board(squares)

        # Determine draw by counting turns
        turn += 1
        if turn == 10:
            print(f"You played to a draw, better luck next time.")
            print()
            break
    
        # Display final board    
    create_board(squares)
    print()

    # Displey message to the winner
    if winner(squares):
        player = next_turn(player)
        print(f"Congrats to player {player} for winning!")
        
    print()

# Define clear_term function
def clear_term():
    """
    This function determins what operating system is running and clears the terminal before running the rest of the program
    Parameters: None
    Returns: None
    """
    # Use platform.system() method to determine OS
    op_sys = platform.system()

    # Based on platform.system() clear terminal
    if op_sys.lower() == "linux":
        os.system("clear")
    elif op_sys.lower() == "windows":
        os.system("cls")
    elif op_sys.lower() == "darwin":
        os.system("clear")

# Define create_squares function
def create_squares():
    """
    This function will create a list that contains the numbers 1 through 9
    parameter: none
    returns: squares
    """
    # Create squares list
    squares = []

    # Populate squares list
    for i in range (9):
        squares.append(i+1)
    return squares

# Define create_board function
def create_board(list):
    """
    This function will display the default tic tac toe board before any moves are made
    parameters: none
    returns: nothing
    """
    print(f"{list[0]}|{list[1]}|{list[2]}")
    print(f"-+-+-")
    print(f"{list[3]}|{list[4]}|{list[5]}")
    print(f"-+-+-")
    print(f"{list[6]}|{list[7]}|{list[8]}")
    print()

# Define winner function
def winner(squares):
    """
    This function holds the positions of all possible winning solutions
    parameters: squares
    return: True or False
    """
    if (squares[0] == squares[1] == squares[2] or
        squares[3] == squares[4] == squares[5] or
        squares[6] == squares[7] == squares[8] or
        squares[0] == squares[3] == squares[6] or
        squares[1] == squares[4] == squares[7] or
        squares[2] == squares[5] == squares[8] or
        squares[0] == squares[4] == squares[8] or
        squares[2] == squares[4] == squares[6]):
        return True
    else:
        return False

# Define get_move functin
def get_move(player, squares):
    """
    This function executes the game by asking each player to move
    parameters:
        player: x or o
        squares: the game board
    returns: nothing
    """
    print()
    move = int(input(f"It's {player}'s turn. Please choose your square (1 - 9): "))
    squares[move -1] = player
    print()

# Define next_turn function
def next_turn(player):
    """
    This function determins whose turn it is next
    parameters: player
    returns: player
    """
    if player == "x":
        player = "o"
        return player
    elif player == "o":
        player = "x"
        return player

# Run the program
if __name__ == "__main__":
    main()