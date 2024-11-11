# Install required Python packages
install:
    pip install --upgrade pip &&\
        pip install -r requirements.txt

# Run tests with pytest, show verbose output, and check code coverage
test:
    python -m pytest -vv --cov=mylib test_*.py

# Format code with Black
format:    
    black *.py 

# Lint code using ruff (uncomment pylint for alternative linting)
lint:
    # Uncomment below to test with pylint
    # pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py
    # ruff linting is 10-100X faster than pylint
    ruff check *.py mylib/*.py

# Lint Dockerfile using hadolint
container-lint:
    docker run --rm -i hadolint/hadolint < Dockerfile

# Refactor code by running format and lint sequentially
refactor: format lint

# Placeholder for deploy commands
deploy:
    # Deploy commands go here

# Run install, lint, test, format, and deploy in sequence
all: install lint test format deploy

# Add, commit, and push generated files to GitHub (useful in CI/CD)
generate_and_push:
    # Add, commit, and push the generated files to GitHub
    @if [ -n "$$(git status --porcelain)" ]; then \
        git config --local user.email "action@github.com"; \
        git config --local user.name "GitHub Action"; \
        git add .; \
        git commit -m "Add output log"; \
        git push; \
    else \
        echo "No changes to commit. Skipping commit and push."; \
    fi
