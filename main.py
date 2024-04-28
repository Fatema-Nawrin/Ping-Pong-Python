import pygame
import random


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700

COLOR_BG = (29, 35, 50)
COLOR_BALL = (170, 238, 187)
COLOR_SCORE = (255, 255, 255)

def main(): 
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pong game")

    clock = pygame.time.Clock()
    started = False

    paddle_1_rect = pygame.Rect(50, 0, 7, 100)
    paddle_2_rect = pygame.Rect(SCREEN_WIDTH - 50, 0, 7, 100)

    paddle_1_move = 0
    paddle_2_move = 0
    ball_rect = pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 20, 20)

    ball_accel_x = random.randint(2, 3) * 0.1
    ball_accel_y = random.randint(2, 4) * 0.1

    if random.randint(1, 2) == 1:
        ball_accel_x *= -1
    if random.randint(1, 2) == 1:
        ball_accel_y *= -1

    score_1 = 0
    score_2 = 0

    # GAME LOOP
    while True:
        screen.fill(COLOR_BG)

        if not started:
            font = pygame.font.SysFont('Verdana', 20)
            # draw some text to the center of the screen
            text = font.render('Press Space', True, COLOR_BALL)
            text_rect = text.get_rect()
            text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            screen.blit(text, text_rect)
            pygame.display.flip()
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        started = True
            continue

        delta_time = clock.tick(60)

        # checking for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    paddle_1_move = -0.5
                if event.key == pygame.K_s:
                    paddle_1_move = 0.5
                if event.key == pygame.K_UP:
                    paddle_2_move = -0.5
                if event.key == pygame.K_DOWN:
                    paddle_2_move = 0.5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s: 
                    paddle_1_move = 0.0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    paddle_2_move = 0.0

        paddle_1_rect.top += paddle_1_move * delta_time
        paddle_2_rect.top += paddle_2_move * delta_time

        if paddle_1_rect.top < 0:
            paddle_1_rect.top = 0
        if paddle_1_rect.bottom > SCREEN_HEIGHT:
            paddle_1_rect.bottom = SCREEN_HEIGHT
        if paddle_2_rect.top < 0:
            paddle_2_rect.top = 0
        if paddle_2_rect.bottom > SCREEN_HEIGHT:
            paddle_2_rect.bottom = SCREEN_HEIGHT      

        if ball_rect.top < 0:
            ball_accel_y *= -1
            ball_rect.top = 0
        if ball_rect.bottom > SCREEN_HEIGHT - ball_rect.height:
            ball_accel_y *= -1
            ball_rect.top = SCREEN_HEIGHT - ball_rect.height-30

        if ball_rect.left <= 0:
            score_2 += 1
            reset_ball(ball_rect)
        elif ball_rect.right >= SCREEN_WIDTH:
            score_1 += 1
            reset_ball(ball_rect)

        if paddle_1_rect.colliderect(ball_rect) and paddle_1_rect.left < ball_rect.left:
            ball_accel_x *= -1
            ball_rect.left += 5
        if paddle_2_rect.colliderect(ball_rect) and paddle_2_rect.left > ball_rect.left:
            ball_accel_x *= -1
            ball_rect.left -= 5

        if started:
            # move the ball
            ball_rect.left += ball_accel_x * delta_time 
            ball_rect.top += ball_accel_y * delta_time

        pygame.draw.rect(screen, COLOR_BALL, paddle_1_rect)
        pygame.draw.rect(screen, COLOR_BALL, paddle_2_rect)
        pygame.draw.rect(screen, COLOR_BALL, ball_rect)

        # Display scores
        font = pygame.font.SysFont('Verdana', 15)
        score_text_1 = font.render(str(score_1), True, COLOR_SCORE)
        score_rect_1 = score_text_1.get_rect()
        score_rect_1.bottomleft = (SCREEN_WIDTH/2- 25 , SCREEN_HEIGHT - 20)
        screen.blit(score_text_1, score_rect_1)

        score_text_2 = font.render("  -  "+ str(score_2), True, COLOR_SCORE)
        score_rect_2 = score_text_2.get_rect()
        score_rect_2.bottomright = (SCREEN_WIDTH/2 +25, SCREEN_HEIGHT - 20)
        screen.blit(score_text_2, score_rect_2)

        pygame.display.update()

def reset_ball(ball_rect):
    ball_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

# run the game
if __name__ == '__main__':
    main()
