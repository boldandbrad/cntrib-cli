
# activate venv
venv:
    . .venv/bin/activate

# install cntrib-cli from local
install:
    pip install -q .

# install cntrib-cli via flit
flit-install:
    pip install flit
    flit install

# install editable
dev-install:
    pip install -q -e .

# lint and format
lint:
    pre-commit run --show-diff-on-failure --all-files

# run all tests
test: install
    pytest

# run all tests with coverage
test-cov: install
    pytest -v --cov-report xml --cov cntrib

# build dist
build:
    flit build

# generate homebrew formula
brew: install
    poet -f cntrib-cli >> formula.rb

# remove artifacts
# TODO: remove __pycache__ dirs from src/ and tests/
cleanup:
    rm -f .coverage
    rm -f coverage.xml
    rm -f formula.rb
    rm -rf .pytest_cache
    rm -rf build
    rm -rf dist
    rm -rf *.egg-info
    rm -rf .ruff_cache
