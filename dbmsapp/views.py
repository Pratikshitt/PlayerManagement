 

from django.shortcuts import render, redirect ,Http404 
from django.http import HttpResponse,HttpResponseRedirect
from .forms import players,SearchForm,play,RegisterForm
from .models import playe,player
from django.db.models import Max
# C:\wamp64\bin\mysql\mysql5.7.26>cd bin
def emp(request):  
        if request.method == "POST":  
            form = players(request.POST)  
            if form.is_valid():  
                try:  
                    form.save()  
                    return redirect('/show')  
                except:  
                    pass  
        else:  
            form = players()  
        return render(request,'index.html',{'form':form})  
def show(request): 
    if request.method=="POST":
        search=SearchForm(request.POST)
        if search.is_valid():
            value=search.cleaned_data.get('q')
            playerss=playe.objects.filter(team_name=value)
            return render(request,'show.html',{'playerss':playerss,'form':SearchForm()}) 
            
    form=SearchForm()
    playerss = playe.objects.all() 
    maximum_value =  playe.objects.all().aggregate(Max('total_score')) 
    maximu_value =  playe.objects.all().aggregate(Max('total_wicket')) 
    print(maximum_value)
    return render(request,"show.html",{'playerss':playerss,'form':form,'maximum_value':maximum_value,'maximu_value':maximu_value})  

def showw(request,team_name):
    if request.method=="POST":
        search=SearchForm(request.POST)
        if search.is_valid():
            value=search.cleaned_data.get('q')
            playerss=playe.objects.filter(player_name=value)
            return render(request,'show.html',{'playerss':playerss,'form':SearchForm()}) 
            
    form=SearchForm()
    playerss = playe.objects.get(team_name=team_name)  
    return render(request,"showw.html",{'playerss':playerss,'form':form})

def edit(request, id):  
        playerss = playe.objects.get(id=id)  
        return render(request,'edit.html', {'playerss':playerss})  
def update(request, id):  
        playerss = playe.objects.get(id=id)  
        print(playerss)
        form = players(request.POST, instance = playerss)  
        print(form)
        print(form.is_valid())
        if form.is_valid(): 
            print(4) 
            form.save()
              
            return redirect("/show") 
           
        return render(request, 'edit.html', {'playerss': playerss})  
def destroy(request, id):  
        playerss = playe.objects.get(id=id)  
        playerss.delete()  
        return redirect("/show")  
    # Create your views here.  


def emp1(request):  
        if request.method == "POST": 
            
            form = play(request.POST)  
            if form.is_valid():  
                try:  
                    form.save()  
                    return redirect('/show1')  
                except:  
                    pass  
         
        form = play()  
        return render(request,'index1.html',{'form':form})  
def show1(request): 
    if request.method=="POST":
        search=SearchForm(request.POST)
        if search.is_valid():
            value=search.cleaned_data.get('q')
            playerss=player.objects.filter(team_name=value)
            return render(request,'show1.html',{'playerss':playerss,'form':SearchForm()}) 
            
    form=SearchForm()
    playerss = player.objects.all()  
    return render(request,"show1.html",{'playerss':playerss,'form':form})  
def edit1(request, id):  
        playerss = player.objects.get(id=id)  
        return render(request,'edit1.html', {'playerss':playerss})  
def update1(request, id):  
        playerss = player.objects.get(id=id)  
        print(playerss)
        form = play(request.POST, instance = playerss)  
        print(form)
        print(form.is_valid())
        if form.is_valid(): 
            print(4) 
            form.save()
              
            return redirect("/show1") 
           
        return render(request, 'edit1.html', {'playerss': playerss})  
def destroy1(request, id):  
        playerss = player.objects.get(id=id)  
        playerss.delete()  
        return redirect("/show1")  

def tournament(request):
    if(request.POST.get("World Cup")):
        return redirect('/show')
    elif(request.POST.get('IPL')):
        return redirect('/show1')
         
    else:
        return render(request,'tournament.html')

def register(response):
    if response.method == "POST":
	    form = RegisterForm(response.POST)
	    if form.is_valid():
	        form.save()

	    return HttpResponseRedirect('http://127.0.0.1:8000/accounts/login/')
    else:

	    form = RegisterForm()

    return render(response, "register.html", {"form":form})
    

      

    # Create your views here.  


    