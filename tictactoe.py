import os
from colorama import Fore, Back
import random


def main():
    
    players = 0
    while int(players) != 1 and int(players) != 2:
        os.system('cls')
        players = int(input("Podaj liczbę graczy (1 albo 2): "))

    os.system('cls')
    size = 0

    win_req = 3
    while size < 3:
        size = int(input("Podaj rozmiar planszy większy od 2: "))
        os.system('cls')
        if size < 3:
            print("Nieprawidłowa wielkość planszy")
        elif size >= 5:
            win_req = 4

    gameOver = False

    data = []
    for i in range(size):
        kolumna = [{"player": 0, "value": 0} for i in range(size)]
        data.append(kolumna)

    winner = 0

    if players == 2:
        player = 1
        while not gameOver:
            screenXO(data)
            if player == 1: printGreen("Gracz 1\n")
            else: printRed("Gracz 2\n")
            x = int(input("Podaj wsp x: ")) - 1
            y = int(input("Podaj wsp y: ")) - 1
            if not data[y][x]["player"]:
                data[y][x]["player"] = player
                gameOver = checkWin(data, x, y, player, win_req)
                player *= -1
    else:
        player = 1
        while not gameOver:
            screenXO(data)
            len(data)
            if player == 1: 
                printGreen("Twoja tura\n")
                x = int(input("Podaj wsp x: ")) - 1
                y = int(input("Podaj wsp y: ")) - 1
            else:
                highest = 0
                viable = []
                i = 0
                j = 0
                # very inteligent highly advanced AI
                for row in data:
                    for column in row:
                        if column["value"] > highest and not column["player"]: 
                            highest = column["value"]
                            viable.clear()
                        if column["value"] == highest and not column["player"]: 
                            viable.append([i,j])
                        j+=1
                    j = 0
                    i += 1
                index = random.randint(0,len(viable)-1)
                y = viable[index][0]
                x = viable[index][1]

            if not data[y][x]["player"]:
                data[y][x]["player"] = player
                
                gameOver = checkWin(data, x, y, player, win_req)
                if gameOver: 
                    winner = player # jeśli checkwin zwróci prawdę, możemy zapisać aktualnego gracza jako zwyciężce
                    break
                player *= -1

                # jeśli wszystkie pola zostały zajęte, kończymy grę
                gameOver = True
                for list_ in data:
                    if any(d["player"] == 0 for d in list_): 
                        gameOver = False 
                        break
                    
                

    screenXO(data)
    if winner == 1:
        printGreen("Player X won!")
    elif winner == -1:
        printRed("Player O won!")
    else:
        printWhite("Draw!")
        print(data)


def printWhite(data):
    print(Fore.WHITE,data,end="",sep="")

def printRed(data):
    print(Fore.RED,data,end="",sep="")

def printGreen(data):
    print(Fore.GREEN,data,end="",sep="")

def screenXO(screen):
    os.system('cls')
    
    corners = {
               "upperLeft":     "┌",    #218 np. chr(218)
               "upperRight":    "┐",    #191
               "mediumLeft":    "├",    #195 
               "mediumRight":   "┤",    #180
               "bottomLeft":    "└",    #192
               "bottomRight":   "┘",    #217
               "upperMid":      "┬",    #194
               "midiumMid":     "┼",    #197
               "bottomMid":     "┴"     #193
              }
    lines =   {
               "vertical": "│",         #179
               "horizontal": "─"        #196
              }
    
    size = len(screen)                  #rozmiar ekranu

    verticalLine = [lines["horizontal"]*3]*size         #lista zawierająca poziome linie
    # print(verticalLine)
    
    verticalUp = corners["upperMid"].join(verticalLine)
    verticalMid = corners["midiumMid"].join(verticalLine)
    verticalDown = corners["bottomMid"].join(verticalLine)
    # print(verticalUp)
    # print(verticalMid)
    # print(verticalDown)

   

    printWhite(corners["upperLeft"]+verticalUp+corners["upperRight"]+"\n")
 
    for i,row in enumerate(screen):
        printWhite(lines["vertical"])
        for j in row:
            if(j["player"]>0): printGreen(" X ")
            elif j["player"]<0: printRed(" O ")
            else: printWhite("   ")
            printWhite(lines["vertical"])            
        print()
        if(i < size-1): printWhite(corners["mediumLeft"]+verticalMid+corners["mediumRight"]+"\n")

    printWhite(corners["bottomLeft"]+verticalDown+corners["bottomRight"]+"\n")

