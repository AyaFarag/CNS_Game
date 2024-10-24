import pygame
import random
import webbrowser  # Necessary for opening the registration link

# Initialize Pygame
pygame.init()

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BRICK_WIDTH = 80
BRICK_HEIGHT = 30
BALL_RADIUS = 10
PADDLE_WIDTH = 150
PADDLE_HEIGHT = 10
BALL_SPEED_X = 7
BALL_SPEED_Y = -7

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)  # Black for the paddle
BLUE = (0, 0, 255)  # Blue for the ball
SILVER = (192, 192, 192)
BLUE_BLACK = (10, 10, 40)  # Blue-Black color for the "Game Over" text

# Game setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bricks Breaker")
copilot_background = pygame.image.load(r"C:\Users\AttyaM\OneDrive - cns-me.com\Desktop\VS Code\breaker game\Copilot.jpg")
copilot_background = pygame.transform.scale(copilot_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
microsoft_logo = pygame.image.load(r"C:\Users\AttyaM\OneDrive - cns-me.com\Desktop\VS Code\breaker game\microsoft_logo.png")
microsoft_logo = pygame.transform.scale(microsoft_logo, (BRICK_WIDTH, BRICK_HEIGHT))
cns_logo = pygame.image.load(r"C:\Users\AttyaM\OneDrive - cns-me.com\Desktop\VS Code\breaker game\CNS.png")
cns_logo = pygame.transform.scale(cns_logo, (BRICK_WIDTH, BRICK_HEIGHT))

ball = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed = [BALL_SPEED_X, BALL_SPEED_Y]
paddle = pygame.Rect(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - 30, PADDLE_WIDTH, PADDLE_HEIGHT)
bricks = [pygame.Rect(col * BRICK_WIDTH, row * BRICK_HEIGHT, BRICK_WIDTH, BRICK_HEIGHT) for row in range(5) for col in range(10)]
score = 0
font = pygame.font.Font(None, 36)

# Registration Link
REGISTRATION_LINK = "https://forms.office.com/Pages/ResponsePage.aspx?id=Se8oF0VYv0ij-tILIIJR2WHObAW-S8lKjVDM86zOFEpUNUtBQk81Tko4SDlIRTgwVExNWkxSSTU5Sy4u"

# Game Loop
clock = pygame.time.Clock()
running = True
game_over = False
win = False  # Flag to check if the player has won

while running:
    screen.blit(copilot_background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_x = pygame.mouse.get_pos()[0]
    paddle.x = mouse_x - PADDLE_WIDTH // 2

    if not game_over:
        ball.x += ball_speed[0]
        ball.y += ball_speed[1]

        # Ball collision with walls
        if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
            ball_speed[0] = -ball_speed[0]
        if ball.top <= 0:
            ball_speed[1] = -ball_speed[1]
        # Check if ball misses the paddle
        if ball.bottom >= SCREEN_HEIGHT:
            game_over = True

        # Ball collision with the paddle
        if ball.colliderect(paddle):
            ball_speed[1] = -ball_speed[1]

        # Ball collision with bricks
        for brick in bricks[:]:
            if ball.colliderect(brick):
                ball_speed[1] = -ball_speed[1]  # Bounce the ball back
                bricks.remove(brick)
                score += 10

        # Check if all bricks are destroyed
        if not bricks:
            win = True
            game_over = True  # To stop the ball movement

    # Drawing the paddle and the ball
    pygame.draw.rect(screen, BLACK, paddle)
    pygame.draw.ellipse(screen, BLUE, ball)

    # Drawing the bricks
    for index, brick in enumerate(bricks):
        if index % 2 == 0:
            screen.blit(microsoft_logo, brick)
        else:
            screen.blit(cns_logo, brick)

    # Displaying the score
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (20, 20))

    # Handling game over state
    if game_over:
        if win:
            win_text = "Congratulations, " + username + "! You Won!"
            win_message = font.render(win_text, True, BLUE_BLACK)
            win_rect = win_message.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50))
            screen.blit(win_message, win_rect)
            
            # Add celebration effects (e.g., fireworks)
            for _ in range(10):  # Create 10 fireworks
                # (Implement your fireworks effect here)
            
            pygame.display.flip()
            pygame.time.delay(3000)  # Show the message for 3 seconds
            # Optionally, redirect to another page or restart the game
        else:
            game_over_text = font.render("Game Over", True, BLUE_BLACK)
            text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
            screen.blit(game_over_text, text_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()