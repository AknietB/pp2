import json
with open("sample-data.json") as my_file:
    data = json.load(my_file)
imdata = data.get("imdata" , [])
print("Interface Status")
print("=" * 80)
print('{:<50} {:<20} {:<8} {:<6}'.format('DN', 'Description' , 'Speed' , 'MTU'))
print('-'*50, '-'*20 , '-'*8 , '-'*6)
for i in imdata:
    l1PhysIf= i.get('l1PhysIf', {})
    attrib = l1PhysIf.get('attributes' , {})
    dn = attrib.get('dn' , '')
    description = attrib.get('descr' , '')
    speed = attrib.get('speed' , '')
    mtu = attrib.get('mtu' , '')
    print('{:<50} {:<20} {:<8} {:<6}'.format(dn , description , speed , mtu))