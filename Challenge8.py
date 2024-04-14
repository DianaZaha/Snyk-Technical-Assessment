"""
An English text needs to be encrypted using the following encryption scheme.
First, the spaces are removed from the text. Let L be the length of this text.
Then, characters are written into a grid, whose rows and columns have the following
constraints: ⌊√L⌋ ≤ row ≤ column ≤ ⌈√L⌉, where ⌊x⌋ is floor function and ⌈x⌉ is a ceil function.
"""

def encrypt(str):
    words = str.split(" ")
    new_str = "".join(words)
    L = len(new_str)
    floor = int(L**(1/2))
    ceiling = floor+1
    characters = list(new_str)
    grid = []
    print("As plain text:")
    for i in range(floor):
        print("".join(characters[i*ceiling:(i+1)*ceiling]))
        grid.append(characters[i*ceiling:(i+1)*ceiling])
    print("\nAs grid form:")
    for i in grid:
        print(i)

encrypt("if man was meant to stay on the ground god would have given us roots")
print("")
encrypt(input("What sentence do you want to encrypt?\n"))