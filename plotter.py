import queue
import matplotlib.pyplot as plt
import time

def Plotter(data_queue):
    # Initialize empty lists for sensor data
    ldr_data = []
    soil_moisture_data = []
    humidity_data = []
    temperature_data = []
    times = []  # List to store timestamps for plotting

    plt.ion()  # Enable interactive plotting
    fig, axes = plt.subplots(2, 2, figsize=(10, 10))  # Create a 2x2 subplot grid

    axes[0, 0].set_title('LDR')
    axes[0, 1].set_title('Soil Moisture')
    axes[1, 0].set_title('Humidity')
    axes[1, 1].set_title('Temperature')

    while True:
        try:
            # Get data from the queue
            data = data_queue.get()
            ldr, soil_moisture, humidity, temperature = data

            # Append data to lists
            ldr_data.append(ldr)
            soil_moisture_data.append(soil_moisture)
            humidity_data.append(humidity)
            temperature_data.append(temperature)
            times.append(time.time())

            # Update plots
            axes[0, 0].clear()
            axes[0, 0].plot(times, ldr_data)
            axes[0, 1].clear()
            axes[0, 1].plot(times, soil_moisture_data)
            axes[1, 0].clear()
            axes[1, 0].plot(times, humidity_data)
            axes[1, 1].clear()
            axes[1, 1].plot(times, temperature_data)

            plt.pause(0.1)  # Update the plot every 0.1 seconds

        except queue.Empty:
            # Handle empty queue gracefully
            pass

