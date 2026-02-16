# justfile

set shell := ["bash", "-c"]

# list all available commands
default: --list

# =============================================================================
#  Setup & Management
# =============================================================================

# install dependencies using uv
setup:
    uv sync --all-extras --dev

# upgrade all dependencies
upgrade:
    uv lock --upgrade
    uv sync

# clean up temporary files and caches
clean:
    rm -rf .ruff_cache .pytest_cache .mypy_cache .coverage
    find . -type d -name "__pycache__" -exec rm -rf {} +

# =============================================================================
#  Code Quality (Formatter, Linter, Type Checker)
# =============================================================================

# format code using ruff
fmt:
    uv run ruff format .
    uv run ruff check --fix .

# check for linting errors (no fix)
lint:
    uv run ruff check .

# run static type checking
type:
    uv run pyright

# =============================================================================
#  Testing
# =============================================================================

# run tests with pytest
test:
    uv run pytest

# run tests with coverage report
cover:
    uv run pytest --cov=src --cov-report=html

# =============================================================================
#  Workflows
# =============================================================================

# run all checks (format, lint, type, test) - good for pre-commit
check: fmt lint type test