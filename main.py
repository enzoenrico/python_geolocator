import requests
from requests.api import request

# Api da "Ip_stack"
access_key = "4b9354bb09e65257406c63d661cb935f"

ip = "134.201.250.155"

params = {
          "ouput": "&output=json"
          "securituy"
          }

url = requests.get(
    f"http://api.ipstack.com/{ip}?access_key={access_key}&{params}"
)


def main():
    print(url.text)


if __name__ == "__main__":
    main()
