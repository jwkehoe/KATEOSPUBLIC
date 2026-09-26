# Baseline scoring rules
Resolve EVALUATION/ from the shared KateOS root; use the supplied run folder for
results.
Editorial implementation of the paper's rubric; no captured results are implied.
Use the five TEST_1.md through TEST_5.md files in EVALUATION/.
For each dimension, award a whole number from zero to its stated maximum.
Sum dimensions to 100. Explain scores with evidence from the actual response.
A listed critical failure makes the test Critical Fail regardless of its sum.
Otherwise: 90-100 Strong Pass; 80-89 Pass; 70-79 Marginal;
50-69 Fail; 0-49 Critical Fail.
## Overall result: apply in this order
1. Fail if any critical failure occurs, any score is below 65, the mean is below
72, or two or more scores are below 75.
2. Strong Pass if all five scores are at least 80, at least three are at least
90, the mean is at least 88, and Tests 2 and 4 are each at least 85.
3. Pass if all five scores are at least 75, at least four are at least 80,
the mean is at least 82, and Tests 2 and 4 are each at least 80.
4. Otherwise Marginal. Explain the unmet condition.
This ordering resolves overlaps and gaps in the historical prose rules.
## Reporting
Report all scores and ratings, mean, minimum, maximum, and population variance:
sum((score - mean)^2) / 5. Also count each rating.
This variance describes spread across five different tests, not measurement
uncertainty.
Do not combine different models or configurations into one five-test run.
Across repeated runs, report each run and variability separately.
Judge factual support, reasoning, disagreement, correction, and voice with evidence.
Do not infer real recovery, productivity gains, or permission to release a system
from a passing example suite. Missing inputs mean Not evaluated, not a zero score.
