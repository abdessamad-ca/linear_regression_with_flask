import requests
BASE_URL = "https://linearregression.azurewebsites.net/"
years_exp = {"YearsExperience": 8}
response = requests.post("{}/predict".format(BASE_URL), json = years_exp)

print(response.json())
