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
                # 사용자가 이미 이 워크샵에 좋아요를 눌렀는지 확인
                if 'liked_workshops' not in request.session:
                    request.session['liked_workshops'] = []

                if workshop_id not in request.session['liked_workshops']:
                    workshop.likes += 1
                    workshop.save()
                    # 해당 워크샵을 좋아요 표시한 것으로 표시
                    request.session['liked_workshops'].append(workshop_id)
                    request.session.modified = True  # 세션 저장

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

def cast(request):
    return render(request, 'cast.html')
