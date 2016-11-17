import json
import requests

from django.http.response import HttpResponse


def test_giphy(request):

    body = "channel_id=5p9xd4brfincpgr5mjnpm31sko&channel_name=testing-commands&command=%2Fgiphy&response_url=not+supported+yet&team_domain=unit-d&team_id=ukfjbw1113yh8koubk7ocumfgw&text=sdfasdfsdf&token=1nd87ztd3ib5mckuekqxxtsjow&user_id=cgqfob68cjnm8bap3rwz8yhshw&user_name=domjones"
    r = requests.get('http://localhost:8081/giphy', body=body, )

    return HttpResponse(True)


def giphy_remote(request):
    gif = ""
    dict = {}
    args = request.body.split('&')

    text = None
    for arg in args:
        arg_tmp = arg.split('=')
        dict[arg_tmp[0]] = arg_tmp[1]

    keywords = dict.get('text', None)

    if keywords:
        gif = "(%s)" % query_giphy_api(keywords)

    json_data = {
        "response_type": "in_channel",
        'text': gif,
    }
    json_dump = json.dumps(json_data)
    return HttpResponse(json_dump)


def query_giphy_api(keywords):
    url = "http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=american+psycho"
    r = requests.get(url)
    dict = json.loads(r.text)
    data = dict.get('data', None)
    if data:
        return data.get('url', None)
    return None