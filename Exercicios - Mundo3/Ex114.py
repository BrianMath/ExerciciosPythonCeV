from requests import get, ConnectionError

try:
    site = get("http://www.pudim.com.br")
except ConnectionError:
    print("\033[31mNão foi possível conectar-se ao PUDIM\033[m")
else:
    print("\033[32mFoi possível conectar-se ao PUDIM\033[m")
