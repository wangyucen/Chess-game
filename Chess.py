board = ['♜','♞','♝','♛','♚','♝','♞','♜',
         '♟','♟','♟','♟','♟','♟','♟','♟',
         '▭','▭','▭','▭','▭','▭','▭','▭',
         '▭','▭','▭','▭','♙','▭','▭','▭',
         '▭','▭','▭','▭','▭','▭','▭','▭',
         '▭','▭','▭','▭','▭','▭','▭','▭',
         '♙','♙','♙','♙','♙','♙','♙','♙',
         '♖','♘','♗','♕','♔','♗','♘','♖']
bottom_panel=['a','b','c','d','e','f','g','h']
first_column=[0,8,16,24,32,40,48,56]
last_column=[7,15,23,31,39,47,55,63]
first_row=[0,1,2,3,4,5,6,7]
last_row=[56,57,58,59,60,61,62,63]
black = ['♞','♝','♛','♚','♜','♟']
white = ['♘','♗','♕','♔','♖','♙']




board_size = 8
def print_board():
    side_panel = board_size
    for i in range(len(board)):
        if i % board_size == 0:
            print(side_panel,end=' ')
            side_panel-=1
        print(board[i],end=' ')
        if (i+1) % board_size == 0:
            print()
    print(' ',end=' ')
    for j in bottom_panel:
        print(j,end='\u2003')
    print()

#for i in range(48,56):
#    print(board[i])
def promote_pawn_white(target_pos):
    if target_pos in first_row :
        inp = input("Promotion chance for the pawn, enter y/Y to agree the pawn to be promoted: ")
        if inp.lower() == 'y':
            promotion = input("please choose what you would like the pawn to be promoted to(1.rook 2.knight 3.bishop 4.queen: ")
            if promotion == '1':
                board[target_pos]='♖'
            elif promotion == '2':
                board[target_pos]='♘'
            elif promotion == '3':
                board[target_pos]='♗'
            elif promotion == '4':
                board[target_pos]='♕'
            else:
                print("not a valid input, please try again")
        else:
            print("not a valid input, please try again")


def promote_pawn_black(target_pos):
    if target_pos in first_row :
        inp = input("Promotion chance for the pawn, enter y/Y to agree the pawn to be promoted: ")
        if inp.lower() == 'y':
            promotion = input("please choose what you would like the pawn to be promoted to(1.rook 2.knight 3.bishop 4.queen: ")
            if promotion == '1':
                board[target_pos]='♜'
            elif promotion == '2':
                board[target_pos]='♞'
            elif promotion == '3':
                board[target_pos]='♝'
            elif promotion == '4':
                board[target_pos]='♛'
            else:
                print("not a valid input, please try again")
        else:
            print("not a valid input, please try again")


