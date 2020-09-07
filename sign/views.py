from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event,Guest
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render,get_object_or_404
# Create your views here.
def index(request):
    return render(request,'index.html')
def login_action(request):
    if request.method=="POST":
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)#登录
            response= HttpResponseRedirect('/event_manage/')
            #response.set_cookie('user',username,360000) #添加浏览器cookie user，3600是存储时间
            request.session['user']=username #将session记录到浏览器
            return response
        else:
            return render(request,'index.html',{'error':'username or password is error!'})
@login_required
def event_manage(request):
    #username=request.COOKIES.get('user','')#读取浏览器cookie
    event_list=Event.objects.all()
    username = request.session.get('user', '')  # 读取浏览器session
    return render(request,'event_manage.html',{'user':username,'events':event_list})
@login_required
def search_name(request):
    username=request.session.get('user','')
    search_name=request.GET.get('name','')
    event_list=Event.objects.filter(name=search_name)
    return render(request,"event_manage.html",{"user":username,"events":event_list})
@login_required
def guest_manage(request):
    username=request.session.get('user','')
    guest_list=Guest.objects.all()
    paginator=Paginator(guest_list,2)#每页显示两个嘉宾
    page=request.GET.get('page')
    try:
        contacts=paginator.page(page)
    except PageNotAnInteger: #如果page不是整数，取第一页
        contacts=paginator.page(1)
    except EmptyPage:        #如果page不在范围内，取最后一页
        contacts=paginator.page(paginator.num_pages)
    return render(request,"guest_manage.html",{"user":username,"guests":contacts})
@login_required
def sign_index(request,eid):
    event=get_object_or_404(Event,id=eid) #get_object_or_404默认调用objects.get()查询不到就报404
    return render(request,'sign_index.html',{'event':event})
@login_required
def logout(request):
    auth.logout(request)
    response=HttpResponseRedirect('/index')
    return response
@login_required
def search_phone(request):
    username = request.session.get('username', '')
    search_phone = request.GET.get("phone", "")
    search_name_bytes = search_phone.encode(encoding="utf-8")
    guest_list = Guest.objects.filter(phone__contains=search_name_bytes)

    paginator = Paginator(guest_list, 10)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, "guest_manage.html", {"user": username,
                                                   "guests": contacts,
                                                   "phone":search_phone})