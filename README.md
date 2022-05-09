# DataVisTutorial
Jupyter notebooks for a python data visualisation tutorial

The pdfs slides are in the repository for future look up of the references and links therein. To run the notebooks, you will need to install the necessary packages. I recommend setting up a new conda environment to contain your visualization packages:

```bash
conda create -n scivis python=3.9
conda activate scivis
conda install numpy pandas matplotlib seaborn bokeh
conda install -c plotly plotly=5.7.0
conda install -c conda-forge cmocean
conda install "jupyterlab>=3" "ipywidgets>=7.6"
conda install -c conda-forge -c plotly jupyter-dash

```
then, launch your JupyterLab with
```bash
jupyter-lab
```

There are three main notebooks:
1. `scatterPlots.ipynb`: Creates some example data spread randomly along some trend line split into different subsets. Shows some different options and problems for visualizations.
2. `colorMapNotebook.ipynb`: Makes several types of artifical images and compares different color maps and how specific colormaps may induce artifacts.
3. `plottingLibraries.ipynb`: A simple notebook which reproduces some plots using different packages to highlight how they are different and what they can include.
