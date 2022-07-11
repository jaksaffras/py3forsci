s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
sx = "spam\\n"  # don't do this
s5 = r"spam\n"   # do this!

print(s1 == s2 == s3 == s4)

print("Guido's the ex-BDFL of Python")
print('Guido is the ex-"BDFL" of Python')
print("""Guido's the ex-"BDFL" of Python""")

query = """
select p.first_name, p.last_name, c.city_name
from people p, cities c
join on p.city_id = c.city_id
desc
"""


actor = "Chris Hemsworth"
print(len(actor), type(actor))

print(actor.upper())
x = actor.upper()
print(actor, x)
print("actor.count('h'): {}".format(actor.count('h')))
print("actor.count('Chris'): {}".format(actor.count('Chris')))
print("actor.count('H'): {}".format(actor.count('H')))
print("actor.lower().count('h'): {}".format(actor.lower().count('h')))

print("actor.startswith('Chris'): {}".format(actor.startswith('Chris')))
print("actor.startswith('Liam'): {}".format(actor.startswith('Liam')))

print("'wort' in actor: {}".format('wort' in actor))
print("'is' in actor: {}".format('is' in actor))
print("'was' in actor: {}".format('was' in actor))


print("actor.find('Chris'): {}".format(actor.find('Chris')))
print("actor.find('Liam'): {}".format(actor.find('Liam')))
print("actor.find('wo'): {}".format(actor.find('wo')))

print("actor.replace('Chris', 'Liam'): {}".format(actor.replace('Chris', 'Liam')))

s = "        All my exes live in Texas        "
print("|" + s + "|")
print("|" + s.lstrip() + "|")  #  " \t\n\r\b\f"
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print()

x = """

fruitbat    

     walrus

    wallaby

honey     badger

jellybean       



"""
print("|" + x + "|")
print("|" + x.strip() + "|")


w = "will.i.iam..;.."
print(w.rstrip(';.'))

raw_line = "Mary had a little lamb\n"

line = raw_line.rstrip()

print(line)


m = "xxxyxxxspamyyyxyyy"
print("m.strip('xy'): {}".format(m.strip('xy')))





























