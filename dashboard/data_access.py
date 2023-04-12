import pandas as pd


def read_gapminder():
    return pd.read_csv("dashboard/static/gapminderData2.csv")


def read_migrantes():
    return pd.read_excel("dashboard/static/MigrantesChile.xlsx")
