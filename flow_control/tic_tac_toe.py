
#TODO MOSTRAR TABLERO CADA VEZ E IR ACUTALIZANDO CADA MOVIMEINTO, COMPROBACIONES DE RANGOS, EXCEPCIONES
def get_player():
    '''el jugador escoge el símbolo'''
    symbol_valid = False
    print("WELCOME TO TIC TAC TOE :D")
    while not symbol_valid:

        player1_symbol = input("Please choose ur symbol (O or X)").upper()
        if player1_symbol != 'X' and player1_symbol != 'O':
            print("Please enter a valid symbol:/")
            symbol_valid = False
        elif player1_symbol == 'X':
            player2_symbol = 'O'
            symbol_valid = True
        else:
            player2_symbol='X'
            symbol_valid = True

    return player2_symbol, player2_symbol
    
def start_game():
    
    gameOver= False
    players = get_player() 
    player1 = players[0]
    player2 = players[1]
    board = init_board()
    num_cols = len(board[0]) 
    current_player=player1
    while not gameOver:

        print(f"PLAYER {current_player} IS UR TURN:)")
        number_move = int(input("Pick a spot (1-9): "))
        row = (number_move-1) // num_cols
        col = (number_move-1) % num_cols 

        #comprobamos que el numeor qu eesochio ya no este usado
        if board[row][col] == 0:
             board[row][col] = current_player
        else: 
            #hacer while de que vuelva intentarlo
            print("This spot is not empty:/")

        game_status= check_winner(board)
        if game_status !=None:
           
            if game_status == "DRAW":
                print("IT'S A DRAW!")
            else:
                print(f"CONGRATULATIONS PLAYER {game_status}!!")
            
            gameOver = True
        
        if current_player == player1:
            current_player = player2
        else:
            current_player = player1

        print("PLAYER 2 IS UR TURN:)")
        number_move = int(input("Pick a spot;) player2"))
        row = (number_move-1)// num_cols
        col = (number_move-1)% num_cols
        board[row][col]= player2

        return 9
    

    
    
def check_winner(board):

    #chequeo primero las diagoanles
    diagonal_1 = (board[0][0] == board[1][1] and board[1][1] == board[2][2])
    diagonal_2 = (board[0][2] == board[1][1] and board[1][1] == board[2][0])
    if (diagonal_1 or diagonal_2) and board[1][1] != 0:
        return board[1][1]
    
    #fooorma laaarga
    # if (board[0][0]==board[1][1] and board[1][1]== board[2][2]) or (board[0][2]==board[1][1] and board[2][0]) and board[1][1]!=0:
    #     return board[0][0]
    #comprobamos las filas 

    for i in range(len(board)):
        if board[i][0]==board[i][1] and board[i][1] == board[i][2] and board[i][0]!=0:
            return board[i][0]
        
    #comprob col 

    for j in range(len(board[0])):
        # tb pse podria meter la condicion y guardar una varibale ahi de esta forma:D
        col_win = (board[0][j] == board[1][j] and 
                            board[1][j] == board[2][j])
        
        not_empty = board[0][j] != 0
        
        if col_win and not_empty:
            return board[0][j] 
    # si llega hasta significa que no hay ganador entoces 

    is_full=True
    for row in board:
        if 0 in row:
            is_full = False
            break

    if is_full:
        return "DRAW:|"
    
    return None # sigue aca ya que ay todavia 0 en el tqablero:)
    
def show_board():

    return 

def init_board():
    '''Restablece los valores de la tabla de jeugo:D'''
    # lo relleno con 0 o le pongo los numeros para que el uusario sepa q casilla¿??
    return [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]


