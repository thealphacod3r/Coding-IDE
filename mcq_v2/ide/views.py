from django.shortcuts import render

# Create your views here.




def ide(request):
	return render(request,"ide/ide_home.html",{})
