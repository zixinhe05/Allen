import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk with 5,000 points.
    rw = RandomWalk(5_000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.plot(rw.x_values, rw.y_values, linewidth=1, c='blue')  # Plot with a line

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)  # Starting point
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)  # Ending point

    # Remove the axes for a cleaner look.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    # Prompt to continue or stop.
    keep_running = input("Make another walk? (y/n): ").lower()
    if keep_running == 'n':
        break
