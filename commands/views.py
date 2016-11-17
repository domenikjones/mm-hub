import json

from django.http.response import HttpResponse


def giphy_remote(request):

    print("Body: %s" % request.body)
    print("GET: %s" % request.GET)
    print("POST: %s" % request.POST)

    #1nd87ztd3ib5mckuekqxxtsjow

    json_data = {
        "response_type": "in_channel",
        'text': "this is a test commands response",
    }

    json_dump = json.dumps(json_data)
    print(json_dump)

    return HttpResponse(json_dump)