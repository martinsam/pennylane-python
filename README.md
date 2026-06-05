# Pennylane Python Library
> [!WARNING]
> This project is currently under active development. Your feedback is greatly appreciated and will help the future of the project.


The Pennylane Python library provides convenient access to the Pennylane API from applications written in Python.

Following Domain-Driven Design (DDD) principles, Pennylane resources are represented as rich domain objects rather than raw JSON payloads. The library offers a clean, type-safe, and object-oriented interface for interacting with customers, invoices, suppliers, accounting entries, and other financial resources.

## Installation

This package is available on PyPI:

```sh
pip install --upgrade pennylane
```

Alternatively, install from source with:

```sh
python -m pip install .
```

## Usage
The library needs to be configured with your account's secret key which is available in your Pennylane Dashboard.

```python
import os

from pennylane import PennylaneClient

client = PennylaneClient(
    api_key=os.environ["PENNYLANE_API_KEY"]
)
```
