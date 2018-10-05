import requests
res=requests.post('https://textbelt.com/text', {
  'phone': '+91 indian mobile code and type your code....?',
  'message': 'Hello world',
  'key': 'textbelt',
})
result=res.json()
print(result)
