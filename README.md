# Olori AI Engineer

A production-ready Python AI project scaffold built with best practices.

## Architecture

This project follows the **src-layout**, ensuring a clean separation between source code, tests, and metadata.

### Directory Structure
- `src/`: Core application logic.
  - `core/`: Configuration, logging, and exception handling.
  - `services/`: Business logic and AI model integrations.
  - `utils/`: Helper functions and utilities.
- `tests/`: Pytest suite.
- `docs/`: Project documentation.
- `.env.example`: Template for environment variables.

## Getting Started

### Prerequisites
- Python 3.10+
- Recommended: `venv` or `conda`

### Installation
1. Clone the repository.
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your specific configuration
   ```

### Running the Project
```bash
python -m src.main
```

### Running Tests
```bash
pytest
```

## Production Readiness
- **Validation:** Pydantic Settings for strict configuration validation.
- **Logging:** Dual console and file logging with structured formatting.
- **Type Safety:** Full type hint coverage (Python 3.10+).
- **Modularity:** Clear separation of concerns.
- **Error Handling:** Centralized custom exception hierarchy.
