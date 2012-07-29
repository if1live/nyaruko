# -*- coding: utf-8 -*-

from htmlmin.minify import html_minify
from functools import wraps
import gettext
from constant import *

#gettext.bindtextdomain('nyaruko', os.path.join(app.root_path, 'lang')
#gettext.textdomain('nyaruko')

_ = gettext.gettext

def minify(f):
    @wraps(f)
    def minify(*args, **kwargs):
        response = f(*args, **kwargs)
        if isinstance(response, (unicode, str)):
          return html_minify(isinstance(response, unicode) and response.encode('utf-8') or response)
        return response
 
    return minify

def get_category_data():
  category_list = get_category_list()
  category_data = []
  for category_info in category_list:
    category_code = category_info[0]
    category_name = category_info[1]
    category_id = category_name.lower()
    category_data.append({
        'code' : category_code,
        'name' : category_name,
        'id' : 'category_' + category_id
        })
  return category_data
