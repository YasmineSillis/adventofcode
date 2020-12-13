input='''..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#'''

newInput=input.split('\n')
def split(line):
    return [char for char in line]
matrix=[]
for line in newInput:
    matrix.append(split(line))
#print(matrix[1][3])
current_row=0
current_column=0
aantal_bomen=0
while current_row<len(matrix):
    if matrix[current_row][current_column%len(matrix[current_row])] == '#':
        aantal_bomen +=1
    current_row +=1
    current_column +=3
print(aantal_bomen)