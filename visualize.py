
def graphviz(filename):
    out = "digraph g { \n\tgraph [ rankdir = \"LR\" ];\n"
    a_file = [ x.strip() for x in open(filename).readlines() ]
    i = 0
    links = []
    while i < len(a_file):
        line = a_file[i]
        if line.startswith('create table'):
            table_name = line.split('create table ')[1].split(' (')[0]
            s = """
    \"%s\" [
    shape=none
    label = <
      <table border="0" cellspacing="0" cellborder="1">
      <tr><td bgcolor="lightblue2" colspan="2"><font face="Arial"> %s </font></td></tr>
""" % (table_name, table_name)
            ss = ''
            while line != ');':
                i += 1
                line = a_file[i]
                try:
                    aname, atype = line.strip(',').split(maxsplit=1)
                    assert aname != 'foreign'
                    ss += '      <tr><td bgcolor="grey96" align="right"><font face="Arial"> %s </font></td><td align="left"><font face="Arial"> %s </font></td></tr>\n' % (aname, atype)
                except ValueError:
                    pass
                except AssertionError:
                    table_to = atype.split('references ')[1].split('(')[0]
                    links += [(table_name, table_to)]
                
            s += ss
            s += """      </table>
    >];"""
            out += s        
        i += 1
    for a, b in links:
        out += "\t %s -> %s [arrowhead=\"none\"]\n" % (a, b)
    out += "}\n"
    
    return out

if __name__ == '__main__':
    filename = 'create_tables.sql'
    graf = graphviz(filename)
    open('model.dot', 'w').write(graf)