def pawn_move(current_pos, target_pos,pawn):
    if pawn in white:
        isWhite = True
    else:
        isWhite = False
    if isWhite:
        if current_pos in range(48,56):
            if((target_pos - current_pos)==-8 or (target_pos-current_pos)==-16)and board[target_pos]=='▭':

                board[current_pos]='▭'
                board[target_pos]=pawn
            elif current_pos in first_column and (target_pos-current_pos)==-7 and board[target_pos]!='▭':
                board[current_pos]='▭'
                board[target_pos]=pawn
            elif current_pos in last_column and (target_pos-current_pos)==-9 and board[target_pos]!='▭':
                board[current_pos] = '▭'
                board[target_pos] = pawn
            elif (target_pos-current_pos==-9 or target_pos-current_pos==-7) and board[target_pos]!= '▭':
                board[current_pos] = '▭'
                board[target_pos] = pawn
            else:
                print("not a valid input, please try again")
        else:
            if(target_pos - current_pos)==-8 and board[target_pos]=='▭':
                board[current_pos]='▭'
                board[target_pos]=pawn
                promote_pawn_white(target_pos)
            elif current_pos in first_column and (target_pos-current_pos)==-7 and board[target_pos]!='▭':
                board[current_pos]='▭'
                board[target_pos]=pawn
                promote_pawn_white(target_pos)
            elif current_pos in last_column and (target_pos-current_pos)==-9 and board[target_pos]!='▭':
                board[current_pos] = '▭'
                board[target_pos] = pawn
                promote_pawn_white(target_pos)
            elif (target_pos - current_pos == -9 or target_pos - current_pos == -7) and board[target_pos] != '▭':
                board[current_pos] = '▭'
                board[target_pos] = pawn
                promote_pawn_white(target_pos)
            else:
                print("not a valid input, please try again")
    if not isWhite:
        if current_pos in range(8,16):

            if((target_pos - current_pos)==8 or (target_pos-current_pos)==16)and board[target_pos]=='▭':
                board[current_pos]='▭'
                board[target_pos]=pawn
            elif current_pos in first_column and (target_pos-current_pos)==7 and board[target_pos]!='▭':
                board[current_pos]='▭'
                board[target_pos]=pawn
            elif current_pos in last_column and (target_pos-current_pos)==9 and board[target_pos]!='▭':
                board[current_pos] = '▭'
                board[target_pos] = pawn
            elif (target_pos-current_pos==9 or target_pos-current_pos==7) and board[target_pos]!= '▭':
                board[current_pos] = '▭'
                board[target_pos] = pawn
            else:
                print("not a valid input, please try again")
        else:
            if(target_pos - current_pos)==8 and board[target_pos]=='▭':
                board[current_pos]='▭'
                board[target_pos]=pawn
                promote_pawn_black(target_pos)
            elif current_pos in first_column and (target_pos-current_pos)==7 and board[target_pos]!='▭':
                board[current_pos]='▭'
                board[target_pos]=pawn
                promote_pawn_black(target_pos)
            elif current_pos in last_column and (target_pos-current_pos)==9 and board[target_pos]!='▭':
                board[current_pos] = '▭'
                board[target_pos] = pawn
                promote_pawn_black(target_pos)
            elif (target_pos - current_pos == 9 or target_pos - current_pos == 7) and board[target_pos] != '▭':
                board[current_pos] = '▭'
                board[target_pos] = pawn
                promote_pawn_black(target_pos)
            else:
                print("not a valid input, please try again")

def bishop_move(current_pos, target_pos,bishop):
    if bishop in white:
        isWhite = True
    else:
        isWhite = False
    current_row,current_col = count_row_col(current_pos)
    target_row,target_col = count_row_col(target_pos)
    check_row = 0
    check_col = 0
    if current_row+current_col == target_row+target_col:
        if target_row > current_row:
            check_row = current_row+1
            check_col = current_col-1
            while check_row<target_row:
                if board[count_index(check_row,check_col)] !='▭':
                    print("not a valid input, please try again")
                    break
                check_row+=1
                check_col-=1
            else:
                if board[target_pos] in white and isWhite:
                    print("not a valid input, please try again")
                elif board[target_pos] in black and not isWhite:
                    print("not a valid input, please try again")
                else:
                    board[current_pos] = '▭'
                    board[target_pos] = bishop
        elif target_row<current_row:
            check_row = current_row-1
            check_col = current_col+1
            while check_col<target_col:
                if board[count_index(check_row,check_col)]!='▭':
                    print("not a valid input, please try again")
                    break
                check_row-=1
                check_col+=1
            else:
                if board[target_pos] in white and isWhite:
                    print("not a valid input, please try again")
                elif board[target_pos] in black and not isWhite:
                    print("not a valid input, please try again")
                else:
                    board[current_pos] = '▭'
                    board[target_pos] = bishop
    elif current_row-current_col == target_row- target_col:
        if target_row > current_row:
            check_row = current_row+1
            check_col = current_col+1
            while check_row<target_row:
                if board[count_index(check_row, check_col)] != '▭':
                    print("not a valid input, please try again")
                    break
                check_row+=1
                check_col+=1
            else:
                if board[target_pos] in white and isWhite:
                    print("not a valid input, please try again")
                elif board[target_pos] in black and not isWhite:
                    print("not a valid input, please try again")
                else:
                    board[current_pos] = '▭'
                    board[target_pos] = bishop
        if target_row < current_row:
            check_row=current_row-1
            check_col=current_col-1
            while check_row>target_row:
                if board[count_index(current_row, current_col)] != '▭':
                    print("not a valid input, please try again")
                    break
                check_row-=1
                check_col-=1
            else:
                if board[target_pos] in white and isWhite:
                    print("not a valid input, please try again")
                elif board[target_pos] in black and not isWhite:
                    print("not a valid input, please try again")
                else:
                    board[current_pos] = '▭'
                    board[target_pos] = bishop
    else:
        print("not a valid input, please try again")

