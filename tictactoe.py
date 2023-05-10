import os
from colorama import Fore, Back



def main():
    
    players = 0
    while int(players) != 1 and int(players) != 2:
        os.system('cls')
        players = int(input("Podaj liczbę graczy (1 albo 2): "))

    rozmiar = 10
    dane = []
    for i in range(rozmiar):
        kolumna = [0 for i in range(rozmiar)]
        dane.append(kolumna)
    
    # print(dane)

    if players == 2:
        gracz = 1
        while True:
            screenXO(dane)
            if gracz == 1: printGreen("Gracz 1\n")
            else: printRed("Gracz 2\n")
            x = int(input("Podaj wsp x: "))
            y = int(input("Podaj wsp y: "))
            if not dane[x][y]:
                dane[y][x] = gracz
                gracz *= -1


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
            if(j>0): printGreen(" X ")
            elif j<0: printRed(" O ")
            else: printWhite("   ")
            printWhite(lines["vertical"])            
        print()
        if(i < size-1): printWhite(corners["mediumLeft"]+verticalMid+corners["mediumRight"]+"\n")

    printWhite(corners["bottomLeft"]+verticalDown+corners["bottomRight"]+"\n")



if __name__ == "__main__":
    main()