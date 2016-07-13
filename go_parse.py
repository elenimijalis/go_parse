#!/usr/bin/env python
import os
import json
import argparse
import sys

def parseObo(handle, count=-1, outdir=None):
    json_objects = []
    go_term = {}
    term_start = False
    output_terms = 0

    for num, line in enumerate(handle):
        if not line.strip() and term_start:
            json_objects.append(go_term)

            x = go_term['def']
            go_term['def'] = x[1:x.rindex('[')-2]

            db_xref = x[x.rindex('[')+1:x.rindex(']')].split(', ')
            d = {}
            for i in db_xref:
                if ':' in i:
                    key, val = i.split(':', 1)
                    if key in d:
                        d[key].append(val)
                    else:
                        d[key] = [val]
                else:
                    print i

            go_term['db_xref'] = d

            out = '%s.json' % go_term['id']
            if outdir:
                out = os.path.join(outdir, out)

            with open(out, 'w') as handle:
                json.dump(go_term, handle)
                output_terms += 1
                if count != -1 and output_terms > count:
                    sys.exit()

            go_term = {}
            term_start = False

        elif term_start:
            key, val = line.split(':', 1)
            go_term[key] = val.strip()

        elif line.startswith('[Term]'):
            term_start = True


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('obo', type=file, help='Path to OBO file')
    parser.add_argument('--count', type=int, help="Maximum number of OBO terms to dump before quitting. Useful in testing", default=-1)
    parser.add_argument('--outdir', help="output directory")
    args = parser.parse_args()

    parseObo(args.obo, count=args.count, outdir=args.outdir)
