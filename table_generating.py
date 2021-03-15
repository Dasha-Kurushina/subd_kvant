import re
from translit import translify, detranslify
from pprint import pprint
from random import choice, shuffle

such = [
    'Сущность "%s" содержит в себе информацию о характеристиках %s.',
    '"%s" предназначено для хранения информации о %s.',
    'Сущность "%s" состоит из основных характеристик %s.',
    'Такая сущность  как "%s" наполнена информацией о ключевых параметрах %s.',
]

otn = [
    'Существует отношение "%s", которое определено арностью %s.',
    'Отношение "%s" обладает арностью %s.',
    'К тоже же, было необходимо отношение "%s", арность которого определена как %s.',
    'Исходя из логических отношений была выявлена потребность в отношении "%s" с арностью %s.',
]

atr_1 = [
    'Сущность "%s" имеет атрибут "%s".',
    'В сущности "%s" есть атрибут "%s".',
    'В сущности "%s" находится атрибут "%s".',
    '"%s" содердит атрибут "%s".',
]

atr_2 = [
    '"%s" - это сущность, которая содержит атрибуты: "%s". ',
    '"%s" состоит из таких атрибутов как "%s".',
    'В сущности "%s" имеются атрибуты: "%s".',
    'Сущность "%s" содержит: "%s".',
]

sva = [
    '"%s" - это связь между "%s" и "%s".',
    'Связь "%s" объединяет "%s" и "%s".',
    'Существует "%s", которая связывает "%s" и "%s".',
]

def to_translit(x):
    return translify(x).replace(' ', '_')

tables = {}
text = []

for line in [x.strip() for x in open("digraphg.dot").readlines() if x.find('>') == -1 ]:
    if line.find('"') == 0:
        such_name = line.split('[')[0].strip('" ')
        text += [ choice(such) % (such_name, such_name.lower()) ]
        table_name = to_translit(such_name)
        tables.update({table_name: ['id integer primary key not null']})

pprint(tables)
        
for line in [x.strip() for x in open("digraphg.dot").readlines() if x.find('>') != -1 ]:
    if line.count('->') == 1:
        table, field = [ to_translit(x.strip('"\' ')) for x in line.split('->')]
        if field.count('['):
            field = field.split('[')[0].strip('_"')
        tables[table] += ['%s text' % field ]

for table in tables:
    such_name = detranslify(table)
    if len(tables[table]) == 2:
        atr_name = tables[table][-1].split()[0]
        atr_name = detranslify(atr_name)
        text += [ choice(atr_1) % (such_name, atr_name) ]
        
    elif len(tables[table]) > 2:
        atr_names = '", "'.join([ detranslify(x.split()[0]) for x in tables[table][1:] ])
        text += [ choice(atr_2) % (such_name, atr_names) ]
    
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

otn_otn = [ (x,1) for x in one2many ] + [ (x, 2) for x in many2many ]
shuffle(otn_otn)
tt = {
    1: "один ко многим",
    2: "многие ко многим",
}

for x, y in otn_otn:
    arnost = tt[y]
    text += [ choice(otn) % (x, arnost) ]

pprint(many2many)

for line in [x.strip() for x in open("digraphg.dot").readlines() if x.find('>') != -1 ]:
    if line.count('->') == 2:
        table_from, rel, table_to = [ x.strip('" ') for x in line.split('->')]
        if table_to.count('['):
            table_to = table_to.split('[')[0].strip('_ "')
        text += [ choice(sva) % (rel, table_from, table_to) ]
        
        
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

p = [
	'В базе данных существует таблица "%s", хранящая в себе данные атрибуты: %s и первичный ключ "%s".',
	'В базе данных есть таблица "%s", в которой хранятся такие свойства, как %s и первичный ключ "%s". ',
	'Также в базе есть таблица "%s", в которой хранятся следующие данные: %s и первичный ключ "%s".',
]
v = [
	'База данных имеет таблицу "%s" с атрибутами: %s, первичным ключом "%s" и внешними ключами: "%s".',
	'База данных содержит таблицу "%s" с атрибутами: %s, а также она имеет первичный ключ" %s" и внешний ключ:"%s".',
	'База данных имеет таблицу "%s", со свойствами %s, первичным ключом "%s" и внешним ключом "%s".',
]

another_text = []

def create_table(table):
    global created_tables
    global script
    global another_text
    
    if table not in created_tables:
        fields = []
        fkeys = []
        created_tables += [table]
        script += 'create table %s (\n' % table
        for field in tables[table]:
            if  not field.startswith('foreign key'):
                script += '\t%s,\n' % field
                fields += [field]
        for field in tables[table]:
            if field.startswith('foreign key'):
                script += '\t%s,\n' % field
                fkeys += [field]
                
        script = script.rstrip(',\n')
        script += '\n);\n\n'
        
        text_fields = ", ".join([ "%s c типом %s" % tuple(x.split()) for x in fields[1:] ])
        text_fkeys = ", ".join([ x.split('(')[1].split(')')[0] for x in fkeys ])
        id_field = fields[0].split()[0]
        
        if fkeys:
            another_text += [ choice(v) % (table, text_fields, id_field, text_fkeys) ]
        else:
            another_text += [ choice(p) % (table, text_fields, id_field) ]

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
open('log_model.txt','w').write("\n".join(text))
open('phyz_model.txt','w').write("\n".join(another_text))