board = ['♜','♞','♝','♛','♚','♝','♞','♜',
         '♟','♟','♟','♟','♟','♟','♟','♟',
         '▭','▭','▭','▭','▭','▭','▭','▭',
         '▭','▭','▭','▭','▭','▭','▭','▭',
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
                boardp[target_pos]='♕'
            else:
                print("invalid input")
        else:
            print("invalid input")

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
                boardp[target_pos]='♛'
            else:
                print("invalid input")
        else:
            print("invalid input")


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
                print("not a valid input")
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
                print("not a valid input")
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
                print("not a valid input")
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
                print("not a valid input")

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
                    print("not a valid input")
                    break
                check_row+=1
                check_col-=1
            else:
                if board[target_pos] in white and isWhite:
                    print("not a valid input")
                elif board[target_pos] in black and not isWhite:
                    print("not a valid input")
                else:
                    board[current_pos] = '▭'
                    board[target_pos] = bishop
        elif target_row<current_row:
            check_row = current_row-1
            check_col = current_col+1
            while check_col<target_col:
                if board[count_index(check_row,check_col)]!='▭':
                    print("not a valid input")
                    break
                check_row-=1
                check_col+=1
            else:
                if board[target_pos] in white and isWhite:
                    print("not a valid input")
                elif board[target_pos] in black and not isWhite:
                    print("not a valid input")
                else:
                    board[current_pos] = '▭'
                    board[target_pos] = bishop
    elif current_row-current_col == target_row- target_col:
        if target_row > current_row:
            check_row = current_row+1
            check_col = current_col+1
            while check_row<target_row:
                if board[count_index(check_row, check_col)] != '▭':
                    print("not a valid input")
                    break
                check_row+=1
                check_col+=1
            else:
                if board[target_pos] in white and isWhite:
                    print("not a valid input")
                elif board[target_pos] in black and not isWhite:
                    print("not a valid input")
                else:
                    board[current_pos] = '▭'
                    board[target_pos] = bishop
        if target_row < current_row:
            check_row=current_row-1
            check_col=current_col-1
            while check_row>target_row:
                if board[count_index(current_row, current_col)] != '▭':
                    print("not a valid input")
                    break
                check_row-=1
                check_col-=1
            else:
                if board[target_pos] in white and isWhite:
                    print("not a valid input")
                elif board[target_pos] in black and not isWhite:
                    print("not a valid input")
                else:
                    board[current_pos] = '▭'
                    board[target_pos] = bishop
    else:
        print("not a valid input")

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
                    print("not a valid input")
                elif board[target_pos] in black and not isWhite:
                    print("not a valid input")
                else:
                    board[current_pos] = '▭'
                    board[target_pos] = rook
        if target_row<current_row:
            while target_row<current_row:
                current_row-=1
                if board[count_index(target_row,target_col)] != '▭':
                    print("invalid input")
                    break
            else:
                if board[target_pos] in white and isWhite:
                    print("not a valid input")
                elif board[target_pos] in black and not isWhite:
                    print("not a valid input")
                else:
                    board[current_pos] = '▭'
                    board[target_pos] = rook
    else:
        print("not a valid input")



def knight_move(current_pos,target_pos,knight):
    if knight in white:
        isWhite = True
    else:
        isWhite = False
    list = [current_pos-17,current_pos-10,current_pos-15,current_pos-6,
            current_pos+17,current_pos+10,current_pos+15,current_pos+6]
    if target_pos in list:
        if board[target_pos] in white and isWhite:
            print("not a valid input")
        elif board[target_pos] in black and not isWhite:
            print("not a valid input")
        else:
            board[current_pos] = '▭'
            board[target_pos] = knight

    else:
        print("not a valid input")

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
                    print("invalid input")
                    break
                check_row += 1
            else:
                if board[target_pos] in white and isWhite:
                    print("not a valid input")
                elif board[target_pos] in black and not isWhite:
                    print("not a valid input")
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
                    print("not a valid input")
                elif board[target_pos] in black and not isWhite:
                    print("not a valid input")
                else:
                    board[current_pos] = '▭'
                    board[target_pos] = queen
    elif current_row+current_col == target_row+target_col:

        if target_row > current_row:
            check_row=current_row+1
            check_col=current_col-1
            while target_row > check_row:
                if board[count_index(check_row,check_col)] !='▭':
                    print("not a valid input")
                    break
                check_row+=1
                check_col-=1
            else:
                if board[target_pos] in white and isWhite:
                    print("not a valid input")
                elif board[target_pos] in black and not isWhite:
                    print("not a valid input")
                else:
                    board[current_pos] = '▭'
                    board[target_pos] = queen
        elif target_row < current_row:
            check_row=current_row-1
            check_col=current_col+1
            while target_row < check_row:
                if board[count_index(check_row,check_col)]!='▭':
                    print("not a valid input")
                    break
                check_row-=1
                check_col+=1
            else:
                if board[target_pos] in white and isWhite:
                    print("not a valid input")
                elif board[target_pos] in black and not isWhite:
                    print("not a valid input")
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
                    print("not a valid input")
                    break
                check_row+=1
                check_col+=1
            else:
                if board[target_pos] in white and isWhite:
                    print("not a valid input")
                elif board[target_pos] in black and not isWhite:
                    print("not a valid input")
                else:
                    board[current_pos] = '▭'
                    board[target_pos] = queen
        if target_row < current_row:
            check_row=current_row-1
            check_col=check_col-1
            while target_row<check_row:
                if board[count_index(current_row, current_col)] != '▭':
                    print("not a valid input")
                    break
                check_row-=1
                check_col-=1
            else:
                if board[target_pos] in white and isWhite:
                    print("not a valid input")
                elif board[target_pos] in black and not isWhite:
                    print("not a valid input")
                else:
                    board[current_pos] = '▭'
                    board[target_pos] = queen
    else:
        print("not a valid input")

def king_move(current_pos,target_pos,king):
    black_row, black_col = count_row_col(board.index('♚'))
    white_row, white_col = count_row_col(board,index('♔'))

    if target_pos>63 or target_pos<0:
        print("not a valid input")
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
                        print("not a valid input")
                    elif board[target_pos] in black and not isWhite:
                        print("not a valid input")
                    else:
                        if check_mate(king,target_pos):
                            board[current_pos] = '▭'
                            board[target_pos] = king
                        else:
                            print("not a valid input")
            if not isWhite:
                listb =[current_pos+1,current_pos-1,current_pos-8,
                current_pos-7,current_pos-9]
                if target_pos in listb:
                    if board[target_pos] in white and isWhite:
                        print("not a valid input")
                    elif board[target_pos] in black and not isWhite:
                        print("not a valid input")
                    else:
                        if check_mate(king,target_pos):
                            board[current_pos] = '▭'
                            board[target_pos] = king
                        else:
                            print("not a valid input")
        elif target_pos in list:
            if board[target_pos] in white and isWhite:
                print("not a valid input")
            elif board[target_pos] in black and not isWhite:
                print("not a valid input")
            else:
                if check_mate(king, target_pos):
                    board[current_pos] = '▭'
                    board[target_pos] = king
                else:
                    print("not a valid input")

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

#print(count_index(0,6))
#print(count_row_col(60))
blackKing_check = False
whiteKing_check = False

print_board()
while True:
#White player
    if blackKing_check == True:
        print("Game Over, white player win!!")
        break
    playerPosition = input("White turn,Please insert a valid chess position you wanna move(eg.a2): ")
    col_number = bottom_panel.index(playerPosition[-2])
    row_number = board_size-int(playerPosition[-1])
#    print(row_number,col_number)
    currentPlayerPosition = count_index(row_number,col_number)
#    print(currentPlayerPosition)
    playerPosition = input("What is the target position you would like to move to: ")
    col_number = bottom_panel.index(playerPosition[-2])
    row_number = board_size-int(playerPosition[-1])
    targetPlayerPosition = count_index(row_number,col_number)
#    print(targetPlayerPosition)

    if board[currentPlayerPosition]=='♙':
        pawn_move(currentPlayerPosition,targetPlayerPosition,'♙')
        print_board()
        if not check_mate('♚',board.index('♚')):
            blackKing_check = True
            print("The black king is being checked!")
    elif board[currentPlayerPosition]=='♖':
        rook_move(currentPlayerPosition,targetPlayerPosition,'♖')
        print_board()
        if not check_mate('♚',board.index('♚')):
            blackKing_check = True
            print("The black king is being checked!")
    elif board[currentPlayerPosition]=='♘':
        knight_move(currentPlayerPosition,targetPlayerPosition,'♘')
        print_board()
        if not check_mate('♚',board.index('♚')):
            blackKing_check = True
            print("The black king is being checked!")
    elif board[currentPlayerPosition]=='♗':
        bishop_move(currentPlayerPosition,targetPlayerPosition,'♗')
        print_board()
        if not check_mate('♚',board.index('♚')):
            blackKing_check = True
            print("The black king is being checked!")
    elif board[currentPlayerPosition]=='♔':
        king_move(currentPlayerPosition,targetPlayerPosition,'♔')
        print_board()
        if not check_mate('♚',board.index('♚')):
            blackKing_check = True
            print("The black king is being checked!")
    elif board[currentPlayerPosition]=='♕':
        queen_move(currentPlayerPosition,targetPlayerPosition,'♕')
        print_board()
        if not check_mate('♚',board.index('♚')):
            blackKing_check = True
            print("The black king is being checked!")
    else:
        print("not a valid input")
    if check_mate('♔',board.index('♔')):
        whiteKing_check=False
#Black player
    if whiteKing_check == True:
        print("Game Over, black player win!!")
        break
    playerPosition = input("Black turn,Please insert a valid chess position you wanna move(eg.a2): ")
    col_number = bottom_panel.index(playerPosition[-2])
    row_number = board_size-int(playerPosition[-1])

    currentPlayerPosition = count_index(row_number,col_number)
    playerPosition = input("What is the target position you would like to move to: ")
    col_number = bottom_panel.index(playerPosition[-2])
    row_number = board_size-int(playerPosition[-1])
    targetPlayerPosition = count_index(row_number,col_number)

    if board[currentPlayerPosition]=='♟':

        pawn_move(currentPlayerPosition,targetPlayerPosition,'♟')
        print_board()

        if not check_mate('♔',board.index('♔')):
            whiteKing_check = True
            print("The white king is being checked!")
    elif board[currentPlayerPosition]=='♜':
        rook_move(currentPlayerPosition,targetPlayerPosition,'♜')
        print_board()
        if not check_mate('♔',board.index('♔')):
            whiteKing_check = True
            print("The white king is being checked!")
    elif board[currentPlayerPosition]=='♞':
        knight_move(currentPlayerPosition,targetPlayerPosition,'♞')
        print_board()
        if not check_mate('♔',board.index('♔')):
            whiteKing_check = True
            print("The white king is being checked!")
    elif board[currentPlayerPosition]=='♝':
        bishop_move(currentPlayerPosition,targetPlayerPosition,'♝')
        print_board()
        if not check_mate('♔',board.index('♔')):
            whiteKing_check = True
            print("The white king is being checked!")
    elif board[currentPlayerPosition]=='♚':
        king_move(currentPlayerPosition,targetPlayerPosition,'♚')
        print_board()
        if not check_mate('♔',board.index('♔')):
            whiteKing_check = True
            print("The white king is being checked!")
    elif board[currentPlayerPosition]=='♛':
        queen_move(currentPlayerPosition,targetPlayerPosition,'♛')
        print_board()
        if not check_mate('♔',board.index('♔')):
            whiteKing_check = True
            print("The white king is being checked!")
    else:
        print("not a valid input")
    if check_mate('♚',board.index('♚')):
        blackKing_check=False



