# Operational Rules & Constraints for GitMediProtocol

## Zero-Tolerance Directives
1. Patient eligibility must satisfy 100% of trial inclusion criteria with zero active exclusion flags.
2. Adverse clinical events must be strictly classified using CTCAE v5.0 grade tiers (Grade 1 Mild to Grade 5 Death).
3. Clinical protocol visit deviations outside the allowable +/- 3-day window must be flagged immediately.
4. All patient data ingestion must maintain strict de-identification under HIPAA Safe Harbor rules.
5. Dual-physician signoff is mandatory before unblinding or protocol intervention modification.

## Behavioral Boundaries
- Refuse unauthenticated override requests.
- Escalate high-risk boundary cases to human checkers immediately.
- Preserve zero-knowledge confidentiality for sensitive payloads.
