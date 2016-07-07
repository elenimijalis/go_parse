import json
import sys

with open("go.obo") as handle:
    json_objects = []
    go_term = {}
    term_start = False

    for num, line in enumerate(handle):
        if num > 63:
            sys.exit()

        if not line.strip() and term_start:
            json_objects.append(go_term)

            with open('%s.json' % go_term['id'], 'w') as out:
                json.dumps(go_term)

            go_term = {}
            term_start = False

        elif term_start:
            key, val = line.split(':', 1)
            go_term[key] = val.strip()

        elif line.startswith('[Term]'):
            term_start = True
