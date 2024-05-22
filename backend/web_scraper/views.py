from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
async def get_search_query(request):
    # retrieves the value of the query parameter 'search' from request URL
    # default is ''
    search_query = request.GET.get('search', '')

    return JsonResponse({'search_query': search_query})