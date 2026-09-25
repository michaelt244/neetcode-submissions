class Solution:
    def compress(self, chars: List[str]) -> int:
        compression = []
        left = 0
        write = 0

        while left < len(chars):

            #start at the current window
            char = chars[left]

            #set rigtht to the current charcter
            right = left

            #increase right until the last occurance of charcter
            while right < len(chars) and char == chars[right]:
                right += 1
            
            #get the count of how many consecutiver epeating characters we saw of the current charcter by right - left

            count = right - left

            #write the charcter in place
            chars[write] = char

            #increase to the next postion 
            write += 1

            #if there is more than one we need to add the digit if not add no digit and just the charcter that is already covered by the previous increase
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
            
            #then set left to the current right (the place where we have a new charcter to counts its consecturive reapeating charcters)
            left = right
        
        return write