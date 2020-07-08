def counting_sort(arr, index):
	string_arr = arr

	counter = []
	for i in range(10): 
		counter.append([])

	for element in string_arr:
		counter[int(element[index])].append(element)
		
	sorted_list = []
	for sub_count in counter:
		for num in sub_count:
			sorted_list.append(num)
			
	return sorted_list

def radix_sort(arr):
	len_max = len([int(i) for i in str(max(arr))])
	current_sort = []

	for num in arr:
		diff = len_max - len(str(num)) 
		new_num = ""
		if diff != 0:
			for i in range(diff):
				new_num += "0"
		new_num += str(num)
		current_sort.append(new_num)

	for i in range(len_max):
		current_sort = counting_sort(current_sort, -(i+1))

	final = []
	for num in current_sort:
		final.append(int(num))

	return final

print(radix_sort([12,34,6,5,43,78,987,1432,5,654,123,89,70]))





