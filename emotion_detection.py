import requests
import json

def emotion_detector(text_to_analyze):
    """
    Detect emotions in the provided text using Watson NLP Emotion Predict function.
    
    Args:
        text_to_analyze: The text string to analyze for emotions
        
    Returns:
        The text attribute from the response object
    """
    # Watson NLP API endpoint
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService'
    
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
    
    # Return the text attribute of the response object
    return response.text
