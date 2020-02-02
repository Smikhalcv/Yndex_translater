# a = {}
# a['Омлет'] = []
# a['Омлет'].append({'ingedient_name': 'Яйцо', 'quantity': '2', 'measure': 'шт.'})
# a['Омлет'].append({'ingedient_name': 'Молоко', 'quantity': '100', 'measure': 'мл.'})
# print(a)
# with open('recipes.txt', encoding='utf-8-sig') as f:
#     print(f.read().split()[17])
    # print(f.readline().strip())
    # print(int(f.readline()))
    # for line in f:
    #     #if line == ''
    #     print(bool(line))


    # cook_book = {}
    # while True:
    #     cook = f.readline().strip()
    #     cook_book[cook] = []
    #     count = f.readline().strip()
    #     i = 1
    #     for i in range(int(count)+1):
    #         cook_book[cook].append(f.readline().strip().split())
    #         i += 1
        # while f.readline().strip() != False:
        #     cook_book[cook].append(f.readline().strip().split())
        #print(bool(f.readline().strip()))


    #print(cook_book)
with open('recipes.txt', encoding='utf-8-sig') as f:
    def parser(file_data):
        data = file_data.read().split('\n')
        result = {}
        while data:
            next_recipe = int(data[1]) + 2
            recipe = data[:next_recipe:1]
            keys = ['ingredient_name', 'quantity', 'measure']
            # result[recipe[0]] = list(
            #     map(lambda elem: {key: value for key, value in zip(keys, elem.split('|'))}, recipe[2:])
            # )
            result[recipe[0]] = list(
                map(lambda elem: {a: b for a, b in zip(keys, elem.split('|'))}, recipe[2:])
            )
            data = data[next_recipe + 1::1]
        return result

    print(parser(f))