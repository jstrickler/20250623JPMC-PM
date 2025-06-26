def trimmed(file_name):
    with open(file_name) as file_in:
        for line in file_in:
            yield line.rstrip('\n\r')  # 'yield' causes this function to return a generator object

mary_in = trimmed('../DATA/mary.txt')
print(mary_in)
for trimmed_line in mary_in:
    print(trimmed_line)

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date"]

fruits_gen = (f.upper() for f in fruits)
print(fruits_gen)
for fruit in fruits_gen:
    print(fruit)
print()

# (VALUE for VARIABLE in ITERABLE)
trimmed_lines = (line.rstrip() for line in open('DATA/mary.txt'))
for line in trimmed_lines:
    print(line)

