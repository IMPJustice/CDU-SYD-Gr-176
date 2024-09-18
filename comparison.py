def compare(scispacy_ent, biobert_ent):

    # Total diseases and drugs detected by each model
    total_scispacy = len(scispacy_ent[0]) + len(scispacy_ent[1])
    total_biobert = len(biobert_ent[0]) + len(biobert_ent[1])

    # Similarities and differences
    common_diseases = set(scispacy_ent[0]).intersection(set(biobert_ent[0]))
    common_drugs = set(scispacy_ent[1]).intersection(set(biobert_ent[1]))

    diff_diseases = set(scispacy_ent[0]).symmetric_difference(set(biobert_ent[0]))
    diff_drugs = set(scispacy_ent[1]).symmetric_difference(set(biobert_ent[1]))

    return {
        "total_scispacy": total_scispacy,
        "total_biobert": total_biobert,
        "common_diseases": common_diseases,
        "common_drugs": common_drugs,
        "diff_diseases": diff_diseases,
        "diff_drugs": diff_drugs
    }
