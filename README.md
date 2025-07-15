# DATA-PIPELINE-DEVELOPMENT

# 🧪 ETL Process on Sales Data using Pandas & Scikit-Learn

This project performs a complete ETL (Extract, Transform, Load) process on a sales dataset using Python libraries **Pandas** and **Scikit-Learn**.

---

## 🎯 Objective

Preprocess raw sales data by:

- Handling missing values  
- Scaling numerical features  
- Encoding categorical features  
- Exporting the cleaned dataset for further use (e.g., machine learning)

---

## 📁 Input Data

Input is read from a CSV file: `sales_data_sample1.csv`

- The dataset contains both numeric and categorical columns.
- The target column is: `STATUS`

---

## 🧠 What This Project Does

1. **Extracts Data**  
   - Reads the CSV file into a pandas DataFrame using `latin1` encoding.

2. **Transforms Data**  
   - Splits features (`X`) and target (`y`)
   - Identifies numeric and categorical columns
   - Applies:
     - **Mean imputation** and **StandardScaler** for numeric columns  
     - **Most frequent imputation** and **OneHotEncoder** for categorical columns
   - Uses `ColumnTransformer` and `Pipeline` to process the data

3. **Loads Data**  
   - Combines transformed features and the target column
   - Saves the final dataset to `processed_data2.csv`

---

## ✅ Sample Output

```python
['num__Feature1', 'num__Feature2', ..., 'cat__Country_US', 'cat__Country_UK']
Data Transformed Successfully.
Transformed Data Loaded and Saved to processed_data2.csv.

