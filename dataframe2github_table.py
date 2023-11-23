def dataframe2github(df):
    print('|', ' | '.join(df.columns), '|')
    print('|-----'*len(df.columns),'|')
    def round_float(value, decimals=6):
        try:
            return round(value, decimals)
        except:
            return value
    np=df.apply(round_float).astype(str).to_numpy()
    for val in np:
        print('|', ' | '.join(val), '|')
