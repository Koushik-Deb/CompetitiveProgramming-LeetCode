# Short answer
# Number of steps = number of divisions by 2 + number of subtractions = number of bitshifts + number of subtractions.
# Every non-zero binary number has a leading bit. The algorithm only stops when the leading bit is bitshifted enough to become the last bit and then it's subtracted by 1. Thus, number of bitshifts = number of bits that are not the leading bit = length of bitstring - 1. (Ex. 22 = 10110 requires 4 bitshifts for the number to become 1. 4 = length of bitstring - 1 = 5 - 1).

# As the number is shifted, each 1 eventually reaches the least significant bit position (the last, rightmost bit). A 1 in the last bit means the number is odd (which causes a subtraction), so the number of subtractions = number of 1s.

# number of steps = number of bitshifts + number of subtractions = (length of bitstring - 1) + number of 1s.

# Long answer
# The two operations in the problem are divide the number by 2 when even, or subtract 1 from the number when odd.
# In binary form, every even number will end in 0 (ex. 8 = 1000, 22 = 10110) and every odd number ends in 1 (5 = 101, 15 = 1111).
# So this last bit is important.

# Futhermore, every divide by 2 is equivalent to a single right bit shift (ex. 14 / 2 = 7 is the same as 1110 >> 1 = 111 = 7 where >> 1 is a single right shift). Thus, the goal is to count the number of bitshifts and the number of subtractions needed for the number to become 0.

# Now, if we think of any power of two, they always have a single 1 (ex. 16 = 10000, 128 = 10000000). In these cases, the algorithm would just be divide by 2 (equivalent to a single right bitshift) up until when? Remember, we ONLY subtract by 1 when the LAST bit is 1. So if we take a number like 16 = 10000. How many bit shifts will I do? Well there's a single 1 with four 0s blocking its path from becoming the last bit. Thus, the number of bitshifts is 4. After 4 bitshifts, our number is 1. So only 1 subtraction is needed. Thus, the number of steps = number of 0s + 1 (for the final subtraction) = 5 = length of bitstring. Said differently, the number of bitshifts = length of bitstring - 1

# Now, do we agree that every non-zero number has at least a 1 bit somewhere? Well if every non-zero number has at least 1 bit, then one of those 1 bits has to be the FIRST 1 bit doesn't it? Ex. 22 = 10110 has three 1 bits, so it has a FIRST 1 bit. Above, we saw 10000 has 4 bitshifts. How many bitshifts does 10110 require? Well, we stop shifting when the FIRST bit reaches the end, right? So other bits actually don't affect the number of shifts. Thus, the number of bitshifts is still going to be 4 = length of bitstring - 1. What about the number of subtractions? Well as we do a bitshift, each 1 eventually reaches the last position and if there's a 1 in the last position the algorithm dictates that we subtract 1 (ex. 1011 becomes 1010). This reduces the number of 1s in the bitstring. Since each 1 bit will eventually become the LAST bit, then the number of subtractions = number of 1s. Thus, the number of steps = length of bitstring - 1 + number of 1s


class Solution:
    def numberOfSteps (self, num: int) -> int:
        bitstring = bin(num)[2:] # [2:] will remove the '0b' that is prepended to each bitstring by bin()
        return len(bitstring) - 1 + bitstring.count('1')


class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while(num):
            if num&1:
                num-=1
            else:
                num = num>>1
            count+=1
        return count