import time as tt
import numpy as np
import pandas as pd
import polars as pl


# create dictionary for time measurements
times_pandas = {
    "load_data_time": [],
    "join_time": [],
    "filter_time": [],
    "calc_avg_hr_time": [],
    "save_data_time": []
}
times_polars = {
    "load_data_time": [],
    "join_time": [],
    "filter_time": [],
    "calc_avg_hr_time": [],
    "save_data_time": []

}


# implement methods
def load_data_pandas(file_name):
    """
    Load the data from a CSV file into a pandas DataFrame.

    parameters
    ----------
    file_name: str
        The path to the CSV file.


    returns
    -------
    pd.DataFrame
        The DataFrame containing the data from the CSV file
        """
    return pd.read_csv(file_name)


def load_data_polars(file_name):
    """
    Load the data from a CSV file into a Polars DataFrame.

    parameters
    ----------
    file_name: str
        The path to the CSV file.

    returns
    -------
    pl.DataFrame
        The DataFrame containing the data from the CSV file
    """
    return pl.read_csv(file_name)

def join_pd(df1, df2):
    """
    Join two pandas DataFrames on the "time" and "activity" column.

    parameters
    ----------
    df1: pd.DataFrame
        The first DataFrame to join.
    df2: pd.DataFrame
        The second DataFrame to join.

    returns
    -------
    pd.DataFrame
        The joined DataFrame.
    """
    return pd.merge(df1, df2, on=["time", "activity"])

def join_pl(df1, df2):
    """
    Join two Polars DataFrames on the "time" and "activity" column.

    parameters
    ----------
    df1: pl.DataFrame
        The first DataFrame to join.
    df2: pl.DataFrame
        The second DataFrame to join.

    returns
    -------
    pl.DataFrame
        The joined DataFrame.
    """
    return df1.join(df2, on=["time", "activity"])


def filter_data_pandas(df):
    """
    Filter the data of both athletes in a pandas DataFrame to only include values between 60 and 200.
    
    parameters
    ----------
    df: pd.DataFrame
        The DataFrame containing the data to be filtered.
    
    returns
    -------
    pd.DataFrame
        The filtered DataFrame.
    """
    return df[(df["athlete_1"].between(60, 200)) & (df["athlete_2"].between(60, 200))]


def filter_data_polars(df):
    """
    Filter the data of both athletes in a Polars DataFrame to only include values between 60 and 200.

    parameters
    ----------
    df: fpl.DataFrame
        The DataFrame containing the data to be filtered.

    returns
    -------
    pl.DataFrame
        The filtered DataFrame.
    """
    return df.filter(pl.col("athlete_1").is_between(60, 200) & pl.col("athlete_2").is_between(60, 200))


def avg_heart_rate_pandas(df):
    """
    Calculate the average heart rate for each activity in a pandas DataFrame.

    parameters
    ----------
    df:pd.DataFrame
        The DataFrame containing the data.
    
    returns
    -------
    pd.Series:
        The average heart rate for each activity.
    """

    return df.groupby("activity")["athlete_1"].mean(), df.groupby("activity")["athlete_2"].mean()


def avg_heart_rate_polars(df):
    """
    Calculate the average heart rate for each activity in a Polars DataFrame.

    parameters
    ----------
    df: pl.DataFrame
        The DataFrame containing the data.

    returns
    -------
    pl.DataFrame
        The average heart rate for each activity.
    """

    return df.group_by("activity").agg(
        pl.col("athlete_1").mean().alias("avg_heart_rate1")
    ), df.group_by("activity").agg(
        pl.col("athlete_2").mean().alias("avg_heart_rate2"))

def save_df_to_csv_pd(df, filename):
    """
    Save a pandas DataFrame to a CSV file.
    
    parameters
    ----------
    df: pd.DataFrame
        The DataFrame to save.
    filename: str
        The path to the CSV file.
    
    returns
    -------
    None
        """
    df.to_csv(filename, index=False)

def save_df_to_csv_pl(df, filename):
    """
    Save a Polars DataFrame to a CSV file.
    
    parameters
    ----------
    df: pl.DataFrame
        The DataFrame to save.
    filename: str
        The path to the CSV file.
    
    returns
    -------
    None
        """
    df.write_csv(filename)

wrong_input = True
while wrong_input:
    print("Select sample size:")
    print("[1] 1,000")
    print("[2] 10,000")
    print("[3] 100,000")
    print("[4] 1,000,000")
    print("[5] 10,000,000")
    choice = input("What sample size you want to test(1-5): ")

    if choice == '1':
        SAMPLE_COUNT = 1000
        wrong_input = False
    elif choice == '2':
        SAMPLE_COUNT = 10000
        wrong_input = False
    elif choice == '3':
        SAMPLE_COUNT = 100000
        wrong_input = False
    elif choice == '4':
        SAMPLE_COUNT = 1000000
        wrong_input = False
    elif choice == '5':
        SAMPLE_COUNT = 10000000
        wrong_input = False
    else:
        print("Invalid choice. Please select a valid option.")


