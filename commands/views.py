import json
import requests
from django.http.response import HttpResponse


def giphy_remote(request):
    response_text = ""
    dict = {}
    args = request.body.split('&')
    for arg in args:
        arg_tmp = arg.split('=')
        dict[arg_tmp[0]] = arg_tmp[1]
    keywords = dict.get('text', None)
    if keywords:
        response_text = "/giphy %s     ![alt text](%s \"%s\")" % (keywords, query_giphy_api(keywords), keywords)
    json_data = {
        "response_type": "in_channel",
        'text': response_text,
    }
    json_dump = json.dumps(json_data)
    return HttpResponse(json_dump)


def query_giphy_api(keywords):
    url = "http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=%s" % keywords
    r = requests.get(url)
    dict = json.loads(r.text)
    data = dict.get('data', None)
    if data:
        return data.get('image_original_url', None)
    return None