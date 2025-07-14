import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def extract_data(file_path):
    df = pd.read_csv(file_path, encoding= 'latin1')
    print("Data Extracted Successfully.")
    return df

def transform_data(df):
    X = df.drop('STATUS', axis=1)
    y = df['STATUS']

    numeric_features = X.select_dtypes(include=['int64', 'float64']).columns
    categorical_features = X.select_dtypes(include=['object']).columns

    numeric_pipeline = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])

    categorical_pipeline = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoder', OneHotEncoder(handle_unknown='ignore'))
    ])

    preprocessor = ColumnTransformer(transformers=[
        ('num', numeric_pipeline, numeric_features),
        ('cat', categorical_pipeline, categorical_features)
    ])

    X_transformed = preprocessor.fit_transform(X)
    feature_names = preprocessor.get_feature_names_out()
    print(feature_names)

    print("Data Transformed Successfully.")
    return X_transformed, y, preprocessor

def load_data(X, y, output_file='processed_data2.csv'):
    X_df = pd.DataFrame(X.toarray() if hasattr(X, "toarray") else X)
    X_df['target'] = y.reset_index(drop=True)
    X_df.to_csv(output_file, index=False)
    print(f"Transformed Data Loaded and Saved to {output_file}.")

def main():
    input_file = 'sales_data_sample1.csv'  
    df = extract_data(input_file)
    X_transformed, y, _ = transform_data(df)
    load_data(X_transformed, y)

if __name__ == "__main__":
    main()