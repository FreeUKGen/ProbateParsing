# Probate-Parsing
Probate Parsing as a GSoC Student for Free UK Genealogy. Refer to the [wiki](https://github.com/FreeUKGen/ProbateParsing/wiki).

Free UK Genealogy aims to launch a new project to expose genealogical information from wills and probate books. These books record the date and location of people's deaths, their occupations, and often the same information about the family members that executed the wills.

In previous projects, all this material was transcribed manually by volunteers, as the source documents were handwritten. The probate books are different, however, in that they are printed and thus are accessible to OCR. We should be able to use OCR text to seed a database by parsing the text for names, dates, occupations, and relationships. We should also be able to use OCR bounding box coordinates to associate regions of a scanned page with an entry for presentation to researchers or for correction by volunteers.

Tools for OCR and parsing of probate books to be loaded into the MyopicVicar search engine.

## Features
**[Bounding Box](../master/Bounding_Boxes)**
In phase 1, the scanned images of probate books are refined using Image Processing methods. For example, one page in a probate book consists of many entries. The aim of this phase is to isolate each entry by cropping the original image entry-wise to get the best possible output owing to some OCR discrepancies.

**[Optical Character Recognition](../master/OCR)**
In phase 2, the cropped images of the probate books are parsed under an Optical Character Recognition algorithm to generate the information in text.

**[Named Entity Recognition](../master/NER)**
One of the most challenging parts of the project involves extracting meaningful information from the text generated in Phase 2. For the algorithm to extract particular fields like name, relationships and occupation, it must “learn” the semantics of each probate entry. Methods that tackle such problems form an integral part of Natural Language Processing.
