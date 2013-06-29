#!/usr/bin/env python
#
# Copyright 2012 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import httplib2
import logging
import os
import pickle

from apiclient.discovery import build
from optparse import OptionParser
from oauth2client.appengine import OAuth2Decorator
from oauth2client.client import AccessTokenRefreshError
from google.appengine.api import memcache
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

class MainHandler(webapp.RequestHandler):

  def get(self):
    youtube = build("youtube", "v3", developerKey="AIzaSyA3rTFemFJxBEq9Md28bI1dqNXMGTf4eec") 
    search_response = youtube.search().list(q="Hello", part="id, snippet", maxResults=5).execute()
    self.response.out.write(search_response)

def main():
  application = webapp.WSGIApplication(
      [
       ('/', MainHandler),
      ],
      debug=True)
  run_wsgi_app(application)


if __name__ == '__main__':
  main()
