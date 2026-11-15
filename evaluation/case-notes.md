# Case-specific evaluation notes

Use the same complete paper and declared reading resources for independent repetitions. The current evaluator includes supplied reference texts by default and uses the current no-repair reviewer prompt for every case. The notes below explain differences in the published reports.

## 008: supporting reference and continued review

[Example 008](../examples/008/README.md) supplies the complete Bennett–Bohman paper in [paper/references/](../examples/008/paper/references/README.md). Its initial medium review received the manuscript alone. The supplemented medium report continued the same context with this public reference; the six high, xhigh and ultra reviews used fresh contexts with the reference.

The two medium reports therefore count as two report records from one context. When comparing independent contexts, use the continuation as that context's final report. A new `--repeats 2` run creates two independent requests and does not reproduce that continuation.

The default evaluator includes the reference's complete extracted text. `--references omit` selects the manuscript-only text condition.

## 010: reviewer instruction

In [example 010](../examples/010/README.md), `reviewer_high_02.md`, `reviewer_xhigh_02.md`, both ultra reports and both max reports used the explicit instruction to assess the printed proof without adding assumptions, completing missing arguments or supplying a repaired proof. The medium, first high and first xhigh reports used the earlier reviewer instruction.

All new evaluator runs use [the current reviewer prompt](../protocol/reviewer-template.txt), including this no-repair instruction. Compare reports using both their effort and their supplied instruction. The case page records target detection independently of the overall verdict.

## 011: five public references

[Example 011](../examples/011/README.md) supplies Bei16, FK01, HY18, RS22 and Xu20 in [paper/references/](../examples/011/paper/references/README.md). The published baseline, medium review and six high/xhigh/ultra repetitions received this same complete packet. The medium review was completed within one continued context.

The default evaluator includes all five extracted reference texts. `--references omit` selects a different input condition. The reference README identifies the exact versions and attribution.
