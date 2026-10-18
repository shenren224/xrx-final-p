from fastapi import FastAPI

app = FastAPI(title="MLOps Cars CRUD Demo")

@app.get("/")
def root():
    return {"msg": "Hello MLOps", "status": "ok"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
