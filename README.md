# DATA-PIPELINE-DEVELOPMENT

🧪 ETL Pipeline using Pandas & Scikit-Learn
This project performs a basic ETL (Extract, Transform, Load) process on a CSV dataset using Python libraries.

🔁 ETL Workflow
1. Extract
Reads data from sales_data_sample1.csv using pandas.read_csv() with 'latin1' encoding.

2. Transform
Splits features (X) and target (y) where STATUS is the target.

Applies preprocessing:

Numerical Columns:

Imputes missing values using the mean.

Scales features with StandardScaler.

Categorical Columns:

Imputes missing values with the most frequent value.

Encodes categories using OneHotEncoder.

3. Load
Transformed data is converted back into a DataFrame.

Target column is added back.

Saves final processed data to processed_data2.csv.
