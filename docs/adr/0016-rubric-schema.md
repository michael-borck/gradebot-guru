# ADR 0016: Rubric Schema for GradeBotGuru

### Context

In GradeBotGuru, the grading rubric is a critical component used to evaluate student submissions. The schema and format of this rubric must be consistent and well-defined to ensure accurate and meaningful assessments.

### Decision

The rubric schema will follow a CSV format with the following columns:
- `criterion`: The name of the grading criterion (e.g., "Content").
- `description`: A detailed description of what the criterion evaluates (e.g., "Quality and relevance of content."). This field can be left empty if no description is provided.
- `max_points`: The maximum points that can be awarded for the criterion (e.g., 10).

This schema allows for flexibility and clarity, ensuring that each criterion is clearly defined and can be properly evaluated.

### Example

A sample CSV file following this schema would look like:

```csv
criterion,description,max_points
Content,Quality and relevance of content.,10
Clarity,Clarity of expression and organization.,5
Grammar,Proper use of grammar and syntax.,5
```

### Rationale

1. **Clarity**: Including a description for each criterion ensures that both graders and the LLM understand what each criterion evaluates.
2. **Flexibility**: Allowing descriptions to be optional provides flexibility for simpler rubrics.
3. **Consistency**: A well-defined schema ensures consistency across different grading tasks and prevents errors in interpretation.

### Consequences

1. **Implementation**: The `load_rubric` function and other related components must be updated to handle this schema.
2. **Documentation**: All documentation and examples must reflect this schema to ensure users understand how to create and use grading rubrics.
3. **Testing**: Comprehensive tests must be written to ensure that the schema is correctly implemented and that edge cases (e.g., missing descriptions) are handled properly.