print("SAMPLE_COUNT: ", SAMPLE_COUNT/1000000, "Mio")


for i in range(5):
    #--------------------------------------------------------------------------------------------------
    # Data manipulation with pandas
    #--------------------------------------------------------------------------------------------------


    t0=tt.perf_counter()
    # load the sample data from the CSV file (pandas)
    df_pd_athlete_1 = load_data_pandas(f"code/Abschlussbericht/sample_data/athlete_1sample_data_{SAMPLE_COUNT}.csv")
    df_pf_athlete_2 = load_data_pandas(f"code/Abschlussbericht/sample_data/athlete_2sample_data_{SAMPLE_COUNT}.csv")
    times_pandas["load_data_time"].append(tt.perf_counter() - t0)
    print("time to load data pandas: ", times_pandas["load_data_time"][i])

    # join the data of athlete_1 and athlete_2 (pandas)
    t0 = tt.perf_counter()
    df_joined_pd = join_pd(df_pd_athlete_1, df_pf_athlete_2)
    times_pandas["join_time"].append(tt.perf_counter() - t0)
    print("time to join data: ", times_pandas["join_time"][i])


    # filter out values under 100 and over 200 (pandas)
    t0 = tt.perf_counter()
    df_filtered_pd = filter_data_pandas(df_joined_pd)
    times_pandas["filter_time"].append(tt.perf_counter() - t0)
    print("time to filter data: ", times_pandas["filter_time"][i])


    # calculate the average heart rate for each phase (pandas)
    t0 = tt.perf_counter()
    average_hr_pd = avg_heart_rate_pandas(df_filtered_pd)
    times_pandas["calc_avg_hr_time"].append(tt.perf_counter() - t0)
    print("time to calc avg heart rate: ", times_pandas["calc_avg_hr_time"][i])

    print(f"average heart rate: {average_hr_pd}")

    # save the data to a CSV file (pandas)
    t0 = tt.perf_counter()
    save_df_to_csv_pd(df_filtered_pd, "filtered_df_pd.csv")
    times_pandas["save_data_time"].append(tt.perf_counter() - t0)
    print("time to save data: ", times_pandas["save_data_time"][i])


    #--------------------------------------------------------------------------------------------------
    # Data manipulation with polars
    #--------------------------------------------------------------------------------------------------


    # convert the data to a polars DataFrame
    t0 = tt.perf_counter()
    df_pl_athlete_1 = load_data_polars(f"code/Abschlussbericht/sample_data/athlete_1sample_data_{SAMPLE_COUNT}.csv")
    df_pl_athlete_2 = load_data_polars(f"code/Abschlussbericht/sample_data/athlete_2sample_data_{SAMPLE_COUNT}.csv")
    times_polars["load_data_time"].append(tt.perf_counter() - t0)
    print("time to load data polars: ", times_polars["load_data_time"][i])


    # join the data of athlete_1 and athlete_2 (polars)
    t0 = tt.perf_counter()
    df_joined_pl = join_pl(df_pl_athlete_1, df_pl_athlete_2)
    times_polars["join_time"].append(tt.perf_counter() - t0)
    print("time to join data: ", times_polars["join_time"][i])


    # filter out values under 100 and over 200
    t0 = tt.perf_counter()
    df_filtered_pl = filter_data_polars(df_joined_pl)
    times_polars["filter_time"].append(tt.perf_counter() - t0)
    print("time to filter data: ", times_polars["filter_time"][i])


    # calculate the average heart rate for each phase (polars)
    t0 = tt.perf_counter()
    average_hr_pl = avg_heart_rate_polars(df_filtered_pl)
    times_polars["calc_avg_hr_time"].append(tt.perf_counter() - t0)
    print("time to calc avg heart rate: ", times_polars["calc_avg_hr_time"][i])

    print(f"average heart rate: {average_hr_pl}")

    # save the data to a CSV file (polars)
    t0 = tt.perf_counter()
    save_df_to_csv_pl(df_filtered_pl, "filtered_df_pl.csv")
    times_polars["save_data_time"].append(tt.perf_counter() - t0)
    print("time to save data: ", times_polars["save_data_time"][i])


# show results
print(f"Results for {SAMPLE_COUNT/1000000} Mio rows:")
for key in times_pandas:
    avg_time_pandas = np.mean(times_pandas[key])
    avg_time_polars = np.mean(times_polars[key])
    speedup = avg_time_pandas / avg_time_polars
    print(f"Average {key} time: Pandas = {avg_time_pandas:.6f}s, Polars = {avg_time_polars:.6f}s, Speedup = {speedup:.2f}x")
