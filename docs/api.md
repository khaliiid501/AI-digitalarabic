# API Documentation

## ArabicProcessor Class

The main class for Arabic text processing and AI operations.

### Constructor

```python
ArabicProcessor(config: Optional[dict] = None)
```

Initialize the Arabic processor with optional configuration.

**Parameters:**
- `config` (dict, optional): Configuration dictionary for the processor

### Methods

#### process(text: str) -> str

Process Arabic text with normalization and cleaning.

**Parameters:**
- `text` (str): Input Arabic text

**Returns:**
- `str`: Processed and normalized Arabic text

**Example:**
```python
processor = ArabicProcessor()
result = processor.process("مرحبا    بكم في    عالم الذكاء الاصطناعي")
print(result)  # "مرحبا بكم في عالم الذكاء الاصطناعي"
```

#### analyze_sentiment(text: str) -> str

Analyze sentiment of Arabic text.

**Parameters:**
- `text` (str): Input Arabic text

**Returns:**
- `str`: Sentiment classification ("Positive", "Negative", "Neutral")

**Example:**
```python
sentiment = processor.analyze_sentiment("هذا المنتج رائع جداً")
print(sentiment)  # "Positive"
```

#### extract_entities(text: str) -> List[Tuple[str, str]]

Extract named entities from Arabic text.

**Parameters:**
- `text` (str): Input Arabic text

**Returns:**
- `List[Tuple[str, str]]`: List of (entity, type) tuples

**Example:**
```python
entities = processor.extract_entities("محمد يعمل في شركة جوجل في الرياض")
print(entities)  # [('محمد', 'PERSON'), ('جوجل', 'ORG'), ('الرياض', 'LOC')]
```

#### generate_content(prompt: str, max_length: int = 100) -> str

Generate Arabic content based on a prompt.

**Parameters:**
- `prompt` (str): Text prompt for content generation
- `max_length` (int, optional): Maximum length of generated content (default: 100)

**Returns:**
- `str`: Generated Arabic text

**Example:**
```python
content = processor.generate_content("اكتب عن الذكاء الاصطناعي", max_length=200)
print(content)
```

## Error Handling

The library provides specific exceptions for different error conditions:

- `ArabicProcessingError`: General processing errors
- `ModelNotFoundError`: When required models are not available
- `InvalidConfigError`: Configuration-related errors

## Configuration

See `config.yaml` for detailed configuration options.