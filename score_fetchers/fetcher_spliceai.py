from typing import List
import requests
from .fetcher_base import GenomicVariant, HGVSVariant, Prediction



def get_spliceai_predictions(variant: GenomicVariant | HGVSVariant) -> List[Prediction]:
    SPLICE_AI_URL = "https://spliceailookup-api.broadinstitute.org/spliceai/?hg=37&distance=500&mask=1&variant=19-11233940-G-A&raw=19-11233940%20-%20G-A"

    if isinstance(variant, GenomicVariant):
        if variant.assembly in ("GRCh37", "hg19"):
            assemblyint = 37
        elif variant.assembly in ("GRCh38", "hg38"):
            assemblyint = 38
        else:
            raise RuntimeError(f"Unsupported assembly string {variant.assembly}")
    elif isinstance(variant, HGVSVariant):
        variant.hgvs_string

    params = {
        "hg": assemblyint,
        "distance": 500,
        "mask": 1,
    }
