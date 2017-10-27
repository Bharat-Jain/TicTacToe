import numpy
arr = numpy.array([-1,-1,-1,-1,-1,-1,-1,-1,-1,]).reshape((3,3))


def manage_input(i_o,player):
    if player == "pl1":
        if i_o == 1 and arr[0][0]==(-1):
            arr[0][0]=1
        elif i_o == 2 and arr[0][1]==(-1):
            arr[0][1]=1
        elif i_o == 3 and arr[0][2]==(-1):
            arr[0][2]=1
        elif i_o == 4 and arr[1][0]==(-1):
            arr[1][0]=1
        elif i_o == 5 and arr[1][1]==(-1):
            arr[1][1]=1
        elif i_o == 6 and arr[1][2]==(-1):
            arr[1][2]=1
        elif i_o == 7 and arr[2][0]==(-1):
            arr[2][0]=1
        elif i_o == 8 and arr[2][1]==(-1):
            arr[2][1]=1
        elif i_o == 9 and arr[2][2]==(-1):
            arr[2][2]=1
    elif player == "pl2":
        if i_o == 1 and arr[0][0]==(-1):
            arr[0][0]=0
        elif i_o == 2 and arr[0][1]==(-1):
            arr[0][1]=0
        elif i_o == 3 and arr[0][2]==(-1):
            arr[0][2]=0
        elif i_o == 4 and arr[1][0]==(-1):
            arr[1][0]=0
        elif i_o == 5 and arr[1][1]==(-1):
            arr[1][1]=0
        elif i_o == 6 and arr[1][2]==(-1):
            arr[1][2]=0
        elif i_o == 7 and arr[2][0]==(-1):
            arr[2][0]=0
        elif i_o == 8 and arr[2][1]==(-1):
            arr[2][1]=0
        elif i_o == 9 and arr[2][2]==(-1):
            arr[2][2]=0        
    return(arr)

def overwrite(i_o,player):
    if player == "pl1":
        if i_o == 1 and arr[0][0]!=(-1):
            return(True)
        elif i_o == 2 and arr[0][1]!=(-1):
            return(True)
        elif i_o == 3 and arr[0][2]!=(-1):
            return(True)
        elif i_o == 4 and arr[1][0]!=(-1):
            return(True)
        elif i_o == 5 and arr[1][1]!=(-1):
            return(True)
        elif i_o == 6 and arr[1][2]!=(-1):
            return(True)
        elif i_o == 7 and arr[2][0]!=(-1):
            return(True)
        elif i_o == 8 and arr[2][1]!=(-1):
            return(True)
        elif i_o == 9 and arr[2][2]!=(-1):
            return(True)
        else:
            return(False)
    elif player == "pl2":
        if i_o == 1 and arr[0][0]!=(-1):
            return(True)
        elif i_o == 2 and arr[0][1]!=(-1):
            return(True)
        elif i_o == 3 and arr[0][2]!=(-1):
            return(True)
        elif i_o == 4 and arr[1][0]!=(-1):
            return(True)
        elif i_o == 5 and arr[1][1]!=(-1):
            return(True)
        elif i_o == 6 and arr[1][2]!=(-1):
            return(True)
        elif i_o == 7 and arr[2][0]!=(-1):
            return(True)
        elif i_o == 8 and arr[2][1]!=(-1):
            return(True)
        elif i_o == 9 and arr[2][2]!=(-1):
            return(True)
        else:
            return(False)
        
def display_board(arr):
    print(" ","o"*arr[0][0]+"x"*int(not(arr[0][0]))+" "*(arr[0][0]*(-1))," | ","o"*arr[0][1]+"x"*int(not(arr[0][1]))+" "*(arr[0][1]*(-1))," | ","o"*arr[0][2]+"x"*int(not(arr[0][2]))+" "*(arr[0][2]*(-1)))
    print("-"*17)                                                     
    print(" ","o"*arr[1][0]+"x"*int(not(arr[1][0]))+" "*(arr[1][0]*(-1))," | ","o"*arr[1][1]+"x"*int(not(arr[1][1]))+" "*(arr[1][1]*(-1))," | ","o"*arr[1][2]+"x"*int(not(arr[1][2]))+" "*(arr[1][2]*(-1)))
    print("-"*17)
    print(" ","o"*arr[2][0]+"x"*int(not(arr[2][0]))+" "*(arr[2][0]*(-1))," | ","o"*arr[2][1]+"x"*int(not(arr[2][1]))+" "*(arr[2][1]*(-1))," | ","o"*arr[2][2]+"x"*int(not(arr[2][2]))+" "*(arr[2][2]*(-1)))
       
