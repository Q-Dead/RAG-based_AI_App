import requests

def render_animation():
    animation_response = requests.get('https://lottie.host/6debe06f-7332-4d04-bd62-85a3d23891d1/kx4j1rvT9h.json')
    animation_json = dict()
    
    if animation_response.status_code == 200:
        animation_json = animation_response.json()
    else:
        print("Error in the URL")     
                           
    return animation_json