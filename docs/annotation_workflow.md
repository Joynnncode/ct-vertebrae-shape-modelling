# Annotation workflow

The annotation process evolved through multiple revision folders rather than a single pass.

## Observed workflow structure

The uploaded project materials show:

- versioned annotation directories (`version1` to `version8(avg4)`)
- separate observer-labelled point folders
- intermediate averaged point folders (`avg2`, `avg4`)
- comparison scripts for per-point and per-image distance analysis

## Publicly retained evidence in this repo

To keep the GitHub version reviewable and ownership-safe, this repo keeps:

- summary CSV files instead of the full annotation tree
- four representative averaged `.pts` examples
- analysis scripts used to compare annotation revisions
- a revision-trend figure derived from the summary spreadsheet

## What the version labels suggest

A reasonable interpretation of the folder structure is:

1. initial independent annotations were created
2. observer disagreement was measured
3. annotations were revised through multiple rounds
4. averaged point sets were generated for downstream modelling

That process is one of the most important parts of the project because it demonstrates data-quality improvement before model fitting.
