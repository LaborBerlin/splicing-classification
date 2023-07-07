"""Clean the excel input data and create a list of variants for which we can fetch scores.
"""

import pandas as pd
import pickle

from score_fetchers.fetcher_base import HGVSVariant
from score_fetchers.fetcher_vep import convert_hgvs_genomic

all_splice_data = pd.read_excel("./data/LR_splice_20230707.xlsx", sheet_name="Data", skiprows=1)
all_splice_data["genomic"] = all_splice_data["name"].apply(lambda n: convert_hgvs_genomic(HGVSVariant.from_string(n)))

with open("./data/LR_splice_20230707.pkl", "wb") as outfile:
    pickle.dump(all_splice_data, outfile)
