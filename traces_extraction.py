import extract_epahttp as t1
import extract_sdschttp as t2
import extract_calgaryaccess as t3


def extract_entries(id_traces, random_entries=False, size_entries=0,
                    nb_distinct=0, distribution=()):
    """
    Extract what will be used as entries.
    :param id_traces: Id of the trace chosen. '22' for the second sdsc trace.
    :type id_traces: String.
    :return: A dictionary with various information on the entries.
    """
    if random_entries:
        entries = generate_random_entries(size_entries, nb_distinct,
                                          distribution)
    elif id_traces == '1':
        entries = t1.extract_sources()
    elif id_traces[0] == '2':
        entries = t2.extract_sources(id_traces[1])
    else:
        entries = t3.extract_filename()
    various_information = {'elements': entries,
                           'distinct_elements': list(set(entries)),
                           'size': len(entries),
                           'frequency': {}}
    for e in various_information['distinct_elements']:
        various_information['frequency'][e] = \
            len([el for el in entries if el == e]) / len(entries)

    return various_information


def generate_random_entries(size, nb_distinct, distribution):
    """
    Generate a random list of integers.
    :param size: Size of the list.
    :param nb_distinct: Number of distinct items.
    :param distribution: Distribution in the list for each element.
    :type distribution: Tuple or list, of the size of the number of distinct
                        items, of numbers between 0 and 1.
    :return: List of integers.
    """
    entries = []
    for i in range(0, nb_distinct):
        entries += [i] * (size / distribution[i])
    return entries

extract_entries('1')
