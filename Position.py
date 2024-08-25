#Marking an x on the grid of nested lists and rows
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? Column A, B or C? Lines 1,2 or 3?")
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
#this maybe refers to the second digit, since it is position 1 instead of position o?
# For example if the input is C2, the C is the 0 position and the 2 is the 1 position
# For C2, the 2 would represent 2-1 as 1 so because it goes, 0,1,2 instead of 1,2,3
map[number_index][letter_index] = "X"
#number_index is before letter because the letter is nested inside of the number so it is number first and then letter.
print(f"{line1}\n{line2}\n{line3}")
#\n is a space for each line to go to the next line.