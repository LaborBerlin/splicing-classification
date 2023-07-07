import requests

from .fetcher_base import GenomicVariant, HGVSVariant


def convert_hgvs_genomic(inVariant: HGVSVariant) -> GenomicVariant | None:
    """Convert HGVS String to genomic variant.
    """
    URL = "https://grch37.rest.ensembl.org/vep/human/hgvs/{hgvs_string}?content-type=application/json&vcf_string=1"
    url = URL.format(hgvs_string=inVariant.hgvs_string)
    resp = requests.get(url)
    resp.raise_for_status()
    data = resp.json()
    vcf_strings = {d['vcf_string'] for d in data}

    if len(vcf_strings) == 1:
        vcf_string, = vcf_strings
        return GenomicVariant.from_string(vcf_string, "GRCh37")
