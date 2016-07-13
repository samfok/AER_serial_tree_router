"""Writes ij indexing for tile connections to file

Takes in filename.act.ref
Looks for pint M, pint p4M
Calculates maps of flat indexing to ij indexing
Copies filename.act.ref and inserts indexing maps into filename.act
"""
import sys
import re

NRN_PTILE = 16 # neurons per tile

def addr_1of4_to_ij(addr_1of4):
    """Converts address from 1of4 to i,j"""
    words = len(addr_1of4)
    addrs = 4**words
    ijlen = 2**words
    addr_i = 0
    addr_j = 0
    for word in addr_1of4:
        ijlen /= 2
        addr_i += word%2 * ijlen
        addr_j += word/2 * ijlen
    return addr_i, addr_j

def addr_flat_to_1of4(addr_flat, words):
    """Converts address from flat to 1of4"""
    flatlen = 4**words
    addr_1of4 = []
    for w in xrange(words):
        flatlen /= 4
        addr_1of4.append(addr_flat/flatlen % 4)
    return addr_1of4

def addr_flat_to_ij(addr_flat, words):
    """Converts address from flat to ij"""
    addr_i, addr_j = addr_1of4_to_ij(addr_flat_to_1of4(addr_flat, words))
    return addr_i, addr_j

def extract_pint(pint, f_str):
    """looks for a pint's value"""
    matches = re.findall(r'.*pint ' + pint + r' *= *([0-9]+)*;.*', f_str)
    assert len(matches) > 0, "No match for {}. Must declare pint {}".format(pint)
    assert len(matches) == 1, \
        "More than 1 match for {}. Found ".format(pint) + str(matches)
    pint_val = int(matches[0])
    return pint_val

def insert_tile_ij(tile_i, tile_j, f_str):
    """overwrite SCRIPT directives for tile_i and tile_j"""
    matches = re.findall(r".*#SCRIPT (pint tile_i\[p4M/16\]);.*", f_str)
    assert len(matches) > 0, 'No match for "#SCRIPT pint tile_i[p4M/16];".' + \
        ' File must contain tile_i directive'
    assert len(matches) == 1, 'More than 1 match for "#SCRIPT pint ' + \
        'tile_i[p4M/16];". File may only contain 1 tile_i directive'
    matches = re.findall(r".*#SCRIPT (pint tile_j\[p4M/16\]);.*", f_str)
    assert len(matches) > 0, 'No match for "#SCRIPT pint tile_j[p4M/16];".' + \
        ' File must contain tile_j directive'
    assert len(matches) == 1, 'More than 1 match for "#SCRIPT pint ' + \
        'tile_j[p4M/16];". File may only contain 1 tile_j directive'

    fw_str = re.sub(
        r".*#SCRIPT (pint tile_i\[p4M/16\];).*",
        r"\1\ntile_i = {"+str(tile_i)[1:-1]+r"};",
        f_str)
    fw_str = re.sub(
        r".*#SCRIPT (pint tile_j\[p4M/16\];).*",
        r"\1\ntile_j = {"+str(tile_j)[1:-1]+r"};",
        fw_str)
    return fw_str
    

def parse_file(fname):
    """read in the act file"""
    assert fname[-8:] == '.act.ref', "filename must end with .act.ref"
    with open(fname, 'r') as f:
        f_str = f.read()
    M = extract_pint("M", f_str)
    p4M = extract_pint("p4M", f_str)
    assert 4**M == p4M, "p4M != 4^M"
    ntiles = p4M / NRN_PTILE
    M_TILE = M-2 # because 16 neurons per tile

    tile_i, tile_j = zip(
        *map(lambda x: addr_flat_to_ij(x, M_TILE), range(ntiles)))

    fw_str = insert_tile_ij(tile_i, tile_j, f_str)
    print fw_str

if __name__ == "__main__":
    assert len(sys.argv) == 2, "must give file to parse"
    try:
        parse_file(sys.argv[1])
    except AssertionError as e:
        print 'Failed to run index_tile_ij.py on ' + sys.argv[1]
        raise
