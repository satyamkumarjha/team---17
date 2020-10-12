from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.
def upload(request):
    if request.method == 'POST':
        context = {}
        uploadedFile = request.FILES['document']
        courseName = request.POST['text']
        print(courseName)
        #print(uploadedFile.name)
        #print(uploadedFile.size)
        fs = FileSystemStorage()
        name = fs.save(name = uploadedFile.name,content = uploadedFile)
        context['url'] = fs.url(name)
    return render(request,'videoUpload.html',context)