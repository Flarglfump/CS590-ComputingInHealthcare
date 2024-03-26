import urllib.request as rq

result = rq.urlopen("https://www.encodeproject.org/search/?type=Experiment&assay_title=DNase-seq&replicates.library.biosample.donor.organism.scientific_name=Homo+sapiens&biosample_ontology.organ_slims=blood&biosample_ontology.cell_slims=T+cell&assembly=GRCh38&limit=200&files.read_length=101&files.read_length=151")

