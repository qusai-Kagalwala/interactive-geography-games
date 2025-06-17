# 🎯 Coordinate Mapper Tool for Geography Games
# Angela Yu's 100 Days of Code - Python Bootcamp Helper Tool
# Interactive tool to map coordinates on images for creating educational games

# ============================================================================
# 📚 LEARNING OBJECTIVES:
# - Event handling with turtle graphics (mouse clicks and keyboard)
# - Working with CSV files for coordinate data storage
# - Global variables and state management
# - Interactive GUI development with turtle
# - Screen clearing and dynamic content updates
# ============================================================================

# 📦 Import required libraries
import turtle  # For graphics, event handling, and interactive interface
import csv     # For saving coordinate data to CSV files

# ============================================================================
# 🖥️ SCREEN SETUP: Initialize the coordinate mapping interface
# ============================================================================

# 🎮 Step 1: Create and configure the main screen
screen = turtle.Screen()
screen.title("Click to Get Coordinates")  # Set descriptive window title
screen.setup(width=1000, height=800)      # Set screen dimensions for better visibility

# 🗺️ Step 2: Load and display the target image
# This image will be used as the background for coordinate mapping
image_name = "blank_states_img.gif"  # Your map image file
screen.addshape(image_name)           # Register image as a turtle shape

# 🐢 Step 3: Create turtle to display the background image
image_turtle = turtle.Turtle()
image_turtle.shape(image_name)  # Set turtle to display the map image
image_turtle.penup()            # Prevent drawing lines when moving
image_turtle.goto(0, 0)         # Center the image on screen

# ============================================================================
# 📊 DATA MANAGEMENT: Variables to track clicks and coordinates
# ============================================================================

# 🔢 Global variables for state management
click_counter = 0        # Track number of clicks made
coordinates_list = []    # Store all clicked coordinates as [click_number, x, y]

# ============================================================================
# 🖱️ EVENT HANDLER FUNCTIONS: Mouse and keyboard interactions
# ============================================================================

# 📍 Step 4: Mouse click handler function
def get_coordinates(x, y):
    """
    Handles mouse click events to capture and display coordinates
    Parameters: x, y - mouse click coordinates from turtle screen
    """
    global click_counter  # Access global counter variable
    click_counter += 1    # Increment click counter
    
    # 🖥️ Display coordinates in console for immediate feedback
    print(f"Click {click_counter}: x={int(x)}, y={int(y)}")
    
    # 💾 Store coordinates in list for later CSV export
    # Format: [click_number, x_coordinate, y_coordinate]
    coordinates_list.append([click_counter, int(x), int(y)])
    
    # 🎯 Visual feedback: Show numbered marker at click location
    number_turtle = turtle.Turtle()
    number_turtle.hideturtle()  # Hide turtle icon for cleaner appearance
    number_turtle.penup()       # No drawing lines
    number_turtle.speed(0)      # Fastest drawing speed
    number_turtle.goto(x, y)    # Move to clicked location
    number_turtle.color("red")  # Set text color for visibility
    # Write click number at the location
    number_turtle.write(str(click_counter), align="center", font=("Arial", 12, "bold"))

# 💾 Step 5: Save coordinates to CSV file
def save_coordinates():
    """
    Exports all collected coordinates to a CSV file
    Creates a structured data file for use in geography games
    """
    filename = "clicked_coordinates.csv"
    
    # 📝 Write coordinates to CSV file
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        # Write header row for data structure
        writer.writerow(["click_number", "x", "y"])
        # Write all coordinate data
        writer.writerows(coordinates_list)
    
    # ✅ Confirmation feedback to user
    print(f"\nCoordinates saved to {filename}")
    print(f"Total clicks recorded: {len(coordinates_list)}")

# 🧹 Step 6: Clear all data and reset interface
def clear_all():
    """
    Resets the entire interface and clears all recorded data
    Useful for starting over or correcting mistakes
    """
    global click_counter, coordinates_list
    
    # 🔄 Reset all tracking variables
    click_counter = 0
    coordinates_list = []
    
    # 🖥️ Clear screen and redraw background image
    screen.clear()                    # Remove all drawings
    screen.addshape(image_name)       # Re-register the image shape
    image_turtle.shape(image_name)    # Reset turtle to show image
    image_turtle.penup()              # Ensure no drawing
    image_turtle.goto(0, 0)           # Center image again
    
    print("Cleared all points!")

# ============================================================================
# 🎮 EVENT BINDING: Connect user actions to functions
# ============================================================================

# 🖱️ Step 7: Bind mouse click events
# When user clicks anywhere on screen, call get_coordinates function
screen.onclick(get_coordinates)

# ⌨️ Step 8: Bind keyboard shortcuts for efficiency
screen.onkey(save_coordinates, "s")  # Press 's' to save coordinates to CSV
screen.onkey(clear_all, "c")         # Press 'c' to clear all points and restart

# ============================================================================
# 📋 USER INSTRUCTIONS: Display help information
# ============================================================================

# 📖 Step 9: Provide clear instructions to user
print("Click on each state to get its coordinates!")
print("Numbers will show where you clicked.")
print("Press 's' to save coordinates to CSV file")
print("Press 'c' to clear all points and start over")

# ============================================================================
# 🔄 MAIN PROGRAM LOOP: Keep the application running
# ============================================================================

# 🎧 Step 10: Activate event listening and start main loop
screen.listen()     # Enable keyboard event detection
screen.mainloop()   # Keep window open and responsive to events

# ============================================================================
# 🎯 KEY CONCEPTS LEARNED:
# - Event-driven programming with turtle graphics
# - Mouse click coordinates capture and processing
# - Keyboard shortcuts for user interface efficiency
# - CSV file creation and data export
# - Global state management in interactive applications
# - Screen clearing and dynamic content management
# ============================================================================

# 📝 TOOL PURPOSE: This coordinate mapper helps create the data files needed
# for geography games by allowing users to click on map locations and 
# automatically generating a CSV file with precise coordinates for each location!