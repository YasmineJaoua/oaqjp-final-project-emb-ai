import requests
import json

def emotion_detector(text_to_analyze):

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    response = requests.post(url, json=payload, headers=headers)

    formatted_response = json.loads(response.text)

    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    anger = emotions["anger"]
    disgust = emotions["disgust"]
    fear = emotions["fear"]
    joy = emotions["joy"]
    sadness = emotions["sadness"]

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion
    }