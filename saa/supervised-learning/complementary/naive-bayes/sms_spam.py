"""Download the SMS Spam Collection once, and load it as a DataFrame."""

import csv
import io
import urllib.request
import zipfile
from pathlib import Path

import pandas as pd

SOURCE_URL = "https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip"
DATA_FILE = Path(__file__).parent / "data" / "SMSSpamCollection"


def load_sms_spam() -> pd.DataFrame:
    """Return one row per message, with columns `label` ("ham" or "spam") and `message`."""
    if not DATA_FILE.exists():
        DATA_FILE.parent.mkdir(exist_ok=True)
        with urllib.request.urlopen(SOURCE_URL) as response:
            archive = zipfile.ZipFile(io.BytesIO(response.read()))
        DATA_FILE.write_bytes(archive.read("SMSSpamCollection"))
    # The messages contain quotation marks that are not field delimiters, so quoting is switched off.
    return pd.read_csv(DATA_FILE, sep="\t", names=["label", "message"], quoting=csv.QUOTE_NONE, encoding="utf-8")
