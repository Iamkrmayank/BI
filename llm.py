import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def validate_data(data):
    prompt = ""
    if "query" in data:
        prompt = data["query"]
    else:
        # Improved Prompt for Business Data Validation
        prompt = f"""
        Verify the following business data based on these rules:
        - Name should not contain promotional keywords.
        - Address should be properly formatted and contain a valid Indian Pincode.
        - Website should be an official business website (avoid social media links like facebook.com, instagram.com, twitter.com).
        - Phone number should be a valid Indian 10-digit number.
        - Reviews should be more than 10.
        - Rating should be greater than or equal to 3.0.
        - Latitude and Longitude should be valid coordinates within India.
        
        Data:
        Name: {data['name']}
        Address: {data['address']}
        Website: {data['website']}
        Phone: {data['phone_number']}
        Reviews: {data['reviews']}
        Rating: {data['rating']}
        Latitude: {data['latitude']}
        Longitude: {data['longitude']}

        Return only 'Valid' or 'Invalid' with a short reason if invalid.
        """

    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a strict data validation assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message["content"].strip()