def rook_move(current_pos,target_pos,rook):
    if rook in white:
        isWhite = True
    else:
        isWhite = False
    current_row, current_col = count_row_col(current_pos)
    target_row, target_col = count_row_col(target_pos)
    if target_pos // 10 == current_pos//10:
        if target_pos>current_pos:
            for i in range(current_pos+1,target_pos):
                if board[i]!= '▭':
                    print("invalid input")
                    break
            else:
                if board[target_pos] in white and isWhite:
                    print("invalid input")
                elif board[target_pos] in black and not isWhite:
                    print("invalid input")
                else:
                    board[current_pos] = '▭'
                    board[target_pos] = rook
        if target_pos<current_pos:
            for i in range(target_pos+1,current_pos):
                if board[i]!= '▭':
                    print("invalid input")
                    break
            else:
                if board[target_pos] in white and isWhite:
                    print("invalid input")
                elif board[target_pos] in black and not isWhite:
                    print("invalid input")
                else:
                    board[current_pos] = '▭'
                    board[target_pos] = rook
    elif current_col == target_col:
        if target_row>current_row:
            while target_row>current_row:
                current_row+=1
                if board[count_index(target_row,target_col)] != '▭':
                    print("invalid input")
                    break
            else:
                if board[target_pos] in white and isWhite:
                    print("not a valid input, please try again")
                elif board[target_pos] in black and not isWhite:
                    print("not a valid input, please try again")
                else:
                    board[current_pos] = '▭'
                    board[target_pos] = rook
        if target_row<current_row:
            while target_row<current_row:
                current_row-=1
                if board[count_index(target_row,target_col)] != '▭':
                    print("not a valid input, please try again")
                    break
            else:
                if board[target_pos] in white and isWhite:
                    print("not a valid input, please try again")
                elif board[target_pos] in black and not isWhite:
                    print("not a valid input, please try again")
                else:
                    board[current_pos] = '▭'
                    board[target_pos] = rook
    else:
        print("not a valid input, please try again")



def knight_move(current_pos,target_pos,knight):
    if knight in white:
        isWhite = True
    else:
        isWhite = False
    list = [current_pos-17,current_pos-10,current_pos-15,current_pos-6,
            current_pos+17,current_pos+10,current_pos+15,current_pos+6]
    if target_pos in list:
        if board[target_pos] in white and isWhite:
            print("not a valid input, please try again")
        elif board[target_pos] in black and not isWhite:
            print("not a valid input, please try again")
        else:
            board[current_pos] = '▭'
            board[target_pos] = knight

    else:
        print("not a valid input, please try again")

