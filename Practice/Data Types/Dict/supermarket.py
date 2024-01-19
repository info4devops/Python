super_market = { 'store-1': { 
                             'name': 'KRISHNA GENERAL STORE',
                             'items': [
                               {'name':'soap','quantity':20},
                               {'name':'Brush','quantity':10}
                                      ]
  
                            },
                
                'store-2':{
                            'name': 'SRAVANTHI BOOK STORE',
                            'items':[
                              {'name':'Python','quantity':222},
                              {'name':'Java','quantity':111} 

                                    ]
                              
                          }
  
  
  
                 }

# To print the name of the store

print('Name of the Store:',super_market['store-1']['name'])

# To print the name of the store using get() function

print('Name of the Store using get() function:',super_market.get('store-1').get('name'))

# To print the all items present in store-1
print('-------:All Items present in store-1:--------')
for d in super_market['store-1']['items']:
  print(d['name'])
  
# To print number of python books present in super_market
print('-------:No.of Python books present in store-2:--------')
for item in super_market['store-2']['items']:
  if item['name']=='Python':
    print('The No.of Python Books:',item['quantity'])
    