import json
import requests

def emotion_detector(text_to_analyse):
    """Run emotion detection using the Emotion Predict function of the Watson NLP Library.
    
    Args:
        text_to_analyze (str): The text to be analyzed.
    
    Returns:
        dict: A dictionary containing the emotion scores and the dominant emotion.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=myobj, headers=headers)
    formatted_response = json.loads(response.text)

    if response.status_code == 400:
        # Return the dictionary with all values set to None for error response
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Extract emotion scores
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Find dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Construct output dictionary
    output = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
    
    return output