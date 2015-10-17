def extract_sources():
    sources = []
    with open('traces/traces/1epahttp.txt') as logF:
        for line in logF:
            sources += [sum(ord(c) for c in line.split(' ')[0])]
    return sources
