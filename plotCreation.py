import pandas as pd
import matplotlib.pyplot as plt


# Define a function to filter out outliers
def filter_outliers(values, threshold):
    return [value if value < threshold else None for value in values]


# csv_base = "/Users/danielarturi/Desktop/McGill Fall 2024/ECSE 429/Project/PartC/ECSE429_PartC/final_findings/"
csv_base = "final_findings/"

# Load the CSV file
csv_files = [
    csv_base + "final_cpu_usage.csv",
    csv_base + "final_mem_usage.csv",
    csv_base + "final_time_elapsed.csv",
    csv_base + "final_time_per_todo.csv"
]

chart_title_names_scaled = [
    "Number of Todos vs. CPU Usage",
    "Number of Todos vs. Available Bytes of Memory",
    "Number of Todos vs. Total Time Elapsed",
    "Number of Todos vs. Time Taken per Todo",
]

chart_y_axis_names = [
    "CPU Percentage in Use (%)",
    "Bytes Available",
    "Time Elapsed (microsecond)",
    "Time Per Todo (microsecond)"
]

for i in range(4):
    data = pd.read_csv(csv_files[i])

    # The first column contains the series names
    series_names = data['Label']

    # The rest of the columns are the categories
    categories = [int(i.split("_")[-1]) for i in data.columns[1:]]

    # Set the outlier threshold (example: 50)
    outlier_threshold = 120000

    # Plot each series with triangle markers
    for j, series in enumerate(series_names):
        # Filter out outliers for the current series
        if csv_files[i] == csv_files[3]:
            filtered_values = filter_outliers(data.iloc[j, 1:], outlier_threshold)
        else:
            filtered_values = data.iloc[j, 1:]

        # Plot the filtered values
        plt.plot(categories, filtered_values, marker='^', label=series)

    # Add labels, title, and legend
    plt.xlabel("Number of Todos")
    plt.ylabel(chart_y_axis_names[i])
    plt.title(chart_title_names_scaled[i])
    plt.legend()
    plt.grid(False)

    # Display the plot
    plt.show()

