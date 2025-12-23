import requests

def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    res = requests.get(url)
    data = res.json()
    

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        location = user_data["location"]["country"]
        return username, location
    else:
        raise Exception("Failed To Fetch User Data")
    
def main():
    try:
        username, country = fetch_random_user()
        print(f"Username : {username}, \nCountry : {country}")
    except Exception as e: 
        print(str(e))

if __name__ == "__main__":
    main()