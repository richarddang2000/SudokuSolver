import pygame
import time as t



grid =[
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


#--------- Initial Board Creation
pygame.font.init()

screen = pygame.display.set_mode((550, 550))

pygame.display.set_caption("sudoku solver and visualization")

screen.fill((255, 255, 255))

font = pygame.font.SysFont("comicsans", 20)
#draw lines
for i in range(0, 10):
    if (i % 3 == 0):
        pygame.draw.line(screen, (0, 0, 0), (50 + 50*i, 50), (50 + 50*i, 500), 4)
        pygame.draw.line(screen, (0, 0, 0), (50, 50 + 50*i), (500, 50 + 50*i), 4)
    pygame.draw.line(screen, (0, 0, 0), (50 + 50*i, 50), (50 + 50*i, 500), 2)
    pygame.draw.line(screen, (0, 0, 0), (50, 50 + 50*i), (500, 50 + 50*i), 2)

for i in range(0, 9):
    for j in range(0, 9):
        if grid[i][j] != 0:
            num = font.render(str(grid[i][j]), 1, (0, 0, 0))
            screen.blit(num, ((j + 1)*50 + 15, (i+1)*50 + 15))
#----- Where sudoku solving starts
def solveSudoku(grid):
    solved = solve(grid, 0, 0)
    return 


def solve(grid, i, j):
    #check out of bounds index
    if i == 9:
        return True #board is done and everything is valid
    if j == 9:
        return solve(grid, i + 1, 0) # end of row (last column), move to next row
    if grid[i][j] != 0:
        return solve(grid, i, j + 1)

    for n in range(1, 10): #test each number on every open cell
        if isValidSudoku(grid, i, j, n):
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((j + 1)*50 + 5, (i+1)*50 + 5, 40, 40))
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect((j + 1)*50, (i+1)*50, 50, 50), 4)
            num = font.render(str(n), 1, (0, 0, 0))
            screen.blit(num, ((j + 1)*50 + 15, (i+1)*50 + 15))
            pygame.display.update()
            #t.sleep(0.08)
            grid[i][j] = n 
            if solve(grid, i, j + 1):
                return True
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((j + 1)*50 + 5, (i+1)*50 + 5, 40, 40))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect((j + 1)*50, (i+1)*50, 50, 50), 4)
    num = font.render(str(0), 1, (0, 0, 0))
    screen.blit(num, ((j + 1)*50 + 15, (i+1)*50 + 15))
    pygame.display.update()
    #t.sleep(0.08)
    grid[i][j] = 0
    return False


def isValidSudoku(grid, row, column, n):
    grid[row][column] = n 
    for i in range(0, 9):
        for j in range(0, 9):
            if grid[i][j] != 0:
                if not isValid(grid, grid[i][j], i, j):
                    return False
    return True

#checks validity of number within row and column
def isValid(grid, num, row, column):
    count = 0
    #row and column validity
    for j in range(0, 9):
        if grid[row][j] == num:
            count += 1
        if grid[j][column] == num:
            count += 1
    
    #grid validity
    for i in range ((row//3)*3, (row//3)*3+3):
        for j in range((column//3)*3, (column//3)*3+3):
            if (grid[i][j] == num):
                count += 1
    return not count > 3
    #--------- Solving Done ------------------
    
pygame.display.update()
solveSudoku(grid)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()





