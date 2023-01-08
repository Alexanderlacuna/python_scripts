SELECT 
    Symbol,mean,description,additive
FROM
    ProbeSet, ProbeSetFreeze, ProbeSetXRef
WHERE
    ProbeSet.Id=ProbeSetXRef.ProbeSetId and
    ProbeSetFreeze.Id = ProbeSetXRef.ProbeSetFreezeId and
    ProbeSet.Name = "1460303_at" and
    ProbeSetFreeze.Name = "HC_M2_0606_P"






SELECT 
    LRS
FROM
    ProbeSet, ProbeSetFreeze, ProbeSetXRef
WHERE
    ProbeSet.Id=ProbeSetXRef.ProbeSetId and
    ProbeSetFreeze.Id = ProbeSetXRef.ProbeSetFreezeId and
    ProbeSet.Name = "1460303_at" and
    ProbeSetFreeze.Name = "HC_M2_0606_P"



HC_M2_0606_P
1460303_at


** what I need ,Location,,Peak LOD,Peak Location,Effect size

found:Symbol,mean,Description,LRS,additive(effect size)



**am missing peak location and peak LOD
#note   lrs_location -> lrs_location_repr -> chr + mb check the formation

"""display fields available for the above dataset

['name', 'symbol', 'description', 'probe_target_description', 'chr', 'mb', 'alias', 'geneid', 'genbankid', 'unigeneid', 'omim', 'refseq_transcriptid', 'blatseq', 'targetseq', 'chipid', 'comments', 'strand_probe', 'strand_gene', 'proteinid', 'uniprotid', 'probe_set_target_region', 'probe_set_specificity', 'probe_set_blat_score', 'probe_set_blat_mb_start', 'probe_set_blat_mb_end', 'probe_set_strand', 'probe_set_note_by_rw', 'flag']


"""



    """
    import time
    init_time = time.time()
    with database_connector() .cursor() as cursor:

        cursor.execute(
            """
            SELECT Symbol,mean,description,additive
            FROM  ProbeSet, ProbeSetFreeze, ProbeSetXRef
            WHERE ProbeSet.Id=ProbeSetXRef.ProbeSetId
            and ProbeSetFreeze.Id = ProbeSetXRef.ProbeSetFreezeId
            and ProbeSet.Name in {}
            and ProbeSetFreeze.Name = '{}'
            """.format(create_in_clause(trait_list),dataset.name)

            )

        results_2 = cursor.fetchall()

    end_time = time.time()-init_time

    """

    Geno.Name = 'rs4140265'

    Species.Name = 'mouse'


query = """
    select ProbeSet.Name,Symbol,mean,description,additive,LRS,Geno.Chr, Geno.Mb
    from Geno, Species,ProbeSet,ProbeSetXRef,ProbeSetFreeze
    where Species.Name = 'mouse' and
    Geno.Name = ProbeSetXRef.Locus and
    ProbeSet.Name = '1460303_at' and
    Geno.SpeciesId = Species.Id and
    ProbeSet.Id=ProbeSetXRef.ProbeSetId and
    ProbeSetFreeze.Id = ProbeSetXRef.ProbeSetFreezeId and
    ProbeSetFreeze.Name = "HC_M2_0606_P"

    """


SELECT 
    Symbol,mean,description,additive
FROM
    ProbeSet, ProbeSetFreeze, ProbeSetXRef
WHERE
    ProbeSet.Id=ProbeSetXRef.ProbeSetId and
    ProbeSetFreeze.Id = ProbeSetXRef.ProbeSetFreezeId and
    ProbeSet.Name = "1460303_at" and
    ProbeSetFreeze.Name = "HC_M2_0606_P"


('1415733_a_at', 'Shb', 10.755535353535398, 'Src homology 2 domain containing adaptor protein B', -0.0436819047619045, 8.86130102028889, '5', 69.527298)
(Pdb) len(results[0])


            cursor.execute(
                """
            SELECT ProbeSet.Name,ProbeSet.Chr ,ProbeSet.Mb,
            Symbol,mean,description,additive,LRS,Geno.Chr, Geno.Mb
            from Geno, Species,ProbeSet,ProbeSetXRef,ProbeSetFreeze
            where Species.Name = '{}' and
            Geno.Name = ProbeSetXRef.Locus and
            ProbeSet.Name in {} and
            Geno.SpeciesId = Species.Id and
            ProbeSet.Id=ProbeSetXRef.ProbeSetId and
            ProbeSetFreeze.Id = ProbeSetXRef.ProbeSetFreezeId and
            ProbeSetFreeze.Name = '{}'
            """.format(dataset.group.species, create_in_clause(trait_list), dataset.name)


            )


