from django.http import JsonResponse
from django.views import View
from .task_manager import ScraperTaskManager

class ScraperTaskView(View):
    # get_products
    def post(self, request):
        try:
            task_manager = ScraperTaskManager()
            result = task_manager.start_scraper()
            return JsonResponse({'status': 'Playwright initialized', 'task_id': result.id}, status=202)
        except Exception as e:
            return JsonResponse({'status': 'Error', 'message': str(e)}, status=500)
