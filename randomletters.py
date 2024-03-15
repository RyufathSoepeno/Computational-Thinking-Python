import random

r = 10
FILLER = '.'

# Create a list to represent a row. The row at first is filled with FILLER '.'
line = [FILLER] * r

# Create a matrix. The matrix is the maze to walk.
a = []
for i in range(r):
    a.append(line[:])

# List to keep track of which positions have been filled with letters
filled_positions = set()

# A sequence of random walk steps. The below loop will settle the next letter.
letter = 'A'
while letter <= 'Z':
    # Find a random position for the current letter
    while True:
        x = random.randint(0, r - 1)
        y = random.randint(0, r - 1)
        if (x, y) not in filled_positions:
            filled_positions.add((x, y))
            a[x][y] = letter
            break

    # Update the letter to present
    letter = chr(ord(letter) + 1)

# Print the matrix
for i in range(r):
    print(' '.join(a[i]))
