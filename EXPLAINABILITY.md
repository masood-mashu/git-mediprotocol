# Explainability & Governance Statement

## Decision Architecture
GitMediProtocol evaluates clinical trial eligibility and safety using deterministic medical decision rules. When a patient profile is evaluated, laboratory parameters (e.g. eGFR, absolute neutrophil count, platelets) are parsed against strict numeric eligibility gates. Toxicities and symptoms are indexed to standard CTCAE toxicity descriptors. If a lab value fails the inclusion threshold or a Grade 3+ adverse event is detected, the agent immediately issues an alert with clinical rationale.

## Input Data Provenance
Data sources consumed by GitMediProtocol include structured electronic case report forms (eCRFs), de-identified clinical lab panels, and trial protocol schedule matrices. All inputs conform to CDISC clinical data standards.

## Operational Limits & Non-Goals
GitMediProtocol operates strictly on structured laboratory metrics and documented adverse observations; it does not replace physician clinical diagnostic acumen or bedside bedside evaluation. Protocol amendments must be synchronized before execution.
