def drawboard():
    print('     |     |')
    print(f'  {sec7}  |  {sec8}  |  {sec9} ')
    print('     |     |')
    print('-------------------')
    print('     |     |')
    print(f'  {sec4}  |  {sec5}  |  {sec6} ')
    print('     |     |')
    print('-------------------')
    print('     |     |')
    print(f'  {sec1}  |  {sec2}  |  {sec3} ')
    print('     |     |')
    return None


def playercin():
    global sec1, sec2, sec3, sec4, sec5, sec6, sec7, sec8, sec9
    play = input()
    toint = int(play)
    if toint == 1:
        sec1 = "X"
    elif toint == 2:
        sec2 = "X"
    elif toint == 3:
        sec3 = "X"
    elif toint == 4:
        sec4 = "X"
    elif toint == 5:
        sec5 = "X"
    elif toint == 6:
        sec6 = "X"
    elif toint == 7:
        sec7 = "X"
    elif toint == 8:
        sec8 = "X"
    elif toint == 9:
        sec9 = "X"



sec1 = " "
sec2 = " "
sec3 = " "
sec4 = " "
sec5 = " "
sec6 = " "
sec7 = " "
sec8 = " "
sec9 = " "

playercin()
drawboard()
