# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import logging
import json
from django.views.decorators.csrf import csrf_exempt
from payment_status.models import payment_status as paystat
from shipment_update.views import shipment_details_update as ship_update

### Hàm này để lấy chi tiết thanh toán.
def get_transaction_details(uname):
    user = paystat.objects.filter(username = uname)
    for data in user.values():
        return data
    
### Hàm này để lưu thông tin thanh toán vào cơ sở dữ liệu.
def store_data(uname, prodid, price, quantity, mode_of_payment, mobile):
    user_data = paystat(username = uname, product_id = prodid, price = price, 
                        quantity = quantity, mode_of_payment = mode_of_payment, 
                        mobile = mobile, status = "Success")
    user_data.save()
    return 1

### This function will get the data from the front end.
@csrf_exempt
def payment_reg_update(request):
    username = request.POST.get("User Name")
    prodid = request.POST.get("Product id")
    price = request.POST.get("Product price")
    quantity = request.POST.get("Product quantity")
    mode_of_payment = request.POST.get("Payment mode")
    mobile = request.POST.get("Mobile Number")
        
    resp = {}
    respdata = store_data(username, prodid, price, quantity, mode_of_payment, mobile)
        
    if respdata:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['message'] = 'Payment is ready to dispatch.'
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Failed to update payment details.'
    return HttpResponse(json.dumps(resp), content_type='application/json')


from django.http import HttpResponse, JsonResponse
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests

@csrf_exempt
def paymentUpdate(request):
    data = json.loads(request.body)
    uname = data.get('User Name', '')
    resp = {}
    ship_dict = ship_update(uname)
    
    if ship_dict:
        resp['status'] = 'Success'
        resp['status_code'] = 200
        resp['message'] = 'Transaction is completed.'
        resp['data'] = ship_dict
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = 400
        resp['message'] = 'Transaction is failed, Please try again.'
    
    return JsonResponse(resp)




### Hàm này để xử lý yêu cầu thanh toán.
@csrf_exempt
def get_payment(request):
    uname = request.POST.get("User Name")
    prodid = request.POST.get("Product id")
    price = request.POST.get("Product price")
    quantity = request.POST.get("Product quantity")
    mode_of_payment = request.POST.get("Payment mode")
    mobile = request.POST.get("Mobile Number")
    resp = {}
    
    if uname and prodid and price and quantity and mode_of_payment and mobile:
    ### It will call the store data function.
        respdata = store_data(uname, prodid, price, quantity, mode_of_payment, mobile)
        respdata2 = ship_update(uname)
        
        logging.info(f"ship_update response: {respdata2}")
        
        ### If it returns value then will show success.
        if respdata:
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Transaction is completed.'
        ### If it is returning null value then it will show failed.
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Transaction is failed, Please try again.'
        
    ### If any mandatory field is missing then it will be through a failed message.
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'All fields are mandatory.'
        
    return HttpResponse(json.dumps(resp), content_type = 'application/json')


### Hàm này để lấy thông tin giao dịch của một người dùng.
@csrf_exempt
def user_transaction_info(request):
    # uname = request.POST.get("User Name")
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            val1 = json.loads(request.body)
            uname = val1.get('User Name')
            resp = {}
            
            if uname:
            ## Calling the getting the user info.
                respdata = get_transaction_details(uname)
                if respdata:
                    resp['status'] = 'Success'
                    resp['status_code'] = '200'
                    resp['data'] = respdata
                ### If a user is not found then it give failed as response.
                else:
                    resp['status'] = 'Failed'
                    resp['status_code'] = '400'
                    resp['message'] = 'User Not Found.'
            ### The field value is missing.
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'Fields is mandatory.'
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Request type is not matched.'
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Request type is not matched.'
        
    return HttpResponse(json.dumps(resp), content_type = 'application/json')