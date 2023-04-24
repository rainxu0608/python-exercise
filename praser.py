from Bio import Medline
import pandas as pd
from tqdm import tqdm

alldata = []
with open("pubmed-medullobla-set.txt",encoding = "utf-8") as f:
	pmids = Medline.parse(f)
	for pmid in pmids:
		try:
			pid = pmid["PMID"]
		except:
			pid = ""
		try:
			title = pmid["TI"]
		except:
			title = ""
		try:
			Abstract = pmid["AB"]
		except:
			title = ""
		dic = {
			"PMID":pid,
			"Title":title,
			"Abstract":Abstract
			}
		alldata.append(dic)

df = pd.DataFrame(alldata)
df.to_csv("output.csv",index = False)
print("finished")


