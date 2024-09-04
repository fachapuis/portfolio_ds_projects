# DS.v2.5.2.1.5
# Module 2: Data Analysis v2.5

## Sprint 1: Mental Health in the Tech Industry

### Overview

According to the https://www.theceomagazine.com/opinion/mental-health-tech-industry/, the COVID-19 pandemic has significantly increased the focus on mental health, especially in the technology sector, which already experiences high rates of depression among its employees. A study by the British Interactive Media Association in the UK found that tech industry workers are five times more likely to be depressed compared to the general population, with 52% having experienced anxiety or depression. The tech industry, highly populated in the digital age, employed over 53.2 million full-time workers in 2019, with this number expected to reach 62 million this year.

### Installation

For the installation purposes and guidance, this project is structured as described below:
| File                                                    | Folder Path                           |  Context                                                                                      |
| ----------------------------------------------| -----------------------------------|---------------------------------------------------------------------------------------------------------|
| _`eda.ipynb`_                                 | _`analytical/`_                    | Main jupyter notebook with the project analysis                                                         |
| _`functions.py`_                              | _`analytical/assets/utils/`_        | Python file to store the functions to be used in this project                                           |


### Project Dataset

The original dataset can be found [here](https://www.kaggle.com/datasets/anth7310/mental-health-in-the-tech-industry/code).


### Usage

To use this notebook, you can download it and open it with Jupyter Notebook website, or from your IDE, you can install the Jupyter notebook extension and open it from there.

- Important to remember: 
  - Upload the _"eda.ipynb"_ file and place it into the _"analytical"_ folder.
  - Upload the _"functions.py"_ file and placed it into the _"analytical/assets/utils/"_ folder.

### Requirements

To proper use this notebook, please install the requirements from the route path, executing the command line as below:

```bash
pip install -r requirements.txt
```

### Dependencies

Also, some functions were developed for code reusability, efficiency and optimization.</br>
To host these functions, a `functions.py` file is used and stored in the `analytical/assets/utils/` path, as already mentioned on the Usage part.</br>

### Code checking

To proper adjust code to be compliant with PEP8, the [pycodestyle_magic](https://github.com/mattijn/pycodestyle_magic?tab=readme-ov-file) was used. To install it, run the following command:

```bash
pip install flake8 pycodestyle_magic
```

### Contributing

Feel free to contribute with comments and suggestions to this project.
