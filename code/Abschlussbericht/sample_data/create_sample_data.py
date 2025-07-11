import pandas as pd
import numpy as np
import polars as pl

def create_sample(sample_count, athlete):
    data = {
        "time": pd.date_range(start="2024-11-10 08:00:00", periods=sample_count, freq="5s"),  # time stamps every 5 seconds
        athlete: np.random.normal(125, 55, sample_count).astype(int),  # random heart rate values between 60 and 180 bpm
        "activity": ["Ruhe"] * (sample_count // 4) + ["Aufwärmen"] * (sample_count // 4) + ["Hauptteil"] * (sample_count // 2)  # different activity phases
    }
    df = pl.DataFrame(data)
    df.write_csv(f"code/Abschlussbericht/sample_data/{athlete}sample_data_{sample_count}.csv")
    return data

for i in [1000, 10000, 100000, 1000000, 10000000]:
    create_sample(i, "athlete_1")
    create_sample(i, "athlete_2")