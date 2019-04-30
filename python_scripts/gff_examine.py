# import pprint
# from BCBio.GFF import GFFExaminer
#
# in_file = "C:/Users\John\Documents\School\Kimble Lab\c_elegans.canonical_bioproject.current.annotations (1).gff3"
# examiner = GFFExaminer()
# in_handle = open(in_file)
# pprint.pprint(examiner.parent_child_map(in_handle))
# in_handle.close()


import gffutils
# path = 'intro_docs_example.gff'
path = "C:/Users\John\Documents\School\Kimble Lab\c_elegans.canonical_bioproject.current.annotations (1).gff3"
fn = gffutils.example_filename(path)
print(open(fn).read())


db = gffutils.create_db(fn, dbfn='c_elegans_anotations.db', force=True, keep_order=False,
    merge_strategy='merge', sort_attribute_values=True)
# db = gffutils.FeatureDB('test.db', keep_order=True)
# gene = db['FBgn0031208']
# print(gene.start,gene.end)
# print( gene.attributes['Name'], gene['Name'])
# print(gene)
# for i in db.children(gene, featuretype='mRNA', order_by='start'):
#     print(i)
# print()
# for i in db.children(gene, featuretype='exon', order_by='start'):
#     print(i)

# from BCBio import GFF
#
#
# limit_info = dict(
#         gff_id = ["I"],
#         gff_source = ["inverted"])
#
# in_handle = open(in_file)
# for rec in GFF.parse(in_handle, limit_info=limit_info):
#     print(rec.features[0])
# in_handle.close()