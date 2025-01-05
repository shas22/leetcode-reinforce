class Solution:
   def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
       string_length = len(s)
       
       diff = [0] * (string_length + 1)
       
       for start, end, direction in shifts:
           if direction == 1:
               diff[start] += 1
               diff[end + 1] -= 1
           else:
               diff[start] -= 1
               diff[end + 1] += 1
       
       for i in range(1, string_length + 1):
           diff[i] += diff[i - 1]
       
       result = []

       for i in range(string_length):
           shift_count = diff[i] % 26
           
           if shift_count < 0:
               shift_count += 26
           
           current_char = ord(s[i]) - ord('a') 
           new_char = (current_char + shift_count) % 26  
           result.append(chr(new_char + ord('a')))
       
       return ''.join(result)