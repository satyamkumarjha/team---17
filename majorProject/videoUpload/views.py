from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.
def upload(request):
    if request.method == 'POST':
        uploadedFile = request.FILES['document']
        #print(uploadedFile.name)
        #print(uploadedFile.size)
        fs = FileSystemStorage()
        fs.save(name = uploadedFile.name,content = uploadedFile)
    return render(request,'videoUpload.html')