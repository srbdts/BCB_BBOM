# BCB_BBOM

This repository contains some material to illustrate the steps taken to digitise the Biographie Coloniale Belge/Biographie Belge d’Outre-Mer (BCB/BBOM).

The repository is structured as follows:
  - "data" contains the raw ocr transcription of the first volume of the BCB/BBOM, which is our input data. The other volumes of the BCB/BBOM have been processed in the same way.
  - "scripts" contain two jupyter notebooks. One was used to convert the raw OCR of each volume into a json-file with individual records. This script was executed iteratively, each time followed by a manual correction stage in which we had a look at and corrected the OCR file whenever the error log indicated that the page couldn't be processed. These errors included OCR mistakes in the names of the lemmata (in the header or the running text), lack of space between the two columns on the page and lack of space between the header and the body of the text.
  The other one takes this json file as input and tries to extract some metadata (the name of the author and the date of writing) from the records. This directory also contains the python script used to query the resulting corpus and generate the keyword-in-context files that formed the basis of our discourse analysis.
  - "output" contains the eventual corpus of the first volume in json-format, as well as an excel data sheet with keywords-in-context. Some preliminary categorisation has already been carried out on this file, but the analysis is not complete. There exists three more of these files.

