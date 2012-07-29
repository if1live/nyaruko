# -*- coding: utf-8 -*-

from htmlmin.minify import html_minify
from functools import wraps

def minify(f):
    @wraps(f)
    def minify(*args, **kwargs):
        response = f(*args, **kwargs)
        if response.status_code == 200 and 'text/html' in response['Content-Type']:
            response.content = html_minify(isinstance(x, unicode) and x.encode('utf-8') or x)
        return response
 
    return minify
