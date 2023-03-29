import joblib
import pandas as pd


def predict(Age, SystolicBP, DiastolicBP, BS, BodyTemp, HeartRate):
    clf = joblib.load('util/model.pkl')
    data = {
        "Age": [Age], "SystolicBP": [SystolicBP], "DiastolicBP": [DiastolicBP], "BS": [BS], "BodyTemp": [BodyTemp],
        "HeartRate": [HeartRate]
    }
    df = pd.DataFrame(data)
    pred = clf.predict(df)
    print(pred)
    return pred[0]
