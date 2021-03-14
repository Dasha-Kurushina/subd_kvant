import re
from translit import translify
from pprint import pprint

def to_translit(x):
    return translify(x).replace(' ', '_')

tables = {}

for line in [x.strip() for x in open("digraphg.dot").readlines() if x.find('>') == -1 ]:
    if line.find('"') == 0:
        table_name = to_translit(line.split('[')[0].strip('" '))
        tables.update({table_name: ['id integer primary key not null']})

pprint(tables)
        
for line in [x.strip() for x in open("digraphg.dot").readlines() if x.find('>') != -1 ]:
    if line.count('->') == 1:
        table, field = [ to_translit(x.strip('"\' ')) for x in line.split('->')]
        if field.count('['):
            field = field.split('[')[0].strip('_"')
        tables[table] += ['%s text' % field ]

pprint(tables)

one2many = []

for line in [x.strip() for x in open("digraphg.dot").readlines() if x.find('n:1') != -1]:
    one2many += [to_translit(line.split()[0])]

pprint(one2many)

for line in [x.strip() for x in open("digraphg.dot").readlines() if x.find('>') != -1 ]:
    if line.count('->') == 2:
        table_from, rel, table_to = [ to_translit(x.strip('" ')) for x in line.split('->')]
        if rel in one2many:
            if table_to.count('['):
                table_to = table_to.split('[')[0].strip('_"')
            table_to_id = '%s_id' % table_to
            tables[table_from] += ['%s integer' % table_to_id ]
            tables[table_from] += ['foreign key (%s) references %s(id) ' % (table_to_id, table_to) ]
        
pprint(tables)

many2many = []
for line in [x.strip() for x in open("digraphg.dot").readlines() if x.find('n:m') != -1]:
    many2many += [to_translit(line.split()[0])]
    
pprint(many2many)

for line in [x.strip() for x in open("digraphg.dot").readlines() if x.find('>') != -1 ]:
    if line.count('->') == 2:
        table_from, rel, table_to = [ to_translit(x.strip('" ')) for x in line.split('->')]
        if table_to.count('['):
            table_to = table_to.split('[')[0].strip('_"')
        if rel in many2many:
            tables.update({rel: ['id integer primary key not null']})
            for table in [table_from, table_to]:
                table_id = '%s_id' % table
                tables[rel] += ['%s integer' % table_id ]
                tables[rel] += ['foreign key (%s) references %s(id) ' % (table_id, table)]

pprint(tables)

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
