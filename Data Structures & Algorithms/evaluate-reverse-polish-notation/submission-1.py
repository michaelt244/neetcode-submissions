class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        numbers = []
        operations = ["+", "-", "*", "/"]

        for token in tokens:
            if token in operations:
                num1 = numbers.pop()
                num2 = numbers.pop()
                if token == "+":
                    numbers.append(num1 + num2)
                elif token == "-":
                    numbers.append(num2 - num1)
                elif token == "*":
                    numbers.append(num2 * num1)
                else:
                    numbers.append(int(num2 / num1))
            else:
                numbers.append(int(token))
        
        return numbers.pop()