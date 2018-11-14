############################################################
import tkinter
from tkinter import *
from tkinter import ttk
root = Tk()
root.attributes("-fullscreen", True)
def doSomething():
    root.destroy()

def variables():
    global col_1, col_2, col_3, col_4, col_5, col_6, col_6, col_7, col_all, player, turn, brk
    col_1 = [None,None,None,None,None,None] 
    col_2 = [None,None,None,None,None,None]
    col_3 = [None,None,None,None,None,None]
    col_4 = [None,None,None,None,None,None]
    col_5 = [None,None,None,None,None,None]
    col_6 = [None,None,None,None,None,None]
    col_7 = [None,None,None,None,None,None]
    col_all = [col_1,col_2,col_3,col_4,col_5,col_6,col_7]
    turn = 0
    player = 'P1'
    brk = 'idk'
############################################################
def bdisable():
    global cbutt
    for x in range(43):
        if x == 0:
            pass
        else:
            cbutt[x].configure(state=DISABLED)
        



    
#######################[MENU]###############################
def exitt():
    quit()
def restart():
    global cbutt, brk, turn
    brk = 'idk'
    variables()
    for x in range(43):
        if x == 0:
            pass
        else:
            cbutt[x].configure(bg='SystemButtonFace', state=NORMAL)
    turn = 1
    turnn()

def about():
    top = Toplevel()
    top.title("About")

    msg = Message(top, text='CONNECT 4 \n\nFirst person to get 4 in arow wins. This can include vertical, horizontal, or diagonal combinations.')
    msg.pack()
    menubar = Menu(root)

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Restart", command=restart)
filemenu.add_command(label="Exit", command=exitt)

menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="About", command=about)

menubar.add_cascade(label="Help", menu=editmenu)
root.config(menu=menubar)
############################################################  
def turnn():
    global turn, color, player, turn_label,brk, winner
    turn += 1
    if brk != 'end':
        if turn % 2 == 0:
            player = 'P1'
        else:
            player = 'P2'
            
        if player == 'P1':
            color = 'FireBrick1'
        if player == 'P2':
            color = 'RoyalBlue3'
    else:
        player = winner
    turn_label.config(text='Turn> ' +str(player))
###################[WIN CHECK]#############################       
def win_check():
    global countp1, countp2, winner
    countp1 = 0 ; countp2 = 0 ; winner = ''
############################          
    def vert_check():
        global countp1, countp2, winner, x
        for x in range(7):
            for y in range(3):
                if col_all[x][y] == col_all[x][y+1] and col_all[x][y] != None:
                    if col_all[x][y+1] == col_all[x][y+2] and col_all[x][y+1] != None:
                        if col_all[x][y+2] == col_all[x][y+3] and col_all[x][y+2] != None:
                            if col_all[x][y+2] == 'P1':
                                countp1 = 4
                            if col_all[x][y+2] == 'P2':
                                countp2 = 4
                            temp222()
                        
############################
    def side_check():
        global countp1, countp2, winner, col_all, brk
        for x in range(6):
            if col_1[x] == col_2[x] and col_2[x] == col_3[x] and col_3[x] == col_4[x] and col_1[x] != None:
                if col_4[x] == 'P1':
                    countp1 = 4
                if col_4[x] == 'P2':
                    countp1 = 4    
                temp222()
            if col_2[x] == col_3[x] and col_3[x] == col_4[x] and col_4[x] == col_5[x] and col_2[x] != None:
                if col_5[x] == 'P1':
                    countp1 = 4
                if col_5[x] == 'P2':
                    countp1 = 4    
                temp222()
            if col_3[x] == col_4[x] and col_4[x] == col_5[x] and col_5[x] == col_6[x] and col_3[x] != None:
                if col_6[x] == 'P1':
                    countp1 = 4
                if col_6[x] == 'P2':
                    countp1 = 4    
                temp222()
            if col_4[x] == col_5[x] and col_5[x] == col_6[x] and col_6[x] == col_7[x] and col_4[x] != None:
                if col_7[x] == 'P1':
                    countp1 = 4
                if col_7[x] == 'P2':
                    countp1 = 4    
                temp222()
