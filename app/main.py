from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os

app = FastAPI(title="MLOps 二手车价格预测")

# 定义前端传过来的数据格式
class CarInput(BaseModel):
    age: float       # 车龄
    mileage: float   # 里程数
    displacement: float # 排量

# 加载训练好的模型
model_path = "model/car_price_model.pkl"
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    model = None

@app.get("/")
def root():
    return {"msg": "MLOps 二手车预测服务", "status": "ok"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# 模型预测接口
@app.post("/predict")
def predict_car_price(car: CarInput):
    if model is None:
        return {"error": "模型文件不存在，请先训练并保存模型"}
    features = [[car.age, car.mileage, car.displacement]]
    pred_price = model.predict(features)[0]
    return {"predicted_price": round(float(pred_price),2)}
