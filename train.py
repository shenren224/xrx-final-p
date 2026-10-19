import mlflow
import mlflow.sklearn
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# ---------------------- 1. 生成模拟二手车数据集 ----------------------
np.random.seed(42)
n_samples = 1000
data = pd.DataFrame({
    "mileage": np.random.randint(10000, 200000, n_samples),
    "year": np.random.randint(2010, 2025, n_samples),
    "horsepower": np.random.randint(100, 300, n_samples),
})
# 构造价格
data["price"] = (
    25000 - data["mileage"] * 0.08 + (data["year"] - 2010)*1200
    + data["horsepower"] * 40 + np.random.normal(0, 2000, n_samples)
)
data.to_csv("data/cars.csv", index=False)

# ---------------------- 2. 读取数据、划分训练测试集 ----------------------
df = pd.read_csv("data/cars.csv")
X = df.drop("price", axis=1)
y = df["price"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ---------------------- 3. MLflow 实验记录 ----------------------
mlflow.set_experiment("car_price_prediction")

with mlflow.start_run():
    # 超参数
    n_estimators = 100
    model = RandomForestRegressor(n_estimators=n_estimators, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # 记录参数、指标
    mlflow.log_param("n_estimators", n_estimators)
    mlflow.log_metric("mse", mse)
    mlflow.log_metric("r2", r2)

    # ========== 重点新增 skops_trusted_types 解决报错 ==========
    mlflow.sklearn.log_model(
        model,
        "model",
        skops_trusted_types=["sklearn.tree._tree.Tree"]
    )
    print(f"MSE: {mse:.2f}")
    print(f"R2: {r2:.4f}")
    print("MLflow run finished")
