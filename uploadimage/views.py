from django.shortcuts import render
from .models import Photo, Category
# Create your views here.
from .form import ImageForm
# image gallary
def index(request):
    category = request.GET.get('category')
    if category ==None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name = category )

    category = Category.objects.all()

    context = {'cat':category, "photos":photos}
    return render(request, "index.html", context)

# add image here
def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'add.html', {'form': form})