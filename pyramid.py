blocks = int(input("Enter the number of blocks: "))
height = 0
layer_blocks = 1  # Number of blocks in the current layer

while blocks >= layer_blocks:
  height += 1
  blocks -= layer_blocks
  layer_blocks += 1


# Input: Number of blocks

# Calculate and output the height of the pyramid
print(f"The height of the pyramid is: {height}")
