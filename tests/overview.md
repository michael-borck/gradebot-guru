# Testing Overview

## Purpose of Tests

The primary goal of testing is to ensure that the code behaves as expected and to identify any potential issues before they affect the end users. Testing helps maintain code quality, reliability, and performance.

## Types of Tests

In this project, we have implemented various types of tests to cover different aspects of the code:

### 1. Unit Tests

Unit tests focus on testing individual functions or methods in isolation. These tests are designed to validate that each function or method works correctly on its own.

### 2. Integration Tests

Integration tests verify that different parts of the system work together as expected. These tests ensure that the interactions between various modules and components function correctly.

### 3. Doctests

Doctests are embedded in the docstrings of functions or methods. They provide examples of how to use the function and validate that the function produces the expected results when executed with the provided examples.

## Test Frameworks and Tools

We use the following tools and frameworks for testing:

### Pytest

Pytest is a powerful and flexible testing framework for Python. It is used for writing and running unit tests and integration tests. Pytest provides various features like fixtures, parameterized testing, and easy integration with other tools.

### Mock

The `unittest.mock` module allows you to replace parts of your system under test and make assertions about how they were used. Mock objects are used to simulate the behavior of real objects in controlled ways.

### MkDocStrings

MkDocStrings is a plugin for MkDocs that automatically generates documentation from docstrings in your code. It supports Python and other languages, providing a convenient way to include function and class documentation in your project's documentation site.

## Running Tests

### Running All Tests

To run all tests, use the following command:

```bash
pytest
```