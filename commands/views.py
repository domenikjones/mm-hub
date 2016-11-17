import json

from django.http.response import HttpResponse


def giphy_remote(request):

    print("GET: %s" % request.GET)
    print("POST: %s" % request.POST)

    json_data = {
        'text': "this is a test commands response",
    }

    json_dump = json.dumps(json_data)
    print(json_dump)

    return HttpResponse(json_dump)