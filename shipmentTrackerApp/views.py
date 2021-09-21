from django.shortcuts import render, redirect
from django.contrib import messages
from . models import *
import bcrypt


# Create your views here.


#render the index (GOOD)
def index(request):
    request.session.flush()
    return render(request, 'index.html')

#validate the registration (GOOD)
def register(request): #post redirect
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        print(errors)
        if len(errors) != 0: 
            for key, value in errors.items():
                messages.error(request, value)
            return redirect ('/')
        #hash the password
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        #create a user
        new_user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = hashed_pw 
        )
        #create a session
        request.session['user_id'] = new_user.id
        return redirect ('/ships')
    return redirect('/')

#log in (GOOD)
def login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        this_user = User.objects.filter(email=request.POST['email'])
        request.session['user_id'] = this_user[0].id
        return redirect('/ships')
    return redirect('/')

#log out (GOOD)
def logout(request):
    request.session.flush()
    return redirect('/')

#renders add ship page (GOOD)
def addship(request):
    if 'user_id' not in request.session:
        return redirect('/')
    return render(request, 'addship.html')

#render the ships (GOOD)
def ships(request):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user = User.objects.filter(id=request.session['user_id'])
    context = {
        'user': this_user[0],
        'all_the_ships': Ship.objects.all()
    }
    return render(request, 'ships.html', context)

#creates ship 
def create_ship(request):
    if 'user_id' not in request.session:
        return redirect('/')
    if request.method == "POST":
        errors = Ship.objects.ship_validator(request.POST)
        if len(errors) != 0: 
            for key, value in errors.items():
                messages.error(request, value)
            return redirect ('/addship')
        this_user = User.objects.filter(id=request.session['user_id'])
        if request.POST['date_booked'] == '':
            date_booked = None
        else: 
            date_booked = request.POST['date_booked']
        if request.POST['ship_start'] == '':
            ship_start = None
        else: 
            ship_start = request.POST['ship_start']
        if request.POST['ship_end'] == '':
            ship_end = None
        else: 
            ship_end = request.POST['ship_end']
        if request.POST['last_day_pricing'] == '':
            last_day_pricing = None
        else: 
            last_day_pricing = request.POST['last_day_pricing']
        if request.POST['eta_gh'] == '':
            eta_gh = None
        else: 
            eta_gh = request.POST['eta_gh']
        if request.POST['etd_gh'] == '':
            etd_gh = None
        else: 
            etd_gh = request.POST['etd_gh']
        if request.POST['eta_disport'] == '': 
            eta_disport = None
        else: 
            eta_disport = request.POST['eta_disport']
        new_ship = Ship.objects.create(date_booked=date_booked, client=request.POST['client'], batch=request.POST['batch'], volume=request.POST['volume'], basis=request.POST['basis'], ship_start=ship_start, ship_end=ship_end,vessel_name=request.POST['vessel_name'], last_day_pricing=last_day_pricing, eta_gh=eta_gh, etd_gh=etd_gh, eta_disport=eta_disport, notes=request.POST['notes'], user=User.objects.get(id=request.session['user_id']))
        return redirect('/addship')

# shows individual ship (GOOD)
def view(request, ship_id):
    if 'user_id' not in request.session:
        return redirect('/')
    one_ship = Ship.objects.get(id=ship_id)
    this_user = User.objects.filter(id=request.session['user_id'])
    context = {
        'ship': one_ship,
        'user': this_user[0],
        'one_ship': one_ship,
    }
    return render(request, 'view.html', context)

