from pygame.math import Vector2
# screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
TILE_SIZE = 64

OVERLAY_POSITIONS = {
    'tool' : (40, SCREEN_WIDTH - 15),
    'seed' : (70, SCREEN_HEIGHT - 5)}

PLAYER_TOOL_OFFSET = {
    'left' : Vector2(-50, 40),
    'right' : Vector2(50, 40),
    'up' : Vector2(0, -10),
    'down': Vector2(0, 50)
}

LAYERS = {
    'water' : 0,
    'ground': 1, 
    'soil' : 2, 
    'soil water': 3, 
    'rain floor': 4, 
    'house buttom': 5, 
    'ground plant': 6, 
    'main': 7, 
    
}