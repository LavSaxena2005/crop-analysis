import threading
import queue  # For data exchange between threads

from data_logger import DataLogger  # Import DataLogger class
from plotter import Plotter  # Import Plotter class


def main():
    # Create a queue to store sensor data for plotting
    data_queue = queue.Queue()

    # Create threads for data logger and plotter
    data_logger_thread = threading.Thread(target=DataLogger, args=(data_queue,))
    plotter_thread = threading.Thread(target=Plotter, args=(data_queue,))

    # Start both threads
    data_logger_thread.start()
    plotter_thread.start()

    # Wait for threads to finish (optional)
    # data_logger_thread.join()
    # plotter_thread.join()

if __name__ == "__main__":
    main()
