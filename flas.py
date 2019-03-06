import json
# url='http://127.0.0.1:8000/todo/api/v1.0/tasks'
# the_data=requests.get(url)
# # print (the_data.text)


# with open('falsk_data.json','w+')as send_file:
# 	json.dump(the_data.text,send_file)


with open('falsk_data.json','r')as open_file:
	Dit_open=json.load(open_file)
	print(Dit_open)
