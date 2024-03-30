class Solution {
public:
    static bool valid(vector<vector<char>>& board, int r, int c, char k)
    {
        /* ----- [ CHECK FOR K IN ROW ] ----- */
        for (int i = 0; i < 9; i++)
        {
            if (k == board[r][i]) return false;
        }

        /* ----- [ CHECK FOR K IN COLUMN ] ----- */
        for (int i = 0; i < 9; i++)
        {
            if (k == board[i][c]) return false;
        }
        
        /* ----- [ CHECK FOR K IN BOX ] ----- */
        for (int i = (r / 3) * 3; i < (r / 3) * 3 + 3; i++)
        {
            for (int j = (c / 3) * 3; j < (c / 3) * 3 + 3; j++)
            {
                if (k == board[i][j]) return false;
            }
        }

        return true;
    }

    static bool solve(vector<vector<char>>& board, int r, int c)
    {
        if (r == 9) /* ----- [ END OF BOARD ] ----- */
        {
            return true;
        }
        else if (c == 9) /* ----- [ CHECK FOR K IN BOX ] ----- */
        {
            return solve(board, r + 1, 0);
        }
        else if (board[r][c] != '.') /* ----- [ CELL IS FILLED GO TO NEXT ] ----- */
        {
            return solve(board, r, c + 1);
        }
        else /* ----- [ CELL IS EMPTY ] ----- */
        {
            for (int k = 1; k <= 9; k++)
            {
                char x = k + '0';
                /* ----- [ K CAN BE PLACED ] ----- */
                if (valid(board, r, c, x))
                {
                    board[r][c] = x;

                    /* ----- [ BACKTRACK - GO TO NEXT CELL ] ----- */
                    if (solve(board, r, c + 1))
                    {
                        return true;
                    }
                    board[r][c] = '.';
                }
            }
        }

        /* ----- [ NO SOLUTION EXISTS ] ----- */
        return false;
    }

    void solveSudoku(vector<vector<char>>& board)
    {
        solve(board, 0, 0);
    }
};
