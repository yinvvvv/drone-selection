import pandas as pd

def get_drones(csv_path):
    df = pd.read_csv(csv_path, header=None)
    df = df.fillna('')
    df.columns = df.iloc[0]
    df = df.drop(0)
    df = df.set_index(df.columns[0])
    df = df.transpose()
    df = df.reset_index(drop=False)
    df.rename(columns={df.columns[0]: 'name'}, inplace=True)
    df['name'] = df['name'].astype(str).str.strip()
    df.columns = [str(col).strip().lower().replace(' ', '_').replace('(', '').replace(')', '') for col in df.columns]
    drones = df.to_dict(orient='records')
    return drones