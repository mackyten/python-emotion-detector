import requests
import json

def emotion_detector(text_to_analyze):
    # Watson NLP API endpoint (Fixed URL)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers with the model ID
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Input JSON format
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    # Make the POST request to Watson NLP API
    response = requests.post(url, headers=headers, json=input_json)
    
    # Check for status code 400 (blank/invalid input)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Convert the response text into a dictionary using json library
    response_dict = json.loads(response.text)
    
    # Extract emotions with their scores
    emotions = response_dict['emotionPredictions'][0]['emotion']
    
    # Extract required emotions
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Find the dominant emotion (emotion with the highest score)
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Return the output in the required format
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }