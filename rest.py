import json
import requests

# TODO: what if the page doesn't exists?
def findDegrees(source, target):
    payload = {"source": source, "target": target}
    headers = {'Accept': 'application/json, text/plain, */*', 'Content-Type': 'application/json;charset=UTF-8'}
    url = 'https://api.sixdegreesofwikipedia.com/paths'
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    number_of_degrees = len(response.json()['paths'][0]) - 1
    number_of_paths = len(response.json()['paths'])

    occurrences = [0, 0, 0]

    if number_of_degrees == 1:
        occurrences[0] = number_of_paths
    elif number_of_degrees == 2:
        occurrences[1] = number_of_paths
    else:
        occurrences[2] = number_of_paths

    return occurrences
