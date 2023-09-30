import requests

def send_msg(text):
   token = "6142407861:AAEX-DX236aX2X4mYHXRsIkadr_p6Kc0QaM"
   chat_id = "6061208576"
   url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text 
   results = requests.get(url_req)
   print(results.json())

