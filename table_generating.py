import re

x = """create table table2 (
	a integer primary key not null,
	b text  unique not null,
	c real not null
);"""

tables = {}

for line in [x.strip() for x in open("translit.dot").readlines() if x.find('>') == -1 ]:
    if line.find('"') == 0:
        print(line)
        tables.update({line.strip('"'): ['id integer primary key not null']})
        
        
for line in [x.strip() for x in open("translit.dot").readlines() if x.find('>') != -1 ]:
    if line.count('->') == 1:
        print([ x.strip('" ') for x in line.split('->')])
        table, field = [ x.strip('"\' ') for x in line.split('->')]
        tables[table] += ['%s text' % field ]
        
one2many = []
for line in [x.strip() for x in open("translit.dot").readlines() if x.find('n:1') != -1]:
    print(line.split()[0])
    one2many += [line.split()[0]]
    
for line in [x.strip() for x in open("translit.dot").readlines() if x.find('>') != -1 ]:
    if line.count('->') == 2:
        print([ x.strip('" ') for x in line.split('->')])
        table_from, rel, table_to = [ x.strip('" ') for x in line.split('->')]
#        tables[table] += ['%s text' % field ]
        if rel in one2many:
            print(table_from, rel, table_to)
            table_to_id = '%s_id' % table_to
            tables[table_from] += ['%s integer' % table_to_id ]
            tables[table_from] += ['foreign key (%s) references %s(id) ' % (table_to_id, table_to) ]
        
many2many = []
for line in [x.strip() for x in open("translit.dot").readlines() if x.find('n:m') != -1]:
    print(line.split()[0])
    many2many += [line.split()[0]]
    
for line in [x.strip() for x in open("translit.dot").readlines() if x.find('>') != -1 ]:
    if line.count('->') == 2:
        print([ x.strip('" ') for x in line.split('->')])
        table_from, rel, table_to = [ x.strip('" ') for x in line.split('->')]
#        tables[table] += ['%s text' % field ]
        if rel in many2many:
            print(table_from, rel, table_to)
            tables.update({rel: ['id integer primary key not null']})
            for table in [table_from, table_to]:
                table_id = '%s_id' % table
                tables[rel] += ['%s integer' % table_id ]
                tables[rel] += ['foreign key (%s) references %s(id) ' % (table_id, table)]

created_tables = []
script = ''

def create_table(table):
    global created_tables
    global script
    if table not in created_tables:
        created_tables += [table]
        script += 'create table %s (\n' % table
        for field in tables[table]:
            if  not field.startswith('foreign key'):
                script += '\t%s,\n' % field
        for field in tables[table]:
            if field.startswith('foreign key'):
                script += '\t%s,\n' % field            
        script = script.rstrip(',\n')
        script += '\n);\n\n'
        

for table in tables:
    for field in tables[table]:
        try:
            ref_table_name = field.split('references ')[1].split('(')[0]
            if ref_table_name not in created_tables:
                create_table(ref_table_name)
        except IndexError:
            pass
    create_table(table)
    
open('create_tables.sql','w').write(script)
