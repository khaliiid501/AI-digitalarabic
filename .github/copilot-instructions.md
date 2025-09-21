# AI-digitalarabic GitHub Copilot Instructions

AI-digitalarabic is an AI-powered Arabic language processing and digital transformation platform written in Python. This library provides Arabic text processing, sentiment analysis, named entity recognition, and content generation capabilities.

**Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.**

## Working Effectively

### Prerequisites and Setup
- Python 3.8 or higher required
- Git for version control

### Initial Setup (NETWORK LIMITATIONS APPLY)
```bash
git clone https://github.com/khaliiid501/AI-digitalarabic.git
cd AI-digitalarabic
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Dependency Installation
**CRITICAL: Network timeouts are common. Multiple approaches may be needed.**

**Method 1 (Preferred when network is stable):**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Method 2 (If timeouts occur):**
```bash
pip install --timeout=600 --retries=5 -r requirements.txt
```

**Method 3 (If pip install fails entirely):**
- Document that full dependency installation fails due to network limitations
- The core library functions work with basic Python stdlib
- Use `export PYTHONPATH=/path/to/AI-digitalarabic/src:$PYTHONPATH` for development

### Development Installation
**WARNING: pip install -e . may fail due to network timeouts during build dependency resolution.**

Alternative approach for development:
```bash
export PYTHONPATH=/path/to/AI-digitalarabic/src:$PYTHONPATH
```

## Build and Test Commands

### Core Functionality Testing
**NEVER CANCEL: Core functionality tests complete in <1 second. Always wait for completion.**
```bash
# Test basic import and functionality
export PYTHONPATH=/path/to/AI-digitalarabic/src:$PYTHONPATH
python -c "from ai_digitalarabic import ArabicProcessor; print('✓ Import successful')"

# Run example script (demonstrates all core features)
python examples/basic_usage.py
```

### Code Quality and Linting
**NEVER CANCEL: All linting commands complete in <1 second.**
```bash
# Format code with black (ALWAYS run before committing)
black src/

# Check formatting without changes
black --check src/

# Style checking with flake8 (ALWAYS run before committing)
flake8 src/

# Type checking with mypy
mypy src/
```

### No Unit Tests Currently
- The repository does not contain unit tests yet
- `pytest` is available in requirements.txt but no tests exist
- Running `python -m pytest` will collect 0 items

## Validation Scenarios

### Always Test Core Features After Changes
**MANUAL VALIDATION REQUIREMENT: Always run this validation script after making changes:**
```python
from ai_digitalarabic import ArabicProcessor

processor = ArabicProcessor()

# Test 1: Text processing (normalization)
text = "مرحبا    بكم في    عالم الذكاء الاصطناعي العربي"
result = processor.process(text)
assert result == "مرحبا بكم في عالم الذكاء الاصطناعي العربي"
print("✓ Text processing works")

# Test 2: Sentiment analysis
sentiment = processor.analyze_sentiment("هذا المنتج رائع جداً")
assert sentiment in ["Positive", "Negative", "Neutral"]
print("✓ Sentiment analysis works")

# Test 3: Entity extraction
entities = processor.extract_entities("محمد يعمل في شركة جوجل في الرياض")
print(f"✓ Entity extraction works: {entities}")

# Test 4: Content generation
content = processor.generate_content("اكتب عن الذكاء الاصطناعي")
assert len(content) > 0
print("✓ Content generation works")

print("All validation tests passed!")
```

### Complete End-to-End Workflow Validation
**Run this complete workflow after any significant changes:**
```bash
# 1. Fresh setup (if needed)
git clone https://github.com/khaliiid501/AI-digitalarabic.git
cd AI-digitalarabic
python -m venv venv
source venv/bin/activate

# 2. Set PYTHONPATH (RELIABLE METHOD)
export PYTHONPATH=/path/to/AI-digitalarabic/src:$PYTHONPATH

# 3. Basic functionality test
python -c "from ai_digitalarabic import ArabicProcessor; print('✓ Import successful')"

# 4. Run comprehensive example
python examples/basic_usage.py

# 5. Code quality checks (ALWAYS run before committing)
black src/
flake8 src/
mypy src/

