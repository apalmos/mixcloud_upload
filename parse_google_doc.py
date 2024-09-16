"""parse the Google doc"""

import pandas as pd
from datetime import timedelta

def get_google_sheet():
    link = "https://docs.google.com/spreadsheets/d/1F9J0MWeBtNDc2sC-pEEZtAqQxiZh-U3NQVLkDcZlX0U/gviz/tq?tqx=out:csv&sheet=Form-reponses-1"

    df = pd.read_csv(link)

    # Creating new columns '30m before' and '30m after'
    df['30m before'] = df['Start time of your show'] - timedelta(minutes=30).dt.time
    df['30m after'] = df['Start time of your show'] + timedelta(minutes=30).dt.time

    return df
