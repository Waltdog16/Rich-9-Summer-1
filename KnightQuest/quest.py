# Import the Pygame module to start using its functions
from turtle import Screen
import pgzrun
# Define width and height of the game grid & size of each grid tile
GRID_WIDTH = 16  # defines How many squares wide the game board is
GRID_HEIGHT = 12 # defines How many squares tall the game board is
GRID_SIZE = 50
# Define the size of the game window
WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE
# This function converts a grid position to screen coordinates
def GetScreenCoords(x, y):
  return (x * GRID_SIZE, y * GRID_SIZE)
# This function draws the dungeon floor as a background on screen
def DrawBackground():
  for y in range(GRID_HEIGHT): # Loop over each grid row
    for x in range(GRID_WIDTH): # Loop over each grid column
      Screen.blit("floor1", GetScreenCoords(x, y)) # Draws the named image at the given screen position
def Draw():
  DrawBackground()
# Start the Pygame
pgzrun.go()









