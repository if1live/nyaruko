#-*- coding: utf-8 -*-

'''
Reference
  * http://tkhwang.kr/blog/2011/12/03/generate-md5-hash-of-string-and-file-in-python/
  * https://github.com/if1live/nyaruko/wiki/file_hash.py
'''

import sys
import hashlib
import os

class HashHelper:
  @staticmethod
  def file_to_hash(filename):
    '''해시 계산을 위해서 까볼 파일이 실제로 존재하는지, 안하는지를 모르니까 예외로 처리'''
    try:
      f = open(filename, 'r')
      chunk = f.read(1024 * 4)
      ''' get filesize reference
      http://mwultong.blogspot.com/2007/04/python-file-size-in-bytes.html'''
      filesize = os.path.getsize(filename)
      f.close()
      hashcode = HashHelper.chunk_to_hash(chunk, filesize)
      return hashcode

    except IOError as err:
      print err
      return None

  @staticmethod
  def chunk_to_hash(chunk, filesize):
    '''data chunk 중에서 가장 앞부분 4k를 읽어서 md5를 통해서 해시를 구성하고
    파일 사이즈중 8자리를 앞에 붙여서 40글자의 해시로 만든다'''
    md5_part = HashHelper.chunk_to_md5(chunk)
    filesize_part = filesize % (10 ** 10)
    hashcode = '%010d%s' % (filesize_part, md5_part)
    return hashcode

  @staticmethod
  def chunk_to_md5(chunk):
    '''calculate binary chunk to md5'''
    md5 = hashlib.md5()
    md5.update(chunk)
    return md5.hexdigest()


def show_help():
  help_txt = '''*** Project::Nyaruko ***
Overview : File to Hash Util

Usage : %s <filename>
Result : (Sample, 40 length string) 4567890123912ec803b2ce49e4a541068d495ab570
'''
  str = help_txt % (sys.argv[0])
  print str

if __name__ == '__main__':
  argc = len(sys.argv)
  if argc == 1:
    show_help()
  elif argc == 2:
    # 2번째 인자는 파일명으로 간주하고 처리한다
    hashcode = HashHelper.file_to_hash(sys.argv[1])
    if hashcode != None:
      print hashcode
    else:
      sys.exit(1)

  # print HashHelper.chunk_to_md5('asff')
  # print HashHelper.chunk_to_hash('asdf', 1234567890123)

