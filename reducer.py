#!/usr/bin/env python

import sys

table_count = {}

last_userid = None

for line in sys.stdin:
    line = line.strip()
    
    userid, table = line.split('\t')
    
    
    if last_userid and userid != last_userid: #If encounter new users, output last user
        for table in table_count.keys():
            print "%s\t%s:%d" % (last_userid, table, table_count[table])
        table_count.clear()
    
    else:
        table_count[table] = table_count.get(table, 0) + 1
        
    last_userid = userid
