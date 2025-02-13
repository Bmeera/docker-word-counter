# File: word_counter.py

# Define the filename where results will be saved
filename = "/app/data/word_count.txt"

# Welcome Message
print("Welcome to Word Counter!\nThe console application that counts your words.")

print("No matter how lenghty, convoluted, or you know \"uncountable\" the words are, Word Counter can count them!")

# Get user input
text = input("To begin, please enter the sentence: ")

# Count the number of words
word_count = len(text.split())
print(f"The word count is {word_count} ")

# Save the result in a text file
with open(filename, "w") as f:
    f.write(f"The word count is {word_count}\n")

print(f"Word count saved to {filename}")
