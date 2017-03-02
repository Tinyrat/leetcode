class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        heng = [[False for i in range(10)] for j in range(9)]
        shu = [[False for i in range(10)] for j in range(9)]
        gong = [[False for i in range(10)] for j in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    if heng[i][num] == True:
                        return False
                    else:
                        heng[i][num] = True
                    if shu[j][num] == True:
                        return False
                    else:
                        shu[j][num] = True
                    if i < 3 and j < 3:
                        gongNum = 0
                    elif i < 3 and j < 6:
                        gongNum = 1
                    elif i < 3 and j < 9:
                        gongNum = 2
                    elif i < 6 and j < 3:
                        gongNum = 3
                    elif i < 6 and j < 6:
                        gongNum = 4
                    elif i < 6 and j < 9:
                        gongNum = 5
                    elif i < 9 and j < 3:
                        gongNum = 6
                    elif i < 9 and j < 6:
                        gongNum = 7
                    else:
                        gongNum = 8
                    if gong[gongNum][num] == True:
                        return False
                    else:
                        gong[gongNum][num] = True
        return True