#to update a shipment
def update(request, ship_id):
    if 'user_id' not in request.session:
        return redirect('/')
    if request.method == "POST":
        errors = Ship.objects.ship_validator(request.POST)
        if len(errors) != 0: 
            for key, value in errors.items():
                messages.error(request, value)
            return redirect (f'/view/{ship_id}/')
        this_user = User.objects.filter(id=request.session['user_id'])
        if request.POST['date_booked'] == '':
            date_booked = None
        else: 
            date_booked = request.POST['date_booked']
        if request.POST['ship_start'] == '':
            ship_start = None
        else: 
            ship_start = request.POST['ship_start']
        if request.POST['ship_end'] == '':
            ship_end = None
        else: 
            ship_end = request.POST['ship_end']
        if request.POST['vessel_name'] == '':
            vessel_name = None
        else: 
            vessel_name = request.POST['vessel_name']
        if request.POST['last_day_pricing'] == '':
            last_day_pricing = None
        else: 
            last_day_pricing = request.POST['last_day_pricing']
        if request.POST['eta_gh'] == '':
            eta_gh = None
        else: 
            eta_gh = request.POST['eta_gh']
        if request.POST['etd_gh'] == '':
            etd_gh = None
        else: 
            etd_gh = request.POST['etd_gh']
        if request.POST['eta_disport'] == '': 
            eta_disport = None
        else: 
            eta_disport = request.POST['eta_disport']
        to_update = Ship.objects.get(id=ship_id)
        to_update.date_booked=date_booked
        to_update.client=request.POST['client']
        to_update.batch=request.POST['batch']
        to_update.volume=request.POST['volume']
        to_update.basis=request.POST['basis']
        to_update.ship_start=ship_start
        to_update.ship_end=ship_end
        to_update.vessel_name=vessel_name
        to_update.last_day_pricing=last_day_pricing
        to_update.eta_gh=eta_gh
        to_update.etd_gh=etd_gh
        to_update.eta_disport=eta_disport
        to_update.notes=request.POST['notes']
        to_update.save()
    return redirect('/ships')

# query for user with user_id (NOT DONE)
def profile(request, user_id):
    if 'user_id' not in request.session:
        return redirect('/')
    one_user = User.objects.get(id=user_id)
    this_user = User.objects.filter(id=request.session['user_id'])
    context = {
        'user': one_user,
        'logged_user': this_user[0],
    }
    return render(request, "profile.html", context)

#to update user profile
def updateprofile(request, user_id):
    if 'user_id' not in request.session:
        return redirect('/')
    if request.method == "POST":
        errors = User.objects.profile_validator(request.POST)
        print(errors)
        if len(errors) != 0: 
            for key, value in errors.items():
                messages.error(request, value)
            return redirect (f'/profile/{user_id}/')
        this_user = User.objects.filter(id=request.session['user_id'])
        to_update = User.objects.get(id=user_id)
        to_update.first_name = request.POST['first_name']
        to_update.last_name = request.POST['last_name']
        to_update.email = request.POST['email']
        to_update.save()
    return redirect(f'/profile/{user_id}/')

# query for user profile pic with user_id (NOT DONE)
def profilepic(request, user_id):
    if 'user_id' not in request.session:
        return redirect('/')
    one_user = User.objects.get(id=user_id)
    this_user = User.objects.filter(id=request.session['user_id'])
    context = {
        'user': one_user,
        'logged_user': this_user[0],
    }
    return render(request, "profilepic.html", context)

#to update user profile pic
def updateprofilepic(request, user_id):
    if 'user_id' not in request.session:
        return redirect('/')
    # if request.method == "POST":
    #     errors = User.objects.profile_validator(request.POST)
    #     print(errors)
    #     if len(errors) != 0: 
    #         for key, value in errors.items():
    #             messages.error(request, value)
    #         return redirect ('/profile')
    this_user = User.objects.filter(id=request.session['user_id'])
    to_update = User.objects.get(id=user_id)
    to_update.profile_pic = request.FILES['profile_pic']
    to_update.save()
    return redirect(f'/profilepic/{user_id}/')

# deletes the trip
def delete(request, ship_id):
    if 'user_id' not in request.session:
        return redirect('/')
    to_delete = Ship.objects.get(id=ship_id)
    to_delete.delete()
    return redirect('/ships')