curr.execute(
    """
        SELECT Strain.Name, Strain.Id FROM Strain, Species
        WHERE Strain.Name IN ({})
        and Strain.SpeciesId=Species.Id
        and Species.name = %s
    """.format(", ".join(sample_data_keys)),
    (sample_data_keys + (dataset.group.species,)))




curr.execute(
    """
        SELECT Strain.Name, Strain.Id FROM Strain, Species
        WHERE Strain.Name IN ({})
        and Strain.SpeciesId=Species.Id
        and Species.name = %(species_name)s
    """.format(", ".join([f"%({key})s" for key in sample_data_dict.keys()])),
    {**sample_data_dict, "species_name": dataset.group.species})





curr.execute(
    """
        SELECT Strain.Name, Strain.Id FROM Strain, Species
        WHERE Strain.Name IN ({})
        and Strain.SpeciesId=Species.Id
        and Species.name = %(species_name)s
    """.format(", ".join([f"%({key})s" for key in sample_data_dict.keys()])),
    {**sample_data_dict, "species_name": dataset.group.species})






    with database_connector() as conn:
        with conn.cursor() as cursor:

            if dataset.type == "ProbeSet":      
       

                cursor.execute(
                    """
                SELECT ProbeSet.Name,ProbeSet.Chr,ProbeSet.Mb,
                Symbol,mean,description,additive,LRS,Geno.Chr, Geno.Mb
                from Geno, Species,ProbeSet,ProbeSetXRef,ProbeSetFreeze
                where ProbeSet.Name in ({}) and
                Species.Name = %s and
                Geno.Name = ProbeSetXRef.Locus and
                Geno.SpeciesId = Species.Id and
                ProbeSet.Id=ProbeSetXRef.ProbeSetId and
                ProbeSetFreeze.Id = ProbeSetXRef.ProbeSetFreezeId and
                ProbeSetFreeze.Name = %s
                """.format(", ".join(["%s"]* len(trait_list))),
                (tuple(trait_list) + (dataset.group.name,) + (dataset.name,))
                )

                db_results = cursor.fetchall()



    with database_connector() as conn:
        with conn.cursor() as cursor:

            if dataset.type == "ProbeSet":      
       

                cursor.execute(
                    """
                SELECT ProbeSet.Name,ProbeSet.Chr,ProbeSet.Mb,
                Symbol,mean,description,additive,LRS,Geno.Chr, Geno.Mb
                from Geno, Species,ProbeSet,ProbeSetXRef,ProbeSetFreeze
                where ProbeSet.Name in ({}) and
                Species.Name = %s and
                Geno.Name = ProbeSetXRef.Locus and
                Geno.SpeciesId = Species.Id and
                ProbeSet.Id=ProbeSetXRef.ProbeSetId and
                ProbeSetFreeze.Id = ProbeSetXRef.ProbeSetFreezeId and
                ProbeSetFreeze.Name = %s
                """.format(", ".join(["%s"]* len(trait_list))),
                (tuple(trait_list) + (dataset.group.name,) + (dataset.name,))
                )

                db_results = cursor.fetchall()














# starts here


def fetch_metadata(dataset, trait_list):



    import time 


    init_time = time.time()


    with database_connector() as conn:
        with conn.cursor() as cursor:

            query ="""
                    SELECT ProbeSet.Name,ProbeSet.Chr,ProbeSet.Mb,
                    Symbol,mean,description,additive,LRS,Geno.Chr, Geno.Mb
                    from Geno, Species,ProbeSet,ProbeSetXRef,ProbeSetFreeze
                    where ProbeSet.Name in ({}) and
                    Species.Name = %s and
                    Geno.Name = ProbeSetXRef.Locus and
                    Geno.SpeciesId = Species.Id and
                    ProbeSet.Id=ProbeSetXRef.ProbeSetId and
                    ProbeSetFreeze.Id = ProbeSetXRef.ProbeSetFreezeId and
                    ProbeSetFreeze.Name = %s
                """.format(", ".join(["%s"]* len(trait_list)))
       

            cursor.execute(query,
            (tuple(trait_list) + (dataset.group.species,) + (dataset.name,))
            )

            db_results = cursor.fetchall()





    dict_results = {}

    for(trait_name,probe_chr,probe_mb,symbol, mean, description,
            additive, lrs, chr_score, mb) in db_results:

        dict_results[trait_name] = {
        "name":trait_name,
        "view":True, # not implementd
        "symbol":symbol,
        "dataset":dataset.name,
        "dataset_name":dataset.shortname,
        "mean":mean,
        "description":description,
        "additive":additive,
        "lrs_score":f"{lrs:3.1f}",
        "location":f"Chr{probe_chr}: {probe_mb:.6f}", #not implemented
        "lrs_location":f"Chr{chr_score}: {mb:.6f}"

        }

    return dict_results



                query = """
                        SELECT
                                PublishXRef.Locus, PublishXRef.LRS, PublishXRef.additive
                        FROM
                                PublishXRef, PublishFreeze
                        WHERE
                                PublishXRef.Id = %s AND
                                PublishXRef.InbredSetId = PublishFreeze.InbredSetId AND
                                PublishFreeze.Id =%s
                """ % (trait.name, dataset.id)




