from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
import joblib

app = FastAPI(title="Diabetes Prediction")

templates = Jinja2Templates(directory="templates")

# Load trained model
model = joblib.load("diabetes_model.pkl")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"prediction": None}
    )


@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    Pregnancies: int = Form(...),
    Glucose: float = Form(...),
    BloodPressure: float = Form(...),
    SkinThickness: float = Form(...),
    Insulin: float = Form(...),
    BMI: float = Form(...),
    DiabetesPedigreeFunction: float = Form(...),
    Age: int = Form(...)
):

    data = pd.DataFrame([[
        Pregnancies,
        Glucose,
        BloodPressure,
        SkinThickness,
        Insulin,
        BMI,
        DiabetesPedigreeFunction,
        Age
    ]], columns=[
        "Pregnancies",
        "Glucose",
        "BloodPressure",
        "SkinThickness",
        "Insulin",
        "BMI",
        "DiabetesPedigreeFunction",
        "Age"
    ])

    prediction = model.predict(data)[0]

    result = "ðŸ©º Diabetic" if prediction == 1 else "âœ… Not Diabetic"

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"prediction": result}
    )