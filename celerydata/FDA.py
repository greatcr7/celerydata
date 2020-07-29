"""Main module."""
import requests

fda_base_url = "https://api.fda.gov"
endpoint_type_list = ["drug", "animalandveterinary", "device", "food", "other"]
file_name_dict = dict()



def constructCompleteUrl(fda_base_url: str, endpoint_type: str, file_name: str, search_term: str, limit: str = 1) -> str:
    return fda_base_url + "/" + endpoint_type + file_name + "?search=" + search_term + "&limit=" + limit
