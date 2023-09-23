from django.shortcuts import render
from images.models import Image

def index(request):
    image_url = None

    if request.method == 'POST' and request.FILES.get('imagen'):
        image = request.FILES['imagen']

        aws_image = Image.objects.create(
            name=image.name,
            image=image
        )

        image_url = aws_image.image.url
       

    return render(request, 'index.html', {
        'image_url': image_url
    })