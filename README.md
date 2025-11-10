# Data Exploration with Python — Student Grades EDA

A self-contained, beginner-friendly project to explore, clean, visualize, and analyze a tiny **student study-hours vs grade** dataset using **NumPy**, **Pandas**, **Matplotlib**, **SciPy**, and **Scikit‑learn** in **Jupyter**.

---

## 📦 Project Structure

```
python-eda-student-grades/
├── data/                       # Dataset folder (grades.csv will be downloaded here)
├── notebooks/
│   └── 01_eda_student_grades.ipynb   # Main Jupyter Notebook with step-by-step EDA
├── scripts/
│   └── download_data.py        # Helper to download the dataset offline-friendly
├── .gitignore
├── requirements.txt            # Python dependencies
└── README.md                   # This guide
```

---

## ✅ What you'll learn

- Creating and using **NumPy arrays** vs Python lists
- Building **Pandas DataFrames**, indexing with `loc`/`iloc`, filtering and querying
- Handling **missing values**: `fillna`, `dropna`, and detecting outliers
- **Grouping**, **aggregation**, and basic **visualization** with Matplotlib
- Understanding **distributions**, **central tendency**, and **variance**
- **Normalization (MinMax scaling)**, **correlation**, **scatter plots**, and a simple **linear regression**
- Using regression coefficients to make a simple **prediction function**

---

## 🧰 Prerequisites

- **Python 3.10+** (3.8+ generally works too)
- Ability to run **terminal/command prompt** commands
- (Optional) **VS Code** with Python + Jupyter extensions

> The steps below work on Linux, macOS, and Windows (PowerShell).

---

## 🧪 Quickstart (One-time Setup)

1) **Clone or download** this project (or unzip it anywhere).  
2) **Create a virtual environment** (venv) inside the project:

**Linux/macOS:**
```bash
cd python-eda-student-grades
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell):**
```powershell
cd python-eda-student-grades
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3) **Install dependencies**:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4) **(Recommended) Create a Jupyter kernel for this venv** so your notebook uses the correct interpreter:
```bash
python -m ipykernel install --user --name python-eda-student-grades --display-name "Python (EDA: Student Grades)"
```

5) **Download the dataset** (either run the helper or use curl):  
**Option A — Python helper (no external tools needed):**
```bash
python scripts/download_data.py
```
**Option B — curl/wget:**
```bash
curl -o data/grades.csv "https://raw.githubusercontent.com/faizulkhan56/python-eda-discovery/main/grades.csv"
                    
# or
wget -O data/grades.csv "https://raw.githubusercontent.com/faizulkhan56/python-eda-discovery/main/grades.csv"
```

6) **Start Jupyter** and open the notebook:
```bash
jupyter notebook
```
Then open: `notebooks/01_eda_student_grades.ipynb`

---

## 💡 Selecting the Kernel in VS Code or Jupyter

- **VS Code**: Open the notebook → top-right choose **Kernel** → select **"Python (EDA: Student Grades)"**.  
  If you don't see it, run the *Create kernel* step above and reload the window.
- **Classic Jupyter**: In the menu **Kernel → Change kernel** → select **"Python (EDA: Student Grades)"**.

> Why this matters: The kernel must point to your **.venv** so imports like `numpy`, `pandas`, and `matplotlib` work.

---

## ▶️ How to Run the Project

1. Activate your **venv** (see Quickstart step 2).  
2. Ensure `data/grades.csv` exists (run step 5).  
3. Launch Jupyter and run the notebook **cell-by-cell**.  
4. Explore, modify, and re-run to learn!

---

## 📚 Notebook Contents (What’s inside)

The notebook walks through **exactly** these topics (with runnable code):

- **NumPy** arrays vs lists; shapes, indexing, vectorized ops
- **Pandas** DataFrames; `loc`, `iloc`, `query`, filtering
- Loading CSV (`read_csv`) and saving cleaned views
- **Missing value** detection and handling (`isnull`, `fillna`, `dropna`)
- **Exploratory plots**: bar charts, histograms, boxplots, density
- **Descriptive statistics**: min, max, mean, median, mode
- **Outlier handling** via quantiles
- **Variance metrics**: range, variance, standard deviation
- **Normal distribution** intuition with standard deviations (68-95-99.7 rule)
- **Normalization** using `MinMaxScaler`
- **Correlation** and **scatter plot** with **regression line (least squares)**
- **Prediction** using regression coefficients (`y = mx + b`)

---

## 🧹 Common Issues & Fixes

- **Plots don’t display** in Jupyter → ensure `%matplotlib inline` is present or using JupyterLab/VS Code built-in plotting.
- **Import errors** (`ModuleNotFoundError`) → confirm the **correct kernel** is selected and `pip install -r requirements.txt` ran **inside the venv**.
- **Permission errors** on Windows when activating venv → run PowerShell as Administrator:  
  `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

---

## 🗑️ Clean Up

```bash
# Deactivate environment
deactivate

# (Optional) Remove everything created by this project
cd ..
rm -rf python-eda-student-grades
```

---

## 📄 License

This project is provided for educational purposes. Do anything you like—learn, remix, adapt!

---

Happy exploring! 🚀
