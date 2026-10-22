# Success Metrics

## Product Initiative

Improve Duplicate-Payment Detection

## Purpose

Define how the Product Owner will measure whether the selected
solution produces a measurable improvement after implementation.

The current project contains baseline support data, but no
post-implementation results yet.

Therefore, this document defines the measurement framework only.
It does not claim that the solution has already produced an impact.

---

## Baseline

The current synthetic support-ticket analysis provides the following
baseline for Payment:

- Payment-related tickets: 63
- SLA breaches: 48
- SLA breach rate: 76.19%
- Average resolution time: approximately 1,970 minutes

For the Duplicate Payment problem:

- Duplicate Payment tickets: 26
- Share of Payment tickets: 41.27%

These values represent the current synthetic dataset and should be
treated as the baseline for the portfolio experiment.

---

## Primary Success Metric

### Duplicate Payment Ticket Rate

Measure the number of Duplicate Payment tickets after the solution
compared with the baseline.

Formula:

Duplicate Payment Ticket Rate =
Duplicate Payment Tickets / Total Payment Tickets × 100

### Target

The target should be defined after validating the baseline,
expected product impact, and implementation scope.

No target percentage is assumed at this stage.

---

## Secondary Metrics

### 1. Payment-Related SLA Breach Rate

Measure whether payment-related support cases are breaching SLA
less frequently after the solution.

Formula:

SLA Breaches / Payment Tickets × 100

Baseline:

76.19%

---

### 2. Average Resolution Time

Measure whether the average time required to resolve payment-related
support tickets decreases.

Baseline:

Approximately 1,970 minutes.

---

### 3. Payment Support Ticket Volume

Measure whether the number of payment-related support tickets
changes after implementation.

This metric should be interpreted together with payment transaction
volume because ticket volume alone does not necessarily represent
business performance.

---

### 4. Customer Impact

Where appropriate customer-level data becomes available, measure:

- Number of affected customers
- Repeat contacts
- Customer complaints
- Customer experience indicators

Customer impact must be measured rather than assumed.

---

### 5. Business Impact

Potential business metrics include:

- Payment success rate
- Checkout conversion rate
- Failed transaction rate
- Revenue affected by payment failures
- Support operational cost

These metrics require additional business or product data.

They are not currently validated by the support-ticket dataset.

---

# Measurement Design

## Before

Measure the baseline during a defined period before implementation.

```text
Baseline Period
      ↓
Payment Metrics
      ↓
Duplicate Payment Rate
SLA Breach Rate
Resolution Time