def queen_move(current_pos,target_pos,queen):
    if queen in white:
        isWhite = True
    else:
        isWhite = False
    current_row, current_col = count_row_col(current_pos)
    target_row, target_col = count_row_col(target_pos)
    check_row = 0
    check_col = 0
    if current_row == target_row:
        if target_pos>current_pos:
            for i in range(current_pos+1,target_pos):
                if board[i]!= '▭':
                    print("invalid input")
                    break
            else:
                if board[target_pos] in white and isWhite:
                    print("invalid input")
                elif board[target_pos] in black and not isWhite:
                    print("invalid input")
                else:
                    board[current_pos] = '▭'
                    board[target_pos] = queen
        if target_pos<current_pos:
            for i in range(target_pos+1,current_pos):
                if board[i]!= '▭':
                    print("invalid input")
                    break
            else:
                if board[target_pos] in white and isWhite:
                    print("invalid input")
                elif board[target_pos] in black and not isWhite:
                    print("invalid input")
                else:
                    board[current_pos] = '▭'
                    board[target_pos] = queen
    elif current_col == target_col:
        if target_row>current_row:
            check_row = current_row+1
            while target_row>check_row:
                if board[count_index(check_row,target_col)] != '▭':
                    print("not a valid input, please try again")
                    break
                check_row += 1
            else:
                if board[target_pos] in white and isWhite:
                    print("not a valid input, please try again")
                elif board[target_pos] in black and not isWhite:
                    print("not a valid input, please try again")
                else:
                    board[current_pos] = '▭'
                    board[target_pos] = queen
        if target_row<current_row:
            check_row = current_row-1
            while target_row<check_row:
                if board[count_index(check_row,target_col)] != '▭':
                    print("invalid input")
                    break
                check_row -= 1
            else:
                if board[target_pos] in white and isWhite:
                    print("not a valid input, please try again")
                elif board[target_pos] in black and not isWhite:
                    print("not a valid input, please try again")
                else:
                    board[current_pos] = '▭'
                    board[target_pos] = queen
    elif current_row+current_col == target_row+target_col:

        if target_row > current_row:
            check_row=current_row+1
            check_col=current_col-1
            while target_row > check_row:
                if board[count_index(check_row,check_col)] !='▭':
                    print("not a valid input, please try again")
                    break
                check_row+=1
                check_col-=1
            else:
                if board[target_pos] in white and isWhite:
                    print("not a valid input, please try again")
                elif board[target_pos] in black and not isWhite:
                    print("not a valid input, please try again")
                else:
                    board[current_pos] = '▭'
                    board[target_pos] = queen
        elif target_row < current_row:
            check_row=current_row-1
            check_col=current_col+1
            while target_row < check_row:
                if board[count_index(check_row,check_col)]!='▭':
                    print("not a valid input, please try again")
                    break
                check_row-=1
                check_col+=1
            else:
                if board[target_pos] in white and isWhite:
                    print("not a valid input, please try again")
                elif board[target_pos] in black and not isWhite:
                    print("not a valid input, please try again")
                else:
                    board[current_pos] = '▭'
                    board[target_pos] = queen
    elif current_row-current_col == target_row- target_col:
        print("yes")
        if target_row > current_row:
            check_row = current_row+1
            check_col = current_col+1
            while target_row > check_row:
                if board[count_index(check_row,check_col)] != '▭':
                    print("not a valid input, please try again")
                    break
                check_row+=1
                check_col+=1
            else:
                if board[target_pos] in white and isWhite:
                    print("not a valid input, please try again")
                elif board[target_pos] in black and not isWhite:
                    print("not a valid input, please try again")
                else:
                    board[current_pos] = '▭'
                    board[target_pos] = queen
        if target_row < current_row:
            check_row=current_row-1
            check_col=check_col-1
            while target_row<check_row:
                if board[count_index(current_row, current_col)] != '▭':
                    print("not a valid input, please try again")
                    break
                check_row-=1
                check_col-=1
            else:
                if board[target_pos] in white and isWhite:
                    print("not a valid input, please try again")
                elif board[target_pos] in black and not isWhite:
                    print("not a valid input, please try again")
                else:
                    board[current_pos] = '▭'
                    board[target_pos] = queen
    else:
        print("not a valid input, please try again")

