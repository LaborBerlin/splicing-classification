import requests
from .fetcher_base import GenomicVariant, Prediction


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}


def get_franklin_predictions(variant: GenomicVariant):
    FRANKLIN_URL = "https://franklin.genoox.com/api/fetch_predictions"
    json_data = {
        "chr": f"{variant.chr}",
        "pos": f"{variant.position}",
        "ref": variant.ref,
        "alt": variant.alt,
        "version":"",
        "analysis_id":"",
        "reference_version":variant.assembly
    }
    response = requests.post(FRANKLIN_URL, json=json_data, headers=HEADERS)
    response.raise_for_status()
    resp_data = response.json()

    if "prediction" in resp_data:
        predictions = [
            Prediction(
                score_name=algo_name,
                score_value=algo_results["score"],
                score_label=algo_results.get("prediction"),
                score_source="Franklin", variant=variant
            ) for algo_name, algo_results in resp_data["prediction"].items()
        ]
        return predictions
    return []
