import math


def reflect_point(px, py, x1, y1, x2, y2):
    # Calculate the slope and intercept of the folding line (x1, y1) to (x2, y2)
    dx = x2 - x1
    dy = y2 - y1

    # Line equation: A*x + B*y + C = 0
    A = dy
    B = -dx
    C = dx * y1 - dy * x1

    # Formula to reflect point (px, py) over line
    d = (px + (py * B - C) * A / (A ** 2 + B ** 2) - px) / 2
    reflected_x = px + 2 * d * A / (A ** 2 + B ** 2)
    reflected_y = py + 2 * d * B / (A ** 2 + B ** 2)

    return reflected_x, reflected_y


def main():
    # Read input
    area = int(input())
    x1, y1, x2, y2 = map(int, input().split())

    # Calculate side length of the square
    side = math.sqrt(area)

    # Initial corners of the square
    corners = [(0, 0), (0, side), (side, side), (side, 0)]

    # Fold each corner and store the reflected corners
    folded_corners = set(corners)  # To avoid duplicates

    for (cx, cy) in corners:
        reflected = reflect_point(cx, cy, x1, y1, x2, y2)
        folded_corners.add(reflected)

    # Sort by x then y
    folded_corners = sorted(folded_corners, key=lambda p: (p[0], p[1]))

    # Print the result with two decimal places
    for x, y in folded_corners:
        print(f"{x:.2f} {y:.2f}")


if __name__ == "__main__":
    main()