def king_move(current_pos,target_pos,king):
    black_row, black_col = count_row_col(board.index('♚'))
    white_row, white_col = count_row_col(board.index('♔'))

    if target_pos>63 or target_pos<0:
        print("not a valid input, please try again")
    else:
        if king in white:
            isWhite = True
        else:
            isWhite = False
        list = [current_pos+1,current_pos-1,current_pos+8,current_pos-8,
                current_pos-7,current_pos-9,current_pos+7,current_pos+9]
        if black_row-1 == white_row:
            if isWhite:
                listw = [current_pos+1,current_pos-1,current_pos+8,
                current_pos+7,current_pos+9]
                if target_pos in listw:
                    if board[target_pos] in white and isWhite:
                        print("not a valid input, please try again")
                    elif board[target_pos] in black and not isWhite:
                        print("not a valid input, please try again")
                    else:
                        if check_mate(king,target_pos):
                            board[current_pos] = '▭'
                            board[target_pos] = king
                        else:
                            print("not a valid input, please try again")
            if not isWhite:
                listb =[current_pos+1,current_pos-1,current_pos-8,
                current_pos-7,current_pos-9]
                if target_pos in listb:
                    if board[target_pos] in white and isWhite:
                        print("not a valid input, please try again")
                    elif board[target_pos] in black and not isWhite:
                        print("not a valid input, please try again")
                    else:
                        if check_mate(king,target_pos):
                            board[current_pos] = '▭'
                            board[target_pos] = king
                        else:
                            print("not a valid input, please try again")
        elif target_pos in list:
            if board[target_pos] in white and isWhite:
                print("not a valid input, please try again")
            elif board[target_pos] in black and not isWhite:
                print("not a valid input, please try again")
            else:
                if check_mate(king, target_pos):
                    board[current_pos] = '▭'
                    board[target_pos] = king
                else:
                    print("not a valid input, please try again")

