class Solution {

    int ROWS, COLS;
    boolean[][] path;

    public boolean exist(char[][] board, String word) {
        ROWS = board.length;
        COLS = board[0].length;

        path = new boolean[ROWS][COLS];

        for(int r = 0; r < ROWS; r++){
            for(int c = 0; c < COLS; c++){
                if(dfs(board, word, r, c, 0)){
                    return true;
                }
            }
        }
        return false;
    }

    boolean dfs(char[][] board, String word, int r, int c, int i){

        if(i == word.length()){
            return true;
        }

        if(r < 0 || c < 0 || r >= ROWS || c >= COLS ||
           board[r][c] != word.charAt(i) || path[r][c]){
            return false;
        }

        path[r][c] = true;

        boolean res =
            dfs(board, word, r + 1, c, i + 1) ||
            dfs(board, word, r - 1, c, i + 1) ||
            dfs(board, word, r, c + 1, i + 1) ||
            dfs(board, word, r, c - 1, i + 1);

        path[r][c] = false;

        return res;
    }
}