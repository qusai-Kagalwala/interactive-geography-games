# 🇮🇳 Day 25 - India States Geography Game
# Angela Yu's 100 Days of Code - Python Bootcamp (Personal Version - Not US States)
# Interactive geography quiz game for learning Indian States and Union Territories

# ============================================================================
# 📚 LEARNING OBJECTIVES:
# - Working with CSV data using pandas
# - Turtle graphics for interactive games
# - User input handling with GUI dialogs
# - Data filtering and manipulation
# - Creating study materials from game results
# ============================================================================

# 📦 Import required libraries
import turtle    # For graphics and game interface
import pandas    # For CSV data handling and manipulation
from debugpy.adapter.components import missing  # Debug import (unused in this code)

# ============================================================================
# 🎮 GAME SETUP: Initialize the game screen and load map
# ============================================================================

# 🖥️ Step 1: Create and configure the game screen
screen = turtle.Screen()
screen.title("India States Game")  # Set window title

# 🗺️ Step 2: Load and display the India map background
image = "blank_states_img.gif"  # Background image file (India map outline)
screen.addshape(image)          # Register the image as a turtle shape
turtle.shape(image)             # Set the background turtle to display the map

# ============================================================================
# 📊 DATA LOADING: Read state information from CSV file
# ============================================================================

# 📖 Step 3: Load the CSV containing state names and coordinates
# CSV structure expected: columns for 'state', 'x', 'y' coordinates
data = pandas.read_csv("28_states_8_u.t.csv")  # 28 states + 8 union territories data
all_states = data.state.to_list()              # Convert state column to list for easy checking
guessed_states = []                             # Track correctly guessed states

# ============================================================================
# 🎯 MAIN GAME LOOP: Interactive guessing game
# ============================================================================

# 🔄 Step 4: Game loop - continues until 50 correct guesses or user exits
# Note: 50 seems high for 28 states + 8 UTs (36 total), might be a placeholder
while len(guessed_states) < 50:
    
    # 💬 Step 5: Get user input with current progress displayed
    # Using turtle's built-in dialog box for clean user interaction
    answer_state = screen.textinput(title=f"{len(guessed_states)}/31 States Correct",
                                    prompt="What's another state's name?").title()
    print(answer_state)  # 🐛 Debug output to console
    
    # ❌ Step 6: Handle exit condition
    # User can type "Exit" to quit game and get study materials
    if answer_state == "Exit":
        # 📝 Create list of states the user hasn't guessed yet
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        
        # 💾 Save missed states to CSV file for future study
        # This creates a personalized study guide based on mistakes
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        print("📚 Study file 'states_to_learn.csv' created!")
        break
    
    # ✅ Step 7: Check if the guessed state is correct
    if answer_state in all_states:
        guessed_states.append(answer_state)  # Add to correct guesses list
        
        # 🐢 Step 8: Create turtle to write state name on map
        t = turtle.Turtle()
        t.hideturtle()  # Hide the turtle icon (cleaner appearance)
        t.penup()       # Don't draw lines when moving
        
        # 📍 Step 9: Get coordinates and place state name on map
        # Filter data to get x,y coordinates for the correctly guessed state
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())  # Move to state location
        t.write(answer_state)  # Write state name at the correct position

# ============================================================================
# 🎯 KEY CONCEPTS LEARNED:
# - turtle.Screen() and turtle graphics setup
# - pandas.read_csv() for loading geographic data
# - Boolean indexing: data[data.state == answer_state]
# - .item() method to extract single values from pandas Series
# - Creating study materials from user performance data
# - Interactive GUI elements with textinput()
# ============================================================================

# 📝 CHALLENGE COMPLETED: Created an interactive geography game that helps
# users learn Indian states and union territories while generating personalized
# study materials based on their performance!