SELECT ProbeSet.Name,Strain.Name, ProbeSetData.value
FROM (ProbeSetData, ProbeSetFreeze, Strain, ProbeSet,ProbeSetXRef)
LEFT JOIN ProbeSetSE ON (ProbeSetSE.DataId = ProbeSetData.Id AND
ProbeSetSE.StrainId = ProbeSetData.StrainId) 
LEFT JOIN NStrain ON (NStrain.DataId = ProbeSetData.Id AND 
NStrain.StrainId = ProbeSetData.StrainId)
WHERE ProbeSetXRef.ProbeSetId = ProbeSet.Id 
AND ProbeSetXRef.ProbeSetFreezeId = ProbeSetFreeze.Id 
AND ProbeSetFreeze.Name = "HC_M2_0606_P" AND 
ProbeSetXRef.DataId = ProbeSetData.Id
AND ProbeSetData.StrainId = Strain.Id
ORDER BY ProbeSet.Name








{'db': {'dataset_name': 'HC_M2_0606_P', 'dataset_type': 'ProbeSet', 'Name': 'BXD', 'Id': 1, 'group': 'BXD', 'groupid': 1}, 'trait_fullname': 'HC_M2_0606_P::1460303_at::unknown', 'trait_name': '1460303_at', 'cellid': 'unknown', 'name': '1460303_at', 'symbol': 'Nr3c1', 'description': 'nuclear receptor subfamily 3, group C, member 1 (glucocorticoid receptor 1, cortisol/corticosterone receptor, dexamethasone-binding receptor)', 'probe_target_description': "distal 3' UTR", 'chr': '18', 'mb': 39.570418, 'alias': 'GR; Grl-1; Grl1', 'geneid': '14815', 'genbankid': 'NM_008173', 'unigeneid': 'Mm.129481', 'omim': '138040', 'refseq_transcriptid': 'NM_008173', 'blatseq': 'GAAGTTTTCTCATTTTCCAGACTATTTTCGGTCAGCCTGGTCTATCAAGATCGGTAACCAGGTCTTCAGGAAAGGGTTGGCTTCTATCTAGGACATGCCTGAAGGCTGTATGAAAATACCCTCCTAAATACCCTGCTTAACTACAGTGTGTCAATATTCTATTTTGTAGTTGTAGTTTTTTATTCATGCTGAATAACCTGTAGTTT', 'targetseq': 'gaagttttctcattttccagactattttcggtcagcctggtctatcaagatcggtaaccaggtcttcaggaaagggttggcttctatctaggacatgcctgaaaggattttattttctgataaatggctgtatgaaaataccctcctaaataccctgcttaactacatatagatttcagtgtgtcaatattctattttgtatattaaacaaatgctatataatggggacaaatctatattatactgtgtatggcattattaagaagctttttcattattttttatcacagtaatttttaaatgtgtaaaaattaaaaaccagtgactcctgtttaaaaataaaagttgtagttttttattcatgctgaataacctgtagttt', 'chipid': 4, 'comments': 'robwilliams modified description, probe_target_description, alias at Thu Mar  2 00:15:25 2006\n', 'strand_probe': '-', 'strand_gene': '-', 'probe_set_target_region': None, 'proteinid': None, 'probe_set_specificity': 10.15, 'probe_set_blat_score': 203.0, 'probe_set_blat_mb_start': 39.570418, 'probe_set_blat_mb_end': 39.570799, 'probe_set_strand': None, 'probe_set_note_by_rw': None, 'flag': '1', 'haveinfo': True, 'BlatSeq': 'GAAGTTTTCTCATTTTCCAGACTATTTTCGGTCAGCCTGGTCTATCAAGATCGGTAACCAGGTCTTCAGGAAAGGGTTGGCTTCTATCTAGGACATGCCTGAAGGCTGTATGAAAATACCCTCCTAAATACCCTGCTTAACTACAGTGTGTCAATATTCTATTTTGTAGTTGTAGTTTTTTATTCATGCTGAATAACCTGTA




'SELECT Id, FullName FROM ProbeSetFreeze WHERE Name = HC_M2_0606_P' 



select name,strainid,value from (ProbeSet,ProbeSetXRef,ProbeSetData)
where ProbeSetFreezeId = 112
  and ProbeSet.Id = ProbeSetXRef.ProbeSetId
  and ProbeSetData.id = ProbeSetXRef.DataId
  and ((strainid>=4 and strainid<=31) or strainid in (33,35,36,37,39,98,100,103))
;







[6.639, 6.49, 6.62, 6.528, 6.644, 6.676, 6.401, 6.452, 6.568, 6.642, 6.486, 6.446, 6.582, 6.484, 6.877, 6.474, 6.28, 6.486, 6.53, 6.618, 6.565, 6.484, 6.494, 6.636, 6.562, 6.61, 6.668, 6.607, 6.513, 6.601, 6.573, 6.639, 6.656, 6.578, 6.636, 6.638, 6.266, 6.357, 6.456, 6.59, 6.568, 6.581, 6.322, 6.519, 6.543, 6.549, 6.502, 6.584, 6.263, 6.541, 6.662, 6.628, 6.556, 6.572, 6.53, 6.608, 6.548, 6.52, 6.494, 6.496, 6.393, 6.261, 6.646, 6.584, 6.79, 6.536, 6.534, 6.352, 6.476, 6.545, 6.742]


[6.777, 6.528, 6.62, 6.49, 6.644, 6.676, 6.401, 6.452, 6.568, 6.642, 6.486, 6.446, 6.582, 6.484, 6.877, 6.474, 6.28, 6.486, 6.53, 6.618, 6.565, 6.484, 6.494, 6.636, 6.562, 6.61, 6.668, 6.607, 6.513, 6.601, 6.573, 6.639, 6.656, 6.578, 6.636, 6.638, 6.266, 6.357, 6.456, 6.59, 6.568, 6.581, 6.322, 6.519, 6.543, 6.549, 6.502, 6.584, 6.263, 6.541, 6.662, 6.628, 6.556, 6.572, 6.53, 6.608, 6.548, 6.52, 6.494, 6.496, 6.393, 6.261, 6.646, 6.584, 6.79, 6.536, 6.534, 6.352, 6.476, 6.545, 6.742]




    def test_for_caching(self):

        with database_connection()  as conn,conn.cursor() as cursor:

            cursor.execute(
                "SELECT ProbeSet.Name,Strain.Name, ProbeSetData.value "
                "FROM (ProbeSetData, ProbeSetFreeze, Strain, ProbeSet, "
                "ProbeSetXRef) LEFT JOIN ProbeSetSE ON "
                "(ProbeSetSE.DataId = ProbeSetData.Id AND "
                "ProbeSetSE.StrainId = ProbeSetData.StrainId) "
                "LEFT JOIN NStrain ON "
                "(NStrain.DataId = ProbeSetData.Id AND "
                "NStrain.StrainId = ProbeSetData.StrainId) "
                "WHERE ProbeSetXRef.ProbeSetId = ProbeSet.Id "
                "AND ProbeSetXRef.ProbeSetFreezeId = ProbeSetFreeze.Id "
                "AND ProbeSetFreeze.Name = %s AND "
                "ProbeSetXRef.DataId = ProbeSetData.Id "
                "AND ProbeSetData.StrainId = Strain.Id "
                "ORDER BY Strain.Name",
                (self.name,)
            )
            results = cursor.fetchall()


        seen = ["ID"]
        data = {}
        for (trait,name,value) in results:


            if name not in seen:
                seen.append(name)
            if trait in  data:
                data[trait].append(value)
            else:
                data[trait] = [value]


        import csv
        with open('data.csv', 'w+', encoding='UTF8') as f:
            writer = csv.writer(f)

            writer.writerow(seen)
            for (key,vals) in data.items():
                writer.writerow([key]+ vals)


        return results


