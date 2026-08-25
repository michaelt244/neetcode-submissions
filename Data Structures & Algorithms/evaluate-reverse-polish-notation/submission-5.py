class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        
        numbers = []
        operations = {"+", "-", "*", "/"}

        for token in tokens:
            #if the token is not a number we perform the arithmetic
            if token in operations:
                #poping the two numbers in the stack
                num1 = numbers.pop()
                num2 = numbers.pop()
                
                #peforming the arithmetic, num2 is the first number, num1 is the latest number
                if token == "+":
                    numbers.append(num1 + num2)
                elif token == "-":
                    numbers.append(num2 - num1)
                elif token == "*":
                    numbers.append(num2 * num1)
                else:
                    numbers.append(int(num2 / num1))
            else:
                #if the token we add it to the stack
                #ready to pop when we have an arithmetic
                numbers.append(int(token))
        
        #return the number in the stack
        #assuming we did all the math we should only the 
        #cumlative sum in the stack so we can just pop it
        return numbers.pop()