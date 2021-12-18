real_input = ((137, 171), (-98, -73))
test_input = ((20, 30), (-10, -5))

input = test_input

min_x, max_x = min(input[0][0], input[0][1]), max(input[0][0], input[0][1])
min_y, max_y_pos = min(input[1][0], input[1][1]), max(input[1][0], input[1][1])

def collides(position):
    x, y = position
    return x >= min_x and x <= max_x and y >= min_y and y <= max_y_pos

def overshot(position):
    x, y = position
    return x > max_x or y < min_y


max_y = -2
max_init = None
for intial_x in range(0, max_x + 1):
    for initial_y in range(0, max(abs(max_y_pos), abs(min_y))):
        curr_max_y = -1
        velocity = [intial_x, initial_y]
        position = [0, 0]
        collided = False

        # while we are moving
        while True:
            if position[1] > curr_max_y:
                curr_max_y = position[1]

            position[0] += velocity[0]
            position[1] += velocity[1]

            # gravity
            velocity[1] -= 1

            # drag
            if velocity[0] > 0:
                velocity[0] -= 1
            elif velocity[0] < 0:
                velocity[0] += 1

            if collides(position):
                collided = True
                break

            if overshot(position):
                break

        if curr_max_y > max_y and collided:
            max_y = curr_max_y
            max_init = (intial_x, initial_y)

        print(f"Tested {(intial_x, initial_y)} and max is {max_y}")


print(max_y, max_init)
