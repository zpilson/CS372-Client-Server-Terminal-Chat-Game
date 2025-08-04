# CS_372: Client-Server Chat/Game (Portfolio Assignment)
# client.py
# Zachary Pilson
# pilsonz@oregonstate.edu

# imported libraries
from socket import *
from socketHelperFunctions import *
from tic_tac_toe_class import tic_tac_toe

def runClient():
    """Send first, then recv"""
    sockObj = socket(AF_INET, SOCK_STREAM)
    sockObj.connect(ADDRESS)
    print(f"Connected to: localhost, port {PORT}")
    print("Type \"/q\" to quit")
    print ("Type \"Play tic tac toe\" to start a game of tic tac toe\n")

    # Client running...
    playTicTacToe = False
    game = tic_tac_toe()
    gameStatus = None
    while True:
        # validating input
        while True:
            data_to_send = input("Enter Input > ")
            # Validating sending data when playing tic tac toe
            if playTicTacToe:
                game.startingMsg()
                print("You are player X")
                gameStatus = game.player1_move(data_to_send)
                game.printScore()
                # Re-enter move if invalid
                if gameStatus == "move was invalid": 
                    print("Move was invalid, try again!")
                # game is not over yet, keep playing
                elif gameStatus == "": 
                    break
                # game is over, end game 
                else:
                    playTicTacToe = False
                    print(gameStatus) 
                    break 
            # Validating sending data when in chat
            else:
                if len(data_to_send) > 4096:
                    print("Input exceeds 4096 bytes limit! Please rewrite all of that, but shorter")
                else:
                    break                  
        # sending data
        sendData(sockObj, data_to_send)
        # checking for key values in data to send
        if checkForQuit(data_to_send): break
        if checkForPlayTicTacToe(data_to_send): 
            playTicTacToe = True
            game.startingMsg()
            print("You are player X")
            game.printScore()
            game.printBoard()

        # receiving data
        received_data = requestData(sockObj)
        # When playing tic tac toe
        if playTicTacToe:
            game.startingMsg()
            print("You are player O")
            gameStatus = game.player2_move(received_data)
            game.printScore()
            # If game is over, stop playing
            if gameStatus != "":
                playTicTacToe = False
                print(gameStatus)
        # When in chat
        else:
            print(received_data)
        # checking for key values in received data
        if checkForQuit(received_data): break
        if checkForPlayTicTacToe(received_data): 
            playTicTacToe = True
            game.startingMsg()
            print("You are player X")
            game.printScore()
            game.printBoard()
    
    # Close sockets
    sockObj.close()


if __name__ == "__main__":
    runClient()
