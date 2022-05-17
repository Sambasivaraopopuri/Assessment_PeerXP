import email
from django.shortcuts import redirect, render
from .models import Login,Ticket
import datetime
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    if request.method == "POST": 
        database_data = Login.objects.all()
        print(request.POST["pass"])
        for i in database_data:
            if i.email==request.POST["email"] and i.password == request.POST["pass"]:
                # data={eamil:i.email,name:i.name}
                # print(i.name)
                request.session["email"] = i.email
                request.session["name"] = i.name
                return render(request,"Home.html",{})
    return render(request,"index.html",{})
def ticket(request):
    if request.session["email"]!="" and request.session["name"]!="":
        if request.method=="POST":
            Department=request.POST['Department']
            Category=request.POST['Category']
            url=request.POST['url']
            Subject=request.POST['Subject']
            Description=request.POST['Description']
            ContactName=request.POST['ContactName']
            email=request.POST['email']
            Phone=request.POST['Phone']
        
            upload_file=request.POST['file']
            time = datetime.datetime.now()
            obj=Ticket.objects.create(Department=Department,Category=Category,VegaOps_GitLab_Project_URL=url,Subject=Subject,Description=Description,Contact_Name=ContactName,Email=email,Phone=Phone,upload_file=upload_file,upload_date=time)
            obj.save()

            return redirect('Home')
    return render(request,"register.html",{})
def Home(request):
    ticketdata = Ticket.objects.all()
    print(request.session["email"])
    for i in ticketdata:
        if request.session["email"]==i.Email :
            return render(request,"test.html",{'count':len(ticketdata),'tickets':ticketdata})
    return render(request,"index.html",{})