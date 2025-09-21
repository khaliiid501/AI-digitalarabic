# AI-digitalarabic - Arabic AI Digital Content Project

AI-digitalarabic is an Arabic AI project focused on digital Arabic content processing, including Arabic data collection, text model development, user interface design, and AI integration.

Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.

## Current Repository State

**IMPORTANT**: This repository is currently in its initial development phase with minimal content.

### What Currently Exists
- README.md with basic project title
- .github directory with Copilot instructions (this file)
- Git repository structure

### What Does NOT Currently Exist
- No source code files
- No build system (no package.json, requirements.txt, Dockerfile, etc.)
- No dependencies or package managers
- No test suites
- No CI/CD workflows
- No development environment setup

## Working Effectively

### Initial Development Setup
Since this is a greenfield Arabic AI project, you will likely need to establish the development environment:

1. **Identify the intended technology stack** by checking issues and project requirements
2. **Set up appropriate tooling** for AI/ML development (likely Python-based)
3. **Create project structure** following Arabic AI/NLP best practices

### Common Development Patterns for Arabic AI Projects
When code is added to this repository, it will likely follow these patterns:

#### Python-based AI Development (Most Likely)
```bash
# Typical setup for Arabic AI projects
pip install -r requirements.txt  # When requirements.txt exists
python -m venv venv              # Virtual environment setup
source venv/bin/activate         # Activate virtual environment
```

#### Common Arabic NLP Libraries
Projects in this domain typically use:
- `transformers` for Arabic language models
- `torch` or `tensorflow` for deep learning
- `arabic-reshaper` and `python-bidi` for Arabic text handling
- `datasets` for Arabic data processing

### Expected Build Times (When Applicable)
Since no build system exists yet, these are estimates for typical Arabic AI projects:
- **Environment Setup**: 5-10 minutes
- **Dependency Installation**: 10-30 minutes (AI/ML libraries are large)
- **Model Training**: Hours to days (NEVER CANCEL - set timeout to 8+ hours)
- **Testing**: 5-15 minutes

## Validation Requirements

### Before Making Changes
1. **Check for existing project structure** - files may have been added since these instructions
2. **Review open issues** for current development priorities
3. **Validate Arabic text handling** if working with Arabic content

### After Making Changes
1. **Test Arabic text processing** if applicable - ensure proper RTL handling
2. **Verify Unicode support** for Arabic characters
3. **Test on sample Arabic text** to ensure encoding is correct

## Project Context and Goals

Based on repository issues, this project aims to include:

1. **Arabic Data Collection** (جمع البيانات العربية)
   - Gathering Arabic text datasets for training
   - Data preprocessing and cleaning for Arabic text

2. **Arabic Text Model Development** (تطوير نموذج النص العربي)
   - Building ML models for Arabic language processing
   - Training and fine-tuning Arabic language models

3. **User Interface Design** (تصميم واجهة المستخدم)
   - Creating interfaces for Arabic content interaction
   - Ensuring proper RTL (right-to-left) text display

4. **Development and Testing Tools** (أدوات التطوير والاختبار)
   - Setting up development environment
   - Creating testing frameworks for Arabic AI

5. **AI Integration** (تكامل الذكاء الاصطناعي)
   - Integrating AI models with applications
   - API development for Arabic AI services

## Common Tasks

### Repository Structure Check
```bash
# Always run this first to see current state
ls -la
find . -name "*.py" -o -name "*.json" -o -name "requirements.txt" -o -name "Dockerfile"
```

### Git Operations
```bash
# Check current branch and status
git --no-pager status
git --no-pager branch -a
git --no-pager log --oneline -5
```

### Issue Management
Always check GitHub issues for current priorities:
- Issue #2: Initial project task planning (in Arabic)
- Issue #6: Copilot instructions setup (this task)

## Development Guidelines

### When Adding New Code
1. **Create appropriate project structure** for the chosen technology stack
2. **Include Arabic language support** from the beginning
3. **Add proper Unicode handling** for Arabic text processing
4. **Follow Arabic NLP best practices** for data handling
5. **Include RTL text support** in any UI components

### When Working with Arabic Text
1. **Always test with actual Arabic text samples**
2. **Verify proper character encoding** (UTF-8)
3. **Test bidirectional text handling** (Arabic mixed with English)
4. **Ensure proper text direction** (RTL) in displays

### Future Development Notes
- Repository will likely evolve to include Python AI/ML stack
- Arabic text processing will be a core requirement
- Model training workflows will need long execution times
- Consider Arabic-specific preprocessing needs early in development

## Critical Reminders

- **NEVER CANCEL** long-running model training operations
- **Always validate Arabic text encoding** before committing changes
- **Test with real Arabic content** not just ASCII text
- **Check existing issues** for current development priorities
- **Expect this repository to evolve rapidly** from its current minimal state