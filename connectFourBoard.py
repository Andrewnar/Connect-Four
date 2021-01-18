'''
Author: Andrew Narvaez
Connect 4 - GameBoard - No AI

'''

class Board(object):

    def __init__(self, width = 7, height = 6):
        '''Contructer for objects of type Board'''

        self.__width = width
        self.__height = height
        board = []

        for x in range(height):
            row = []
            for y in range(width):
                row += ' '
            board.append(row)
        self.__board = board

    def __str__(self):
        '''returns a string representation for the object of type Board
        that calls it (named self)'''
        temp = ''

        for x in self.__board:
            temp += '|'
            for y in x:
                if y: temp += y
                else: temp += ' '
                temp += "|"
            temp += '\n'
        
        temp += '-' * ((2 * self.__width) + 1) + '\n'
        count = 0
        for z in range((2 * self.__width) + 1):
            if z % 2 == 1: 
                temp += str(count)
                count += 1
            else: temp += ' '
           
        return temp

    def allowsMove(self, col):
        '''returns boolean expression on whether board can accept input on 
        inputted column'''
        if not 0 <= col < self.__width: return False
        for z in range(self.__width - 1):
            if self.__board[z][col] == ' ': return True
        return False

    def addMove(self, col, ox):
        '''Adds 'X" or "O" into column col where the lowest move can be played'''
        slot = 0
        if self.allowsMove(col):
            if self.__board[self.__height -1][col] == ' ':
                slot = self.__height -1
            else:
                for x in range(self.__height - 1):
                    if self.__board[x][col] == ' ' and self.__board[x + 1][col] != ' ':
                        slot = x   
            self.__board[slot][col] = ox   

    def delMove(self, col, ox):
        '''removes the top checker from column col in board self'''
        if self.__board[0][col] != ' ': self.__board[0][col] = ' '
        else:
            for x in range(self.__height - 1):
                    if self.__board[x][col] == ' ' and \
                    self.__board[x + 1][col] != ' ':
                        self.__board[x + 1][col] = ' '
                        break

    def setBoard(self, moveString):
        """ takes in a string of columns and places alternating checkers 
        in those columns, starting with 'X' For example, call b.setBoard('012345')
        to see 'X's and 'O's alternate on the bottom row, or b.setBoard('000000') to
        see them alternate in the left column. moveString must be a string of integers
        """
        nextCh = 'X'  # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width: self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'
