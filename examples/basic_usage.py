#!/usr/bin/env python3
"""
Basic example demonstrating AI-digitalarabic usage.

This example shows how to use the AI-digitalarabic library for
basic Arabic text processing tasks.
"""

# Note: This is a demonstration example. The actual implementation
# would require the full AI-digitalarabic package to be developed.

class ArabicProcessor:
    """Demo Arabic text processor class."""
    
    def __init__(self):
        """Initialize the Arabic processor."""
        print("Initializing AI-digitalarabic processor...")
        
    def process(self, text: str) -> str:
        """Process Arabic text with basic normalization."""
        # Demo processing - remove extra spaces and normalize
        processed = " ".join(text.split())
        return processed
        
    def analyze_sentiment(self, text: str) -> str:
        """Analyze sentiment of Arabic text."""
        # Demo sentiment analysis
        positive_words = ["رائع", "ممتاز", "جيد", "أحب"]
        negative_words = ["سيء", "أكره", "فظيع", "مروع"]
        
        for word in positive_words:
            if word in text:
                return "Positive"
        for word in negative_words:
            if word in text:
                return "Negative"
        return "Neutral"
        
    def extract_entities(self, text: str) -> list:
        """Extract named entities from Arabic text."""
        # Demo entity extraction
        entities = []
        # This would use actual NER models in production
        words = text.split()
        for word in words:
            if word in ["محمد", "أحمد", "فاطمة", "عائشة"]:
                entities.append((word, "PERSON"))
            elif word in ["جوجل", "مايكروسوفت", "أبل"]:
                entities.append((word, "ORG"))
            elif word in ["الرياض", "القاهرة", "دبي", "بيروت"]:
                entities.append((word, "LOC"))
        return entities
        
    def generate_content(self, prompt: str, max_length: int = 100) -> str:
        """Generate Arabic content based on prompt."""
        # Demo content generation
        templates = {
            "الذكاء الاصطناعي": "الذكاء الاصطناعي هو تقنية متقدمة تحاكي القدرات البشرية في التفكير والتعلم...",
            "التكنولوجيا": "التكنولوجيا تلعب دوراً مهماً في تطوير المجتمعات الحديثة...",
            "البرمجة": "البرمجة هي فن وعلم كتابة التعليمات للحاسوب..."
        }
        
        for key in templates:
            if key in prompt:
                return templates[key]
        
        return "المحتوى المُولد باستخدام الذكاء الاصطناعي العربي."


def main():
    """Main demonstration function."""
    print("=== AI-digitalarabic Demo ===\n")
    
    # Initialize processor
    processor = ArabicProcessor()
    
    # Example 1: Text processing
    print("1. Text Processing:")
    arabic_text = "مرحبا    بكم في    عالم الذكاء الاصطناعي العربي"
    processed = processor.process(arabic_text)
    print(f"Original: {arabic_text}")
    print(f"Processed: {processed}\n")
    
    # Example 2: Sentiment analysis
    print("2. Sentiment Analysis:")
    sentiments = [
        "هذا المنتج رائع جداً",
        "أكره هذا التطبيق",
        "التطبيق عادي"
    ]
    
    for text in sentiments:
        sentiment = processor.analyze_sentiment(text)
        print(f"Text: {text}")
        print(f"Sentiment: {sentiment}\n")
    
    # Example 3: Entity extraction
    print("3. Named Entity Recognition:")
    entity_text = "محمد يعمل في شركة جوجل في الرياض"
    entities = processor.extract_entities(entity_text)
    print(f"Text: {entity_text}")
    print(f"Entities: {entities}\n")
    
    # Example 4: Content generation
    print("4. Content Generation:")
    prompts = [
        "اكتب عن الذكاء الاصطناعي",
        "اكتب عن التكنولوجيا",
        "اكتب عن البرمجة"
    ]
    
    for prompt in prompts:
        content = processor.generate_content(prompt)
        print(f"Prompt: {prompt}")
        print(f"Generated: {content}\n")


if __name__ == "__main__":
    main()