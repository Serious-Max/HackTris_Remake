import copy


class Tetris:
    def __init__(self, xsize, ysize):
        self.xsize = xsize
        self.ysize = ysize
        self.board = [list([0] * xsize) for _ in range(ysize)]

    # def get_board(self):
    #    return self.board

    def figure(self, type, pozition):
        figure_list = [
            # 0 - line, 1 - square, 2 - 'L',
            # 3 - 'Z', 4 - 'T', 5 - 'L's, 6 - 'Z's
            [[1, 4, '1111', 0, 0, 2],
             [4, 1, '1111', 0, -1, 1]],

            [[2, 2, '1111', 1, -1, 2]],

            [[2, 3, '101011', 2, 0, 4],
             [3, 2, '111100', 2, 1, 1],
             [2, 3, '110101', 2, 2, 2],
             [3, 2, '001111', 2, -1, 3]],

            [[3, 2, '011110', 3, 0, 2],
             [2, 3, '101101', 3, -1, 1]],

            [[3, 2, '010111', 4, 0, 4],
             [2, 3, '101110', 4, 1, 1],
             [3, 2, '111010', 4, 2, 2],
             [2, 3, '011101', 4, -1, 3]],

            [[2, 3, '010111', 5, 0, 4],
             [3, 2, '100111', 5, 1, 1],
             [2, 3, '111010', 5, 2, 2],
             [3, 2, '111001', 5, -1, 3]],

            [[3, 2, '110011', 6, 0, 2],
             [2, 3, '011110', 6, -1, 1]]
        ]
        return figure_list[type][pozition]

    def is_intersection(self, figure, x, y):
        # print(figure, x, y, self.xsize, self.ysize)
        # print(self.board)
        if (figure[0] + x > self.xsize) \
                or (x < 0) or (figure[1] + y > self.ysize):
            # print('Out border')
            return True
        else:
            # print('another')
            temp = list(figure[2])
            for i in range(len(temp)):
                # print(temp, self.board)
                if (temp[i] == '1') \
                        and (self.board[y + i // figure[0]][x + i % figure[0]] != 0):
                    return True
            return False

    def rotate(self, figure, degree=0):
        if degree == 0:
            return self.figure(figure[3], figure[4] + 1)
        else:
            return self.figure(figure[3], figure[5] + 1)

    def render(self, figure, x, y):
        # print(1, self.board)
        # print('Render...')
        temp1 = copy.deepcopy(self.board)
        #print(2, self.board)
        # print(figure)
        # print(figure[2])
        temp2 = list(figure[2])
        # print(temp2, len(temp2))
        for i in range(len(temp2)):
            # print(i)
            # print(figure[1], figure[0])
            # print(y + i // figure[0], x + i % figure[1])
            # print(i, self.board)
            if int(temp2[i]):
                temp1[y + i // figure[0]][x + i % figure[0]] = int(temp2[i])
        # print('Render...OK')
        # print(3, self.board)
        # print('---------')
        return temp1

    def add(self, figure, x, y):
        #print('Add...')
        temp2 = list(figure[2])
        for i in range(len(temp2)):
            if int(temp2[i]):
                self.board[y + i // figure[0]][x + i % figure[0]] = int(temp2[i])

    def del_line(self, n):
        #print('Deleting')
        for i in range(n, -1, -1):
            if i:
                self.board[i] = list(self.board[i - 1])
            else:
                self.board[i] = list([0] * self.xsize)
