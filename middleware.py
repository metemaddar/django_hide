from django.core import signing
class CSRFHIDEMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.method == "POST":
            if not request.POST._mutable:
                request.POST._mutable = True
            csrf_token = request.POST.get('csrfmiddlewaretoken', '')
            if csrf_token == '':
                csrf_field = signing.dumps('csrfmiddlewaretoken').partition(':')[0]
                request_csrf_token = request.POST.get(csrf_field, '')
                request.POST['csrfmiddlewaretoken'] = request_csrf_token
                request.POST._mutable = False
            
            
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response