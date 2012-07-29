# -*- coding: utf-8 -*-

from htmlmin.minify import html_minify
from functools import wraps
import gettext

#gettext.bindtextdomain('nyaruko', os.path.join(app.root_path, 'lang')
#gettext.textdomain('nyaruko')

_ = gettext.gettext

def minify(f):
    @wraps(f)
    def minify(*args, **kwargs):
        response = f(*args, **kwargs)
        return html_minify(isinstance(response, unicode) and response.encode('utf-8') or response)
 
    return minify
