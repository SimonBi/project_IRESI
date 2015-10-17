def extract_sources():
    """
    Extract the sources of the requests and convert them into integers.
    :return: List of integers.
    """
    sources = []
    with open('traces/traces/3Calgaryaccess_log.txt') as logF:
        for line in logF:
            host_request = line.split(' ')[0]
            sources += [int(host_request == 'local')]
    return sources


def extract_filename():
    """
    Extract the filenames of the requests and convert them intro integers.
    :return: List of integers.
    """
    filenames = []
    with open('traces/traces/3Calgaryaccess_log.txt') as logF:
        for line in logF:
            file_request = line.split(' ')[6]
            filenames += [sum(ord(c) for c in file_request)]
    return filenames

