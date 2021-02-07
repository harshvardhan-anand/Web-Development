from django.shortcuts import render
import braintree
from django.conf import settings
from django.http import HttpResponse

# Create your views here.

gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)

def home(request):
    price = 500
    if request.method == 'POST':
        print(f"request: {request.POST}")
        nonce = request.POST.get('payment_method_nonce')
        print(f"Nonce: {nonce}")
        result = gateway.transaction.sale(
            {
                'amount':price,
                'payment_method_nonce':nonce,
                'options':{
                    'submit_for_settlement':True
                }
            }
        )
        print(f"Result: {result}")
        return HttpResponse(result)
    else:
        client_token = gateway.client_token.generate()
    return render(
        request, 'home.html',
        {
            'order':price,
            'client_token':client_token
        }
    )