# DS.v3.2.3.4
# Module 2: Data Analysis v2.5

## Sprint 3: Project -> Regression

### Overview

This project aims to analyze the winequality-red dataset, which contains quemical information after wine quality analysis and the goal to apply initial concepts of regression analysis.

### Installation

For the installation purposes and guidance, this project is structured as described below:
| File                                                    | Folder Path                           |  Context                                                     |
| ----------------------------------| --------------------|------------------------------------------------------------------------------------------------------------------|
| _`wine_quality_analysis.ipynb`_      | _`analytical/`_     | Main jupyter notebook with the project analysis for the wine dataset provided                             |
| _`functions.py`_                  | _`analytical/assets/utils/`_        | Python file to store the functions to be used in this project                        |

### Project Dataset

The original dataset for Red Wine Quality can be found [here](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009).

### Dataset Structure
| Column  | Description | Datatype | Count |
|--|--|--|--|
| fixed acidity         | most acids involved with wine or fixed or nonvolatile (do not evaporate readily) | float64 | 1599 |
| volatile acidity      | the amount of acetic acid in wine, which at too high of levels can lead to an unpleasant, vinegar taste | float64 | 1599 |
| citric acid           | found in small quantities, citric acid can add 'freshness' and flavor to wines | float64 | 1599 |
| residual sugar        | the amount of sugar remaining after fermentation stops, it's rare to find wines with less than 1 gram/liter and wines with greater than 45 grams/liter are considered sweet | float64 | 1599 |
| chlorides             | the amount of salt in the wine | float64 | 1599 |
| free sulfur dioxide   | the free form of SO2 exists in equilibrium between molecular SO2 (as a dissolved gas) and bisulfite ion; it prevents microbial growth and the oxidation of wine. | float64 | 1599 |
| total sulfur dioxide  | amount of free and bound forms of S02; in low concentrations, SO2 is mostly undetectable in wine, but at free SO2 concentrations over 50 ppm, SO2 becomes evident in the nose and taste of wine | float64 | 1599 |
| density               | the density of wine is close to that of water depending on the percent alcohol and sugar content | float64 | 1599 |
| pH                    | describes how acidic or basic a wine is on a scale from 0 (very acidic) to 14 (very basic); most wines are between 3-4 on the pH scale | float64 | 1599 |
| sulphates             | a wine additive which can contribute to sulfur dioxide gas (S02) levels, wich acts as an antimicrobial and antioxidant | float64 | 1599 |
| alcohol               | the percent alcohol content of the wine | float64 | 1599 |

**Output variable (based on sensory data):**
| Column  | Description | Datatype | Count |
|--|--|--|--|
| quality               | output variable (based on sensory data, score between 0 and 10) | int64 | 1599 |

### Usage

To use this notebook, you can download it and open it with Jupyter Notebook website, or from your IDE, you can install the Jupyter notebook extension and open it from there.

- Important to remember: 
  - Upload the the jupyter notebook files and place them into the _"analytical"_ folder.
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
