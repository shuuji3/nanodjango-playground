from django.db import models
from nanodjango import Django

app = Django()

@app.admin(
    list_display=['id', 'timestamp'],
    readonly_fields=['timestamp'],
)
class CountLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)

@app.route('/')
def count(request):
    CountLog.objects.create()
    return f'<p>Access counter: {CountLog.objects.count()}</p>'

@app.api.get('/add')
def add(request):
    CountLog.objects.create()
    return {'count': CountLog.objects.count()}

@app.route('/slow')
async def slow(request):
    import asyncio
    await asyncio.sleep(3)
    return 'async views supported!'
