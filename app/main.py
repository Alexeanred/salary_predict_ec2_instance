from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import pickle
from pathlib import Path
BASE_DIR = Path(__file__).resolve(strict=True).parent
class Salary(BaseModel):
    YearsExperiences : float
# Call constructor and assign to variable app
app = FastAPI()

# Load pre-trained model
with open(f'{BASE_DIR}/salary_lr.pkl', 'rb') as file:
    model = pickle.load(file)



# The root route
@app.get("/")
async def root():
    return {"message": "Welcome to Salary Prediction!"}


# Welcome page
@app.get("/welcome")
async def say_hello():
    return {"message": ""}


@app.post("/predict/")
def predict(data: Salary):
    feature = data.YearsExperiences
    test_data = [[feature]]
    prediction = model.predict(test_data)

    return {"prediction": prediction.tolist()}

