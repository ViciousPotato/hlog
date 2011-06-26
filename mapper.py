#!/usr/bin/env python

import re
import sys

def read_record(f):
    i = 0
    record = ""
    b = f.read(1)
    
    if not b: return ""
    
    while i < 10
        if b == '\x01':
            i = i + 1
        record += b
        b = f.read(1)
    return record
    
record = read_record(sys.stdin)

while record:
    fields = record.split('\x01')
    userid= fields[0].strip()
    query_text = ' '.join(fields[-2].strip().split('\r'))
    
    tables = re.findall(r'insert into (\S*)', query_text, re.I)
    
    for table in tables:
        print '%s\t%s' % (userid, table)
    record = read_record(sys.stdin)
