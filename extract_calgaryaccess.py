def extract_sources():
    sources = []
    with open('traces/traces/3Calgaryaccess_log.txt') as logF:
        for line in logF:
            host_request = line.split(' ')[0]
            sources += [int(host_request == 'local')]
    return sources

