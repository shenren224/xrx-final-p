# generate_data.py
import os
import pandas as pd
os.makedirs("data", exist_ok=True)

# v1 原始二手车数据集
car_data = [
    {"brand":"Toyota", "model":"Camry", "year":2020, "mileage":45000, "price":22000},
    {"brand":"Honda", "model":"Civic", "year":2021, "mileage":32000, "price":21000},
    {"brand":"BMW", "model":"X5", "year":2019, "mileage":60000, "price":58000},
    {"brand":"Audi", "model":"A4", "year":2022, "mileage":20000, "price":39000},
    {"brand":"Ford", "model":"F150", "year":2020, "mileage":52000, "price":42000},
    {"brand":"Kia", "model":"Sportage", "year":2018, "mileage":70000, "price":17000}
]
df = pd.DataFrame(car_data)
df.to_csv("data/cars.csv", index=False)
print("✅ v1二手车数据集生成完毕 data/cars.csv")
