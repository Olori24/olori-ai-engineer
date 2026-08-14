# Olori AI Engineer

> **Intelligent Autonomy, Uncompromised Integrity**

**OAE™ Engineering Standard**

Olori AI Engineer is an AI engineering project focused on reliable, autonomous software-engineering workflows. The repository is maintained under the Open Autonomous Engineer (OAE™) engineering standard: security first, explicit verification, deterministic behaviour where practical, and human oversight for consequential changes.

## Architecture

This project follows a `src`-layout with separation between application code, tests, configuration, and engineering documentation.

```text
src/
├── core/       # Configuration, logging, exceptions, and core concerns
├── router/     # Application routing boundaries
├── services/   # Business logic and AI integrations
├── utils/      # Shared utilities
└── main.py     # Application entry point

tests/          # Automated tests
docs/           # Project documentation
agents/         # Agent definitions and workflows
bin/            # Project tooling
```

## Getting Started

### Prerequisites

- Python 3.10+
- `venv` or another isolated Python environment

### Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Review `.env` before running the application. Never commit credentials or other secrets.

### Running

```bash
python -m src.main
```

### Testing

```bash
pytest
```

### Code quality

```bash
black .
isort .
mypy .
```

## Engineering Standards

OAE™ applies the following principles to this repository:

- Security before convenience
- Correctness before speed
- Human approval for consequential changes
- Tests before integration
- Verification before completion
- Preserve existing behaviour unless a change is intentional
- Prefer explicit contracts over hidden assumptions
- Keep architecture modular and maintainable
- Document significant engineering decisions
- Keep dependencies and configuration auditable

The engineering workflow is:

```text
Analyze
  ↓
Review
  ↓
Plan
  ↓
Human Approval
  ↓
Implement
  ↓
Test
  ↓
Verify
  ↓
Re-analyze
```

## Project Governance

The repository's mission, constitution, workforce model, and roadmap are maintained as first-class engineering documents:

- `MISSION.md`
- `CONSTITUTION.md`
- `ENGINEERING_STANDARDS.md`
- `WORKFORCE.md`
- `ROADMAP.md`
- `MASTER_ROADMAP.md`

These documents should remain consistent with the implementation. Empty or obsolete governance documents are treated as engineering debt and are addressed through controlled changes.

## Status

Active development. This repository is being progressively reviewed and professionalized through OAE™ engineering workflows.

## License

MIT

---

**Engineered with OAE™ — Open Autonomous Engineer**
