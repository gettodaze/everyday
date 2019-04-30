import gzip
import shutil
inpath = "C:/Users\John\Downloads\c_elegans.canonical_bioproject.current.annotations (1).gff3.gz"
outpath = "C:/Users\John\Downloads\c_elegans.canonical_bioproject.current.annotations (1).gff3"
with gzip.open(inpath, 'rb') as f_in:
    with open(outpath, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
