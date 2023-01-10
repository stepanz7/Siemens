import argparse
import re, random, sys
from copy import deepcopy
AI = 1
OPPONENT = 2

class Ai:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.opponentNum = None
        self.aiNum = None
        self.fields =[[0] * cols for _ in range(rows)]

    def firstMove(self):
        x, y = self.cols//2, self.rows//2
        self.fields[y][x] = 1
        return x, y

    def aiMove(self):
        fields = deepcopy(self.fields)
        possible_fields = self.possible_moves(fields)
        if possible_fields == []:
            return "wrong"

        # Checking if ai can win this round
        for f in possible_fields:
            x,y = f[0], f[1]
            fields[y][x] = 1
            try:
                win = self.check_for_win(fields, 1)
                if win:
                    self.fields[y][x] = 1
                    return x, y
            except:
                pass
            fields[y][x] = 0

        # Checking if ai can prevent opponent from winning next round
        for f in possible_fields:
            x, y = f[0], f[1]
            fields[y][x] = 2
            try:
                win = self.check_for_win(fields, 2)
                if win:
                    self.fields[y][x] = 1
                    return x,y
            except:
                pass
            fields[y][x] = 0

        # Checking if ai can make a 3 in a row with possibility to play 4th
        aiFound = []
        for f in possible_fields:
            x, y = f[0], f[1]
            fields[y][x] = 1
            try:
                found = self.check_for_3(fields, 1)
                if found == True:
                    aiFound.append([x, y])
            except:
                pass
            fields[y][x] = 0
        if not aiFound == []:
            field = random.choice(aiFound)
            col = field[0]
            row = field[1]
            self.fields[row][col] = 1
            return col, row

        # Checking if ai can prevent opponent from making a 3 in a row with possibility to play 4th
        aiFound = []
        for f in possible_fields:
            x, y = f[0], f[1]
            fields[y][x] = 2
            try:
                found = self.check_for_3(fields, 2)
                if found == True:
                    aiFound.append([x, y])
            except:
                pass
            fields[y][x] = 0
        if not aiFound == []:
            field = random.choice(aiFound)
            col = field[0]
            row = field[1]
            self.fields[row][col] = 1
            return col,row

        # Checking if ai can make a 2 in a row with possibility to play 3rd and 4th
        aiFound = []
        for f in possible_fields:
            x, y = f[0], f[1]
            fields[y][x] = 1
            try:
                found = self.check_for_2(fields, 1)
                if found == True:
                    aiFound.append([x, y])
            except:
                pass
            fields[y][x] = 0
        if not aiFound == []:
            field = random.choice(aiFound)
            col = field[0]
            row = field[1]
            self.fields[row][col] = 1
            return col, row

        # Checking if ai can make a move with possibility to play 2nd 3rd and 4th
        aiFound = []
        for f in possible_fields:
            x, y = f[0], f[1]
            fields[y][x] = 1
            try:
                found = self.check_for_1(fields, 1)
                if found == True:
                    aiFound.append([x, y])
            except:
                pass
            fields[y][x] = 0
        if not aiFound == []:
            field = random.choice(aiFound)
            col = field[0]
            row = field[1]
            self.fields[row][col] = 1
            return col, row





        return "wrong"

    def check_for_win(self, fields, player):

        for x in range(self.cols):
            for y in range(self.rows):
                # check horizontally
                try:
                    if fields[y][x] == player and fields[y][x+1] == player and fields[y][x+2] == player and fields[y][x+3] == player:
                        return True
                except:
                    pass
                #check vertically
                try:
                    if fields[y][x] == player and fields[y+1][x] == player and fields[y+2][x] == player and fields[y+3][x] == player:
                        return True
                except:
                    pass
                #check diagonaly left -> right, top -> bottom
                try:
                    if fields[y][x] == player and fields[y+1][x+1] == player and fields[y+2][x+2] == player and fields[y+3][x+3] == player:
                        return True
                except:
                    pass
                # check diagonaly left -> right, bottom -> top
                try:
                    if fields[y][x] == player and fields[y-1][x+1] == player and fields[y-2][x+2] == player and fields[y-3][x+3] == player and y-2 >= 0:
                        return True
                except:
                    pass

    def check_for_3(self, fields, player):
        for x in range(self.cols):
            for y in range(self.rows):
                # check horizontally
                try:
                    if (fields[y][x] == player and fields[y][x + 1] == player and fields[y][x + 2] == player) and (
                            fields[y][x + 3] == 0 or
                            (fields[y][x-1] == 0 and x-1 >= 0)):
                        return True
                except:
                    pass
                # check vertically
                try:
                    if (fields[y][x] == player and fields[y+1][x] == player and fields[y+2][x] == player) and (
                            fields[y+3][x] == 0 or
                            (fields[y-1][x] == 0 and y-1 >= 0)):
                        return True
                except:
                    pass
                # check diagonaly left -> right, top -> bottom
                try:
                    if (fields[y][x] == player and fields[y+1][x+1] == player and fields[y+2][x+2] == player) and (
                            fields[y+3][x+3] == 0 or
                            (fields[y-1][x-1] == 0 and y-1 >= 0 and x-1 >= 0)):
                        return True
                except:
                    pass
                # check diagonaly left -> right, bottom -> top
                try:
                    if (fields[y][x] == player and fields[y - 1][x + 1] == player and fields[y - 2][x + 2] == player and y - 2 >= 0) and (
                            (fields[y-3][x+3] == 0 and y-3 >= 0) or
                            (fields[y+1][x-1] == 0 and x-1 >= 0)):
                        return True
                except:
                    pass

    def check_for_2(self, fields, player):
        for x in range(self.cols):
            for y in range(self.rows):
                # check horizontally
                try:

                    if (fields[y][x] == player and fields[y][x + 1] == player) and (
                            (fields[y][x+2] == 0 and fields[y][x + 3] == 0) or
                            (fields[y][x-1] == 0 and fields[y][x - 2] == 0 and x-2 >= 0) or
                            (fields[y][x-1] == 0 and fields[y][x + 2] == 0 and x-1 >= 0)):
                        return True
                except:
                    pass

                # check vertically
                try:
                    if(fields[y][x] == player and fields[y+1][x] == player) and (
                            (fields[y + 2][x] == 0 and fields[y + 3][x] == 0) or
                            (fields[y - 1][x] == 0 and fields[y - 2][x] == 0 and y-2 >= 0) or
                            (fields[y-1][x] == 0 and fields[y+2][x] == 0 and y-1 >= 0)):
                        return True
                except:
                    pass
                # check diagonaly left -> right, top -> bottom
                try:
                    if (fields[y][x] == player and fields[y + 1][x + 1] == player) and (
                            (fields[y + 2][x + 2] == 0 and fields[y + 3][x + 3] == 0) or
                            (fields[y - 1][x - 1] == 0 and fields[y - 2][x - 2] == 0 and y-2 >= 0 and x-2 >= 0) or
                            (fields[y - 1][x - 1] == 0 and fields[y + 2][x + 2] == 0 and x-1 >= 0 and y-1 >= 0)):
                        return True
                except:
                    pass
                # check diagonaly left -> right, bottom -> top
                try:
                    if (fields[y][x] == player and fields[y - 1][x + 1] == player) and (
                            (fields[y - 2][x + 2] == 0 and fields[y - 3][x + 3] == 0 and y-3 >= 0) or
                            (fields[y + 1][x - 1] == 0 and fields[y + 2][x - 2] == 0 and x-2 >= 0 and x-1 >= 0) or
                            (fields[y + 1][x - 1] == 0 and fields[y - 2][x + 2] == 0 and y-2 >= 0 and x-1 >= 0)):
                        return True
                except:
                    pass

    def check_for_1(self, fields, player):
        for x in range(self.cols):
            for y in range(self.rows):
                # check horizontally
                try:

                    if (fields[y][x] == player) and (
                            (fields[y][x+1] and fields[y][x+2] == 0 and fields[y][x + 3] == 0) or
                            (fields[y][x-1] == 0 and fields[y][x - 2] == 0 and fields[y][x-3] and x-3 >= 0) or
                            (fields[y][x-1] == 0 and fields[y][x - 2] == 0 and fields[y][x+1] and x-2 >= 0) or
                            (fields[y][x-1] == 0 and fields[y][x + 1] == 0 and fields[y][x+2] and x-1 >= 0)):
                        return True
                except:
                    pass

                # check vertically
                try:
                    if (fields[y][x] == player) and (
                            (fields[y + 1][x] and fields[y + 2][x] == 0 and fields[y + 3][x] == 0) or
                            (fields[y - 1][x] == 0 and fields[y - 2][x] == 0 and fields[y - 3][x] and y - 3 >= 0) or
                            (fields[y - 1][x] == 0 and fields[y - 2][x] == 0 and fields[y + 1][x] and y - 2 >= 0) or
                            (fields[y - 1][x] == 0 and fields[y + 1][x] == 0 and fields[y + 2][x] and y - 1 >= 0)):
                        return True
                except:
                    pass
                # check diagonaly left->right top->bottom, right->left bottom->top
                try:
                    if (fields[y][x] == player) and (
                            (fields[y + 1][x + 1] and fields[y + 2][x + 2] == 0 and fields[y + 3][x + 3] == 0) or
                            (fields[y - 1][x - 1] == 0 and fields[y - 2][x - 2] == 0 and fields[y - 3][x - 3] and y - 3 >= 0 and x - 3 >= 0) or
                            (fields[y - 1][x - 1] == 0 and fields[y - 2][x - 2] == 0 and fields[y + 1][x + 1] and y - 2 >= 0 and x - 2 >= 0) or
                            (fields[y - 1][x - 1] == 0 and fields[y + 1][x + 1] == 0 and fields[y + 2][x + 2] and y - 1 >= 0 and x - 1 >= 0)):
                        return True
                except:
                    pass
                # check diagonaly left -> right bottom -> top, right -> left top->bottom
                try:
                    if (fields[y][x] == player) and (
                            (fields[y - 1][x + 1] and fields[y - 2][x + 2] == 0 and fields[y - 3][x + 3] == 0 and y - 3 >= 0) or
                            (fields[y + 1][x - 1] == 0 and fields[y + 2][x - 2] == 0 and fields[y + 3][x - 3] and x - 3 >= 0) or
                            (fields[y - 1][x + 1] == 0 and fields[y - 2][x + 2] == 0 and fields[y + 1][x - 1] and y - 2 >= 0 and x - 1 >= 0) or
                            (fields[y + 1][x - 1] == 0 and fields[y + 2][x - 2] == 0 and fields[y - 1][x + 1] and y - 1 >= 0 and x - 2 >= 0)):
                        return True
                except:
                    pass

    def possible_moves(self, fields):
        possible_fields = []
        for x in range(self.cols):
            for y in range(self.rows):
                if fields[y][x] == 0:
                    possible_fields.append([x,y])
        return possible_fields

    def process_input(self, inp):
        numbers = re.findall(r'\d+', inp)
        try:
            x = int(numbers[0])
            y = int(numbers[1])
        except:
            return "wrong"

        if not self.check_inputs(x, y):
            return "wrong"
        else:
            self.fields[y][x] = OPPONENT
            return self.aiMove()

    def check_inputs(self, x, y):
        if x < 0 or x > self.cols or y < 0 or y > self.rows:
            return False
        elif self.fields[y][x] != 0:
            return False
        else:
            return True


def main():
    parser = argparse.ArgumentParser(description='Piskvorky')
    parser.add_argument('cols', type=int, help='field size in X')
    parser.add_argument('rows', type=int, help='field size')
    args = parser.parse_args()
    cols=args.cols
    rows=args.rows
    # cols = 10
    # rows = 10
    ai = Ai(cols, rows)

    while True:
        # Just for testing purposes printing fields
        for i in range(0, cols):
            print(ai.fields[i])


        inp = sys.stdin.readline()
        inp = inp.strip()

        if inp == "start":
            out = ai.firstMove()
            x, y = out[0], out[1]
            print(x, y)
            sys.stdout.flush()

        elif inp == "exit":
            break
        else:
            out =ai.process_input(inp)
            if out == "wrong":
                print(out)
                sys.stdout.flush()

            else:
                x, y = out[0], out[1]
                print(x, y)
                sys.stdout.flush()


if __name__ == "__main__":
    main()





