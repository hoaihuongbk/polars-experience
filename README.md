# Polars Experience

A personal exploration repository for learning and experimenting with Polars - a modern, high-performance data manipulation library in Python.

## About

This repository contains code examples and experiments using Polars, focusing on its familiar syntax for those coming from PySpark background. Polars offers powerful data processing capabilities with features like:

- DataFrame operations similar to PySpark (select, filter, groupby)
- Lazy evaluation for optimized query execution
- High performance on single-node computation
- Intuitive API design

## Why Polars?

- **PySpark-like Syntax**: If you're familiar with PySpark, Polars offers a similar experience with operations like:
    - `select()`
    - `filter()`
    - `groupby()`
    - Lazy evaluation support

- **Single Node Performance**: Optimized for local machine processing while maintaining familiar data manipulation patterns

- **Modern Design**: Built with Rust, focusing on performance and memory efficiency

## Getting Started

This project uses `uv` for Python environment management and includes a Makefile for easy setup and execution.

1. Initialize the environment:
```bash
make init_venv
```

2. Run the example:
```bash
make run
```

## Resources
- [Official Polars Documentation](https://docs.pola.rs/user-guide/getting-started/#reading-writing)

