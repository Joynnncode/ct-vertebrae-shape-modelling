# Results summary

## Annotation agreement

`results/annotation_summary.csv` preserves the headline agreement statistics across version revisions. The trend is broadly consistent with annotation refinement reducing mean distance relative to earlier versions.

## Model comparison

`results/best_model_summary.csv` keeps the two headline configurations:

- best reported single-stage model
- best reported two-stage model

The difference is modest, but the two-stage configuration is reported as slightly better on final mean distance.

## Patch-size sweep

`results/model_patch_sweep_fw50_detailed.csv` preserves the patch-size sweep for frame width 50, including:

- final mean distance
- standard error
- standard deviation
- median
- percentile metrics
- average search time

This makes it possible to discuss both localisation accuracy and runtime trade-offs in interviews or on GitHub.
