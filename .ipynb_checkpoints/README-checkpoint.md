## File Structures
```
.
├── dashboard
│   ├── dashboard.py
│   └── function.py
│   └── main_data.csv
├── data
│   ├── day.csv
│   └── hour.csv
|   └── Readme.txt
├── README.md
├── Proyek_Analisis_Data.ipynb
└── requirements.txt
```

## Project Dataset
[Bike Sharing Dataset](https://drive.google.com/file/d/1RaBmV6Q6FYWU4HWZs80Suqd7KQC34diQ/view?usp=sharing)

## Setup Environtment
- Install Visual Studio Code or any other source code editor
- If using conda, execute this command on your Command Promp
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install numpy pandas matplotlib seaborn jupyter streamlit
```
- If using pipenv, execute this command on your Command Promp
```
pipenv install
pipenv shell
pip install numpy pandas matplotlib seaborn jupyter streamlit
jupyter-notebook .
```