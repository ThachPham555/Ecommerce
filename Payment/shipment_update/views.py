import json
import urllib.parse
import requests
from payment_status.models import payment_status as paystat

def shipment_details_update(uname):
    ship_dict = {}
    user = paystat.objects.filter(username=uname).first()
    if user:
        ship_dict = {
            'Product Id': user.product_id,
            'Quantity': user.quantity,
            'Payment Status': user.status,
            'Transaction Id': user.id,
            'Mobile Number': user.mobile,
            'Shipment Status': user.status,
        }
    
        payload = {"User Name": uname}
        headers = {'Content-Type': 'application/json'}
        userinfo_url = 'http://127.0.0.1:8000/userinfo'
        response = requests.post(userinfo_url, data=json.dumps(payload), headers=headers)
        
        if response.status_code == 200:
            try:
                userinfo_data = response.json().get('data', {})
                
                ship_dict['First Name'] = userinfo_data.get('First Name', '')
                ship_dict['Last Name'] = userinfo_data.get('Last Name', '')
                ship_dict['Address'] = userinfo_data.get('Address', '')
                ship_dict['Email Id'] = userinfo_data.get('Email Id', '')

                print(ship_dict)

                url = 'http://127.0.0.1:5000/shipment_updates'
                data = json.dumps(ship_dict)
                data_dict = json.loads(data)
                data_form_encoded = urllib.parse.urlencode(data_dict)
                print(data_form_encoded)
                response = requests.post(url, data=data_dict)

                if response.status_code == 200:
                    api_resp = response.json()
                    return api_resp
                else:
                    return {'status': 'Failed', 'message': f'Request failed Update Shipment with HTTP {response.status_code}'}
                
            except json.JSONDecodeError:
                return {"status": "Failed", "message": "Invalid JSON response from /userinfo/"}
        else:
            return {"status": "Failed", "message": f"Failed to retrieve user info: HTTP {response.status_code}"} 
    else:
        return {"status": "Failed", "message": "User not found"}

