from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        testcase1 = emotion_detector("I am glad this happened")
        expected1 = {
            'anger': 0.0,
            'disgust': 0.0,
            'fear': 0.0,
            'joy': 1.0,
            'sadness': 0.0,
            'dominant_emotion': 'joy'
        }
        self.assertEqual(testcase1, expected1)

        testcase2 = emotion_detector("I am really mad about this")
        expected2 = {
            'anger': 1.0,
            'disgust': 0.0,
            'fear': 0.0,
            'joy': 0.0,
            'sadness': 0.0,
            'dominant_emotion': 'anger'
        }
        self.assertEqual(testcase2, expected2)

        testcase3 = emotion_detector("I feel disgusted just hearing about this")
        expected3 = {
            'anger': 0.0,
            'disgust': 1.0,
            'fear': 0.0,
            'joy': 0.0,
            'sadness': 0.0,
            'dominant_emotion': 'disgust'
        }
        self.assertEqual(testcase3, expected3)

        testcase4 = emotion_detector("I am so sad about this")
        expected4 = {
            'anger': 0.0,
            'disgust': 0.0,
            'fear': 0.0,
            'joy': 0.0,
            'sadness': 1.0,
            'dominant_emotion': 'sadness'
        }
        self.assertEqual(testcase4, expected4)

        testcase5 = emotion_detector("I am really afraid that this will happen")
        expected5 = {
            'anger': 0.0,
            'disgust': 0.0,
            'fear': 1.0,
            'joy': 0.0,
            'sadness': 0.0,
            'dominant_emotion': 'fear'
        }
        self.assertEqual(testcase5, expected5)

unittest.main()