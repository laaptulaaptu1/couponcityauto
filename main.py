import requests

def sayHello():
    print("Hello World Lets Run the Job!")
    r = requests.get('https://cvo-api-2.onrender.com/trigger-wp-cv')
    print(r)
    
if __name__ == "__main__":
    sayHello()
