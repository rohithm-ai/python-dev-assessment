# api_client.py

import requests

def fetch_and_display_users(num_users):
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        # Make a GET request to the API
        response = requests.get(url)

        # Check for non-200 status codes
        response.raise_for_status()

        # Parse the JSON response
        users = response.json()

        # Iterate through the list of users and print the requested details
        for i in range(min(num_users, len(users))):  # Ensure we don't go out of bounds
            user = users[i]
            name = user.get('name', 'N/A')
            email = user.get('email', 'N/A')
            city = user.get('address', {}).get('city', 'N/A')
            print(f"Name: {name}, Email: {email}, City: {city}")
    
    except requests.exceptions.RequestException as e:
        # Handle any network-related errors
        print(f"Network error occurred: {e}")
        return None
    except ValueError as e:
        # Handle errors if the JSON structure is unexpected
        print(f"Error parsing JSON: {e}")
        return None
    except KeyError as e:
        # Handle errors if expected keys are missing in the response
        print(f"Missing expected data: {e}")
        return None

# Example usage:

# Fetch and display details of the first 3 users
fetch_and_display_users(3)

# Fetch and display details of the first 15 users (tests out-of-bounds case)
fetch_and_display_users(15)

