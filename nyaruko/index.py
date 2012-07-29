# -*- coding: utf-8 -*-

import os
from flask import Flask
from flask import send_from_directory, render_template
from flask import session
from flask import request
import config
import auth
from util import *
from constant import *

app = Flask(__name__)


''' For favicon ( static/favicon.ico ) '''
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
@minify
#@auth.requires_auth
def index():
  title = "Project::Nyaruko"
  subtitle = u"행성보호기구 연세대학교 지부"

  ''' 
  지원되는 검색 카테고리 목록
  개발에 필요한 속성은 카테고리별 코드와 고유이름뿐이지만
  html에 찍어내기 위해서는 추가 속성(node id, etc)가 필요하다
  적절히 재조합해서 만들어내기
  code:CO / name:Comic / id:category_co 같은것의 배열
  '''
  category_data = get_category_data()
  return render_template('index.html', 
                         title = title,
                         subtitle = subtitle,
                         category_data = category_data)

@app.route('/login')
@minify
def login():
  return render_template('index.html')


@app.route('/search')
@minify
def search():
  keyword = request.args.get('keyword')
  #keyword = request.form['keyword']
  #category는 길어서 축약형으로 씀
  category_list = request.args.getlist('c')  
  category_data = get_category_data()
  for category_info in category_data:
    code = category_info['code']
    cnt = category_list.count(code)
    if cnt == 0:
      category_info['checked'] = False
    else:
      category_info['checked'] = True
  
  return render_template('search.html', 
                         category_data = category_data,
                         keyword = keyword, 
                         category_list = category_list)

if __name__ == '__main__':
  app.jinja_env.add_extension('jinja2.ext.i18n')
  app.run(host=config.SERVER_HOST, port=config.SERVER_PORT, debug=config.SERVER_DEBUG)
