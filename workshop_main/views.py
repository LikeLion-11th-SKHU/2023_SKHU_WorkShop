from django.shortcuts import render, redirect, get_object_or_404
from .forms import Workshop_Form
from django.utils import timezone
from .models import WorkShop
from django.http import JsonResponse
# Create your views here.

# min 변경사항
# #main / startTest / test 로 url 분리

def main(request):
    return render(request, 'main.html')

def startTest(request):
    return render(request, 'startTest.html')

def test(request):
    return render(request, 'test.html')


def guestbook(request):
    if request.method == "POST":
        # 워크샵 리액션 처리
        workshop_id = request.POST.get('workshop_id')
        action = request.POST.get('action')
        
        if action in ('like', 'dislike', 'sad'):
            workshop = WorkShop.objects.get(pk=workshop_id)
            
            if action == 'like':
                workshop.likes += 1
            workshop.save()

    # 워크샵 생성
    if request.method == 'POST':
        form = Workshop_Form(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
        return redirect('guestbook')

    # WorkShop 객체를 pub_date 기준으로 내림차순 정렬
    guest_book = WorkShop.objects.order_by('-pub_date')
    form = Workshop_Form() 
    return render(request, 'guestbook.html', {'guest_book': guest_book, 'form': form})

def introduce(request):
    return render(request, 'introduce.html')
