#!/usr/bin/env python3

import requests
import pandas as pd
from tqdm.auto import tqdm
import os

df = pd.read_csv("country_calendar_metadata.csv")
for link in tqdm(df.link):
  link = link.replace("?download=1", "")
  filename = os.path.basename(link)
  print(filename)
  resp = requests.get(link)
  with open(filename, "wb") as f:
    f.write(resp.content)