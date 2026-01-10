import numpy as np
import pandas as pd

def sanitize_df(df: pd.DataFrame, label_col: str = "Label") -> pd.DataFrame:
    """
    Minimal, SOC-friendly sanitization for CICIDS-2017 flow data.

    What it does:
    - Strips whitespace from column names (CICIDS often has ' Label')
    - Converts infinities to NaN
    - Drops NaN rows
    - Drops duplicates
    - Ensures Label column exists

    This is intentionally minimal:
    We do NOT scale features, encode labels, or perform ML preprocessing here.
    """
    df = df.copy()

    # Normalize CICIDS column names
    df.columns = df.columns.astype(str).str.strip()

    # Replace infinities
    df.replace([np.inf, -np.inf], np.nan, inplace=True)

    # Drop missing rows
    df.dropna(inplace=True)

    # Drop exact duplicates
    df.drop_duplicates(inplace=True)

    # Validate Label presence
    if label_col not in df.columns:
        raise ValueError(
            f"Expected label column '{label_col}' not found.\n"
            f"Columns sample: {df.columns.tolist()[:30]}"
        )

    return df
