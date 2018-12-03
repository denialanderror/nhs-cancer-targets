import pandas as pd
import re
from typing import List
from .const import months, years, link_map, wm_provider_codes


def _get_data_from_url(month: int) -> pd.DataFrame:
    df = pd.read_csv(link_map[month], usecols=[1, 2, 3, 4, 5, 6, 7], header=6)
    df.columns = ['ODS', 'provider', 'cancer_type',
                  'total', 'within_14', 'after_14', 'percentage']
    df = df[df.provider != 'ALL ENGLISH PROVIDERS']
    df['provider'] = df['provider'].apply(_format_provider)
    link_index = list(link_map.keys())
    df['month_index'] = link_index.index(month)
    df['month'] = months[month[0:-2]] + years[month[-2:]]

    return df


def _format_month(month: str) -> str:
    return months[month[0:-2]]


def _format_provider(provider: str) -> str:
    titled = re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                    lambda x: x.group(0)[0].upper() + x.group(0)[1:].lower(),
                    provider)
    return re.sub(r'Nhs', r'NHS', titled)


def dataframe_from_criteria(months: List[int] = [],
                            provider_codes: List[str] = wm_provider_codes,
                            cancers: [str] = ['Suspected gynaecological cancer']) -> pd.DataFrame:
    if not months:
        months = link_map.keys()

    dfs = [_get_data_from_url(month) for month in months]
    df = pd.concat(dfs)
    return df[df['ODS'].isin(provider_codes) & df['cancer_type'].isin(cancers)]
