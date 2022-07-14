import lxml.etree as et

knights = et.Element("knights")
with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight = et.SubElement(knights, "knight", title=title)
        knight_name = et.SubElement(knight, "name")
        knight_name.text = name
        et.SubElement(knight, "color").text = color
        et.SubElement(knight, "quest").text = quest
        et.SubElement(knight, "comment").text = comment


# print(knights)
xml_data = et.tostring(knights, pretty_print=True, xml_declaration=True)
print(xml_data.decode())

doc = et.ElementTree(knights)
doc.write('knights.xml', pretty_print=True, xml_declaration=True)
