def is_collision(new_x, new_y, map):
    # Calculate the player's grid position in the map
    grid_x = int(new_x / 32)  # Assuming each grid cell is 32x32 pixels
    grid_y = int(new_y / 32)

    # Check if the new position is outside the map boundaries
    if grid_x < 0 or grid_x >= len(map[0]) or grid_y < 0 or grid_y >= len(map):
        return True  # Collision with map boundaries

    # Check if the new position collides with a wall (where map value is 1)
    if map[grid_y][grid_x] == 1:
        return True  # Collision with a wall

    return False  # No collision
