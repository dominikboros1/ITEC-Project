import pygame

pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
obstacle_x = 400
obstacle_y = 400
obstacle_width = 40
obstacle_height = 40
player_x = 200
player_y = 400
player_width = 20
player_height = 20
game_state = "start_menu"
dt = 0
pygame.display.set_caption('Echoes of Eden')
bg = pygame.image.load("./images/background.jpg")

def draw_start_menu():
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', 40)
    title = font.render('My Game', True, (255, 255, 255))
    start_button = font.render('Start', True, (255, 255, 255))
    screen.blit(title, (screen_width / 2 - title.get_width() / 2, screen_height / 2 - title.get_height() / 2))
    screen.blit(start_button,
                (screen_width / 2 - start_button.get_width() / 2, screen_height / 2 + start_button.get_height() / 2))
    pygame.display.update()


def draw_game_over_screen():
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', 40)
    title = font.render('Game Over', True, (255, 255, 255))
    restart_button = font.render('R - Restart', True, (255, 255, 255))
    quit_button = font.render('Q - Quit', True, (255, 255, 255))
    screen.blit(title, (screen_width / 2 - title.get_width() / 2, screen_height / 2 - title.get_height() / 3))
    screen.blit(restart_button,
                (screen_width / 2 - restart_button.get_width() / 2, screen_height / 1.9 + restart_button.get_height()))
    screen.blit(quit_button,
                (screen_width / 2 - quit_button.get_width() / 2, screen_height / 2 + quit_button.get_height() / 2))
    pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    if game_state == "start_menu":
        draw_start_menu()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            player_x = 200
            player_y = 400
            game_state = "game"
            game_over = False
    elif game_state == "game_over":
        draw_game_over_screen()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            game_state = "start_menu"
        if keys[pygame.K_q]:
            pygame.quit()
            quit()

    elif game_state == "game":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_y -= 300 * dt
        if keys[pygame.K_s]:
            player_y += 300 * dt
        if keys[pygame.K_a]:
            player_x -= 300 * dt
        if keys[pygame.K_d]:
            player_x += 300 * dt

        if player_x + player_width > obstacle_x and player_x < obstacle_x + obstacle_width and player_y + player_height > obstacle_y and player_y < obstacle_y + obstacle_height:
            game_over = True
            game_state = "game_over"

        screen.blit(bg, (0, 0))
        pygame.draw.rect(screen, (255, 0, 0), (obstacle_x, obstacle_y, obstacle_width, obstacle_height))
        pygame.draw.circle(screen, "white", (player_x, player_y), 40)
        pygame.display.update()
        dt = clock.tick(60) / 1000

    elif game_over:
        game_state = "game_over"
        game_over = False