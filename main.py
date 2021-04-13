# %%
import matplotlib.pyplot as plt
from data import possible_frequencies,possible_rarities
from test_tfidf import TestTFIDF
# %%
plt.rcParams['figure.figsize'] = [12, 5]
testTFIDF = TestTFIDF(possible_frequencies,possible_rarities)
testTFIDF.start_test({ "tf_option": 1, "idf_option": 1 })
testTFIDF.start_test({ "tf_option": 2, "idf_option": 1 })
testTFIDF.start_test({ "tf_option": 2, "idf_option": 2 })
# %%
testTFIDF.draw_graphs()

# %% [markdown]

# %%
