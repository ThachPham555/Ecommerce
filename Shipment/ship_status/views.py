# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from ship_status.models import shipment as ship_obj

### Chèn thông tin vận chuyển mới vào cơ sở dữ liệu. 
#Dữ liệu này được nhận từ front-end thông qua request POST dưới dạng JSON
def ship_data_insert(fname, lname, email, mobile, address, product_id,
                     quantity, payment_status, transaction_id, shipment_status):
    shipment_data = ship_obj(fname = fname,lname = lname, email = email, mobile = mobile,
                             address = address, product_id = product_id, quantity = quantity,
                             payment_status = payment_status, transaction_id = transaction_id, 
                             shipment_status = shipment_status)
    shipment_data.save()
    return 1

### This function will get the data from the front end.
@csrf_exempt
def shipment_reg_update(request):
    fname = request.POST.get("First Name")
    lname = request.POST.get("Last Name")
    email = request.POST.get("Email Id")
    mobile = request.POST.get("Mobile Number")
    address = request.POST.get("Address")
    product_id = request.POST.get("Product Id")
    quantity = request.POST.get("Quantity")
    payment_status = request.POST.get("Payment Status")
    transaction_id = request.POST.get("Transaction Id")
    shipment_status = request.POST.get("Shipment Status")
        
    resp = {}
    respdata = ship_data_insert(fname, lname, email, mobile, address, 
                                product_id, quantity, payment_status, 
                                transaction_id, shipment_status)
        
    if respdata:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['message'] = 'Product is ready to dispatch.'
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Failed to update shipment details.'
    return HttpResponse(json.dumps(resp), content_type='application/json')


### Tìm kiếm shipment
def shipment_data(uname):
    data = ship_obj.objects.filter(email = uname)
    for val in data.values():
        return val

### Lấy thông tin vận chuyển
@csrf_exempt
def shipment_status(request):
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            variable1 = json.loads(request.body)
            ### This is for reading the inputs from JSON.
            uname = variable1.get("User Name")
            resp = {}
            ### It will call the shipment_data function.
            respdata = shipment_data(uname)
            if respdata:
                resp['status'] = 'Success'
                resp['status_code'] = '200'
                resp['message'] = respdata
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'User data is not available.'
    return HttpResponse(json.dumps(resp), content_type = 'application/json')
