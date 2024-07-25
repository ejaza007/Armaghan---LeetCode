class Solution:
    def intToRoman(self, num: int) -> str:
        # Define the mapping of Roman numeral symbols to integer values
        symlist = [
            ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
            ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
            ("X", 10), ("IX", 9), ("V", 5), ("IV", 4),
            ("I", 1)
        ]
        
        roman_numeral = ""
        
        # Iterate over the symlist
        for sym, val in symlist:
            while num >= val:
                roman_numeral += sym
                num -= val
                
        return roman_numeral

