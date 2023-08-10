from django.shortcuts import render,redirect
from chat_app.models import room,message
from django.http import HttpResponse, JsonResponse

def home(request):
    return render(request,'index.html')

def Room(request,Broom):
    username=request.GET.get('username')
    room_details=room.objects.get(roomname=Broom)
    return render(request, 'room.html', {
        'username': username,
        'room': Broom,
        'room_details': room_details
    })

    

def checkview(request):
    roomname=request.POST.get('room_name')
    username=request.POST.get('username')

    if room.objects.filter(roomname=roomname).exists():
        return redirect('/'+roomname+'/?username='+username)
    else:
        new_room=room.objects.create(roomname=roomname)
        new_room.save()
        return redirect('/'+roomname+'/?username='+username)

def send(request):
    Message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = message.objects.create(value=Message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request,broom):
    room_details = room.objects.get(roomname=broom)
    messages = message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})
