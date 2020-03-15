import random, time, os, msvcrt

class Puzzle:
    
    def __init__(self):
        
        self.board_matrix=[]
        starter=1
        
        for looper in range(dim1):
            self.board_matrix.append(range(starter,starter+dim2))
            starter+=dim2

        self.board_matrix[-1][-1]=0
        
        self.solved_matrix=[rw[:] for rw in self.board_matrix]
        
        self.emp_row=dim1-1 # row # (starting from 0)
        self.emp_col=dim2-1 # col #

        self.last_move='w'

    def print_board(self):

        for row in self.board_matrix:

            clean_row=''

            for num in row:
                if num==0:
                    clean_row+='\t'
                else:
                    clean_row+=(str(num)+'\t')

            clean_row+='\n'
            
            print clean_row

    def move_up(self):

        if self.emp_row==dim1-1:
            return

        self.board_matrix[self.emp_row][self.emp_col]=self.board_matrix[self.emp_row+1][self.emp_col]
        self.board_matrix[self.emp_row+1][self.emp_col]=0

        self.emp_row+=1

    def move_down(self):

        if self.emp_row==0:
            return

        self.board_matrix[self.emp_row][self.emp_col]=self.board_matrix[self.emp_row-1][self.emp_col]
        self.board_matrix[self.emp_row-1][self.emp_col]=0

        self.emp_row-=1

    def move_right(self):

        if self.emp_col==0:
            return

        self.board_matrix[self.emp_row][self.emp_col]=self.board_matrix[self.emp_row][self.emp_col-1]
        self.board_matrix[self.emp_row][self.emp_col-1]=0

        self.emp_col-=1

    def move_left(self):

        if self.emp_col==dim2-1:
            return

        self.board_matrix[self.emp_row][self.emp_col]=self.board_matrix[self.emp_row][self.emp_col+1]
        self.board_matrix[self.emp_row][self.emp_col+1]=0

        self.emp_col+=1

    def move_r1(self): # clockwise

        if self.emp_row<dim1-2:
            return

        for looper in range(2*dim2-1):
            
            if self.emp_row==dim1-1:
                
                if self.emp_col==dim2-1:
                    self.move_down()
                    
                else:
                    self.move_left()
            else:
                
                if self.emp_col==0:
                    self.move_up()
                    
                else:
                    self.move_right()

    def move(self,letter):

        if letter=='u':
            self.move_up()

        elif letter=='d':
            self.move_down()

        elif letter=='r':
            self.move_right()

        elif letter=='l':
            self.move_left()

    def move2(self,letter):

        moved=False
        
        if letter=='w':
            self.move_up()
            moved=True

        elif letter=='s':
            self.move_down()
            moved=True

        elif letter=='d':
            self.move_right()
            moved=True
            
        elif letter=='a':
            self.move_left()
            moved=True

        elif letter=='r':
            self.move_r1()
            moved=True

        elif letter=='':
            self.move2(self.last_move)


        if moved:
            self.last_move=letter
            
    def is_solved(self):

        if self.solved_matrix==self.board_matrix:
            return True

        else:
            return False

dim2=0
dim1=0

while True:
    
    try:
        dim2=int(raw_input("How many columns would you like to have? "))

        if dim2>=1 and dim2<=20:
            break
        
    except ValueError:
        pass

while True:
    
    try:
        dim1=int(raw_input("How many rows would you like to have? "))

        if dim1>=1 and dim1<=20:
            break
        
    except ValueError:
        pass

slider=Puzzle()

choices=['u','d','r','l']

start=time.time()

for looper in range(10000):
    
    slider.move(random.choice(choices))

end=time.time()

raw_input("A new game was generated in only "+str(end-start)+" seconds!!!\n")
os.system('cls')

while True:

    slider.print_board()
    slider.move2(msvcrt.getch())
    os.system('cls')

    if slider.is_solved():
        break

print "Congratulations, you win!!!"

raw_input("Press ENTER to continue ...")