############################
    def temp222():
        global countp1, countp2, winner, brk
        if brk != 'end':
            if countp1 > 3:
                winner = 'Player 1 Wins'
                brk = 'end'
            if countp2 > 3:
                winner = 'Player 2 Wins'
                brk = 'end'
            else:
                countp1 = 0 ; countp2 = 0
        if brk == 'end':
            bdisable()
            turnn()
            turn = winner
#################                
    def di_check():
        global countp1, countp2, winner, col_all
        for e in range(3):
            try:
                if col_all[e][e-1] == col_all[e-1][e-2] and col_all[e][e-1] != None:
                    if col_all[e+1][e-2] == col_all[e+2][e-3] and col_all[e+1][e-2] != None:
                        if col_all[e+2][e-3] == col_all[e+3][e-4] and col_all[e+2][e-3] != None:         
                            if col_all[e+2][e-3] == 'P1':
                                countp1 = 4
                            if col_all[e+2][e-3] == 'P2':
                                countp2 = 4
            except:
                pass
            temp222()
        try:
            if col_all[0][-2] == col_all[1][-3] and col_all[0][-2] != None:
                if col_all[1][-3] == col_all[2][-4] and col_all[1][-3] != None:
                    if col_all[2][-4] == col_all[3][-5] and col_all[2][-4] != None:
                        if col_all[2][-4] == 'P1':
                            countp1 = 4
                        if col_all[2][-4] == 'P2':
                             countp2 = 4
                temp222()
            if col_all[-1][3] == col_all[-2][4] and col_all[-1][3] != None:
                if col_all[-2][4] == col_all[3][-5] and col_all[-2][4] != None:
                    if col_all[-3][5] == col_all[-4][6] and col_all[-3][5] != None:
                        if col_all[-3][5] == 'P1':
                            countp1 = 4
                        if col_all[-4][6] == 'P2':
                             countp2 = 4
                temp222()
        except:
            pass
        for e in range(3):
            try:
                if col_all[-e-1][e+2] == col_all[-e-2][-e+3] and col_all[-e-1][-e+2] != None:
                    if col_all[-e-2][-e+3] == col_all[-e-3][-e+4] and col_all[-e-2][-e+3] != None:
                        if col_all[-e-3][-e+4] == col_all[-e-4][-e+5] and col_all[-e-3][-e+4] != None:         
                            if col_all[-e-3][-e+4] == 'P1':
                                countp1 = 4
                            if col_all[-e-3][-e+4] == 'P2':
                                countp2 = 4
            except:
                pass
            temp222()
        for c in range(4):
            for v in range(6):
                try:
                    if col_all[v+c][v] == col_all[v+1+c][v+1] and col_all[v+c][v] != None:
                        if col_all[v+1+c][v+1] == col_all[v+2+c][v+2] and col_all[v+1+c][v+1] != None:
                            if col_all[v+2+c][v+2] == col_all[v+3+c][v+3] and col_all[v+2+c][v+2] != None:
                                if col_all[v+c][v] == 'P1':
                                    countp1 = 4
                                if col_all[v+c][v] == 'P2':
                                    countp2 = 4
                except:
                    pass
                temp222()
            for v in range(6):
                try:
                    if col_all[-v-1-c][-v-1] == col_all[-v-2-c][-v-2] and col_all[-v-1][-v-1] != None:
                        if col_all[-v-2-c][-v-2] == col_all[-v-3-c][-v-3] and col_all[-v-2-c][-v-2] != None:
                            if col_all[-v-3-c][-v-3] == col_all[-v-4-c][-v-4] and col_all[-v-3-c][-v-3] != None:
                                if col_all[-v-1-c][-v-1] == 'P1':
                                    countp1 = 4
                                if col_all[-v-1-c][-v-1] == 'P2':
                                    countp2 = 4
                except:
                    pass
                temp222()
    di_check()
    vert_check()
    side_check()
###########################################################
def col_1check():
    global player, turn, cbutt, color
    win_check()
    turnn()
    for x in range(7):
        y = x 
        if col_1[-y -1] == None:
            col_1[-y -1] = player
            break
    z = (6 - y)
    cbutt[z].configure(bg=color,state=DISABLED)
    
    if turn % 2 == 0:
        player = 'P1'
    else:
        player = 'P2'
    win_check()
