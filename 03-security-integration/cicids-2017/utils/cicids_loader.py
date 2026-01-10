from pathlib import Path
from typing import List, Optional
import pandas as pd

DEFAULT_FILES = [
    "Monday-WorkingHours.pcap_ISCX.csv",
    "Tuesday-WorkingHours.pcap_ISCX.csv",
    "Wednesday-workingHours.pcap_ISCX.csv",
    "Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv",
    "Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv",
    "Friday-WorkingHours-Morning.pcap_ISCX.csv",
    "Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv",
    "Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv",
]

def load_cicids_multi(
    raw_dir: Optional[str] = None,
    files: Optional[List[str]] = None,
    usecols: Optional[List[str]] = None,
    sample_per_file: Optional[int] = None,
    label_filter: Optional[List[str]] = None,
    random_state: int = 42
) -> pd.DataFrame:
    """
    Load CICIDS-2017 from multiple raw CSV files without creating one huge merged file.

    Key Fix:
    - CICIDS column names often contain leading/trailing spaces (e.g., " Label")
      so we normalize via df.columns.str.strip().

    Parameters
    ----------
    raw_dir : Optional[str]
        Optional path override for raw data dir.
    files : Optional[List[str]]
        Specific file list. If None, uses DEFAULT_FILES.
    usecols : Optional[List[str]]
        Restrict columns to save memory.
    sample_per_file : Optional[int]
        Randomly sample N rows from each file.
    label_filter : Optional[List[str]]
        Keep only these labels.
    random_state : int
        Seed for reproducible sampling.

    Returns
    -------
    pd.DataFrame
        Combined dataframe.
    """
    project_root = Path(__file__).resolve().parents[1]  # phase-3.5-soc-detection/
    data_root = project_root / "data" / "raw" if raw_dir is None else Path(raw_dir)

    if not data_root.exists():
        raise FileNotFoundError(
            f"Raw CICIDS folder not found: {data_root}\n"
            f"Create folder: {project_root / 'data' / 'raw'} and place CICIDS CSV files inside."
        )

    target_files = files if files is not None else DEFAULT_FILES

    frames = []
    for fname in target_files:
        fpath = data_root / fname
        if not fpath.exists():
            raise FileNotFoundError(f"Missing CICIDS file: {fpath}")

        df = pd.read_csv(fpath, usecols=usecols, low_memory=False)

        # ✅ CICIDS fix: strip whitespace from column names
        df.columns = df.columns.str.strip()

        # standardize label column
        label_candidates = ["Label", "label", "Class", "class"]
        label_col = None
        for c in label_candidates:
            if c in df.columns:
                label_col = c
                break

        if label_col is None:
            raise ValueError(
                f"No label column found in: {fname}\n"
                f"Available columns sample: {df.columns.tolist()[:25]}"
            )

        if label_col != "Label":
            df = df.rename(columns={label_col: "Label"})

        # filter labels
        if label_filter is not None:
            df = df[df["Label"].isin(label_filter)]

        # sample per file
        if sample_per_file is not None and len(df) > sample_per_file:
            df = df.sample(n=sample_per_file, random_state=random_state)

        frames.append(df)

    combined = pd.concat(frames, ignore_index=True)
    return combined
