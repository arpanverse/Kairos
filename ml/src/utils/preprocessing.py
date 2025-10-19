def clean_data(data):
    # Implement data cleaning logic here
    cleaned_data = data.dropna()  # Example: drop missing values
    return cleaned_data

def normalize_data(data):
    # Implement data normalization logic here
    normalized_data = (data - data.mean()) / data.std()  # Example: standard normalization
    return normalized_data

def split_data(data, test_size=0.2):
    # Implement data splitting logic here
    from sklearn.model_selection import train_test_split
    train_data, test_data = train_test_split(data, test_size=test_size)
    return train_data, test_data