# A simple machine learning project using scikit learn
A sample programs to extract information from web pages.

Features:
- WebScrapping using request
- WebScrapping using Beautiful Soup

## Installing using GitHub
- Fork the project into your GitHub
- Clone it into your dektop
```
git clone https://github.com/jacesca/WebScrapping.git
```
- Setup environment (it requires python3)
```
python -m venv venv
source venv/bin/activate  # for Unix-based system
venv\Scripts\activate  # for Windows
```
- Install requirements
```
pip install -r requirements.txt
```

## Run ML model
```
python web-scrapping.py
python web-scrapping-bs4.py
```

## Others
- Proyect in GitHub: https://github.com/jacesca/WebScrapping
- Commands to save the environment requirements:
```
conda list -e > requirements.txt
# or
pip freeze > requirements.txt

conda env export > env.yml
```
- For coding style
```
black model.py
flake8 model.py
```

## Extra documentation
None
