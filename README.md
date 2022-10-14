# Spaced Repetition Flashcards

## Downloading the code

To download the code, run the following command in your terminal:

```bash
git clone https://github.com/mc1ovins/spaced-repetition.git
# This will create a folder called Spaced-Repetition in your current directory
cd Spaced-Repetition
```

## Dependencies

Before you can run and edit this project, you'll need to install its dependencies. It is strongly recommended that you use a virtual environment like conda or venv to manage your dependencies.

Example with venv (RECOMMENDED):

```bash
# Run this command in your terminal to create a virtual environment
python3 -m venv spaced-repetition
# Mac/Linux activation
source spaced-repetition/bin/activate
# Windows activation
 .\spaced-repetition\Scripts\activate.bat
```

Example with conda (Ignore if you are using venv):

```bash
conda create -n spaced-repetition python=3.10
# Activate the virtual environment
conda activate spaced-repetition
```

Once you are on a virtual environment, run the following command in your terminal to install the dependencies:

```bash
# Using pip 21.2.4
# You may need to use pip3 instead of pip
pip install -r requirements.txt
```

## Running the Project

To run the project, you'll need to run the following command on the project root:

```bash
# Using Python 3.9.12
# You may need to use python3 instead of python
python main.py
```
