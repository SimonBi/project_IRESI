def extract_sources(id_file):
    sources = []
    if id_file == 1:
        filename = '2sdschttp.txt'
    else:
        filename = '2sdschttp' + str(id_file) + '.txt'
    with open('traces/traces/'+filename) as logF:
        for line in logF:
            try:
                sources += [sum(map(int, line.split(' ')[0][:-1].split('+')))]
            except ValueError:
                sources += [sum(ord(c) for c in line.split(' ')[0][:-1])]
    return sources
