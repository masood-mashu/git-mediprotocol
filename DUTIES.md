# Separation of Duties for GitMediProtocol

## Maker Role: ClinicalResearchCoordinator
ClinicalResearchCoordinator who aggregates patient laboratory reports, vitals, and visit logs.

## Checker Role: PrincipalInvestigator
PrincipalInvestigator who audits trial protocol compliance, AE grading, and patient eligibility status.

## Dual-Control Verification Pipeline
1. Ingest de-identified patient laboratory panel and medical history records.
2. Evaluate patient biomarker values against trial inclusion/exclusion thresholds.
3. Map reported adverse events and laboratory toxicities to CTCAE severity grades.
4. Generate protocol adherence certificates and audit logs for regulatory review.
