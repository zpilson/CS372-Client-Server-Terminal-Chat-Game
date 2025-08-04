# CS_372: Client-Server Chat/Game (Portfolio Assignment)
# server.py
# Zachary Pilson
# pilsonz@oregonstate.edu

# imported libraries
from socket import *
from socketHelperFunctions import *
from tic_tac_toe_class import tic_tac_toe

def runSever():
    """Recv first, then send"""
    # Creates, binds, and then listens for client activity
    sockObj = socket(AF_INET, SOCK_STREAM)
    sockObj.bind(ADDRESS)
    sockObj.listen()
    print(f"Server listening on: localhost, port {PORT}")

    # Awaiting to accept clients
    clientConnection, clientAddr = sockObj.accept()
    print("Client connected from address:", clientAddr)
    print("Type \"/q\" to quit")
    print ("Type \"Play tic tac toe\" to start a game of tic tac toe")
    print("Waiting for message....\n")

    # Server running...
    playTicTacToe = False
    game = tic_tac_toe()
    while True:
        # receiving data
        received_data = requestData(clientConnection)
        # When playing tic tac toe
        if playTicTacToe:
            game.startingMsg()
            print("You are player O")
            gameStatus = game.player1_move(received_data)
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
            print("You are player O")
            game.printScore()
            game.printBoard()

        # validating input before sending
        while True:
            data_to_send = input("Enter Input > ")
            # Validating sending data when playing tic tac toe
            if playTicTacToe:
                game.startingMsg()
                print("You are player O")
                gameStatus = game.player2_move(data_to_send)
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
        sendData(clientConnection, data_to_send)
        # checking for key values in data_to_send
        if checkForQuit(data_to_send): break
        if checkForPlayTicTacToe(data_to_send): 
            playTicTacToe = True
            game.startingMsg()
            print("You are player O")
            game.printScore()
            game.printBoard()

    # Close sockets
    clientConnection.close()
    sockObj.close()


if __name__ == "__main__":
    runSever()