###########################################################        
def col_2check():
    global player, turn, cbutt, color
    win_check()
    turnn()
        
    for x in range(7):
        y = x
        if col_2[-y -1] == None:
            col_2[-y -1] = player
            break
    z = (12 - y)
    cbutt[z].configure(bg=color,state=DISABLED) 
    
    if turn % 2 == 0:
        player = 'P1'
    else:
        player = 'P2'
    win_check()
###########################################################        
def col_3check():
    global player, turn, cbutt, color
    win_check()
    turnn()
        
    for x in range(7):
        y = x
        if col_3[-y -1] == None:
            col_3[-y -1] = player
            break
    z = (18 - y)
    cbutt[z].configure(bg=color,state=DISABLED) 
    
    if turn % 2 == 0:
        player = 'P1'
    else:
        player = 'P2'
    win_check()
###########################################################    
def col_4check():
    global player, turn, cbutt, color
    win_check()
    turnn() 
    for x in range(7):
        y = x
        if col_4[-y -1] == None:
            col_4[-y -1] = player
            break
    z = (24 - y)
    cbutt[z].configure(bg=color,state=DISABLED) 
    
    if turn % 2 == 0:
        player = 'P1'
    else:
        player = 'P2'
    win_check()
###########################################################    
def col_5check():
    global player, turn, cbutt, color
    win_check()
    turnn()
        
    for x in range(7):
        y = x
        if col_5[-y -1] == None:
            col_5[-y -1] = player
            break
    z = (30 - y)
    cbutt[z].configure(bg=color,state=DISABLED) 
    
    if turn % 2 == 0:
        player = 'P1'
    else:
        player = 'P2'
    win_check()
###########################################################    
def col_6check():
    global player, turn, cbutt, color
    win_check()
    turnn()
        
    for x in range(7):
        y = x
        if col_6[-y -1] == None:
            col_6[-y -1] = player
            break
    z = (36 - y)
    cbutt[z].configure(bg=color,state=DISABLED) 
    
    if turn % 2 == 0:
        player = 'P1'
    else:
        player = 'P2'
    win_check()
###########################################################    
def col_7check():
    global player, turn, cbutt, color
    turnn()
        
    for x in range(7):
        y = x
        if col_7[-y -1] == None:
            col_7[-y -1] = player
            break
    z = (42 - y)
    cbutt[z].configure(bg=color,state=DISABLED) 
    
    if turn % 2 == 0:
        player = 'P1'
    else:
        player = 'P2'
    win_check()
###########################################################
def button_configure():
    global cbutt,rw,col, player, turn_label
    cbutt = {'temp':'...'}
    rw = 1 ; col = 1 
    for x in range(43):
        if x == 0:
            pass
        else:
            if 'temp' in cbutt:
                del cbutt['temp']
            
            if rw > 6:
                col += 1
                rw = 1
                
            cbutt[x] = Button(root,width=10,height=5,state=NORMAL)
            cbutt[x].grid(column=col,row=rw,sticky='NSEW')
            
            rw += 1
            
            if col == 1:
                cbutt[x].configure(command=col_1check)
            if col == 2:
                cbutt[x].configure(command=col_2check)
            if col == 3:
                cbutt[x].configure(command=col_3check)
            if col == 4:
                cbutt[x].configure(command=col_4check)
            if col == 5:
                cbutt[x].configure(command=col_5check)
            if col == 6:
                cbutt[x].configure(command=col_6check)
            if col == 7:
                cbutt[x].configure(command=col_7check)
                
    imag = PhotoImage(file="connect4image.png")
    label = Label(image=imag)
    label.image = imag
    label.grid(column=3,row=0,columnspan=3)
    labelblank = Label(text='',width=67)
    labelblank.grid(column=0,row=0)

    turn_label = Label(text='Turn> ' +str(player))
    turn_label.config(width=20,font=("Arial", 14))
    turn_label.grid(column=1,row=7,columnspan=7)
    
variables()       
button_configure()
