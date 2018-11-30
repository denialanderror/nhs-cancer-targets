import pandas as pd
import re
from typing import List
from .const import months, wm_provider_codes

link_map = {
    4: 'https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2018/08/3.-Two-Week-Wait-By-Suspected-Cancer-Provider-Data-1.csv',
    5: 'https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2018/07/3.-Two-Week-Wait-By-Suspected-Cancer-Provider-Data-CSV-179KB.csv',
    6: 'https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2018/08/3.-Two-Week-Wait-By-Suspected-Cancer-Provider-Data-CSV-181KB.csv',
    7: 'https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2018/09/3.-Two-Week-Wait-By-Suspected-Cancer-Provider-Data-CSV-178KB.csv',
    8: 'https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2018/10/3.-Two-Week-Wait-By-Suspected-Cancer-Provider-Data-CSV-178-KB.csv',
    9: 'https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2018/11/3.-Two-Week-Wait-By-Suspected-Cancer-Provider-Data-CSV-178KB.csv'
}


def _get_data_from_url(month: int) -> pd.DataFrame:
    df = pd.read_csv(link_map[month], usecols=[1, 2, 3, 4, 5, 6, 7], header=6)
    df.columns = ['ODS', 'provider', 'cancer_type',
                  'total', 'within_14', 'after_14', 'percentage']
    df = df[df.provider != 'ALL ENGLISH PROVIDERS']
    df['provider'] = df['provider'].apply(_format_provider)
    df['month_index'] = month
    df['month'] = months[month]

    return df


def _format_provider(provider: str) -> str:
    titled = re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                    lambda x: x.group(0)[0].upper() + x.group(0)[1:].lower(),
                    provider)
    return re.sub(r'Nhs', r'NHS', titled)


def dataframe_from_criteria(months: List[int] = [4, 5, 6, 7, 8, 9],
                            provider_codes: List[str] = wm_provider_codes,
                            cancers: [str] = ['Suspected gynaecological cancer']) -> pd.DataFrame:
    dfs = [_get_data_from_url(month) for month in months]
    df = pd.concat(dfs)
    return df[df['ODS'].isin(provider_codes) & df['cancer_type'].isin(cancers)]
