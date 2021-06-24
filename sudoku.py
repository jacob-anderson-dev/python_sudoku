import pygame

pygame.font.init()
font1 = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsans", 20)
screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Sudoku")
img = pygame.image.load('icon.png')
pygame.display.set_icon(img)
 
x = 0
y = 0
difference = 500 / 9
value = 0

# Will allow saving and loading boards later
grid =[
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

def getCord(position):
    # Using floor division to go to nearest square
    global x
    x = position[0]//difference
    global y
    y = position[1]//difference

def highlightCell():
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * difference-3, (y + i)*difference), (x * difference + difference + 3, (y + i)*difference), 7)
        pygame.draw.line(screen, (255, 0, 0), ( (x + i)* difference, y * difference ), ((x + i) * difference, y * difference + difference), 7)  
        
def drawGrid():
    fillGridValues()
    drawGridLines()
    
def fillGridValues():
    for i in range (9):
        for j in range (9):
            if grid[i][j]!= 0:
 
                # Fill blue color in already numbered grid
                pygame.draw.rect(screen, (0, 188, 76), (i * difference, j * difference, difference + 1, difference + 1))
 
                # Fill grid with default numbers specified
                text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
                screen.blit(text1, (i * difference + 15, j * difference + 15))

def drawGridLines():
    for i in range(10):
        # Every 3rd line must be thicker
        if i % 3 == 0 :
            thickness = 7
        else:
            thickness = 1

        pygame.draw.line(screen, (0, 0, 0), (0, i * difference), (500, i * difference), thickness)
        pygame.draw.line(screen, (0, 0, 0), (i * difference, 0), (i * difference, 500), thickness)   
     
def drawValue(value):
    # Fill value entered in cell 
    text1 = font1.render(str(value), 1, (0, 0, 0))
    screen.blit(text1, (x * difference + 15, y * difference + 15))   

def raiseError(attempt):
    text1 = font1.render("You can't put {} there".format(attempt), 1, (0, 0, 0))
    screen.blit(text1, (20, 570)) 
 
def checkValidity(gridToCheck, i, j, value):
    # Check if the value entered in board is valid
    for it in range(9):
        if gridToCheck[i][it]== value:
            return False
        if gridToCheck[it][j]== value:
            return False

    it = i//3
    jt = j//3

    for i in range(it * 3, it * 3 + 3):
        for j in range (jt * 3, jt * 3 + 3):
            if gridToCheck[i][j]== value:
                return False

    return True

def checkGridComplete(grid, i, j):
    while grid[i][j] != 0:
        if i < 8:
            i += 1
        elif i == 8 and j < 8:
            i = 0
            j += 1
        elif i == 8 and j == 8:
            return True

    return False

def displayInstructions():
    text1 = font2.render("Press D to reset the game / R to empty the board", 1, (0, 0, 0))
    text2 = font2.render("Click or use arrow keys to select a cell, then type a number", 1, (0, 0, 0))
    screen.blit(text1, (20, 520))       
    screen.blit(text2, (20, 540))
 
def displayResults():
    text1 = font1.render("You did it! You win! Press D or R to start over", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))   


# Main Game Loop


run = True
shouldHighlightCell = False
shouldRaiseError = False
attempt = 0

while run:

    screen.fill((255, 255, 255))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False 
 
        if event.type == pygame.MOUSEBUTTONDOWN:
            shouldHighlightCell = True
            position = pygame.mouse.get_pos()
            getCord(position)

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                x-= 1
                shouldHighlightCell = True
            if event.key == pygame.K_RIGHT:
                x+= 1
                shouldHighlightCell = True
            if event.key == pygame.K_UP:
                y-= 1
                shouldHighlightCell = True
            if event.key == pygame.K_DOWN:
                y+= 1
                shouldHighlightCell = True   

            if event.key == pygame.K_1:
                value = 1
            if event.key == pygame.K_2:
                value = 2   
            if event.key == pygame.K_3:
                value = 3
            if event.key == pygame.K_4:
                value = 4
            if event.key == pygame.K_5:
                value = 5
            if event.key == pygame.K_6:
                value = 6
            if event.key == pygame.K_7:
                value = 7
            if event.key == pygame.K_8:
                value = 8
            if event.key == pygame.K_9:
                value = 9

            # If R pressed clear the sudoku board
            if event.key == pygame.K_r:
                grid =[
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]

            # If D is pressed reset the board to default
            if event.key == pygame.K_d:
                grid =[
                    [7, 8, 0, 4, 0, 0, 1, 2, 0],
                    [6, 0, 0, 0, 7, 5, 0, 0, 9],
                    [0, 0, 0, 6, 0, 1, 0, 7, 8],
                    [0, 0, 7, 0, 4, 0, 2, 6, 0],
                    [0, 0, 1, 0, 5, 0, 9, 3, 0],
                    [9, 0, 4, 0, 6, 0, 0, 0, 5],
                    [0, 7, 0, 3, 0, 0, 0, 1, 2],
                    [1, 2, 0, 0, 0, 7, 4, 0, 0],
                    [0, 4, 9, 2, 0, 6, 0, 0, 7]
                ]

    drawGrid()
    displayInstructions()

    if value != 0:          

        drawValue(value)

        if checkValidity(grid, int(x), int(y), value):
            grid[int(x)][int(y)] = value
            shouldHighlightCell = False
            shouldRaiseError = False
        else:
            grid[int(x)][int(y)] = 0
            shouldRaiseError = True 
            attempt = value

        value = 0 

    if checkGridComplete(grid, 0, 0):
        displayResults()   

    if shouldHighlightCell:
        highlightCell()

    if shouldRaiseError:
        raiseError(attempt)   
 
    pygame.display.update() 

pygame.quit()  