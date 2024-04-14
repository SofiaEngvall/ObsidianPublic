# Sofia 2023-10-01

for year in range(2020, 2024):
    for month in range(1, 13):
        for day in range(1, 32):
            print(f"{str(year)}-{str(month).zfill(2)}-{str(day).zfill(2)}")
