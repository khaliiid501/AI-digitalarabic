# دليل إعداد بيئة التطوير | Development Setup Guide

<div dir="rtl">

## متطلبات النظام

### المتطلبات الأساسية
- **Python 3.8+**: لتطوير نماذج الذكاء الاصطناعي
- **Node.js 14+**: لتطوير واجهة المستخدم
- **Git**: لإدارة الكود المصدري
- **Docker** (اختياري): للتشغيل في حاوية

### المتطلبات الموصى بها
- **GPU متوافق مع CUDA**: لتسريع تدريب النماذج
- **16GB RAM** على الأقل: لمعالجة البيانات الكبيرة
- **SSD**: لتسريع قراءة وكتابة البيانات
- **VS Code** مع امتدادات Python و JavaScript

## خطوات الإعداد

### 1. استنساخ المستودع
```bash
git clone https://github.com/khaliiid501/AI-digitalarabic.git
cd AI-digitalarabic
```

### 2. إعداد بيئة Python
```bash
# إنشاء بيئة افتراضية
python -m venv venv

# تفعيل البيئة الافتراضية
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# تثبيت المتطلبات (عندما تكون متاحة)
pip install -r requirements.txt
```

### 3. إعداد Node.js
```bash
# تثبيت متطلبات Node.js (عندما تكون متاحة)
npm install

# أو باستخدام Yarn
yarn install
```

### 4. إعداد قاعدة البيانات
```bash
# PostgreSQL setup (سيتم إضافته لاحقاً)
# MongoDB setup (سيتم إضافته لاحقاً)
```

### 5. إعداد المتغيرات البيئية
```bash
# إنشاء ملف .env
cp .env.example .env

# تحرير الملف وإضافة المتغيرات المطلوبة
nano .env
```

## هيكل ملفات التكوين

### ملف requirements.txt (Python)
```
# AI and ML libraries
torch>=1.9.0
transformers>=4.12.0
numpy>=1.21.0
pandas>=1.3.0
scikit-learn>=1.0.0

# Arabic NLP libraries
camel-tools>=1.3.0
arabert>=1.0.0
qalsadi>=0.3.0

# Web framework
fastapi>=0.68.0
uvicorn>=0.15.0
sqlalchemy>=1.4.0
psycopg2-binary>=2.9.0

# Utilities
python-dotenv>=0.19.0
requests>=2.26.0
python-multipart>=0.0.5

# Testing
pytest>=6.2.0
pytest-asyncio>=0.15.0
coverage>=5.5.0
```

### ملف package.json (Node.js)
```json
{
  "name": "ai-digitalarabic-frontend",
  "version": "1.0.0",
  "description": "واجهة المستخدم لمشروع الذكاء الاصطناعي العربي",
  "main": "index.js",
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "dependencies": {
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "react-router-dom": "^6.0.0",
    "@mui/material": "^5.0.0",
    "@mui/icons-material": "^5.0.0",
    "axios": "^0.24.0",
    "styled-components": "^5.3.0"
  },
  "devDependencies": {
    "react-scripts": "5.0.0",
    "@testing-library/react": "^11.2.7",
    "@testing-library/jest-dom": "^5.14.1",
    "eslint": "^7.32.0",
    "prettier": "^2.4.1"
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }
}
```

## إعداد أدوات التطوير

### VS Code Extensions
```json
{
  "recommendations": [
    "ms-python.python",
    "ms-python.vscode-pylance",
    "ms-toolsai.jupyter",
    "bradlc.vscode-tailwindcss",
    "esbenp.prettier-vscode",
    "ms-vscode.vscode-typescript-next",
    "ms-vscode.arabic-support"
  ]
}
```

### Git Hooks (pre-commit)
```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.0.1
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files

  - repo: https://github.com/psf/black
    rev: 21.9b0
    hooks:
      - id: black

  - repo: https://github.com/pycqa/flake8
    rev: 3.9.2
    hooks:
      - id: flake8
```

## اختبار الإعداد

### اختبار Python Environment
```python
# test_setup.py
import sys
import torch
import transformers
from camel_tools.utils.charmap import CharMapper

def test_python_setup():
    print(f"Python version: {sys.version}")
    print(f"PyTorch version: {torch.__version__}")
    print(f"Transformers version: {transformers.__version__}")
    print(f"CUDA available: {torch.cuda.is_available()}")
    
    # Test Arabic text processing
    mapper = CharMapper.builtin_mapper("ar")
    test_text = "مرحبا بكم في مشروع الذكاء الاصطناعي العربي"
    mapped_text = mapper(test_text)
    print(f"Arabic processing test: {mapped_text}")

if __name__ == "__main__":
    test_python_setup()
```

### اختبار Node.js Environment
```javascript
// test_setup.js
const React = require('react');
const { version } = require('./package.json');

console.log(`Project version: ${version}`);
console.log(`React version: ${React.version}`);
console.log(`Node.js version: ${process.version}`);

// Test Arabic text support
const arabicText = "مرحبا بكم في مشروع الذكاء الاصطناعي العربي";
console.log(`Arabic text test: ${arabicText}`);
console.log(`Text direction: ${arabicText.match(/[\u0600-\u06FF]/) ? 'RTL' : 'LTR'}`);
```

## أوامر التطوير الشائعة

### خدمات الخلفية (Backend)
```bash
# تشغيل خادم التطوير
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# تشغيل الاختبارات
pytest tests/ -v

# فحص جودة الكود
flake8 src/
black src/ --check
```

### واجهة المستخدم (Frontend)
```bash
# تشغيل خادم التطوير
npm start

# بناء الإنتاج
npm run build

# تشغيل الاختبارات
npm test

# فحص جودة الكود
npm run lint
```

## استكشاف الأخطاء الشائعة

### مشاكل Python
- **ModuleNotFoundError**: تأكد من تفعيل البيئة الافتراضية
- **CUDA errors**: تحقق من تثبيت CUDA وتوافق الإصدارات
- **Memory errors**: قلل حجم البيانات أو استخدم جهاز أقوى

### مشاكل Node.js
- **Port already in use**: غيّر المنفذ أو أوقف العملية المستخدمة له
- **Module not found**: تأكد من تشغيل `npm install`
- **Build errors**: تحقق من إصدارات المكتبات والتوافق

## الدعم والمساعدة

### الموارد المفيدة
- [وثائق Python](https://docs.python.org/)
- [وثائق React](https://reactjs.org/docs/)
- [دليل PyTorch](https://pytorch.org/tutorials/)
- [مكتبات NLP العربية](https://github.com/CAMeL-Lab/camel_tools)

### التواصل
- افتح Issue في GitHub للمشاكل التقنية
- راسل المطور الرئيسي للاستفسارات العامة
- شارك في مناقشات المجتمع

</div>

---

## English Setup Instructions

### Quick Setup
1. Clone the repository: `git clone https://github.com/khaliiid501/AI-digitalarabic.git`
2. Set up Python virtual environment: `python -m venv venv`
3. Activate environment: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt` (when available)
5. Set up Node.js: `npm install` (when available)
6. Configure environment variables: Copy `.env.example` to `.env`
7. Run setup tests to verify installation

### Development Commands
- **Backend**: `uvicorn main:app --reload`
- **Frontend**: `npm start`
- **Tests**: `pytest` for Python, `npm test` for JavaScript
- **Linting**: `flake8` for Python, `npm run lint` for JavaScript

For detailed setup instructions in English, please refer to the Arabic section above or contact the development team.