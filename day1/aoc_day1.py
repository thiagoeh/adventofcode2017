#!/usr/bin/python3

# code for AdventOfCode day 1 http://adventofcode.com/2017/day/1

# get user input WITHOUT validation
# the code will fail when repeating non numeric chars
input_seq = input()


# append first algarism to the end of a new 'extended'
# that way we can use a single 'for' loop for everything
input_seq_extended = str(input_seq) + str(input_seq[0])


# initialize the output as an integer
# total_output = 0

for i in range(0, len(input_seq_extended)-1):
    # not sure if this checking of range happens every loop. 
    # # maybe its inefficient
    
    # permute all the input checking for repeated chars
    if input_seq_extended[i] == input_seq_extended[i+1]:
        print("Match! "+ str(i) + " Total output: " + str(total_output))
        total_output += int(input_seq_extended[i])        


print("Output: " + str(total_output))
