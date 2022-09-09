import requests, json

while True:
    uri = "https://zipcloud.ibsnet.co.jp/api/search"
    while True:
        aee = input('郵便番号を入力:')
        if len(aee) == 7:
            break
        else:
            print('郵便番号が間違っています')
            continue

    uri = uri + "?zipcode={0}".format(aee)
    res = requests.get(uri)
    data = json.loads(res.text)
    area = data['results']
    error = data['status']
    # ms = data['message']

    if error == 200:
        print(area[0]['address1'] + area[0]['address2'] + area[0]['address3'])
        if input('他の郵便番号を入力しますか？ y/n:') == 'y':
            continue
        else:
            break
    elif error == 500 or error == 400:
        print('error')
        break