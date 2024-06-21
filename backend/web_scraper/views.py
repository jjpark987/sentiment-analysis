from django.http import JsonResponse
from django.views import View
from .task_manager import ScraperTaskManager

class ScraperTaskView(View):
    # get_products
    def post(self, request):
        try:
            result = ScraperTaskManager().start_scraper()
            return JsonResponse({'status': 'Playwright initialized', 'session_id': result}, status=202)
        except Exception as e:
            return JsonResponse({'status': 'Error', 'message': str(e)}, status=500)
