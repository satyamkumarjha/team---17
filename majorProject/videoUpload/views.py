from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .uploadForm import UploadFileForm
from django.shortcuts import redirect
import os
from django.conf import settings

# Create your views here.

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            course = request.POST['course']
            print('course',request.POST['course'])
            upFile = request.FILES['file']
            fileName = request.POST['FileName']
            print('filename',fileName)
            fs = FileSystemStorage()
            fs.location = os.path.join(settings.MEDIA_ROOT,'negi123')
            print(fs.location)
            fs.save(name=fileName,content=upFile)
            #handle_uploaded_file(request.FILES['file'])
            return redirect('home/')
    else:
        form = UploadFileForm()
    return render(request, 'videoUpload.html', {'form': form})