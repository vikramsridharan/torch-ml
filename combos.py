import time
from random import sample
import sys

class Combination:
    def __init__(self, list, r):
        self.combos = []
        self.list = list
        self.r = r

    # use combs method to get the index combinations for each of the index in the list
    # get the actual combinations using the combinations of indexes
    def fetch(self):
        new_list = self.list.copy()
        while len(new_list) > 1:
            self.combs(new_list, [len(new_list) - 1])
            new_list.pop(len(new_list) - 1)
        combinations = []
        for c in self.combos:
            combinations.append(tuple([self.list[i] for i in c]))
        def sort_key(c):
            return sum(c)
        return sorted(combinations, key=sort_key)

    # get all combinations with nth index as the index of the last element
    # for example: in list [1,2,3,4,5] with r = 3
    # if n is index corresponding to 5 then the combinations (only the index values) this method will fetch are
    # (3, 4, 5), (2, 4, 5), (1, 4, 5), (2, 3, 5), (1, 3, 5), (1, 2, 5)
    def combs(self, list, index_comb):
        if len(index_comb) < self.r:
            for i in range(index_comb[0] - 1, -1, -1):
                new_index_comb = [i] + index_comb
                self.combs(list, new_index_comb)
        else:
            self.combos.append(tuple(index_comb))



start_time = time.time()
#a = [2981, 7689, 2100, 5960, 1762, 7187,  996, 2204, 6488, 6184, 5100, 1260, 8075, 6675, 3669, 8572, 2661, 6247, 5727, 4070, 3528, 8546, 2775, 1135, 8805]
#available_time = 30000
#a = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]
#a = [-1,-2,-3,-4,-5,10,20,30,40,50,60,70,80,90,100]
#a = [1,2,3,4,5]
costs = [110, 110, 110, 110, 110, 110, 110, 115, 115, 115, 120, 120, 120, 145]
snacks = {
    '110': ['Thattai', 'Thenkuzhal', 'Karaboondhi', 'Ribbon', 'Mul Murukku', 'Butter Murukku', 'Peanut Pakoda'],
    '120': ['Kai Murukku', 'Ragi Thenkuzhal', 'Uppu Seedai'],
    '115': ['Ragi Thattai', 'Milagu Thattai', 'Nendranga Chips'],
    '145': ['Adhirasam']
}
a = costs
available_time = int(sys.argv[1])
def matches_condition(current_list, previous_list):
    return sum(current_list) <= available_time and sum(current_list) > sum(previous_list)

def bsearch_verge_of_max(list, max):
    middle_index = int(len(list)/2) if len(list)%2 == 0 else int((len(list) + 1)/2 - 1)
    search_sum = sum(list[middle_index])
    len_of_list = len(list)
    next_sum = sum(list[middle_index + 1]) if middle_index != len_of_list - 1 else 0
    if search_sum == max: return list[middle_index]
    elif search_sum < max and middle_index == len_of_list - 1: return list[middle_index]
    elif search_sum < max and next_sum > max: return list[middle_index]
    elif search_sum < max and next_sum < max: return bsearch_verge_of_max(list[middle_index+1::1], max)
    elif search_sum < max and next_sum == max: return list[middle_index + 1]
    elif search_sum > max and middle_index != len_of_list - 1: return bsearch_verge_of_max(list[0:middle_index:1], max)
    elif search_sum > max and middle_index == len_of_list - 1: return []

selected_list = list()

for i in range(1, len(a)):
    c = Combination(a, i)
    combos = c.fetch()
    if sum(combos[0]) <= available_time:
        current_list = bsearch_verge_of_max(combos, available_time)
        if current_list != None and sum(current_list) > sum(selected_list):
            selected_list = current_list
            if sum(selected_list) == available_time:
                break
    else:
        break
    
end_time = time.time()
print(selected_list)
print('Your lucky combo: ')
item_caption = 'Snack'
quantity_caption = 'Numbers'
price_caption = 'Price'
total_caption = 'Total'
print(f'{item_caption: <25}{quantity_caption: <25}{price_caption: <25}{total_caption: <25}')
lucky_combo = dict()
for i in selected_list:
    item = sample(snacks[str(i)],1)[0]
    lucky_combo[item] = (lucky_combo[item][0] + 1, i) if item in lucky_combo else (1, i)
for i in lucky_combo:
    print(f'{i: <25}{lucky_combo[i][0]: <25}{lucky_combo[i][1]: <25}{lucky_combo[i][1]*lucky_combo[i][0]: <25}')
    
#print(lucky_combo)
    #print(f'{sample(snacks[str(i)],1)[0]:25} Rs. {i}')
#print(end_time - start_time)