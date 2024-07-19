class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # Initialize pointers for both strings
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []

        # Loop through both strings from end to start
        while i >= 0 or j >= 0 or carry:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0

            # Calculate the sum of current digits and the carry
            total = n1 + n2 + carry
            carry = total // 10  # Compute the carry for the next iteration
            result.append(str(total % 10))  # Append the current digit to the result

            i -= 1
            j -= 1

        # Since we appended digits in reverse order, we need to reverse the result
        return ''.join(result[::-1])

        