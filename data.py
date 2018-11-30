import pandas as pd


def two_week_wait_data():
    xls = pd.ExcelFile(
        'https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2018/11/SEPTEMBER-2018-CANCER-WAITING-TIMES-PROVIDER-WORKBOOK-FINAL-updated-XLSX-1MB.xlsx')
    print(xls.sheet_names)
    df = pd.read_excel(xls, 'TWO WEEK WAIT-BY CANCER',
                       usecols='B:D,J:N', header=6)
    df.columns = ['ODS', 'Provider', 'Cancer Type', 'Within 14 days',
                  '15 to 16 days', '17 to 21 days', '22 to 28 days', 'After 28 days']
    df = df[df.Provider != 'ALL ENGLISH PROVIDERS']

    return df
