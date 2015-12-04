/*
A KBase module: rscount
*/

module rscount {

    typedef string contigset_id;
        
    typedef string workspace_name;

    typedef structure {
        int contig_count;
    } CountContigsResults;

    funcdef count_contigs(workspace_name,contigset_id) returns (CountContigsResults) authentication required;
};
