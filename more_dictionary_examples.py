from pprint import pprint

parties = {}

with open('DATA/primeministers.txt') as pm_in:
    for raw_line in pm_in:
        line = raw_line.rstrip()
        term, first_name, last_name, dob, dod, birthplace, took_office, left_office, party = line.split(':')
        if party not in parties:
            parties[party] = set()

        parties[party].add(f"{first_name} {last_name}")

pprint(parties)
print('-' * 60)
#    key    value              dict
for party, pm_list in sorted(parties.items()):
    print(party)
    for pm in sorted(pm_list):
        print(f"   {pm}")