def check_mate(king,king_index):
    king_row,king_col = count_row_col(king_index)
    check_row = 0
    check_col = 0
    if king in white:
        isWhite = True
    else:
        isWhite = False
    #check if the king is white
    if isWhite:

        #check pawn
        pawn_list = [king_index-9,king_index-7]
        if board.index('♟') in pawn_list:
            return False
        #check knight
        knight_list = [king_index - 17, king_index - 10, king_index - 15, king_index - 6,
                king_index + 17, king_index + 10, king_index + 15, king_index + 6]
        if board.index('♞') in pawn_list:
            return False

        check_col = king_col+1
        while check_col <=7:
            if board[count_index(king_row,check_col)]!='▭':
                if board[count_index(king_row,check_col)] in white:
                    break
                elif board[count_index(king_row,check_col)] == '♛' or board[count_index(king_row,check_col)] == '♜':
                    return False
            check_col+=1
        check_col = king_col-1
        while check_col >=0:
            if board[count_index(king_row,check_col)]!='▭':
                if board[count_index(king_row,check_col)] in white:
                    break
                elif board[count_index(king_row,check_col)] == '♛' or board[count_index(king_row,check_col)] == '♜':
                    return False
            check_col-=1
        check_row = king_row+1
        while check_row<=7:
            if board[count_index(check_row,king_col)]!='▭':
                if board[count_index(check_row,king_col)] in white:
                    break
                elif board[count_index(check_row,king_col)] =='♛' or board[count_index(check_row,king_col)] =='♜':
                    return False
            check_row+=1
        check_row = king_row-1
        while check_row>=0:
            if board[count_index(check_row,king_col)]!='▭':
                if board[count_index(check_row,king_col)] in white:
                    break
                elif board[count_index(check_row,king_col)] =='♛' or board[count_index(check_row,king_col)] =='♜':
                    return False
            check_row-=1
        #check diagonally
        check_row = king_row-1
        check_col = king_col+1

        while check_row>=0 and check_col<=7:
            if board[count_index(check_row,check_col)]!='▭':
                if board[count_index(check_row,check_col)] in white:
                    break
                elif board[count_index(check_row,check_col)] =='♝'or board[count_index(check_row,check_col)]=='♛':
                    return False
            check_row -=1
            check_col +=1

        check_row = king_row-1
        check_col = king_col-1
        while check_row>=0 and check_col>=0:
            if board[count_index(check_row,check_col)]!='▭':
                if board[count_index(check_row,check_col)] in white:
                    break
                elif board[count_index(check_row,check_col)] =='♝'or board[count_index(check_row,check_col)]=='♛':
                    return False
            check_row -= 1
            check_col -= 1
        check_row =king_row+1
        check_col =king_col-1
        while check_row<=7 and check_col>=0:
            if board[count_index(check_row, check_col)] != '▭':
                if board[count_index(check_row, check_col)] in white:
                    break
                elif board[count_index(check_row,check_col)] =='♝'or board[count_index(check_row,check_col)]=='♛':
                    return False
            check_row += 1
            check_col -= 1
        check_row = king_row+1
        check_col = king_col+1
        while check_row<=7 and check_col<=7:
            if board[count_index(check_row, check_col)] != '▭':
                if board[count_index(check_row, check_col)] in white:
                    break
                elif board[count_index(check_row,check_col)] =='♝'or board[count_index(check_row,check_col)]=='♛':
                    return False
            check_row += 1
            check_col += 1
        return True
    #check if the king is black
    if not isWhite:
        #check pawn
        pawn_list = [king_index+9,king_index+7]
        if board.index('♙') in pawn_list:
            return False
        #check knight
        knight_list = [king_index - 17, king_index - 10, king_index - 15, king_index - 6,
                king_index + 17, king_index + 10, king_index + 15, king_index + 6]
        if board.index('♘') in pawn_list:
            return False
        check_col = king_col+1
        while check_col <=7:
            if board[count_index(king_row,check_col)]!='▭':
                if board[count_index(king_row,check_col)] in white:
                    break
                elif board[count_index(king_row,check_col)] == '♕' or board[count_index(king_row,check_col)]=='♖':
                    return False
            check_col+=1
        check_col = king_col-1
        while check_col >=0:
            if board[count_index(king_row,check_col)]!='▭':
                if board[count_index(king_row,check_col)] in white:
                    break
                elif board[count_index(king_row,check_col)] == '♕' or board[count_index(king_row,check_col)]=='♖':
                    return False
            check_col-=1
        check_row = king_row+1
        while check_row<=7:
            if board[count_index(check_row,king_col)]!='▭':
                if board[count_index(check_row,king_col)] in white:
                    break
                elif board[count_index(check_row,king_col)] =='♕' or board[count_index(check_row,king_col)]=='♖':
                    return False
            check_row+=1
        check_row = king_row-1
        while check_row>=0:
            if board[count_index(check_row,king_col)]!='▭':
                if board[count_index(check_row,king_col)] in white:
                    break
                elif board[count_index(check_row,king_col)] =='♕' or board[count_index(check_row,king_col)]=='♖':
                    return False
            check_row-=1
        #check diagonally
        check_row = king_row-1
        check_col = king_col+1
        while check_row>=0 and check_col<=7:
            if board[count_index(check_row,check_col)]!='▭':
                if board[count_index(check_row,check_col)] in white:
                    break
                elif board[count_index(check_row,check_col)] =='♗'or board[count_index(check_row,check_col)] =='♕':
                    return False
            check_row -=1
            check_col +=1

        check_row = king_row-1
        check_col = king_col-1
        while check_row>=0 and check_col>=0:
            if board[count_index(check_row,check_col)]!='▭':
                if board[count_index(check_row,check_col)] in white:
                    break
                elif board[count_index(check_row,check_col)] =='♗'or board[count_index(check_row,check_col)] =='♕':
                    return False
            check_row -= 1
            check_col -= 1
        check_row =king_row+1
        check_col =king_col-1
        while check_row<=7 and check_col>=0:
            if board[count_index(check_row, check_col)] != '▭':
                if board[count_index(check_row, check_col)] in white:
                    break
                elif board[count_index(check_row, check_col)] == '♗' or board[count_index(check_row, check_col)] =='♕':
                    return False
            check_row += 1
            check_col -= 1
        check_row = king_row+1
        check_col = king_col+1
        while check_row<=7 and check_col<=7:
            if board[count_index(check_row, check_col)] != '▭':
                if board[count_index(check_row, check_col)] in white:
                    break
                elif board[count_index(check_row, check_col)] == '♗' or board[count_index(check_row, check_col)] =='♕':
                    return False
            check_row += 1
            check_col += 1
        return True

