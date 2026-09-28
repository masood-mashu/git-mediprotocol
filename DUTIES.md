# Segregation of Duties (SOD) Policy: GitMediProtocol

This document establishes the role boundaries and segregation of duties for the GitMediProtocol agent.

## Role Separation

### 1. Maker
The Maker role is responsible for authoring clinical protocol parameter definitions, preparing de-identified patient laboratory cohorts, and generating automated trial remediation diffs.
This role cannot approve or merge its own changes into protected clinical branches.

### 2. Checker
The Checker role is responsible for reviewing, auditing, and validating incoming clinical trial records, patient eligibility gates, and adverse event grading.
This role operates as an impartial auditor to verify compliance with FDA and GCP regulatory benchmarks.

### 3. Approver
The Approver role is strictly reserved for human principal investigators and institutional review board administrators.
Human approval is required for all production trial deployments, patient enrollment signoffs, and protocol deviation overrides.
