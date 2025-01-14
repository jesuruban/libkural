# This Python file uses the following encoding: utf-8

##Copyright (c) 2013, Muthiah Annamalai
##All rights reserved.
##
##Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
##
##    Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
##    Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
##
##THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.Code and source is licensed under terms of BSD 2 open source license

#See: BSD 2 license, http://opensource.org/licenses/BSD-2-Clause

#Updated the script for Python 3 : changed print command and replaced unicode with str -  jesuruban

from libkural import *

if __name__ == '__main__':
	qral = Thirukkural();
	k= qral.get_kural_no(5);
	print (str(k))
	print ("*"*80)
	k = qral.get_kurals_from_adhikaram(u'''ஊடலுவக''');
	for i,kk in enumerate(k):
		print ("%d>> %s"%(i+1,str(kk)))
	print ("*"*80)
	k = qral.get_kurals_from_pal(u'''காமத்துப்பால''');
	for i,kk in enumerate(k):
		print ("%d>> %s"%(i+1,str(kk)))
	

