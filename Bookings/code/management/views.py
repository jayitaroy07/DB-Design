from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    clist = contact.objects.all()
    ct = {
        'contact_list': clist,
        'login':False,
    }
    return render(request, 'management/home.html', ct)

def home(request):
    login=False
    if request.user.is_authenticated:
        login=True
    clist = contact.objects.all()
    fname = request.GET.get('fname')
    mname = request.GET.get('mname')
    lname = request.GET.get('lname')
    if fname and mname and lname:
        clist = contact.objects.filter(fname=fname, mname=mname, lname=lname)
    elif fname and mname:
        clist = contact.objects.filter(fname=fname, mname=mname)
    elif fname and lname:
        clist = contact.objects.filter(fname=fname, lname=lname)
    elif lname and mname:
        clist = contact.objects.filter(mname=mname, lname=lname)
    elif fname:
        clist = contact.objects.filter(fname=fname)
    elif mname:
        clist = contact.objects.filter(mname=mname)
    elif lname:
        clist = contact.objects.filter(lname=lname)
    count = len(clist)
    ct = {
        'contact_list': clist,
        'login':login,
        'count':count
    }
    return render(request, 'management/home.html', ct)

@login_required
def add(request): # form => sare values... fill the tables... send to homepage
    return render(request, 'management/add.html')


def details(request,pk):
    login=False
    if request.user.is_authenticated:
        login=True
    cont = contact.objects.filter(contact_id=pk)[0]
    all_address_details = address.objects.filter(contact_id=pk)
    if all_address_details:
        present_address_details = address.objects.filter(contact_id=pk).order_by('-address_id')[0]
    else:
        present_address_details = ''
    all_phone_details = phone.objects.filter(contact_id=pk)
    if all_phone_details:
        present_phone_details = phone.objects.filter(contact_id=pk).order_by('-phone_id')[0]
    else:
        present_phone_details=''
    all_booking_details = date.objects.filter(contact_id=pk)
    
    context = {
        'contact':cont,
        'present_address': present_address_details,
        'address_list': all_address_details,
        'present_phone': present_phone_details,
        'phone_list': all_phone_details,
        'booking_list': all_booking_details,
        'login':login,
    }

    return render(request, 'management/details.html', context)

@login_required
def edit(request,pk):
    cont = contact.objects.filter(contact_id=pk)[0]
    all_address_details = address.objects.filter(contact_id=pk)
    if all_address_details:
        present_address_details = address.objects.filter(contact_id=pk).order_by('-address_id')[0]
    else:
        present_address_details = ''
    all_phone_details = phone.objects.filter(contact_id=pk)
    if all_phone_details:
        present_phone_details = phone.objects.filter(contact_id=pk).order_by('-phone_id')[0]
    else:
        present_phone_details=''
    all_booking_details = date.objects.filter(contact_id=pk)
    
    context = {
        'contact':cont,
        'present_address': present_address_details,
        'address_list': all_address_details,
        'present_phone': present_phone_details,
        'phone_list': all_phone_details,
        'booking_list': all_booking_details,
    }
    return render(request, 'management/edit.html', context)

@login_required
def delete(request,pk):
    contact.objects.filter(contact_id=pk).delete()
    return HttpResponseRedirect("/")

@login_required
def add_address(request,pk):
    cont = contact.objects.filter(contact_id=pk)[0]
    new_address=address(contact_id=cont,address_type=request.GET.get('add_type'),address=request.GET.get('address'),state=request.GET.get('state'),city=request.GET.get('city'),zip=request.GET.get('zip'))
    new_address.save()
    return HttpResponseRedirect("/details/"+str(pk)+"/")

@login_required
def add_phone(request,pk):
    cont = contact.objects.filter(contact_id=pk)[0]
    new_phone=address(contact_id=cont,address_type=request.GET.get('add_type'),address=request.GET.get('address'),state=request.GET.get('state'),city=request.GET.get('city'),zip=request.GET.get('zip'))
    new_phone.save()
    return HttpResponseRedirect("/details/"+str(pk)+"/")

@login_required
def add_booking(request,pk):
    cont = contact.objects.filter(contact_id=pk)[0]
    new_book=date(contact_id=cont,date_type=request.GET.get('date_type'),date=request.GET.get('date'))
    new_book.save()
    return HttpResponseRedirect("/details/"+str(pk)+"/")

@login_required
def add_contact(request):
    # if request.GET.get('add_type').lower() in ['home', 'work', 'other'] and request.GET.get('phone_type').lower() in ['home','work','fax'] and len(request.GET.get('area_code'))<=3 and request.GET.get('number').isdecimal():
    new_contact=contact(fname=request.GET.get('fname'),mname=request.GET.get('mname'),lname=request.GET.get('lname'))
    new_contact.save()
    new_address=address(contact_id=new_contact,address_type=request.GET.get('add_type'),address=request.GET.get('address'),state=request.GET.get('state'),city=request.GET.get('city'),zip=request.GET.get('zip'))
    new_address.save()
    new_phone=phone(contact_id=new_contact,phone_type=request.GET.get('phone_type'),area_code=request.GET.get('area_code'),number=request.GET.get('number'))
    new_phone.save()
    # new_contact=contact(fname=request.GET.get('fname'),mname=request.GET.get('mname'),lname=request.GET.get('lname'))
    # return details(request,new_contact.contact_id)
    return HttpResponseRedirect("/details/"+str(new_contact.contact_id)+"/")
    

@login_required    
def update_booking(request,pk1,pk2):
    context = {
        'contact_id':pk1,
        'date_id': pk2,
    }
    return render(request,'management/update_booking.html',context)

@login_required
def change_booking(request,pk1,pk2):
    changebooking=date.objects.filter(contact_id=pk1,date_id=pk2)[0]
    if request.GET.get('date_type'):
        changebooking.date_type=request.GET.get('date_type')
    if request.GET.get('date'):
        changebooking.date=request.GET.get('date')
    changebooking.save()
    return HttpResponseRedirect("/details/"+str(pk1)+"/")

    

