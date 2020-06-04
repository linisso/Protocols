import requests
with open('access_token.txt', 'r') as file:
    token = file.readline()

    
version = 5.95  # api version
#put in user_id that ip or screen name
#user_id = 'solodushkin_si'
user_id = '50368482'
str_name_fields = 'photo_id'
fields = 'nickname'
namecase = 'name_case'
number = 0

if type(user_id) == str:
    response = requests.get('https://api.vk.com/method/users.get',
                            params={
                                'access_token': token,
                                'v': version,
                                'user_ids': user_id,
                                'fields': str_name_fields
                            }
                            )
    info = response.json()
    a = info['response'][0]
    user_id = a['id']

response = requests.get('https://api.vk.com/method/friends.get',
                        params={
                            'access_token': token,
                            'v': version,
                            'user_id': user_id,
                            'fields': fields,
                            'name_case': namecase
                        }
                        )

data = response.json()['response']['items']
print('Колличество друзей:', len(data))
for number in range(len(data)):
    print('user id:', data[number]['id'], '\n'
          + 'user name:', data[number]['first_name'], '\n'
          + 'user family name:', data[number]['last_name'], '\n'
          + '------------')

