# Proposed robotic crown-preparation benchmark

**Status:** research proposal, not validated dataset or clinical system.

## Aim
Evaluate whether autonomous or supervised robotic toolpaths can reproduce a planned full-crown preparation on standardized 3D tooth models under safety constraints.

## Minimum dataset
Paired preoperative tooth mesh, target preparation mesh, coordinate frame, tooth identity, bur geometry, planned trajectory, executed trajectory, and ground-truth surface registration. Keep train/test subjects disjoint.

## Endpoints
- RMS and 95th-percentile surface distance in mm
- Finish-line deviation in mm
- Occlusal and axial reduction errors in mm
- Taper / total occlusal convergence in degrees
- Undercut and collision incidence
- Cutting force/torque when measured
- Procedure time and failure/abort rate

## Baselines
Conventional manually planned trajectory; conventional motion planner; AI-assisted planner. Compare on the same cases and report uncertainty.

## Reproducibility
Document coordinate transforms, registration method, tolerances, simulation physics assumptions, random seeds, compute environment, and failed cases. Do not present simulation-only performance as clinical safety evidence.
