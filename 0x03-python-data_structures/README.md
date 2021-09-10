# PYTHON DATA STRUCTURES
### Exploring The Details Of Lists And Tuples
#### eg
```#!/usr/bin/python3
def element_at(my_list, idx):
ind = len(my_list) - 1
if idx < 0:
	return my_list
elif idx > ind:       # select an index to retrieve
	return None
else:
return (my_list.index(idx))
```