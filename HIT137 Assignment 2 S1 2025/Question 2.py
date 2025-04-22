"""
Name:Shaobin Chen
Date started: 20/04
GitHub URL:https://github.com/MarukiIroha/HIT137-Assignment-2-Group-9/
"""
import os
import pandas as pd

SEASONS = {
    'Summer': ['December', 'January', 'February'],
    'Autumn': ['March', 'April', 'May'],
    'Winter': ['June', 'July', 'August'],
    'Spring': ['September', 'October', 'November']
}
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']


def main():
    folder_path = 'temperature_data'

    try:
        print("Reading temperature data...")
        data = read_temperature_data(folder_path)

        print("Calculating seasonal averages...")
        seasonal_avgs = calculate_seasonal_averages(data)
        print("Seasonal averages saved to average_temp.txt")

        print("Finding station(s) with largest temperature range...")
        max_range_stations, max_range = find_largest_temp_range(data)
        print("Results saved to largest_temp_range_station.txt")

        print("Finding warmest and coolest stations...")
        warmest, coolest = find_warmest_and_coolest_stations(data)
        print("Results saved to warmest_and_coolest_station.txt")

    except Exception as e:
        print(f"Error: {e}")


def get_season(month):
    for season, months in SEASONS.items():
        if month in months:
            return season
    return None


def read_temperature_data(folder_path):
    all_data = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.csv'):
            file_path = os.path.join(folder_path, file_name)
            try:
                df = pd.read_csv(file_path)
                required_columns = ['STATION_NAME', 'STN_ID', 'LAT', 'LON'] + MONTHS
                if not all(col in df.columns for col in required_columns):
                    print(f"Skipping {file_name}: Missing required columns.")
                    continue
                all_data.append(df)
            except Exception as e:
                print(f"Error reading {file_name}: {e}")

    if not all_data:
        raise ValueError("No valid CSV files found in the folder.")

    combined_df = pd.concat(all_data, ignore_index=True)

    melted_df = pd.melt(
        combined_df,
        id_vars=['STATION_NAME', 'STN_ID', 'LAT', 'LON'],
        value_vars=MONTHS,
        var_name='Month',
        value_name='Temperature'
    )

    melted_df = melted_df.dropna(subset=['Temperature'])
    melted_df['Temperature'] = pd.to_numeric(melted_df['Temperature'], errors='coerce')
    melted_df = melted_df.dropna(subset=['Temperature'])

    melted_df['Season'] = melted_df['Month'].apply(get_season)

    return melted_df


def calculate_seasonal_averages(data):
    seasonal_avgs = data.groupby('Season')['Temperature'].mean().round(2)

    with open('average_temp.txt', 'w') as f:
        f.write("Average Temperatures by Season (°C):\n")
        for season, temp in seasonal_avgs.items():
            f.write(f"{season}: {temp}\n")

    return seasonal_avgs


def find_largest_temp_range(data):
    station_ranges = data.groupby('STATION_NAME')['Temperature'].agg(lambda x: x.max() - x.min())

    max_range = station_ranges.max()
    max_range_stations = station_ranges[station_ranges == max_range].index.tolist()

    with open('largest_temp_range_station.txt', 'w') as f:
        f.write(f"Station(s) with largest temperature range ({max_range:.2f} °C):\n")
        for station in max_range_stations:
            f.write(f"{station}\n")

    return max_range_stations, max_range


def find_warmest_and_coolest_stations(data):
    station_avgs = data.groupby('STATION_NAME')['Temperature'].mean()

    max_avg = station_avgs.max()
    min_avg = station_avgs.min()
    warmest_stations = station_avgs[station_avgs == max_avg].index.tolist()
    coolest_stations = station_avgs[station_avgs == min_avg].index.tolist()

    with open('warmest_and_coolest_station.txt', 'w') as f:
        f.write("Warmest Station(s):\n")
        for station in warmest_stations:
            f.write(f"{station} (Average: {max_avg:.2f} °C)\n")
        f.write("\nCoolest Station(s):\n")
        for station in coolest_stations:
            f.write(f"{station} (Average: {min_avg:.2f} °C)\n")

    return warmest_stations, coolest_stations


if __name__ == "__main__":
    main()