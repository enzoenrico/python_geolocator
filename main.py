import requests
import json

# Api da "Ip_stack"
access_key = ""

#Ip para localizar (mudar dps)
ip = ""

#Parametros da api
params = [
    "&output=json",
    "&security=1"
]

#Url pra get request
url = (
    f"api.ipstack.com/{ip}?access_key={access_key}{params}"
)

#Url formatada da request
rmv_char = "'[] :,"

#Tirar caracteres da lista params para rodar tudo certin
def translator():
    formatted_url = url.translate({ord(i): None for i in rmv_char})
    return formatted_url

#Escrever o resultado da api como um json legível
def json_print():
    url_request = translator()
    request = requests.get('http://'+url_request)
    json_request_in = json.loads(request.text)
    json_request_out = json.dumps(json_request_in, indent=2)
    return json_request_out
    
def main():
    print(json_print())

#Falta implementar agora a command line
#coisas como 
#iplocator -i 'ip' --security - sendo isso só um exemplo
#usar alguma biblioteca pra isso



if __name__ == "__main__":
    main()
