import pygame, sys, numpy

pygame.init()

window = pygame.display.set_mode((600, 600))
pygame.display.set_caption(('DotsGame'))

board = numpy.zeros((6, 6))

player = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    window.fill((100, 255, 100))


    # Drawin' lines

    for i in range(10):
        pygame.draw.line(window, (60, 100, 170), (0, i*100), (600, i*100), 5)
        pygame.draw.line(window, (60, 100, 170), (i*100, 0), (i*100, 600), 5)

    # Clickin'

    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        x = x // 100
        y = y // 100

        if player == 1:
            if board[x][y] == 0:
                board[x][y] = 1
                player = 2

        if player == 2:
            if board[x][y] == 0:
                board[x][y] = 2
                player = 1


    for x in range(6):
        for y in range(6):
            if board[x][y] == 1:
                    pygame.draw.rect(window, (200, 90, 90), (x*100+20, y*100+20, 50, 50))

            if board[x][y] == 2:
                    pygame.draw.rect(window, (90, 90, 200), (x*100+20, y*100+20, 50, 50))




    pygame.display.update()