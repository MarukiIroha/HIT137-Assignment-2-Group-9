# Question 2 - Temperature Analysis
import pandas as pd

# 手动列出所有文件路径（你应上传这20个文件）
all_files = [f"/mnt/data/stations_group_{year}.csv" for year in range(1986, 2006)]

# 合并所有数据
dfs = []
for path in all_files:
    df = pd.read_csv(path)
    df["YEAR"] = int(path[-8:-4])
    dfs.append(df)

full_data = pd.concat(dfs, ignore_index=True)

# 月份列
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

# 四季平均
seasons = {
    "Summer": ["December", "January", "February"],
    "Autumn": ["March", "April", "May"],
    "Winter": ["June", "July", "August"],
    "Spring": ["September", "October", "November"]
}
with open("average_temp.txt", "w") as f:
    for season, mon in seasons.items():
        avg = full_data[mon].mean().mean()
        f.write(f"{season}: {avg:.2f}°C\n")

# 温差最大站
full_data["TEMP_RANGE"] = full_data[months].max(axis=1) - full_data[months].min(axis=1)
max_range = full_data.groupby("STATION_NAME")["TEMP_RANGE"].max().reset_index()
top_range = max_range[max_range["TEMP_RANGE"] == max_range["TEMP_RANGE"].max()]
top_range.to_csv("largest_temp_range_station.txt", index=False)

# 最热最冷站
full_data["YEARLY_AVG"] = full_data[months].mean(axis=1)
avg_by_station = full_data.groupby("STATION_NAME")["YEARLY_AVG"].mean().reset_index()
warm = avg_by_station[avg_by_station["YEARLY_AVG"] == avg_by_station["YEARLY_AVG"].max()]
cool = avg_by_station[avg_by_station["YEARLY_AVG"] == avg_by_station["YEARLY_AVG"].min()]
final = pd.concat([warm.assign(TYPE="Warmest"), cool.assign(TYPE="Coolest")])
final.to_csv("warmest_and_coolest_station.txt", index=False)
