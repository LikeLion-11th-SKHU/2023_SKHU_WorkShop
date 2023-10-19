from django.shortcuts import render, redirect, get_object_or_404
from .forms import Workshop_Form
from django.utils import timezone
from .models import WorkShop
from django.http import JsonResponse
# Create your views here.
def workshop_main(request):
    return render(request, 'workshop_main.html')

def workshop_read(request):
    if request.method == "POST":
        # 워크샵 리액션 처리
        workshop_id = request.POST.get('workshop_id')
        action = request.POST.get('action')
        
        if action in ('like', 'dislike', 'sad'):
            workshop = WorkShop.objects.get(pk=workshop_id)
            
            if action == 'like':
                workshop.likes += 1
            elif action == 'dislike':
                workshop.dislikes += 1
            elif action == 'sad':
                workshop.sadness += 1
            workshop.save()

    # 워크샵 생성
    if request.method == 'POST':
        form = Workshop_Form(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()

    # WorkShop 객체를 pub_date 기준으로 내림차순 정렬
    guest_book = WorkShop.objects.order_by('-pub_date')
    form = Workshop_Form() 
    return render(request, 'workshop_read.html', {'guest_book': guest_book, 'form': form})
    
