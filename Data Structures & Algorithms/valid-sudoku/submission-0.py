class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        
        seen_rows = [set() for _ in range(rows)]
        seen_cols = [set() for _ in range(cols)]
        seen_boxes = [set() for _ in range(9)]

        for i in range(rows): 
            for j in range(cols):  
                val = board[i][j]
                if val == '.':
                    continue      
                
                if val in seen_rows[i]:
                    return False
                seen_rows[i].add(val)

                if val in seen_cols[j]:
                    return False
                seen_cols[j].add(val)

                box_index = (i // 3) * 3 + (j // 3)
                if val in seen_boxes[box_index]:
                    return False
                seen_boxes[box_index].add(val)
        
        return True
