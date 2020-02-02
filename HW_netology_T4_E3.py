import csv

flats_list = list()

with open('output.csv', newline='', encoding='utf-8-sig') as csvfile:
	flats_csv = csv.reader(csvfile, delimiter=';')
	flats_list = list(flats_csv)

# for f in flats_list:
# 	print(f)
#TODO 1
i = 0
for flat in flats_list:
	if "новостройка" in flat[2]:
		print('Номер новостройки в документе %s ' % (flat[0]))
		i += 1
print('Всего новостроек: %s' % (i))

#TODO 2

flats = []
flat_info = {"id":[], "rooms":[], "type":[], "price":[]}

for flat in flats_list:
    flat_info['id'] += [flat[0]]
    flat_info['rooms'] += [flat[1]]
    flat_info['type'] += [flat[2]]
    flat_info['price'] += [flat[11]]

for i in range(len(flat_info['id'])):
    print(flat_info['id'][i], flat_info['rooms'][i], flat_info['type'][i], flat_info['price'][i])
    i += 1
print(flat_info)

#TODO 3

subway_dict = {}
subway_list = []
for subway in flats_list[1:]: #список метро
    subway_list += [subway[3].replace("м.", "")]

subway_set = set(subway_list)
subway_r_list = list(subway_set) # список уникальных метро из множества выше
for subway in subway_r_list: # cловарь с ключами уникальных названий метро
    subway_dict[subway] = []

for subway in flats_list: # внесение значений квартир по ключам метро
    if subway[3].replace('м.','') in subway_dict.keys():
        subway_dict[subway[3].replace('м.','')] += [subway[12]]

list_key = list(subway_dict.keys()) # список ключей словаря

for subway in list_key: # вывод количества квартир на станцию метро
    if subway == '':
        print('Количество квартир без указания станции метро: ', len(subway_dict[subway]))
    else:
        print('Количество квартир у станции метро %s : ' % (subway) , len(subway_dict[subway]))

