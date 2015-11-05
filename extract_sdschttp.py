def extract_sources(id_file):
    """
    Extract the sources of the requests and convert them into integers.
    :arg id_file: Id of one of the two sdsc-http traces.
    :type id_file: 1 or 2.
    :return: List of integers.
    """
    sources = []
    if id_file == '1':
        filename = '2sdschttp.txt'
    else:
        filename = '2sdschttp' + str(id_file) + '.txt'
    with open('traces/traces/'+filename, encoding="latin-1") as logF:
        for line in logF:
            sources += [line.split(' ')[0][:-1]]
    return sources


def extract_filenames(id_file):
    filenames = []
    if id_file == '1':
        filename = '2sdschttp.txt'
    else:
        filename = '2sdschttp' + str(id_file) + '.txt'
    with open('traces/traces/'+filename, encoding="latin-1") as logF:
        for line in logF:
            filenames += [line.split(' ')[6][1:][:-2]]
    return filenames
