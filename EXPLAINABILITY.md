# GitMediProtocol Explainability Specification

This document provides a transparent, verifiable architectural breakdown of how **GitMediProtocol** operates, processes input, makes decisions, and enforces security boundaries.

---

## 1. Input Data and Data Sources Used

GitMediProtocol consumes de-identified electronic health records (EHR), clinical trial laboratory panels, patient vital sign logs, and investigational protocol schedule matrices. These data sources include laboratory biomarker metrics such as eGFR, absolute neutrophil count, and platelet levels, as well as encounter timestamps and documented toxicity observations. The agent ingests these inputs in raw JSON, CSV, and clinical text format and parses them into standardized clinical evaluation records for downstream safety verification. External clinical trial protocol specifications and patient consent logs are also monitored as sensitive data sources to ensure research regulatory standards are strictly maintained.

---

## 2. How It Decides and Reasoning Process

The decision making process follows a deterministic, five-stage analytical pipeline designed to eliminate ambiguity and hallucination. When a clinical trial evaluation request is received, the agent first evaluates patient laboratory values using the eligibility-criteria-evaluator tool to verify that baseline inclusion gates are satisfied with zero active exclusion criteria. Next, the reasoning engine invokes the adverse-event-grader tool to compute CTCAE v5.0 severity grades for any documented adverse clinical events. Furthermore, the agent validates protocol schedule adherence using the protocol-visit-window-auditor tool. Finally, the agent correlates all clinical findings against predefined regulatory trial protocols to issue a conclusive verdict of APPROVED, BLOCKED, or NEEDS_REVIEW alongside an automated safety remediation report.

---

## 3. Constraints, Limitations, and Known Issues

GitMediProtocol operates under strict operational constraints to prevent false positives and non-deterministic behavior across different agent frameworks. GitMediProtocol operates under strict operational constraints to prevent diagnostic misclassifications and regulatory non-compliance across execution frameworks. The agent is deliberately limited to structured clinical data audit and protocol verification and cannot execute autonomous medical interventions or bedside patient diagnostic procedures. Another known issue and limitation is that unstructured physician narratives with novel clinical abbreviations may require secondary human clinical review rather than autonomous blocking. Furthermore, the agent enforces a low temperature constraint of 0.1 to maintain strict predictability across all supported export frameworks.
