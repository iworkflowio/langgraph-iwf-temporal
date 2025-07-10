# LangGraph-iWF-Temporal

A library on top of iWF/Temporal to define workflow in LangGraph's Graph APIs (node+edges).

## Overview

This library provides a bridge between LangGraph's intuitive graph-based workflow definition and the powerful execution capabilities of iWF/Temporal. It allows you to define workflows using LangGraph's node and edge paradigm while leveraging iWF/Temporal for robust, scalable workflow execution.

## Installation

Install the library using pip:

```bash
pip install langgraph-iwf-temporal
```

Or using Poetry:

```bash
poetry add langgraph-iwf-temporal
```

## Development

### Setting up Development Environment

1. Clone the repository
2. Install Poetry if you haven't already:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```
3. Install dependencies:
   ```bash
   poetry install
   ```

### Running Tests

```bash
poetry run pytest
```

### Code Formatting

```bash
poetry run black .
poetry run flake8 .
poetry run mypy .
```

### Building the Package

```bash
poetry build
```

### Publishing the Package

```bash
poetry publish
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
