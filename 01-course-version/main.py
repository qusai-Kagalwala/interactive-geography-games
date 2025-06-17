# 🗺️ Day 25 - U.S. States Guessing Game
# Angela Yu's 100 Days of Code - Python Bootcamp
# Interactive Geography Learning Game with Turtle Graphics & Pandas

# ============================================================================
# 📚 LEARNING OBJECTIVES:
# - Combining Turtle Graphics with Pandas data analysis
# - Working with CSV coordinate data
# - Interactive user input with turtle.textinput()
# - List comprehensions and data filtering
# - Exporting learning progress to CSV files
# ============================================================================

# 📦 Import required libraries
import turtle  # For graphics, screen setup, and user interaction
import pandas  # For CSV data handling and manipulation

# ============================================================================
# 🖥️ GAME SETUP - Screen Configuration and Image Loading
# ============================================================================

# Create the main game screen
screen = turtle.Screen()
screen.title("U.S. States Game")  # Set window title

# 🗺️ Load and display the blank US map image
image = "blank_states_img.gif"  # Path to the blank US states map
screen.addshape(image)  # Register the image as a turtle shape
turtle.shape(image)  # Set the main turtle to display the map

# ============================================================================
# 📊 DATA LOADING - Read States and Coordinates from CSV
# ============================================================================

# 📖 Load the states data from CSV file
# CSV contains: state name, x-coordinate, y-coordinate for each state
data = pandas.read_csv("50_states.csv")

# 📝 Convert state names to a list for easy checking
# This creates a list of all 50 state names for validation
all_states = data.state.to_list()

# 🎯 Initialize game tracking variables
guessed_states = []  # List to store correctly guessed states

# ============================================================================
# 🎮 MAIN GAME LOOP - Interactive Guessing Game
# ============================================================================

# Continue the game until all 50 states are guessed
while len(guessed_states) < 50:

    # 💬 Get user input with current progress displayed
    # textinput() creates a popup dialog for user input
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    # 🐛 Debug: Print the user's answer (helpful for testing)
    print(answer_state)

    # ============================================================================
    # 🚪 EXIT MECHANISM - Save Learning Progress
    # ============================================================================

    # Check if user wants to exit the game
    if answer_state == "Exit":
        # 📝 Create a list of states that haven't been guessed yet
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        # 💾 Export the missing states to a CSV file for future study
        # This creates a "states_to_learn.csv" file with unguessed states
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break  # Exit the game loop

    # ============================================================================
    # ✅ CORRECT ANSWER HANDLING - Display State on Map
    # ============================================================================

    # Check if the guessed state is valid (exists in our data)
    if answer_state in all_states:
        # ✅ Add the correct guess to our tracking list
        guessed_states.append(answer_state)

        # 🐢 Create a new turtle to write the state name on the map
        t = turtle.Turtle()
        t.penup()  # Lift pen to move without drawing

        # 🎯 Get the coordinates for the guessed state
        # Filter the DataFrame to get the row for this specific state
        state_data = data[data.state == answer_state]

        # 📍 Move turtle to the state's coordinates on the map
        # .item() extracts the single coordinate value from the pandas Series
        t.goto(state_data.x.item(), state_data.y.item())

        # ✏️ Write the state name at its location on the map
        t.write(answer_state)

# ============================================================================
# 🎯 KEY CONCEPTS DEMONSTRATED:
# - turtle.Screen() for interactive graphics applications
# - pandas.read_csv() and DataFrame filtering
# - Interactive user input with textinput()
# - Coordinate-based positioning with turtle graphics
# - List operations and membership testing
# - CSV export for progress tracking
# - Game loop with exit conditions
# ============================================================================

# 🏆 GAME FEATURES:
# ✅ Interactive map-based learning
# ✅ Progress tracking (X/50 states)
# ✅ Visual feedback on correct answers
# ✅ Study aid generation (missing states CSV)
# ✅ Clean exit mechanism

# 📝 CHALLENGE COMPLETED: Built an educational geography game that combines
# data analysis with interactive graphics for effective learning!