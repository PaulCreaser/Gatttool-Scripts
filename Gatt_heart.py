#!/usr/bin/env python

import pexpect

import sys

class BLEDEV:

def __init__( self, bluetooth_adr ):

self.con = pexpect.spawn('gatttool -i hci0 -b ' + bluetooth_adr + ' -t random -I ') self.con.expect('\[LE\]>')

self.con.sendline('connect')

self.con.expect('\[CON\].*>')

self.con.sendline('primary')

self.con.expect('\[CON\].*>')

self.con.expect('\[CON\].*>')

self.con.sendline('disconnect')

self.con.expect('\[LE\]>')

def loop(self):

while True:

try:self.con.sendline('connect')

self.con.expect('\[CON\].*>')

# Etc.....

self.con.sendline('char-write-req 0xf 01 04 ');

self.con.expect('\[CON\].*>')

self.con.sendline('disconnect')

self.con.expect('\[LE\]>')

except:self.con.sendline('exit');

self.con.kill(1)

exit(0)

datalog = sys.stdout

def main():

bluetooth_adr = sys.argv[1]

bdev = BLEDEV(bluetooth_adr)

bdev .loop()

if __name__ == "__main__":main()
