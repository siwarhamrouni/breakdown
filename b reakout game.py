import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Breakout Game')

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

# Paddle properties
paddle_width = 100
paddle_height = 10
paddle_speed = 10
paddle = pygame.Rect(screen_width // 2 - paddle_width // 2, screen_height - 30, paddle_width, paddle_height)

# Ball properties
ball_radius = 10
ball_speed = [random.choice([-5, 5]), -5]
ball = pygame.Rect(screen_width // 2 - ball_radius, screen_height // 2 - ball_radius, ball_radius * 2, ball_radius * 2)

# Brick properties
brick_rows = 5
brick_cols = 8
brick_width = 75
brick_height = 20
bricks = []
for row in range(brick_rows):
    for col in range(brick_cols):
        brick = pygame.Rect(col * (brick_width + 10) + 35, row * (brick_height + 10) + 35, brick_width, brick_height)
        bricks.append(brick)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < screen_width:
        paddle.right += paddle_speed

    # Ball movement
    ball.left += ball_speed[0]
    ball.top += ball_speed[1]

    # Ball collision with walls
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]
    if ball.bottom >= screen_height:
        running = False  # Game over

    # Ball collision with paddle
    if ball.colliderect(paddle):
        ball_speed[1] = -ball_speed[1]

    # Ball collision with bricks
    for brick in bricks:
        if ball.colliderect(brick):
            ball_speed[1] = -ball_speed[1]
            bricks.remove(brick)
            break

    # Clear screen
    screen.fill(black)

    # Draw paddle
    pygame.draw.rect(screen, blue, paddle)

    # Draw ball
    pygame.draw.ellipse(screen, red, ball)

    # Draw bricks
    for brick in bricks:
        pygame.draw.rect(screen, green, brick)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
