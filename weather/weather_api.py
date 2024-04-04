import requests


class weathers:
    def weather(self,state='delhi')-> dict:
        key = 'b00863b5e88226b1c75fec70a9efcb68'
        state = 'delhi'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={state}&appid={key}'
        response = requests.get(url)
        print(response.json())
        return dict(response.json())






    
    
    