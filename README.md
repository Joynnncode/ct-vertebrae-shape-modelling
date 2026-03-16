# Vertebral CT Landmark Annotation and 3D Shape Modelling Study

A portfolio-ready academic project repository on vertebral landmark annotation, statistical shape modelling, and RFRV-CLM evaluation from CT.

## What this repo is

This is a curated GitHub version of my vertebral modelling project. It is designed to show the parts of the work I can confidently present as my own contribution:

- annotation workflow refinement
- experiment tracking and result curation
- comparative evaluation of model settings
- documentation and public repo packaging

It also makes clear that the original project environment included provided tools and framework components that are **not** claimed here as my own software.

## Project focus

The project investigated vertebral landmark localisation and 3D vertebral shape modelling using CT data. The workflow combined:

- manual vertebral landmark annotation
- multi-round observer comparison and revision
- averaged reference point generation
- statistical shape model construction
- single-stage and two-stage RFRV-CLM fitting
- quantitative evaluation using landmark distance metrics

## Repo structure

```text
.
├── assets/
│   └── figures/
│       ├── annotation/
│       ├── models/
│       └── results/
├── docs/
├── manifests/
├── results/
├── samples/
│   ├── annotations/
│   └── images/
├── scripts/
│   └── analysis/
├── NOTICE.md
└── README.md
```

## What is included

### Documentation
- public-facing project overview
- annotation workflow explanation
- result interpretation notes
- contribution / authorship boundaries
- public repo scope notes

### Results and figures
- annotation revision summary tables
- patch-size sweep tables
- best-model comparison table
- derived GitHub-friendly figures from the uploaded spreadsheets

### Representative sample files
- four averaged `.pts` landmark files
- four linked `.pts.v3i` sample image-volume references

### Selected analysis scripts
- point-comparison scripts
- patch-size comparison scripts
- annotation boxplot script
- single-stage vs two-stage comparison script

## What is intentionally omitted

To keep the repository both professional and ownership-safe, this public version does **not** redistribute:

- provided executable tools
- full binary model folders
- complete raw working directories
- course/supervisor instruction packages
- large private annotation trees

Those materials are described only at a high level in `manifests/` and `docs/public_repo_scope.md`.

## Headline findings

### Annotation refinement
The annotation materials show a genuinely iterative workflow with multiple version folders and observer comparison cycles. The retained summary table suggests that agreement improved after revision.

See:
- `results/annotation_summary.csv`
- `results/annotation_summary_long.csv`
- `assets/figures/annotation/annotation_revision_trends.png`

### Model performance
The public summaries preserve both:
- best reported single-stage setting
- best reported two-stage setting

The two-stage configuration is reported as a modest improvement over the best single-stage result.

See:
- `results/best_model_summary.csv`
- `assets/figures/results/best_model_comparison.png`

### Accuracy / runtime trade-off
The frame-width-50 patch sweep is preserved in a compact CSV and plotted in two ways so the trade-off is easy to explain.

See:
- `results/model_patch_sweep_fw50_detailed.csv`
- `assets/figures/results/patch_size_vs_mean_distance.png`
- `assets/figures/results/accuracy_vs_runtime.png`

## Suggested GitHub description

MSc medical imaging project on vertebral CT landmark annotation, 3D statistical shape modelling, and single-stage / two-stage RFRV-CLM evaluation.

## Suggested GitHub topics

`medical-imaging` `ct` `vertebrae` `statistical-shape-model` `landmark-localisation` `computer-vision` `research-project`

## How to talk about this project in interviews

A safe and accurate summary is:

> I worked on vertebral CT landmark annotation, annotation-quality refinement, experiment tracking, and comparative evaluation for a 3D shape-modelling project, using a provided modelling environment.

That phrasing shows ownership of your real contribution without overstating authorship of external tools.

## Recommended next upgrade

The best future improvement would be to add anonymised annotation-interface screenshots or a small notebook reproducing the summary plots from the CSV files.
