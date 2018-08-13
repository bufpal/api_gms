from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404, redirect, render

from accounts.models import Profile
from v1.models import Inquiry, Notice
from .forms import InquiryCommentForm, NoticeForm

@user_passes_test(lambda u: u.is_superuser)
def root_page(request):
    return render(request, 'admin_page/index.html')


@user_passes_test(lambda u: u.is_superuser)
def profile_list(request):
    qs = Profile.objects.all()
    q = request.GET.get('q', '')
    if q :
        qs = qs.filter(user__username__icontains=q)

    return render(request, 'admin_page/profile_list.html', {
        'profile_list': qs,
    })


@user_passes_test(lambda u: u.is_superuser)
def profile_detail(request, pk):
    profile = get_object_or_404(Profile, pk=pk)

    if profile.latlng:
        lat = float(profile.latlng.split(',')[0])
        lng = float(profile.latlng.split(',')[1])
    else:
        lat = 37.520742
        lng = 127.019410

    return render(request, 'admin_page/profile_detail.html', {
        'profile': profile,
        'lat': lat,
        'lng': lng
    })


@user_passes_test(lambda u: u.is_superuser)
def inquiry_list(request):
    inquiry_list = Inquiry.objects.all().select_related('user')

    return render(request, 'admin_page/inquiry_list.html', {
        'inquiry_list': inquiry_list,
    })


@user_passes_test(lambda u: u.is_superuser)
def inquriy_detail(request, pk):
    inquiry = get_object_or_404(Inquiry, pk=pk)
    if request.method == 'POST':
        form = InquiryCommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.inquiry_id = pk
            comment.save()
            return redirect(inquiry)
    else:
        form = InquiryCommentForm()

    return render(request, 'admin_page/inquiry_detail.html', {
        'inquiry': inquiry,
        'form': form,
    })


@user_passes_test(lambda u: u.is_superuser)
def notice_list(request):
    notice = Notice.objects.all()

    return render(request, 'admin_page/notice_list.html', {
        'notice_list': notice,
    })


@user_passes_test(lambda u: u.is_superuser)
def notice_detail(request, pk):
    notice = get_object_or_404(Notice, pk=pk)

    return render(request, 'admin_page/notice_detail.html', {
        'notice': notice,
    })


@user_passes_test(lambda u: u.is_superuser)
def notice_new(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            notice = form.save()
            return redirect(notice)
    else:
        form = NoticeForm()

    return render(request, 'admin_page/notice_form.html', {
        'form': form,
    })
