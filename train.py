import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

# 构造模拟二手车数据
data = {
    "age": [2,5,8,1,4,6,3,7],
    "mileage": [20000,60000,90000,10000,45000,72000,30000,80000],
    "displacement": [1.5,2.0,1.6,1.2,1.8,2.0,1.5,1.6],
    "price": [120000,75000,42000,150000,88000,63000,105000,51000]
}
df = pd.DataFrame(data)

# 特征与标签
X = df[["age", "mileage", "displacement"]]
y = df["price"]

# 训练随机森林回归（我们自选模型）
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# 保存模型到model文件夹
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/car_price_model.pkl")
print("模型训练完成，已保存至 model/car_price_model.pkl")
