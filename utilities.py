def set_mean(df_to, df_from, idx, column_names):
    for column in column_names:
        df_to.at[idx, column] = df_from[column].mean()

def scale_ratings(df, cols, factor):
    for col in cols:
        df[col] = df[col].apply(lambda x: x*factor)
    return df

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False