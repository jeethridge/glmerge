# glmerge
Give a file containing a list of genes and either a matrix of counts or individual count files, this script does the following:

* Filters each count file such that any genes not in the supplied gene list are removed
* Merges all the filtered count files by index such that the resulting output contains
all counts for the specifeid gene list.

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
