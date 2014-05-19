'''
        linkcheck.py Copyright 2011, Michel J. Anders
        
        A module to check for broken links in urls.

        $Revision: 73 $ $Date: 2011-06-13 16:21:58 +0200 (ma, 13 jun 2011) $
        
        This program is free software: you can redistribute it
        and/or modify it under the terms of the GNU General Public
        License as published by the Free Software Foundation,
        either version 3 of the License, or (at your option) any
        later version.

        This program is distributed in the hope that it will be 
        useful, but WITHOUT ANY WARRANTY; without even the implied
        warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
        PURPOSE. See the GNU General Public License for more
        details.

        You should have received a copy of the GNU General Public
        License along with this program.  If not, see 
        www.gnu.org/licenses.
'''
from pattermatching import BoyerMooreMatch
from urllib2 import Request,urlopen
from urlparse import urlsplit,urljoin,urlunsplit,urldefrag
from urllib2 import HTTPError,URLError
#from html.parser import HTMLParser
from HTMLParser import HTMLParser
from re import compile,MULTILINE,IGNORECASE

class LinkParser(HTMLParser):

        tagsrefs = { 'a':'href', 'img':'src', 'script':'src', 'link':'href' }
        
        def __init__(self,baseurl,callback):
                print "Inside Link Parser"
                self.callback = callback
                self.baseurl = baseurl
                HTMLParser.__init__(self)
                #super(self).__init__()#strict=False)
                
        def handle_starttag(self, tag, attrs):
                if tag in self.tagsrefs:
                        for name,value in attrs:
                                if name == self.tagsrefs[tag]:
                                        newurl=urljoin(self.baseurl,value)
                                        self.callback(newurl)
                                        break

class LinkChecker:

        html=compile('^Content-Type:\s+text/html+$',MULTILINE|IGNORECASE)
        html2 = 'Content-Type: text/html'

        def __init__(self,url,host=None,seen=None,external=True):
                self.url    = url
                self.host   = urlsplit(url).hostname if host is None else host
                self.failed = []
                self.other  = []
                self.notopened = []
                self.duplicates = 0
                self.seen	= set() if seen is None else seen
                print self.seen
                self.external = external

        def check(self,open=True):
                """
                tries to open self.url
                return False if the url cannot be followed (either 
                because it could be openen or its content is not html.
                """
                print "Inside Check",self.url,open
                self.seen.add(self.url)
                if not open :
                        print "If not open in check"
                        self.notopened.append(self.url)
                        return False
                try:
                        print "In check if else"
                        self.req=urlopen(url=self.url)
                        print self.req.read()
                        
                except HTTPError as e:
                        self.failed.append(self.url)
                        return False
                except URLError as e:
                        self.other.append(self.url+' ('+str(e)+')')
                        return False
                except Exception as e:
                        print('Exception',e,type(e))
                        self.failed.append(self.url)
                        return False
                headers=str(self.req.info())
                print headers
                m=self.html.search(headers)
                pt = BoyerMooreMatch()
                res = pt.BoyerMoore(headers,self.html2)
                print res
                print m
                return not (res is None)
                
        def follow(self):
                """
                follows references in an opened html file 
                (a, img, link and script tags)
                
                returns True if there were no errors.
                """
                parser = LinkParser(self.url,self.process)
                print parser
                try:
                        parser.feed(self.req.read().decode())
                except Exception as e:
                        self.other.append(self.url+' ('+str(e)+')')
                return len(self.failed)+len(self.other) == 0
                
        def process(self,newurl):
                newurl=urldefrag(newurl)[0]
                if not newurl in self.seen:
                        lc = LinkChecker(newurl,self.host,self.seen,self.external)
                        samesite = urlsplit(newurl).hostname == self.host
                        # if external is false we do not even open the page
                        # if external is true we only open internal pages 
                        # (but do check if we can open externals)
                        if lc.check(self.external or samesite) and samesite:
                                lc.follow()
                        self.failed.extend(lc.failed)
                        self.other.extend(lc.other)
                        self.notopened.extend(lc.notopened)
                        self.seen.update(lc.seen)
                        self.duplicates+=lc.duplicates
                else:
                        self.duplicates+=1
