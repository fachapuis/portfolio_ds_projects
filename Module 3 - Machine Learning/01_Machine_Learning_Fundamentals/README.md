# DS.v3.3.1.5

# Module 3: Machine Learning

## Sprint 1: Project -> Supervised Machine Learning Fundamentals

### Overview

The goal of this analysis is to predict whether a customer will purchase travel insurance based on their demographic and behavioral data. This analysis will involve data cleaning, exploratory data analysis (EDA), statistical inference, and building supervised machine learning models.

### Installation

For the installation purposes and guidance, this project is structured as described below:
| File                                                    | Folder Path                           |  Context                                                     |
| ----------------------------------| --------------------|------------------------------------------------------------------------------------------------------------------|
| _`travel_insurance_analysis.ipynb`_      | _`analytical/`_     | Main jupyter notebook with the project analysis for the wine dataset provided                             |
| _`functions.py`_                  | _`analytical/assets/utils/`_        | Python file to store the functions to be used in this project                        |

### Project Dataset

The original dataset used for this project can be found [here](https://www.kaggle.com/datasets/tejashvi14/travel-insurance-prediction-data).

### Dataset Structure
 Column  | Description | Datatype | Count |
|--|--|--|--|
| Age                   | Age Of The Customer | int64 | 1987 |
| Employment Type       | The Sector In Which Customer Is Employed  | object | 1987 |
| GraduateOrNot         | Whether The Customer Is College Graduate Or Not | object | 1987 |
| AnnualIncome          | The Yearly Income Of The Customer In Indian Rupees[Rounded To Nearest 50 Thousand Rupees]  | int64 | 1987 |
| FamilyMembers         | Number Of Members In Customer's Family  | int64 | 1987 |
| ChronicDiseases       | Whether The Customer Suffers From Any Major Disease Or Conditions Like Diabetes/High BP or Asthama,etc.  | int64 | 1987 |
| FrequentFlyer         | Derived Data Based On Customer's History Of Booking Air Tickets On Atleast 4 Different Instances In The Last 2 Years[2017-2019]  | object | 1987 |
| EverTravelledAbroad   | Has The Customer Ever Travelled To A Foreign Country[Not Necessarily Using The Company's Services]  | object | 1987 |

**Target variable:**
| Column  | Description | Datatype | Count |
|--|--|--|--|
| TravelInsurance       | Did The Customer Buy Travel Insurance Package During Introductory Offering Held In The Year 2019 | int64 | 1987 |

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