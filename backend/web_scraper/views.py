from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def get_product_keyword(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        return JsonResponse({'keyword': keyword})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)