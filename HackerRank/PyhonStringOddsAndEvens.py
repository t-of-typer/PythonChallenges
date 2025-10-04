# Read the number of test cases (t)
# input() reads a line from input as a string
# .strip() removes leading/trailing whitespace (like spaces/newlines)
# int(...) converts the string to an integer
t = int(input().strip())

# Run the loop t times, once for each test case
# We don’t care about the actual loop index, so we use "_"
for _ in range(t):
    # Read the string for this test case and strip leading/trailing spaces
    s = input().strip()
    
    # Slice notation: s[start:stop:step]
    # s[::2] → characters at indices 0, 2, 4, ... (even indices)
    even_chars = s[::2]
    
    # s[1::2] → characters at indices 1, 3, 5, ... (odd indices)
    odd_chars = s[1::2]
    
    # print() outputs both strings separated by a space (default sep=" ")
    # So output is: even_chars + " " + odd_chars
    print(even_chars, odd_chars)

# # Read number of test cases
# t = int(input().strip())

# # Loop over each test case
# for _ in range(t):
#     # Read the string for this test case
#     s = input().strip()
    
#     # Lists to hold even-indexed and odd-indexed characters
#     evens = []
#     odds = []
    
#     # enumerate(s) gives (index, character) pairs
#     for i, ch in enumerate(s):
#         if i % 2 == 0:      # If index is even
#             evens.append(ch)
#         else:               # If index is odd
#             odds.append(ch)
    
#     # ''.join(list) converts the list of characters back into a single string
#     # Print the results separated by a space
#     print(''.join(evens), ''.join(odds))
