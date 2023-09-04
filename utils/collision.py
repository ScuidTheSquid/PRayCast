from math import floor
def is_collision(x, y, map, grid_size):
    # Calculate the grid coordinates based on the player's position
    grid_x = int(x / grid_size)
    grid_y = int((600 - y) / grid_size)

    # Check if the new position is outside the map boundaries
    if (
        x < 0 or x > 256 or
        y < 344 or y > 600
    ):
        return True  # Collision with map boundaries

    # Check if the new position collides with a wall (where map value is 1)
    if map[grid_y][grid_x] == 1:
        return True  # Collision with a wall

    return False  # No collision
