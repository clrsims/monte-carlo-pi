import random
import matplotlib.pyplot as plt
import time

# Initialize parameters
num_darts = 100000  # Number of points to throw
circle_radius = 1.0  # Radius of the circle
square_side = 2 * circle_radius  # Side length of the square
update_interval = num_darts // 100  # Number of darts per update for consistent timing

# Counters for points inside the circle
inside_circle = 0

# Random number generation setup (not throwing darts yet)
def generate_random_point():
    """Generates a random (x, y) point within the square [-1,1] x [-1,1]"""
    x = random.uniform(-circle_radius, circle_radius)
    y = random.uniform(-circle_radius, circle_radius)
    return x, y

# Create figure and axis for visualization
fig, ax = plt.subplots()
ax.set_xlim(-circle_radius, circle_radius)
ax.set_ylim(-circle_radius, circle_radius)
ax.set_aspect('equal')

# Draw square boundary
square = plt.Rectangle((-circle_radius, -circle_radius), square_side, square_side, fill=False, edgecolor='black')
ax.add_patch(square)

# Draw circle boundary
circle = plt.Circle((0, 0), circle_radius, fill=False, edgecolor='blue')
ax.add_patch(circle)

# Lists to store dart positions
x_inside, y_inside = [], []
x_outside, y_outside = [], []

# Real-time dart throwing simulation
start_time = time.time()
for i in range(num_darts):
    x, y = generate_random_point()
    if x**2 + y**2 <= circle_radius**2:
        inside_circle += 1
        x_inside.append(x)
        y_inside.append(y)
    else:
        x_outside.append(x)
        y_outside.append(y)
    
    # Update plot at a consistent rate
    if (i + 1) % update_interval == 0:
        ax.clear()
        ax.set_xlim(-circle_radius, circle_radius)
        ax.set_ylim(-circle_radius, circle_radius)
        ax.set_aspect('equal')
        ax.add_patch(plt.Rectangle((-circle_radius, -circle_radius), square_side, square_side, fill=False, edgecolor='black'))
        ax.add_patch(plt.Circle((0, 0), circle_radius, fill=False, edgecolor='blue'))
        ax.scatter(x_inside, y_inside, color='green', s=1, label='Inside Circle')
        ax.scatter(x_outside, y_outside, color='red', s=1, label='Outside Circle')
        plt.title(f"Monte Carlo Estimation of Pi\nIteration: {i+1} | Approximation: {4 * inside_circle / (i+1):.6f}")
        plt.pause(0.1)  # Slows down the update rate

# Final plot with all darts
ax.clear()
ax.set_xlim(-circle_radius, circle_radius)
ax.set_ylim(-circle_radius, circle_radius)
ax.set_aspect('equal')
ax.add_patch(plt.Rectangle((-circle_radius, -circle_radius), square_side, square_side, fill=False, edgecolor='black'))
ax.add_patch(plt.Circle((0, 0), circle_radius, fill=False, edgecolor='blue'))
ax.scatter(x_inside, y_inside, color='green', s=1, label='Inside Circle')
ax.scatter(x_outside, y_outside, color='red', s=1, label='Outside Circle')
plt.title(f"Final Monte Carlo Estimation of Pi: {4 * inside_circle / num_darts:.6f}")
plt.legend()
plt.show()

print(f"Final Monte Carlo estimation of Pi: {4 * inside_circle / num_darts:.6f}")
