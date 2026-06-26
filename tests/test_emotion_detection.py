"""
Unit tests for the emotion detection module.
"""

import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """
    Test cases for emotion_detector function.
    """

    def test_joy(self):
        """
        Test that a joyful statement returns joy as dominant emotion.
        """
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_anger(self):
        """
        Test that an angry statement returns anger as dominant emotion.
        """
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_disgust(self):
        """
        Test that a disgust statement returns disgust as dominant emotion.
        """
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_fear(self):
        """
        Test that a fearful statement returns fear as dominant emotion.
        """
        result = emotion_detector("I am afraid that this will happen")
        self.assertEqual(result["dominant_emotion"], "fear")

    def test_sadness(self):
        """
        Test that a sad statement returns sadness as dominant emotion.
        """
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")


if __name__ == "__main__":
    unittest.main()
