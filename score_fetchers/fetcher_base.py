from pydantic import BaseModel

import re


class GenomicVariant(BaseModel):

    assembly: str
    chr: str
    position: int

    ref: str
    alt: str

    @classmethod
    def from_string(cls, data: str, assembly: str) -> "GenomicVariant | None":
        if m := re.match(r"([\dXYxy]+)[ :\-_)]+(\d+)[ \-_:]*([ATCGatcg]+)[ >\-_:]([ATCGatcg]+)", data):
            chr = m.group(1)
            position = int(m.group(2))
            ref = m.group(3)
            alt = m.group(4)
            return cls(assembly=assembly, chr=chr, position=position, ref=ref, alt=alt)


class HGVSVariant(BaseModel):
    hgvs_string: str

    @classmethod
    def from_string(cls, data: str):
        return HGVSVariant(hgvs_string=data)


class Prediction(BaseModel):

    variant: GenomicVariant
    score_value: str
    score_label: str | None = None
    score_name: str

    score_source: str
