import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (128, 128, 128)

# Set up the display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def draw_text(surface, text, size, x, y, color):
    font = pygame.font.Font(pygame.font.match_font('arial'), size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN
        self.score = 0

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = ((cur[0] + x) % GRID_WIDTH, (cur[1] + y) % GRID_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            return False
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()
            return True

    def reset(self):
        self.length = 1
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0] * GRID_SIZE, p[1] * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, BLACK, r, 1)

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1))

    def draw(self, surface):
        r = pygame.Rect((self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, BLACK, r, 1)

def show_start_screen():
    screen.fill(BLACK)
    draw_text(screen, "Snake Game", 64, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 4, WHITE)
    draw_text(screen, "Use arrow keys to move", 22, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, WHITE)
    draw_text(screen, "Press any key to play", 22, WINDOW_WIDTH / 2, WINDOW_HEIGHT * 3 / 4, WHITE)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                waiting = False

def show_game_over_screen(score):
    screen.fill(BLACK)
    draw_text(screen, "GAME OVER", 64, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 4, RED)
    draw_text(screen, f"Score: {score}", 30, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, WHITE)
    draw_text(screen, "Press 'R' to play again or 'Q' to quit", 22, WINDOW_WIDTH / 2, WINDOW_HEIGHT * 3 / 4, WHITE)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_r:
                    waiting = False

def main():
    game_over = True
    running = True
    snake = Snake()
    food = Food()

    while running:
        if game_over:
            if snake.score > 0:
                show_game_over_screen(snake.score)
            else:
                show_start_screen()
            game_over = False
            snake.reset()
            food.randomize_position()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.turn(UP)
                elif event.key == pygame.K_DOWN:
                    snake.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    snake.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.turn(RIGHT)

        if not snake.move():
            game_over = True

        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            food.randomize_position()

        screen.fill(BLACK)
        snake.draw(screen)
        food.draw(screen)
        draw_text(screen, f"Score: {snake.score}", 24, WINDOW_WIDTH / 2, 10, WHITE)
        pygame.display.update()
        clock.tick(15)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
