class Solution:
    def compress(self, chars: List[str]) -> int:
        compression = []
        left = 0
        write = 0

        while left < len(chars):
            char = chars[left]
            right = left

            while right < len(chars) and char == chars[right]:
                right += 1
            
            count = right - left

            chars[write] = char
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
            
            left = right
        

        print(chars)
        return write