def count_row_col(index):
    row = index // board_size
    col = index-(index//board_size)*board_size
    return  row,col
def count_index(row,col):
    return (((row+1)-1)*board_size + (col+1))-1

print(count_index(4,6))
#print(count_row_col(60))
blackKing_check = False
whiteKing_check = False
en_passant_white_pos = 0
en_passant_black_pos = 0
print("<<<<<<Chess Game>>>>>>")
print_board()

while True:
#White player
    if blackKing_check:
        print("Game Over, white player win!!")
        break
    repeat_white = True
    while repeat_white:
        playerPosition = input("White turn,Please insert a valid chess position you wanna move(eg.a2): ")
        current_col_number = bottom_panel.index(playerPosition[-2])
        current_row_number = board_size-int(playerPosition[-1])
#    print(row_number,col_number)
        currentPlayerPosition = count_index(current_row_number,current_col_number)
#    print(currentPlayerPosition)
        playerPosition = input("What is the desired position you would like to move to: ")
        target_col_number = bottom_panel.index(playerPosition[-2])
        target_row_number = board_size-int(playerPosition[-1])
        targetPlayerPosition = count_index(target_row_number,target_col_number)
#    print(targetPlayerPosition)

        if board[currentPlayerPosition]=='♙':
            temp = board.copy()
            if (currentPlayerPosition in first_column) and current_row_number==3 and currentPlayerPosition+1==en_passant_black_pos and targetPlayerPosition==17:
                board[currentPlayerPosition+1]='▭'
                board[currentPlayerPosition]='▭'
                board[targetPlayerPosition]='♙'
            elif (currentPlayerPosition in last_column) and current_row_number==3 and currentPlayerPosition-1==en_passant_black_pos and targetPlayerPosition==22:
                board[currentPlayerPosition-1]='▭'
                board[currentPlayerPosition]='▭'
                board[targetPlayerPosition]='♙'
            elif currentPlayerPosition-1==en_passant_black_pos and currentPlayerPosition-1-8 == targetPlayerPosition:
                board[currentPlayerPosition-1]='▭'
                board[currentPlayerPosition]='▭'
                board[targetPlayerPosition]='♙'
            elif currentPlayerPosition+1==en_passant_black_pos and currentPlayerPosition+1-8 == targetPlayerPosition:
                board[currentPlayerPosition+1]='▭'
                board[currentPlayerPosition]='▭'
                board[targetPlayerPosition]='♙'
            else:
                pawn_move(currentPlayerPosition, targetPlayerPosition, '♙')
                if current_row_number == 6 and target_row_number == 4:
                    en_passant_white_pos= targetPlayerPosition


            if temp != board:
                repeat_white = False
            else:
                continue
            print_board()
            if not check_mate('♚',board.index('♚')):
                blackKing_check = True
                print("The black king gets into check!")
        elif board[currentPlayerPosition]=='♖':
            temp = board.copy()

            rook_move(currentPlayerPosition,targetPlayerPosition,'♖')
            if temp != board:
                repeat_white = False
            else:
                continue
            print_board()
            if not check_mate('♚',board.index('♚')):
                blackKing_check = True
                print("The black king gets into check!")
        elif board[currentPlayerPosition]=='♘':
            temp = board.copy()
            knight_move(currentPlayerPosition,targetPlayerPosition,'♘')
            if temp != board:
                repeat_white = False
            else:
                continue
            print_board()
            if not check_mate('♚',board.index('♚')):
                blackKing_check = True
                print("The black king gets into check!")
        elif board[currentPlayerPosition]=='♗':
            temp = board.copy()
            bishop_move(currentPlayerPosition,targetPlayerPosition,'♗')
            if temp != board:
                repeat_white = False
            else:
                continue
            print_board()
            if not check_mate('♚',board.index('♚')):
                blackKing_check = True
                print("The black king gets into check!")
        elif board[currentPlayerPosition]=='♔':
            temp = board.copy()
            king_move(currentPlayerPosition,targetPlayerPosition,'♔')
            if temp != board:
                repeat_white = False
            else:
                continue
            print_board()
            if not check_mate('♚',board.index('♚')):
                blackKing_check = True
                print("The black king gets into check!")
        elif board[currentPlayerPosition]=='♕':
            temp = board.copy()
            queen_move(currentPlayerPosition,targetPlayerPosition,'♕')
            if temp != board:
                repeat_white = False
            else:
                continue
            print_board()
            if not check_mate('♚',board.index('♚')):
                blackKing_check = True
                print("The black king gets into check!")
        else:
            print("not a valid input, please try again")
    en_passant_black_pos=0
    if check_mate('♔',board.index('♔')):
        whiteKing_check = False

#Black player

    if whiteKing_check:
        print("Game Over, black player win!!")
        break
    repeat_black = True
    while repeat_black:
        playerPosition = input("Black turn,Please insert a valid chess position you wanna move(eg.a2): ")
        current_col_number = bottom_panel.index(playerPosition[-2])
        current_row_number = board_size-int(playerPosition[-1])

        currentPlayerPosition = count_index(current_row_number,current_col_number)
        playerPosition = input("What is the target position you would like to move to: ")
        target_col_number = bottom_panel.index(playerPosition[-2])
        target_row_number = board_size-int(playerPosition[-1])
        targetPlayerPosition = count_index(target_row_number,target_col_number)

        if board[currentPlayerPosition]=='♟':
            temp = board.copy()
            if (currentPlayerPosition in first_column) and current_row_number==4 and currentPlayerPosition+1==en_passant_white_pos and targetPlayerPosition==33:
                board[currentPlayerPosition+1]='▭'
                board[currentPlayerPosition]='▭'
                board[targetPlayerPosition]='♟'
            elif (currentPlayerPosition in last_column) and current_row_number==4 and currentPlayerPosition-1==en_passant_white_pos and targetPlayerPosition==38:
                board[currentPlayerPosition-1]='▭'
                board[currentPlayerPosition]='▭'
                board[targetPlayerPosition]='♟'
            elif currentPlayerPosition-1==en_passant_white_pos and currentPlayerPosition-1+8 == targetPlayerPosition:
                board[currentPlayerPosition-1]='▭'
                board[currentPlayerPosition]='▭'
                board[targetPlayerPosition]='♟'
            elif currentPlayerPosition+1==en_passant_white_pos and currentPlayerPosition+1+8 == targetPlayerPosition:
                board[currentPlayerPosition+1]='▭'
                board[currentPlayerPosition]='▭'
                board[targetPlayerPosition]='♟'
            else:
                pawn_move(currentPlayerPosition,targetPlayerPosition,'♟')
                if current_row_number == 1 and target_row_number == 3:
                    en_passant_black_pos = targetPlayerPosition

            if temp != board:
                repeat_black = False
            else:
                continue
            print_board()
            if not check_mate('♔',board.index('♔')):
                whiteKing_check = True
                print("The white king gets into check!")
        elif board[currentPlayerPosition]=='♜':
            temp = board.copy()


            rook_move(currentPlayerPosition,targetPlayerPosition,'♜')
            if temp != board:
                repeat_black = False
            else:
                continue
            print_board()
            if not check_mate('♔',board.index('♔')):
                whiteKing_check = True
                print("The white king gets into check!")
        elif board[currentPlayerPosition]=='♞':
            temp = board.copy()
            knight_move(currentPlayerPosition,targetPlayerPosition,'♞')
            if temp != board:
                repeat_black = False
            else:
                continue
            print_board()
            if not check_mate('♔',board.index('♔')):
                whiteKing_check = True
                print("The white king gets into check!")
        elif board[currentPlayerPosition]=='♝':
            temp = board.copy()
            bishop_move(currentPlayerPosition,targetPlayerPosition,'♝')
            if temp != board:
                repeat_black = False
            else:
                continue
            print_board()
            if not check_mate('♔',board.index('♔')):
                whiteKing_check = True
                print("The white king gets into check!")
        elif board[currentPlayerPosition]=='♚':
            temp = board.copy()
            king_move(currentPlayerPosition,targetPlayerPosition,'♚')
            if temp != board:
                repeat_black = False
            else:
                continue
            print_board()
            if not check_mate('♔',board.index('♔')):
                whiteKing_check = True
                print("The white king gets into check!")
        elif board[currentPlayerPosition]=='♛':
            temp = board.copy()
            queen_move(currentPlayerPosition,targetPlayerPosition,'♛')
            if temp != board:
                repeat_black = False
            else:
                continue
            print_board()
            if not check_mate('♔',board.index('♔')):
                whiteKing_check = True
                print("The white king gets into check!")
        else:
            print("not a valid input,please try again")
    en_passant_white_pos=0
    if check_mate('♚',board.index('♚')):
        blackKing_check = False



