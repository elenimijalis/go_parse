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
            # print re.split(r"['\"](.*?)['\"]", go_term['def'])

            x = go_term['def']
            go_term['def'] = x[1:x.rindex('[')-2]

            db_xref = x[x.rindex('[')+1:-1].split(', ')
            d = {}
            for i in db_xref:
                key, val = i.split(':')
                if key in d:
                    d[key].append(val)
                else:
                    d[key] = [val]

            go_term['db_xref'] = d

            with open('%s.json' % go_term['id'], 'w') as out:
                json.dump(go_term, out)

            go_term = {}
            term_start = False

        elif term_start:
            key, val = line.split(':', 1)
            go_term[key] = val.strip()

        elif line.startswith('[Term]'):
            term_start = True
