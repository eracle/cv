# Directory Overview

This directory contains the source for a curriculum vitae. The main data is stored in `resume.yaml` and is used to generate the `CV_latest.pdf` file.

# Key Files

*   `resume.yaml`: The single source of truth for the CV. It contains all the information about work experience, education, skills, etc. in a structured YAML format.
*   `CV_latest.pdf`: The latest generated PDF version of the CV.
*   `.gitignore`: Ignores the `.idea/` directory.

# Usage

To update the CV, edit the `resume.yaml` file. A CI/CD pipeline or a local script is likely used to generate the `CV_latest.pdf` from the `resume.yaml` file.
