# Use Factory Pattern for LLM Interface

## Context and Problem Statement

We need a flexible way to interact with different LLMs, potentially including local models for privacy reasons.

## Decision Drivers

- Flexibility
- Future-proofing
- Privacy and security

## Considered Options

- Factory Pattern
- Direct instantiation

## Decision Outcome

Chosen option: "Factory Pattern", because it provides a clean and flexible way to support multiple LLMs.

## Consequences

- Positive: Easy to add support for new LLMs.
- Positive: Improved code maintainability.
- Negative: Slightly increased complexity.
