# DS.v2.5.2.2.5
# Module 2: Data Analysis v2.5

## Sprint 2: Analyzing A/B Tests

### Overview

This project aims to analyze two different datasets:<br/>
- **Fast Food Marketing Campaign:** A fast-food chain plans to add a new item to its menu. However, they are still undecided between three possible marketing campaigns for promoting the new product. In order to determine which promotion has the greatest effect on sales, the new item is introduced at locations in several randomly selected markets. A different promotion is used at each location, and the weekly sales of the new item are recorded for the first four weeks.<br/>
  
- **Mobile Games - Cookie Cats:** Cookie Cats is a hugely popular mobile puzzle game developed by Tactile Entertainment. The goal is to examine what happens when the first gate in the game was moved from level 30 to level 40. When a player installed the game, he or she was randomly assigned to either gate_30 or gate_40.

### Installation

For the installation purposes and guidance, this project is structured as described below:
| File                                                    | Folder Path                           |  Context                                                     |
| ----------------------------------| --------------------|------------------------------------------------------------------------------------------------------------------|
| _`wa_market_analysis.ipynb`_      | _`analytical/`_     | Main jupyter notebook with the project analysis for the Fast Food Marketing Campaign                             |
| _`cookie_cats_analysis.ipynb`_    | _`analytical/`_     | Main jupyter notebook with the project analysis for the Mobile Games - Cookie Cats                               |
| _`functions.py`_                  | _`analytical/assets/utils/`_        | Python file to store the functions to be used in this project                        |

### Project Dataset

The original dataset for Fast Food Marketing Campaign can be found [here](https://www.kaggle.com/datasets/chebotinaa/fast-food-marketing-campaign-ab-test).

The original dataset for Mobile Games - Cookie Cats can be found [here](https://www.kaggle.com/datasets/mursideyarkin/mobile-games-ab-testing-cookie-cats/data).

### Looker Dashboard
As part of the project, a Looker Dashboard was created to visualize the data and insights. The dashboard can be accessed [here](https://lookerstudio.google.com/reporting/cccfc4e2-f8a2-4427-b929-38fe33434274/page/cmC4D/edit).

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
