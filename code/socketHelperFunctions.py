# CS_372: Client-Server Chat/Game (Portfolio Assignment)
# socketHelperFunctions.py
# Zachary Pilson
# pilsonz@oregonstate.edu

# Constants
LOCAL_HOST = '127.0.0.1'
PORT = 4321
ADDRESS = (LOCAL_HOST, PORT)
SIZE = 1024

def requestData(sockObj):
    """requests data from the client until password is received at end of transmit"""
    # recieves data in segments of up to 1024 bytes at a time
    # stops receiving data when "password:abZr12410f@#$"" is found
    total_received_data = ""
    while True:
        total_received_data += sockObj.recv(SIZE).decode("UTF-8")
        if total_received_data[-22:] == "password:abZr12410f@#$": break
    return total_received_data[:-22]

def sendData(sockObj, data):
    sockObj.send((data + "password:abZr12410f@#$").encode("UTF-8"))

def checkForQuit(data):
    if data == "/q":
        print("Shut down keyword detected: Server is closing...")
        return True
    return False

def checkForPlayTicTacToe(data):
    if data.upper() == "PLAY TIC TAC TOE":
        return True
    return False
    