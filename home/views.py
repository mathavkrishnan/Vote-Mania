from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from .models import vote,vote_likes
import math
def homy(request):
    objk = vote.objects.all()
    if request.method == 'GET':
        return render(request,'home/home.html',{'obj':objk})
    else:
        obj = vote.objects.get(pk=1)
        error = 'Vote casted'
        try:
            vote_like = vote_likes.objects.get(user = request.user)
        except vote_likes.DoesNotExist:
            vote_like = None
        if request.POST.get('one') == "one" and not vote_like:
            b = vote_likes(user = request.user)
            b.save()
            p1 = (1/(1+math.pow(10,((obj.onevote-obj.twovote)/400))))
            obj.onevote = obj.onevote+30*(1-p1)
            obj.twovote = obj.twovote+30*(p1-1)
            obj.save()
        elif request.POST.get('two') == "two" and not vote_like:
            b = vote_likes(user = request.user)
            b.save()
            p2 = (1/(1+pow(10,((obj.twovote-obj.onevote)/400))))
            obj.onevote = obj.twovote+30*(1-p2)
            obj.twovote = obj.onevote+30*(p2-1)
            obj.save()
        else:
            error = 'Already voted'
        return render(request,'home/home.html',{'obj':objk,'err':error})
def ind(request):
    return render(request,'home/index.html')
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('ind')
    
