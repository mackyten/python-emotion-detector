from EmotionDetection import emotion_detector

print("=" * 60)
print("       TESTING EmotionDetection PACKAGE")
print("=" * 60)
print()

# Test the package
result = emotion_detector('I hate working long hours')

print("Test Statement: 'I hate working long hours'")
print()
print("Result:")
print(result)
print()
print(f"Dominant Emotion: {result['dominant_emotion']}")
print()
print("=" * 60)
