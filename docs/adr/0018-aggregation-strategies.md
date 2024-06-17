# ADR 0017: Aggregation Strategies

## Context and Problem Statement

To mitigate the variance in grades provided by different LLM providers or repeated evaluations by the same provider, we need a robust strategy for aggregating multiple grades. Different aggregation strategies can be employed to balance the grading outcomes, ensuring fairness and consistency.

## Decision Drivers

- Need to handle variance in LLM grading.
- Ensuring fairness and consistency in the grading process.
- Flexibility to configure different aggregation strategies based on use case.

## Considered Options

- **Simple Average**: Compute the arithmetic mean of all grades.
- **Weighted Average**: Compute the mean of all grades with assigned weights to each provider.
- **Median**: Compute the median of all grades to reduce the impact of outliers.
- **Bias-Adjusted**: Adjust grades based on known biases of specific providers.
- **Normalization**: Normalize grades to a common scale before aggregation.

## Decision Outcome

Chosen options:
- Implemented **Simple Average**, **Weighted Average**, **Median**, and **Bias-Adjusted** aggregation methods. 
- Normalization was considered but not implemented due to current simplicity requirements.

## Consequences

- **Simple Average**:
  - **Pros**: Easy to understand and implement.
  - **Cons**: May be influenced by outliers.

- **Weighted Average**:
  - **Pros**: Allows emphasizing more reliable providers.
  - **Cons**: Requires determining appropriate weights.

- **Median**:
  - **Pros**: Reduces the impact of outliers.
  - **Cons**: May not represent the true average in skewed distributions.

- **Bias-Adjusted**:
  - **Pros**: Compensates for known biases in specific providers.
  - **Cons**: Requires accurate bias estimation.

- **Normalization**:
  - **Pros**: Ensures all grades are on a common scale.
  - **Cons**: Adds complexity to the grading process.

## Implementation

The `grade_submission` function was updated to support these aggregation strategies. The configuration file was also updated to allow specifying the desired aggregation method and any necessary parameters (e.g., weights for weighted average, bias adjustments for bias-adjusted).

Example configuration:
```json
{
    "llm_providers": [
        {"provider": "openai", "api_key": "mock_key", "model": "text-davinci-003"}
    ],
    "number_of_repeats": 3,
    "repeat_each_provider": true,
    "aggregation_method": "bias_adjusted",
    "bias_adjustments": {
        "openai": -5.0
    },
    "rubric_path": "path/to/rubric.csv",
    "submission_path": "path/to/submissions",
    "logging_level": "INFO"
}
```

## Conclusion

The chosen aggregation strategies (simple average, weighted average, median, and bias-adjusted) provide a flexible and robust mechanism to handle the variance in LLM grading. Future work may involve implementing normalization if required by more complex grading scenarios.
