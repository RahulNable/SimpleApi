from bs4 import BeautifulSoup

with open('./drawing1.xml', 'r') as f:
    data = f.read() 

bs_data = BeautifulSoup(data, 'xml') 

x = bs_data.find_all(['xdr:oneCellAnchor'])

for y in x:
    y = str(y)
    # print(y)

    # print('inside extract_imagename function')

    sub1 = 'name="'
    sub2 = '.png"'
    idx1 = y.index(sub1)
    # print(y.find('.png"'))
    if '.png"' in y:
        idx2 = y.index(sub2)
    else:
        sub2 = '.jpg"'
        idx2 = y.index(sub2)
        # print('for jpg')

    # print(idx2)
    
    res = ''
    for idx in range(idx1 + len(sub1), idx2):
        res = res + y[idx]
        # print(y[idx])
    print(res + sub2.replace('"',''))



