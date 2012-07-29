flask를 적절히 서버에 맞춰서 잘 구성하기 위해서 virtualenv를 사용햇다.
간단한 생성 예제는 http://flask.pocoo.org/docs/installation/#virtualenv 에 있다.

디렉토리는 다음과 같은 구조로 구성되도록한다
- root ... 프로젝트의 루트 디렉토리. 저장소와 루트와 일치시킨다
  - nyaruko ... 프로젝트의 실제 구현부분이 들어가는 디렉토리. 라이브러리의 경우는 다른곳으로 뺄수도 잇다
  - venv ... virtualenv를 사용해서 생성한것. root/venv/bin/python이 존재할수 잇도록 root경로에서 virtualenv venv를 사용하면 생성할수있다


## Installation

### Requirement

1. flask
2. django_htmlmin

> pip install flask django_htmlmin