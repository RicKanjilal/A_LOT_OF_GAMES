import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Maze Game")
screen.bgcolor("black")
screen.setup(800, 600)

# Define colors
COLORS = ["white", "red"]

# Define player properties
player_size = 30

# Define maze properties
maze_width = 17
maze_height = 13

# Define levels
levels = []

def generate_maze():
    # Generate random maze using Prim's algorithm

    # Initialize maze with walls
    maze = [["X"] * maze_width for _ in range(maze_height)]

    # Select a random starting point
    start_row = random.randrange(0, maze_height, 2)
    start_col = random.randrange(0, maze_width, 2)
    maze[start_row][start_col] = " "

    # List to store walls
    walls = []
    if start_row - 2 >= 0:
        walls.append((start_row - 2, start_col, start_row - 1, start_col))
    if start_row + 2 < maze_height:
        walls.append((start_row + 2, start_col, start_row + 1, start_col))
    if start_col - 2 >= 0:
        walls.append((start_row, start_col - 2, start_row, start_col - 1))
    if start_col + 2 < maze_width:
        walls.append((start_row, start_col + 2, start_row, start_col + 1))

    # While there are walls
    while walls:
        # Randomly choose a wall
        wall = random.choice(walls)
        row1, col1, row2, col2 = wall

        # Check if the wall is valid
        if maze[row2][col2] == "X":
            # Carve a path
            maze[row1][col1] = " "
            maze[row2][col2] = " "

            # Add neighboring walls
            if row2 - 2 >= 0:
                walls.append((row2 - 2, col2, row2 - 1, col2))
            if row2 + 2 < maze_height:
                walls.append((row2 + 2, col2, row2 + 1, col2))
            if col2 - 2 >= 0:
                walls.append((row2, col2 - 2, row2, col2 - 1))
            if col2 + 2 < maze_width:
                walls.append((row2, col2 + 2, row2, col2 + 1))

        # Remove the wall from the list
        walls.remove(wall)

    # Return the generated maze
    return maze

# Generate 100 random mazes
for _ in range(100):
    maze = generate_maze()
    levels.append(maze)

# Set up game variables
current_level = 0
maze = levels[current_level]

# Create the player turtle
player = turtle.Turtle()
player.shape("square")
player.color("blue")
player.penup()
player.speed(0)
player.goto(0, 0)

# Create the maze turtles
turtles = []
for row in range(maze_height):
    for col in range(maze_width):
        if maze[row][col] == "X":
            turtle_ = turtle.Turtle()
            turtle_.shape("square")
            turtle_.color(random.choice(COLORS))
            turtle_.penup()
            turtle_.speed(0)
            x = col * player_size - (maze_width * player_size) / 2 + player_size / 2
            y = (maze_height - row) * player_size - (maze_height * player_size) / 2 - player_size / 2
            turtle_.goto(x, y)
            turtles.append(turtle_)

# Set up game states
GAME_START = 0
GAME_PLAYING = 1
GAME_OVER = 2
game_state = GAME_START

# Move player functions
def move_up():
    y = player.ycor() + player_size
    if y < HEIGHT / 2:
        player.sety(y)

def move_down():
    y = player.ycor() - player_size
    if y > -HEIGHT / 2:
        player.sety(y)

def move_left():
    x = player.xcor() - player_size
    if x > -WIDTH / 2:
        player.setx(x)

def move_right():
    x = player.xcor() + player_size
    if x < WIDTH / 2:
        player.setx(x)

# Keyboard bindings
screen.listen()
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Game loop
while True:
    # Check game states
    if game_state == GAME_PLAYING:
        # Check if player reached the end of the level
        if player.xcor() < -WIDTH / 2 or player.xcor() > WIDTH / 2 or player.ycor() < -HEIGHT / 2 or player.ycor() > HEIGHT / 2:
            current_level += 1
            if current_level >= len(levels):
                # No more levels, game over
                game_state = GAME_OVER
            else:
                # Load the next level
                maze = levels[current_level]

                # Reset player position
                player.goto(0, 0)

                # Reset maze colors
                for turtle_ in turtles:
                    turtle_.color(random.choice(COLORS))

        # Check for collision with walls
        for turtle_ in turtles:
            if player.distance(turtle_) < player_size:
                # If collision with a wall, reset player position
                player.goto(0, 0)

    if game_state == GAME_START:
        # Display start label
        start_label = turtle.Turtle()
        start_label.shape("square")
        start_label.color("black")
        start_label.penup()
        start_label.hideturtle()
        start_label.goto(0, 0)
        start_label.write("Press arrow keys to start", align="center", font=("Arial", 20, "normal"))

    elif game_state == GAME_OVER:
        # Display game over label
        end_label = turtle.Turtle()
        end_label.shape("square")
        end_label.color("red")
        end_label.penup()
        end_label.hideturtle()
        end_label.goto(0, 0)
        end_label.write("Game Over!", align="center", font=("Arial", 20, "normal"))

    turtle.update()

# Hide player turtle and screen
player.hideturtle()
screen.mainloop()