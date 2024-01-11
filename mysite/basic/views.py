from django.http import HttpResponse
from silk.profiling.profiler import silk_profile


@silk_profile()
def index(request):
    return HttpResponse("Hello, world. You're at the basic index.")

@silk_profile()
def slow_index(request):
    import time
    time.sleep(5)
    return HttpResponse("Hello, world. You're at the basic slow index.")
