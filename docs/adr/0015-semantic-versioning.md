### ADR 0015: Adoption of Semantic Versioning

#### Context

To improve clarity and consistency in versioning, the project will adopt Semantic Versioning (semver) starting from version `0.5.0`. Prior to this version, version increments may not have strictly followed semantic versioning conventions.

Semantic Versioning follows the format `MAJOR.MINOR.PATCH`, where:

- **MAJOR** version changes indicate incompatible API changes.
- **MINOR** version changes add functionality in a backward-compatible manner.
- **PATCH** version changes make backward-compatible bug fixes.

#### Decision

Starting from version `0.5.0`, the project will adhere to Semantic Versioning.

#### Rationale

1. **Clarity**: Semantic Versioning provides a clear and predictable way to understand the nature of changes between releases.
2. **Compatibility**: It helps users understand the impact of updating to a new version, especially regarding backward compatibility.
3. **Industry Standard**: Semantic Versioning is widely adopted and recognized in the software industry, promoting best practices in versioning.

#### Implications

1. **Documentation**: A note will be added to the documentation to inform users of the adoption of Semantic Versioning from version `0.5.0` onwards.
2. **Version Increments**: Future releases will follow the semver rules:
   - Increment the MAJOR version for incompatible API changes.
   - Increment the MINOR version for backward-compatible functionality additions.
   - Increment the PATCH version for backward-compatible bug fixes.
3. **Legacy Versions**: Versions prior to `0.5.0` will remain unchanged, and any inconsistencies in their versioning will be documented.

#### Implementation

1. **Document Versioning Policy**: Add the following note to the `README.md` or `CHANGELOG.md`:

    ```markdown
    ## Versioning

    Starting from version `0.5.0`, this project follows [Semantic Versioning](https://semver.org/).

    - **MAJOR** version increments indicate incompatible API changes.
    - **MINOR** version increments add functionality in a backward-compatible manner.
    - **PATCH** version increments make backward-compatible bug fixes.

    Prior to version `0.5.0`, the version numbers may not have strictly followed semantic versioning conventions.
    ```

2. **Tag Current Version**: Ensure the current version is tagged appropriately.

3. **Future Releases**: Follow Semantic Versioning for all subsequent releases.
