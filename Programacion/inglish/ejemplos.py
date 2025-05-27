spacier = " " \
"\n" \
"\n" \
"\n" \
"\n" \
"\n" \
"\n" \

# Formatting in Python

# Aligning text: left, right, and center
# The ljust(), rjust(), and center() methods help position text neatly within a fixed space.
text = "Python"
print(text.ljust(30, '-'))
print(text.rjust(30, '-'))
print(text.center(30, '-'))

print(spacier)

# Formatting a title
print("Welcome to Python".upper().center(40, '='))

print(spacier)

# Creating a well-structured table using lists
headers = ["Name", "Age", "Country", "Occupation"]
rows = [
    ["Alice", 25, "USA", "Engineer"],
    ["Bob", 30, "UK", "Doctor"],
    ["Charlie", 22, "Canada", "Artist"],
    ["David", 28, "Germany", "Teacher"],
    ["Eve", 35, "France", "Scientist"]
]

# Print table headers with proper spacing
print(f'|{headers[0]:^12}|{headers[1]:^5}|{headers[2]:^10}|{headers[3]:^12}|')
print('-' * 45)  # Creates a visual separator

# Print table rows with formatted alignment
for row in rows:
    print(f'|{row[0]:^12}|{row[1]:^5}|{row[2]:^10}|{row[3]:^12}|')
