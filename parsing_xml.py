import xml.dom.minidom as minidom


xml_file = open('currency.xml', 'r', encoding='windows-1251')
xml_data = xml_file.read()

dom = minidom.parseString(xml_data)
dom.normalize()

elements = dom.getElementsByTagName('Valute')
Name_list = []
Value_list = []

for node in elements:
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName == 'Name':
                if child.firstChild.nodeType == 3:
                    Name = child.firstChild.data
            if child.tagName == 'Value':
                if child.firstChild.nodeType == 3:
                    Value = float((child.firstChild.data.replace(',', '.')))

    Name_list.append(Name)
    Value_list.append(Value)

print('', "Valutes:", '', *Name_list, '', 'Values:', '', *Value_list, sep='\n')


xml_file.close()