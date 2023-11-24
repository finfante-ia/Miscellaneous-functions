# Transform a dataframe to a table format so it can be copied in github and another sites.
#
#Example:
#
#| Dummie | Accuracy | R2 | MSE | MAE |
#|-----|-----|-----|-----|----- |
#| FUELTYPE_D | 474.4 | 0.828225 | 474.4 | 12.8 |
#| FUELTYPE_E | 73.923077 | 0.981241 | 73.923077 | 3.923077 |
#| FUELTYPE_X | 1.118644 | 0.999754 | 1.118644 | 0.288136 |
#| FUELTYPE_Z | 4.230769 | 0.99902 | 4.230769 | 0.512821 |
#| Total | 17.733645 | 0.99617 | 17.733645 | 0.883178 |
#
#
#

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
