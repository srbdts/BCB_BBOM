# BCB_BBOM

This repository contains some material to illustrate the steps taken to digitise the Biographie Coloniale Belge/Biographie Belge d’Outre-Mer (BCB/BBOM).

The repository is structured as follows:
  - "data" contains the raw ocr transcription of the first volume of the BCB/BBOM, which is our input data. The other volumes of the BCB/BBOM have been processed in the same way.
  - "scripts" contain two jupyter notebooks. One was used to convert the raw OCR of each volume into a json-file with individual records. The other one takes this json file as input and tries to extract some metadata (the name of the author and the date of writing) from the records. This directory also contains the python script used to query the resulting corpus and generate the keyword-in-context files that formed the basis of our discourse analysis.
  - "output" contains the eventual corpus of the first volume in json-format, as well as an excel data sheet with keywords-in-context. Some preliminary categorisation has already been carried out on this file, but the analysis is not complete. There exists three more of these files.