# after the player moved checks whether it was a winning move
def checkWin(screen, x, y, player, win_req):

    row = screen[y]

    # counts the amount of repeated symbols in the row
    count = 0
    for i in row:
        if i["player"] == player:
            count += 1
            if count >= win_req: return True
        # resets the count when spotted a different symbol
        else:
            # those are for my highly inteligent AI's decision making
            if i["player"] == 0 and i["value"] < 10**count: i["value"] = 10 ** count
            if x-count >= 0 and row[x-count]["player"] == 0 and row[x-count]["value"]< 10**count: row[x-count]["value"] = 10 ** count
            count = 0
    
    # counts the amount of repeats of a certain symbol in the column
    count = 0
    for i,row in enumerate(screen):
        if row[x]["player"] == player:
            print(i)
            count += 1
            if count >= win_req: return True
        else:
            if row[x]["player"] == 0 and row[x]["value"] < 10**count: row[x]["value"] = 10 ** count
            if i-count >= 0 and screen[i-count][x]["player"] == 0 and screen[i-count][x]["value"]< 10**count: screen[i-count][x]["value"] = 10 ** count
            count = 0
            

    # necessary for the bottom-left top-right diagonals
    if x > y:
        offset = x - y
    else:
        offset = y - x
    size = len(screen)

    #checks for the streak on diagonals
    count = 0
    for i in range(size - offset):
        if  (x >= y and screen[i][i + offset]["player"] == player) or (y > x and screen[i + offset][i]["player"] == player):
            count += 1
            if count >= win_req: return True
        else:
            # increases the value of next and previous field
            prev = i - count - 1
            if x >= y:
                if screen[i][i + offset]["player"] == 0 and screen[i][i + offset]["value"] < 10**count: screen[i][i + offset]["value"] = 10 ** count
                if prev >= 0 and screen[prev][prev + offset]["player"] == 0 and screen[prev][prev + offset]["value"] < 10**count: screen[prev][prev + offset]["value"] = 10 ** count
            else:
                if screen[i + offset][i]["player"] == 0 and screen[i + offset][i]["value"] < 10**count: screen[i + offset][i]["value"] = 10 ** count
                if prev >= 0 and screen[prev + offset][prev]["player"] == 0 and screen[prev + offset][prev]["value"] < 10**count: screen[prev + offset][prev]["value"] = 10 ** count
            count = 0
    
    count = 0
    num_rows = x + y if x + y <= size - 1 else (size - x) + (size - y) - 2 #checks how many diagonal fields are on the axis
    for i in range(num_rows + 1):
        if x + y <= size - 1:
            if screen[num_rows - i][i]["player"] == player: #for each field in diagonal it's y value decreases while x increases
                count += 1
                if count >= win_req: return True
            else:
                if screen[num_rows - i][i]["player"] == 0 and screen[num_rows - i][i]["value"] < 10**count:  #increase the value of next field
                    screen[num_rows - i][i]["value"] = 10 ** count
                count = 0
        elif screen[size - 1 - i][size - num_rows - 1 + i]["player"] == player: #I was writing it at 3am on coffee don't ask
            count += 1
            if count >= win_req: return True
        else:
            if screen[size - 1 - i][size - num_rows - 1 + i]["player"] == player and screen[size - 1 - i][size - num_rows - 1 + i]["value"] < 10**count:
                screen[size - 1 - i][size - num_rows - 1 + i]["value"] = 10**count
            count = 0
    return False
    


if __name__ == "__main__":
    main()