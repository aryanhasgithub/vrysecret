from homeassistant_api import Client
inp = input("hello")
if inp=="on":
 with Client(
    'http://homeassistant.local:8123/api',
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjMGU2NTE4YmNjNjk0OGE3ODA0NjVlN2MyMTYwYzY5YiIsImlhdCI6MTczNzM4MTIyMywiZXhwIjoyMDUyNzQxMjIzfQ.gvr3jtcEkEqU8zX2fCUNdJCFRgUscA9o1ZtGA0Xgx38'
 ) as client:

    light = client.get_domain("switch")

    light.turn_on(entity_id="switch.smart_socket_socket")
else:
    
    with Client(
    'http://homeassistant.local:8123/api',
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjMGU2NTE4YmNjNjk0OGE3ODA0NjVlN2MyMTYwYzY5YiIsImlhdCI6MTczNzM4MTIyMywiZXhwIjoyMDUyNzQxMjIzfQ.gvr3jtcEkEqU8zX2fCUNdJCFRgUscA9o1ZtGA0Xgx38'
 )  as client:

     light = client.get_domain("switch")

     light.turn_off(entity_id="switch.smart_socket_socket")
