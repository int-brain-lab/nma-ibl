# IBL pipeline access for Neuromatch Academy workshop


This package serves as a mini enviroment to interact with the public database of [International Brain Laboratory](https://internationalbrainlab.org) (IBL), as the resource of one of the projects for [Neurmatch Academy workshop 2020](https://www.neuromatchacademy.org/).


## IBL and DataJoint
The [International Brain Laboratory](https://internationalbrainlab.org) is a team of systems and computational neuroscientists, working collaboratively to understand the computations that support decision-making in the brain. IBL public database contains data from a standardized training pipeline, implemented across 9 labs of 7 institutions. Mice learn to make decisions that combine incoming visual evidence with internal beliefs about the dynamic structure of the environment. The contents of the current public reflects data used in the recent [preprint](https://www.biorxiv.org/content/10.1101/2020.01.17.909838v2) published by IBL. The [IBL Data Portal](https://data.internationalbrainlab.org/) provides a interative environment to navigate and visualize the data.

The IBL public database, data pipeline, and the data visualizer are operated by [DataJoint](https://datajoint.io). DataJoint is a general data pipeline framework offered in Python & MATLAB, that allows users to interact with a relational database (e.g. MySQL) intuitively and efficiently. Among many features, it offers a way to develop data pipelines with built-in integrity and consistency checks, and provides facility to define tables for computations with tools to quickly parallelize the processing over multiple computers! To learn more, please visit the website [DataJoint.io](https://datajoint.io). There you will find links to our interactive playgrounds and tutorials.

## Contents of the repository
- Package `nma-ibl`: this is a minimal module to access the database. The package could also be installed with pip: `pip install nma-ibl`.

- Three notebooks to explore the IBL pipeline and replicate Figure 2 of the [IBL preprint](https://www.biorxiv.org/content/10.1101/2020.01.17.909838v2) on the standardized behavior.
