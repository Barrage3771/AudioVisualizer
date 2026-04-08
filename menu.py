import pygame

def show_menu(screen):
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    font_title = pygame.font.SysFont("arial", 64)
    font_options = pygame.font.SysFont("arial", 36)

    title = font_title.render("Music Visualizer", True, (255, 255, 255))
    opt1 = font_options.render("1 - Frequency  (colors react to music)", True, (255, 255, 255))
    opt2 = font_options.render("2 - Monochrome (white particles)", True, (255, 255, 255))
    opt3 = font_options.render("3 - Rainbow    (cycles through colors)", True, (255, 255, 255))

    screen.fill((0, 0, 0))
    screen.blit(title, (screen_width // 2 - title.get_width() // 2, screen_height // 2 - 200))
    screen.blit(opt1,  (screen_width // 2 - opt1.get_width() // 2, screen_height // 2 - 50))
    screen.blit(opt2,  (screen_width // 2 - opt2.get_width() // 2, screen_height // 2 + 20))
    screen.blit(opt3,  (screen_width // 2 - opt3.get_width() // 2, screen_height // 2 + 90))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "frequency"
                if event.key == pygame.K_2:
                    return "monochrome"
                if event.key == pygame.K_3:
                    return "rainbow"
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()