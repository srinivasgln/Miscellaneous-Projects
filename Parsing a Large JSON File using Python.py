# This is a program to parse a JSON File, called foodyo_output, into its constuients.
# This is a solution to a problem asked in a Job- Interview for Machine Learning Engineer position.

import json
import pandas as pd
json_data = json.load(open('foodyo_output.json'))
Res_Name=[]

for iterat in (json_data['body']['Recommendations']):
    Res_Name.append(iterat['RestaurantName'])
print('Names of Restaurant are ', Res_Name)

for iterat in (json_data['body']['Recommendations']):
    for men in iterat['menu']:
        if men['type']=='sectionheader':
            for chd in men['children']:
                if (chd['selected']==1)&(chd['type']=='item'):
                    print('--->', chd['name'])
                    for deepchd in chd['children']:
                        if deepchd['selected']==1:
                            print('-------->',deepchd['name'])
                            try:
                                for deepchd2 in deepchd['children']:
                                    if deepchd2['selected']==1:
                                        print('------------->',deepchd2['name'])
                                        try:
                                            for deepchd3 in deepchd2['children']:
                                                if deepchd3['selected']==1:
                                                    print('----------------------------> :',deepchd3['name'])
                                        except:
                                            continue
                            except:
                                continue
