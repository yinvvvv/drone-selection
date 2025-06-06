def load_data(file_path):
    """
    Load the drone dataset from the CSV file.
    """
    data = pd.read_csv(file_path)
    return data
