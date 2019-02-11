 

data_set = [
              'SUVOJITSU',
              '651SUVOMN',
              '$$$$$SUVOSUVOJIT$$$$$',
            ]

test_cases = [
              'SUVO',
              'SUVOJIT'
              ]

for i,d in enumerate(data_set):

 for x,t in enumerate(test_cases):
    count = d.count(t)
    if(count >0):
        print(f'{t}\t in \t {d} \t\t = \t{count}')
    else:
        print(f'{t}\t in \t {d} \t\t = \t0')
