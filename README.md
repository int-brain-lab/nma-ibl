# IBL pipeline access for Neuromatch Academy workshop


This package serves as a mini enviroment to interact with the public database of [International Brain Laboratory](https://internationalbrainlab.org) (IBL), as the resource for one of the projects for [Neuromatch Academy workshop 2020](https://www.neuromatchacademy.org/).

## Access to the IBL public data pipeline
**PLEASE READ** If you are a NMA student in a group working on the IBL data pipeline for your project, please contact your TA for a dedicated access information specifically for the project purpose, and refrain from using the link below to obtain your data pipeline access!

As part of the Neuromatch Academy course material, we have prepared a dedicated access to IBL public data pipeline for those interested in exploring the data. Please visit and register your email at [DataJoint.io NMA Public Access](https://datajoint.io/events/nma-ibl-public) to receive the access credentials needed to run the notebooks.


## Tutorial notebooks
There are a total of 3 tutorial notebooks stepping through with examples on how to navigate and access the IBL data pipeline. You can also click on the Colab link to run the notebook in [Google Colab](https://colab.research.google.com/)

1. Explore IBL behavior data pipeline [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/int-brain-lab/nma-ibl/blob/master/01-Explore%20IBL%20behavior%20data%20pipeline.ipynb)
2. Plot Psychometric curve [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/int-brain-lab/nma-ibl/blob/master/02-Plot%20Psychometric%20curve.ipynb)
3. Replication of paper figures [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/int-brain-lab/nma-ibl/blob/master/03-Replication%20of%20paper%20figures.ipynb)

## IBL and DataJoint
The [International Brain Laboratory](https://internationalbrainlab.org) is a team of systems and computational neuroscientists, working collaboratively to understand the computations that support decision-making in the brain. IBL public database contains data from a standardized training pipeline, implemented across 9 labs of 7 institutions. Mice learn to make decisions that combine incoming visual evidence with internal beliefs about the dynamic structure of the environment. The contents of the current public reflects data used in the recent [preprint](https://www.biorxiv.org/content/10.1101/2020.01.17.909838v2) published by IBL. The [IBL Data Portal](https://data.internationalbrainlab.org/) provides a interative environment to navigate and visualize the data.

The IBL public database, data pipeline, and the data visualizer are operated by [DataJoint](https://datajoint.io). DataJoint is a general data pipeline framework offered in Python & MATLAB, that allows users to interact with a relational database (e.g. MySQL) intuitively and efficiently. Among many features, it offers a way to develop data pipelines with built-in integrity and consistency checks, and provides facility to define tables for computations with tools to quickly parallelize the processing over multiple computers! To learn more, please visit the website [DataJoint.io](https://datajoint.io). There you will find links to our interactive playgrounds and tutorials.

## Contents of the repository
- Package `nma-ibl`: this is a minimal module to access the database. The package could also be installed with pip: `pip install nma-ibl`.

- Three notebooks to explore the IBL pipeline and replicate Figure 2 of the [IBL preprint](https://www.biorxiv.org/content/10.1101/2020.01.17.909838v2) on the standardized behavior.
