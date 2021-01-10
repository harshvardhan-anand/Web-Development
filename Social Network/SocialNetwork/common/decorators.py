from django.http import HttpResponseBadRequest

def ajax_required(f):
    def checker(request):
        if not request.is_ajax():
            return HttpResponseBadRequest()
        return f(request)
    return checker