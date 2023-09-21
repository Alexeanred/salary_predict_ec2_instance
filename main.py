from fastapi import FastAPI
import uvicorn
from salary import Salary
import pickle

# Call constructor and assign to variable app
app = FastAPI()

# Load pre-trained model
with open('salary_lr.pkl', 'rb') as file:
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


# Run API
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


# to run the main.py
# uvicorn main:app --reload