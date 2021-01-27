def telegramsend(token_id,group_id,message):
    import requests
    send_text = 'https://api.telegram.org/bot' + token_id + '/sendMessage?chat_id=' + group_id + '&parse_mode=Markdown&text=' + message 
    response = requests.get(send_text)
    return response.json()
