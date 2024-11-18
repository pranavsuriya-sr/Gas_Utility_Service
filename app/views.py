from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import sqlite3

def index(request):
    return render(request, 'home.html')

# def allServices(request):
#     currentUser = request.session.get('user')
#     if currentUser is None:
#         return HttpResponseRedirect('/login')

#     db_connection = sqlite3.connect("./db/db.sqlite3")
#     db_cursor = db_connection.cursor()
#     db_cursor.execute("SELECT * FROM serviceData")
#     services = db_cursor.fetchall()
#     services = [dict(zip([key[0] for key in db_cursor.description], service)) for service in services]

#     if currentUser['type'] == 'customer':
#         for i in range(len(services)):
#             services[i] = {
#                 'id': services[i]['id'],
#                 'typeName': services[i]['typeName'],
#                 'description': services[i]['description']
#             }

#     return render(request, 'all_services.html', {'services': services, 'user': currentUser})

def allServices(request):
    currentUser = request.session.get('user')
    if currentUser is None:
        return HttpResponseRedirect('/login')

    db_connection = sqlite3.connect("./db/db.sqlite3")
    db_cursor = db_connection.cursor()

    db_cursor.execute("SELECT * FROM serviceData")
    services = db_cursor.fetchall()
    services = [dict(zip([key[0] for key in db_cursor.description], service)) for service in services]
    if currentUser['type'] == 'admin':
        db_cursor.execute("SELECT * FROM userAsks WHERE approval = 'not approved'")
        all_user_requests = db_cursor.fetchall()
        all_user_requests = [dict(zip([key[0] for key in db_cursor.description], request)) for request in all_user_requests]

        if request.method == "POST":
            selected_request_ids = request.POST.getlist('selected_requests')
            for request_id in selected_request_ids:
                db_cursor.execute("UPDATE userAsks SET approval = 'approved' WHERE reqId = ?", (request_id,))
            db_connection.commit()
            return HttpResponseRedirect('/service/all')

        return render(request, 'all_services.html', {
            'services': services,
            'all_user_requests': all_user_requests,
            'user': currentUser
        })

    elif currentUser['type'] == 'customer':
        db_cursor.execute("SELECT * FROM userAsks WHERE id = ?", (currentUser['id'],))
        user_requests = db_cursor.fetchall()
        user_requests = [dict(zip([key[0] for key in db_cursor.description], request)) for request in user_requests]

        if request.method == "POST":
            selected_service_ids = request.POST.getlist('selected_services')
            for service_id in selected_service_ids:
                db_cursor.execute("SELECT typeName, description FROM serviceData WHERE id = ?", (service_id,))
                service = db_cursor.fetchone()
                if service:
                    typeName, description = service
                    address = currentUser.get('address', 'NA')
                    db_cursor.execute(
                        "INSERT INTO userAsks (id, typeName, description, address, approval) VALUES (?, ?, ?, ?, 'not approved')",
                        (currentUser['id'], typeName, description, address)
                    )
            db_connection.commit()
            return HttpResponseRedirect('/service/all')

        return render(request, 'all_services.html', {
            'services': services,
            'user_requests': user_requests,
            'user': currentUser
        })

    return HttpResponse("Unauthorized")





def newService(request):
    currentUser = request.session.get('user')

    if currentUser is None:
        return HttpResponseRedirect('/login')
    
    if currentUser['type'] != 'admin':
        return HttpResponse('Unauthorized')

    if request.method == "POST":
        typeName = request.POST.get('typeName')
        description = request.POST.get('description')


        db_connection = sqlite3.connect("./db/db.sqlite3")
        db_cursor = db_connection.cursor()

        db_cursor.execute(f"SELECT * FROM serviceData WHERE typeName = '{typeName}'")
        service = db_cursor.fetchone()

        if service is not None:
            return HttpResponse('Service already exists')
        
        db_cursor.execute(f"INSERT INTO serviceData (typeName, description) VALUES ('{typeName}', '{description}')")
        db_connection.commit()

        return HttpResponseRedirect('/service/all')

    elif request.method == "GET":
        return render(request, 'new_service.html')
    
def register(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phoneNumber = request.POST.get('phoneNumber')
        address = request.POST.get('address')

        db_connection = sqlite3.connect("./db/db.sqlite3")
        db_cursor = db_connection.cursor()
        db_cursor.execute(f"SELECT * FROM customerData WHERE email = '{email}'")
        customer = db_cursor.fetchone()

        if customer is not None:
            return HttpResponse('User already exists')
        
        db_cursor.execute(f"INSERT INTO customerData (firstName, lastName, email, password, phoneNumber, address) VALUES ('{firstName}', '{lastName}', '{email}', '{password}', '{phoneNumber}', '{address}')")
        db_connection.commit()

        return HttpResponseRedirect('/login')

    elif request.method == 'GET':
        return render(request, 'register.html')


def login(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            db_connection = sqlite3.connect("./db/db.sqlite3")
            db_cursor = db_connection.cursor()

            db_cursor.execute(f"SELECT * FROM customerData WHERE email = '{email}' AND password = '{password}'")
            customer = db_cursor.fetchone()

            if customer is None:
                customer = {}
            else:
                customer = dict(zip([key[0] for key in db_cursor.description], customer))
                request.session['user'] = {
                    'id': customer['id'],
                    'type': 'customer',
                    'address' : customer.get('address', 'NA')
                }

                return HttpResponseRedirect('/service/all')

            db_cursor.execute(f"SELECT * FROM repData WHERE email = '{email}' AND password = '{password}'")
            rep = db_cursor.fetchone()

            if rep is None:
                rep = {}
            else:
                rep = dict(zip([key[0] for key in db_cursor.description], rep))
                request.session['user'] = {
                    'id': rep['id'],
                    'type': 'rep'
                }

                return HttpResponseRedirect('/service/all')

            db_cursor.execute(f"SELECT * FROM adminData WHERE email = '{email}' AND password = '{password}'")
            admin = db_cursor.fetchone()

            if admin is None:
                admin = {}
            else:
                admin = dict(zip([key[0] for key in db_cursor.description], admin))
                request.session['user'] = {
                    'id': admin['id'],
                    'type': 'admin'
                }

                return HttpResponseRedirect('/service/all')

            return HttpResponse('Invalid login')
        elif request.method == 'GET':
            return render(request, 'login.html')
        
    except Exception as e:
        print(e)
        return HttpResponse('An error occurred')