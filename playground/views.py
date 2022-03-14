from django.shortcuts import render
import logging
import requests

logger = logging.getLogger(__name__)


def say_hello(request):
    try:
        logger.info('Calling httpbin')
        response = requests.get('https://httpbin.org/delay/2')
        logger.info('received the response')
        data = response.json()
    except requests.ConnectionError:
        logger.ctitical('httpbin is offline')
    return render(request, 'hello.html', {'name': 'George'})