import json

from django.http.response import HttpResponse


def giphy_remote(request):

    print("Body: %s" % request.body)
    print("GET: %s" % request.GET)
    print("POST: %s" % request.POST)

    #1nd87ztd3ib5mckuekqxxtsjow

    dict = {}
    args = request.body.split('&')
    for arg in args:
        arg_tmp = arg.split('0')
        dict[arg_tmp[0]] = arg_tmp[1]

    print(dict)

    json_data = {
        "response_type": "in_channel",
        'text': "this is a test commands response",
    }

    json_dump = json.dumps(json_data)
    print(json_dump)

    return HttpResponse(json_dump)