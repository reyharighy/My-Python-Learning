"""Main module that handles all game logics."""

# import necessary libraries
import time
from turtle import Screen
from snake_class import Snake
from food_class import Food
from score_class import Score
from wall_class import Wall, BOTTOM_LEFT_CORNER, TOP_RIGHT_CORNER
from const import SCREEN_WIDTH, SCREEN_HEIGHT, STEP

# setup the screen
SCREEN = Screen()

SCREEN.setup(
    width=SCREEN_WIDTH,
    height=SCREEN_HEIGHT,
    startx=0,
    starty=0
)

SCREEN.bgcolor("black")
SCREEN.title(titlestring="My Snake Game")
SCREEN.tracer(n=0) # wait for the screen update to render

# initialize the game
snake = Snake()

# spawn the food at the start of the game
food = Food(snake_positions=snake.snake_positions())
score = Score()
wall = Wall()

# listen to keyboard inputs to control the snake
keys_functions: dict[Snake] = {
    "Up": snake.head_north,
    "Down": snake.head_south,
    "Left": snake.head_west,
    "Right": snake.head_east
}

for key, func in keys_functions.items():
    SCREEN.onkeypress(
        fun=func,
        key=key
    )

SCREEN.listen()

# game on
game_on: bool = True

while game_on:
    SCREEN.update() # render the updated screen
    time.sleep(.1) # wait before each screen update
    snake.move()

    # check if the snake head hits its body segments and get its current positions
    current_positions = [] # refresh the list to store the current positions

    for segment in snake.the_snake:
        # store the current positions of each segment
        current_positions.append((int(segment.xcor()), int(segment.ycor())))

        if segment == snake.snake_head: # exclude the snake head
            pass
        elif snake.snake_head.distance(segment) < int(STEP / 2):
            score.game_over()
            game_on: bool = False
            break

    # check if the snake head hits the food
    if snake.snake_head.distance(food) < int(STEP / 2):
        score.increase_score()
        snake.extend()

        # pass the current positions list to refresh the food location
        food.refresh(food_positions=food.where(
            snake_positions=snake.snake_positions(current_positions=current_positions)
        ))

    # check if the snake head hits the wall
    if snake.snake_head.xcor() >= TOP_RIGHT_CORNER["x"] or \
        snake.snake_head.xcor() <= BOTTOM_LEFT_CORNER["x"] or \
            snake.snake_head.ycor() >= TOP_RIGHT_CORNER["y"] or \
                snake.snake_head.ycor() <= BOTTOM_LEFT_CORNER["y"]:
        score.game_over()
        game_on: bool = False

# close the screen when clicking on the screen
SCREEN.exitonclick()
