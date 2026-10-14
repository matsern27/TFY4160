import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

SIGMA = 10.0   # standardavvik i Hz (bruk np.sqrt(10.0) hvis varians = 10 Hz^2)
SEED = 42      # samme seed som før, så node1 gir samme støyverdier som tidligere
rng = np.random.default_rng(SEED)

df = pd.read_csv("noice.csv")
nodes = ["node1", "node2", "node3"]
