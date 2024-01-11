import time
from django.http import HttpResponse
from silk.profiling.profiler import silk_profile


@silk_profile()
def index(request):
    time.sleep(5)
    return HttpResponse("Hello, world. You're at the basic-1 index.")

@silk_profile()
def index_2(request):
    time.sleep(5)
    return HttpResponse("Hello, world. You're at the basic-2 index.")
