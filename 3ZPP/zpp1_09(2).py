def pocatecny_stav():
    doska = [[0] * 8 for _ in range(8)]
    
    for wor in range(3):
        for cvab in range(8):
            if (wor + cvab) % 2 == 1:
                doska[wor][cvab] = 1

    for wor in range(5, 8):
        for cvab in range(8):
            if (wor + cvab) % 2 == 1:
                doska[wor][cvab] = 2
    return doska

def doska2(board):
    print("  a b c d e f g h")
    for i in range(len(board)):
        print(f"{i + 1} ", end="")
        for j in range(len(board[i])):
            piece = board[i][j]
            if piece == 0:
                print(". ", end="")
            elif piece == 1:
                print("o ", end="")
            elif piece == 2:
                print("* ", end="")
        print(i + 1)  
    print("  a b c d e f g h")
dostocka = pocatecny_stav()
doska2(dostocka)