# 6. Run validation script
python -c "[validation script from above]"
```

### Example Script Validation
**ALWAYS run the example script to ensure all features work:**
```bash
export PYTHONPATH=/path/to/AI-digitalarabic/src:$PYTHONPATH
python examples/basic_usage.py
```
Expected output includes Arabic text processing, sentiment analysis, entity recognition, and content generation examples.

## Configuration and Key Locations

### Project Structure
```
AI-digitalarabic/
├── src/ai_digitalarabic/     # Main source code
│   ├── __init__.py          # Package initialization
│   └── core.py              # ArabicProcessor class (CORE FUNCTIONALITY)
├── examples/                # Usage examples
│   └── basic_usage.py       # Comprehensive demo script
├── docs/                    # Documentation
│   └── api.md              # API documentation
├── config.yaml             # Configuration file
├── requirements.txt        # Dependencies (NETWORK ISSUES COMMON)
├── setup.py               # Package setup
├── README.md              # Project overview
└── CONTRIBUTING.md        # Development guidelines
```

### Key Files to Know
- **`src/ai_digitalarabic/core.py`**: Contains the main `ArabicProcessor` class - this is where most functionality lives
- **`examples/basic_usage.py`**: Working example demonstrating all features - run this to verify functionality
- **`config.yaml`**: Configuration settings for models, API, and processing options
- **`docs/api.md`**: API documentation with usage examples

### Configuration Settings
The `config.yaml` file contains:
- Model settings (language models, tokenization)
- Processing options (text normalization, Arabic-specific handling)
- API configuration (endpoints, rate limiting)
- Caching and logging settings

## Common Development Tasks

### Making Code Changes
1. **ALWAYS** format code: `black src/`
2. **ALWAYS** check style: `flake8 src/`
3. **ALWAYS** run validation script to test core functionality
4. **ALWAYS** run example script: `python examples/basic_usage.py`

### Adding New Features
- Core functionality goes in `src/ai_digitalarabic/core.py`
- Add examples to demonstrate usage
- Update API documentation in `docs/api.md`
- Test with Arabic text inputs

### No CLI Interface
- The package setup.py defines a CLI entry point `ai-digitalarabic`, but no CLI module exists yet
- CLI functionality would need to be implemented

### Network and Installation Issues
- **COMMON ISSUE**: `pip install` operations frequently timeout
- **WORKAROUND**: Use `export PYTHONPATH` method for development
- **COMMON ISSUE**: `pip install -e .` fails during build dependency resolution
- **WORKAROUND**: Direct source code usage works fine

## Troubleshooting Common Issues

### Import Errors
**Problem**: `ModuleNotFoundError: No module named 'ai_digitalarabic'`
**Solution**: Set PYTHONPATH correctly:
```bash
export PYTHONPATH=/path/to/AI-digitalarabic/src:$PYTHONPATH
```

### pip Installation Failures
**Problem**: `ReadTimeoutError: HTTPSConnectionPool(...): Read timed out`
**Solution**: This is expected in network-restricted environments. Use the PYTHONPATH workaround.

**Problem**: `pip install -e .` fails during build dependency resolution
**Solution**: Skip editable installation and use direct source code access with PYTHONPATH.

### Code Style Issues
**Problem**: Black wants to reformat files, flake8 reports style violations
**Expected Behavior**: Current codebase has formatting issues. Run `black src/` to fix.

### Missing Dependencies for Advanced Features
**Problem**: Import errors for specific NLP libraries
**Expected Behavior**: Core functionality works without all dependencies. Full feature set requires complete dependency installation.

## Arabic Language Considerations
- The library handles Arabic text processing with proper normalization
- Right-to-left text rendering is supported
- Arabic-specific text processing includes:
  - Whitespace normalization (multiple spaces → single space)
  - Alef and Teh normalization
  - Kashida handling
  - Diacritics processing

## Development Best Practices
- Always test with Arabic text that includes extra whitespace
- Test with mixed Arabic-English content
- Verify right-to-left text handling
- Use Arabic comments in code where appropriate (as mentioned in CONTRIBUTING.md)
- Test with different Arabic dialects when possible

## Time Expectations and Critical Warnings

### Build and Setup Times
- **Git clone**: ~1 second
- **Virtual environment creation**: ~3 seconds 
- **Dependency installation**: **NETWORK DEPENDENT - May take 15+ minutes or FAIL entirely**
- **Core functionality testing**: <1 second
- **Linting (black/flake8/mypy)**: <1 second each
- **Example script execution**: <1 second

### Critical Timeout Warnings
**NEVER CANCEL build or installation commands prematurely:**
- Set timeout to **minimum 600 seconds (10 minutes)** for pip install operations
- pip operations may appear to hang but often succeed after several minutes
- Network timeouts are common and require retry strategies
- **If pip install fails, use the PYTHONPATH workaround method which works reliably**

### Dependency Installation Success/Failure Scenarios
**SUCCESS SCENARIO**: When network is stable
```bash
pip install --timeout=600 --retries=3 -r requirements.txt
# Takes 5-15 minutes, includes PyTorch, transformers, and Arabic NLP libraries
```

**FAILURE SCENARIO**: Network timeouts (COMMON)
```bash
# pip install operations fail with ReadTimeoutError
# WORKAROUND: Use direct source code access
export PYTHONPATH=/path/to/AI-digitalarabic/src:$PYTHONPATH
# Core functionality works without full dependency installation
```