# glmerge
Filters count files on a gene list of interest and merges them for analysis.

Note: The count files must be normalized for this analysis to work.
The gene names (index) must always be the first column.

Gene List File Format, e.g.

    $> cat my_gene_list.csv
    ENSG00000174576
    ENSG00000170345
    ENSG00000171223
    ENSG00000135625
    ENSG00000120738
    ENSG00000139793

Example usage:

    $> python glmerge.py ./my_output.csv ./my_gene_list.csv ./count_files/*.csv
