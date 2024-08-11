"""
Emotion Detection Server

This module implements a Flask server for the Emotion 
Detection application.
It provides endpoints for analyzing the emotion in a given 
statement and rendering the index page."""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion detector")

@app.route("/emotionDetector")
def emotion_analyzer():
    '''Analyzes the emotion in a given statement using the Emotion Detection model.

    This function receives a text statement from the user through a request argument
    and applies the Emotion Detection model to analyze the emotion in the statement.
    It returns a system response that includes the scores for different emotions 
    (anger, disgust, fear, joy, sadness)
    and identifies the dominant emotion.
    Args:
        None

    Returns:
        str: The system response containing the emotion scores and the dominant emotion.

    Raises:
        None'''
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    return f'''For the given statement, the system response is: 'anger': {anger},
     'disgust': {disgust},'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. 
     The dominant emotion is {dominant_emotion}'''
@app.route("/")
def render_index_page():
    ''' Renders the index page for the Emotion Detection application.
    This function is responsible for rendering the index page of the Emotion Detection application.
    The index page typically contains a form where users can input their text for emotion analysis.
    Args:
        None
    Returns:
        str: The HTML content of the index page.
    Raises:
        None'''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
