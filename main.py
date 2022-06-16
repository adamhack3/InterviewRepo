import requests
import re

def addresses_for_postcode(input_postcode:str) -> list:
    BASE_URL = "https://6kb2p9kgb0.execute-api.eu-west-2.amazonaws.com/production/api/v1/addresses/"

    params = {
        "postcode": input_postcode
    }

    POSTCODE_REGEX = "[A-Za-z][1-9] [1-9][A-Za-z]{2}"

    if re.match(POSTCODE_REGEX, input_postcode) is None:
        raise ValueError(f"Invalid Postcode format for {input_postcode}, must be alphanumeric with space")

    with open("secrets/token.txt", "r") as outfile:
        token = outfile.read()

    response = requests.get(
        BASE_URL,
        params=params,
        headers= {
            "Authorization" : token
        }
    )

    address_data = response.json()
    address_list = address_data["data"]["address"]
    return address_list

