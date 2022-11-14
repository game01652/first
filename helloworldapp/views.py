from django.shortcuts import render

def helloworldfunction(request):
    return render(request, 'top.html')

def move_to_page(request):
    return render(request, 'book_list.html')

def index(request):
    return render(request, 'index.html')

def form(request):
  msg = request.POST['msg']
  params = {
    'title': 'Hello/Form',
    'msg': 'こんにちは、' + msg + 'さん。',
  }
  return render(request, 'index.html', params)