def extract_sources():
    """
    Extract the sources of the requests and convert them into integers.
    :return: List of integers.
    """
    sources = []
    with open('traces/traces/1epahttp.txt') as logF:
        for line in logF:
            sources += [line.split(' ')[0]]
    return sources
