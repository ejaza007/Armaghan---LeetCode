class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create an array to hold strings for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False
        
        # Iterate over each character in the string
        for char in s:
            # Append the current character to the current row
            rows[current_row] += char
            
            # If we are at the first or last row, reverse direction
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            # Move up or down to the next row
            current_row += 1 if going_down else -1
        
        # Concatenate all rows to get the final string
        return ''.join(rows)

# Example usage
solution = Solution()
string = "PAYPALISHIRING"
num_rows = 3
print(f"The Zigzag Conversion of '{string}' with {num_rows} rows is '{solution.convert(string, num_rows)}'")
