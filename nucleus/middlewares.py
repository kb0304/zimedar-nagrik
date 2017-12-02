import traceback

class LogMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            print(request.body)
            # print(request.META)
            return self.get_response(request)
        except:
            path = request.get_full_path() # Get the URL Path
            tb = traceback.format_exc() # Get the traceback
            meta = request.META # Get request meta information
            # Log everything
            print(path)
            print(tb)
            print(meta)
            raise  # Raise exception again after catching