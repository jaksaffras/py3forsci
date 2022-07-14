import lxml.etree as et
# import xml.etree.ElementTree as et

doc = et.parse('DATA/solar.xml')

print("doc: {}".format(doc))

root = doc.getroot()

print("root: {}".format(root))
print("root.tag: {}".format(root.tag))
for child in root:
    if child.tag.endswith('planets'):
        for planet in child:
            print(planet.get('planetname'))
            for moon in planet:
                print(f"   {moon.text}")




