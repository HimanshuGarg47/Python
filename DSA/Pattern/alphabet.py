name = input("Enter your name: ")

# Define the pattern for each letter
patterns = [
    "  *  \n * * \n*****\n*   *\n*   *", # A
    "**** \n*   *\n**** \n*   *\n**** ", # B
    " *** \n*   *\n*    \n*   *\n *** ", # C
    "**** \n*   *\n*   *\n*   *\n**** ", # D
    "*****\n*    \n**** \n*    \n*****", # E
    "*****\n*    \n**** \n*    \n*    ", # F
    " *** \n*    \n* ** \n*   *\n *** ", # G
    "*   *\n*   *\n*****\n*   *\n*   *", # H
    "*****\n  *  \n  *  \n  *  \n*****", # I
    "  ***\n   * \n   * \n*  * \n **  ", # J
    "*   *\n*  * \n***  \n*  * \n*   *", # K
    "*    \n*    \n*    \n*    \n*****", # L
    "*   *\n** **\n* * *\n*   *\n*   *", # M
    "*   *\n**  *\n* * *\n*  **\n*   *", # N
    " *** \n*   *\n*   *\n*   *\n *** ", # O
    "**** \n*   *\n**** \n*    \n*    ", # P
    " *** \n*   *\n* * *\n*  **\n *** ", # Q
    "**** \n*   *\n**** \n*  * \n*   *", # R
    " *** \n*    \n **  \n   * \n***  ", # S
    "*****\n  *  \n  *  \n  *  \n  *  ", # T
    "*   *\n*   *\n*   *\n*   *\n *** ", # U
    "*   *\n*   *\n * * \n * * \n  *  ", # V
    "*   *\n*   *\n* * *\n** **\n*   *", # W
    "*   *\n * * \n  *  \n * * \n*   *", # X
    "*   *\n * * \n  *  \n  *  \n  *  ", # Y
    "*****\n   * \n  *  \n *   \n*****"  # Z
]

# Define a dictionary mapping letters to patterns
alphabet_patterns = dict(zip(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), patterns))

# Print out the name in pattern characters
for row in range(5):
    for char in name.upper():
        print(alphabet_patterns[char][row], end=" ")
    print()
