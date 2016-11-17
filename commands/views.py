import json

from django.http.response import HttpResponse


def giphy_remote(request):

    json_data = {
        'text': "this is a test commands response",
    }

    return HttpResponse(json.dumps(json_data))