def game_check(arr):
    count = 1
    if arr[0][0] == arr[0][1] and arr[0][0] == arr[0][2] and arr[0][0] == 1:
        print("")
        print("----------player 1 is the winner----------")
        result = "def"
        return(result)
    elif arr[1][0] == arr[1][1] and arr[1][0] == arr[1][2] and arr[1][0] == 1:
         print("")
         print("----------player 1 is the winner----------")
         result = "def"
         return(result)
    elif arr[2][0] == arr[2][1] and arr[2][0] == arr[2][2] and arr[2][0] == 1:
         print("----------player 1 is the winner----------")
         result = "def"
         return(result)
    elif arr[0][0] == arr[1][0] and arr[0][0] == arr[2][0] and arr[0][0] == 1:
         print("----------player 1 is the winner----------")
         result = "def"
         return(result)
    elif arr[0][1] == arr[1][1] and arr[0][1] == arr[2][1] and arr[0][1] == 1:
         print("----------player 1 is the winner----------")
         result = "def"
         return(result)
    elif arr[0][2] == arr[1][2] and arr[0][2] == arr[2][2] and arr[0][2] == 1:
         print("----------player 1 is the winner----------")
         result = "def"
         return(result)
    elif arr[0][0] == arr[1][1] and arr[0][0] == arr[2][2] and arr[0][0] == 1:
         print("----------player 1 is the winner----------")
         result = "def"
         return(result)
    elif arr[0][2] == arr[1][1] and arr[0][2] == arr[2][0] and arr[0][2] == 1:
         print("----------player 1 is the winner----------")
         result = "def"
         return(result)
    elif arr[0][0] == arr[0][1] and arr[0][0] == arr[0][2] and arr[0][0] == 0:
         print("")
         print("----------player 2 is the winner----------")
         result = "def"
         return(result)
    elif arr[1][0] == arr[1][1] and arr[1][0] == arr[1][2] and arr[1][0] == 0:
         print("----------player 2 is the winner----------")
         result = "def"
         return(result)
    elif arr[2][0] == arr[2][1] and arr[2][0] == arr[2][2] and arr[2][0] == 0:
         print("----------player 2 is the winner----------")
         result = "def"
         return(result)
    elif arr[0][0] == arr[1][0] and arr[0][0] == arr[2][0] and arr[0][0] == 0:
         print("----------player 2 is the winner----------")
         result = "def"
         return(result)
    elif arr[0][1] == arr[1][1] and arr[0][1] == arr[2][1] and arr[0][1] == 0:
         print("----------player 2 is the winner----------")
         result = "def"
         return(result)
    elif arr[0][2] == arr[1][2] and arr[0][2] == arr[2][2] and arr[0][2] == 0:
         print("----------player 2 is the winner----------")
         result = "def"
         return(result)
    elif arr[0][0] == arr[1][1] and arr[0][0] == arr[2][2] and arr[0][0] == 0:
         print("----------player 2 is the winner----------")
         result = "def"
         return(result)
    elif arr[0][2] == arr[1][1] and arr[0][2] == arr[2][0] and arr[0][2] == 0:
         print("----------player 2 is the winner----------")
         result = "def"
         return(result)
    else:
        result = "undef"
        return(result)    
        
def tictactoe():
    print("------------------------------------------TIC TAC TOE------------------------------------------------")
    print("")
    print("------------------------------------------INSTRUCTION------------------------------------------------")
    print("")
    print(" ","1"," | ","2"," | ","3")
    print("-"*17)                                                     
    print(" ","4"," | ","5"," | ","6")
    print("-"*17)
    print(" ","7"," | ","8"," | ","9")
    print("")
    print("1.This is the tictactoe matrix")
    print("2.Each box is given a number")
    print("3.If you want to place the symbol in a particular box then input its designated number")
    print("")   
    print("  Player 1 = 'o'")
    print("  Player 2 = 'x'")
    print("")
    print("do you wish to start the game?(yes/no)")
    ans = str(input())
    if ans == "no":
        print("---------------------Goodbye---------------------")
    elif ans=="yes":
        over_write = False
        i=0
        result = "undef"
        pl1 = 0
        pl2 = 0
        while(result=="undef"):
            print("")
            print("Player 1 enter the position:")
            pl1 = int(input())
            over_write = overwrite(pl1,"pl1")
            while(pl1==pl2 or over_write):
                if pl1 == pl2 or over_write:
                    print("You can't do that, please try again")
                    pl1 = int(input())
                    over_write = overwrite(pl1,"pl1")
            manage_input(pl1,"pl1")
            display_board(arr)
            i += 1
            result = game_check(arr)
            if result == "def":
                break
            if i == 9 and result == "undef":
                print("")
                print("--------It's a draw-------")
                result = "def"
                break
            print("")
            print("Player 2 enter the position:")
            pl2 = int(input())
            over_write = overwrite(pl2,"pl2")
            while(pl2==pl1 or over_write):
                if pl1 == pl2 or over_write:
                    print("You can't do that, please try again")
                    pl2 = int(input())
                    over_write = overwrite(pl2,"pl2")
            manage_input(pl2,"pl2")
            display_board(arr)
            i += 1
            result = game_check(arr)
            if i == 9 and result == "undef":
                print("")
                print("--------It's a draw-------")
                result = "def"
                break
        print("")
        print("Total number of moves =",i)
        print("")
        print("----------------Thanks for playing---------------")

tictactoe()    
    




    
