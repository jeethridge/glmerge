#!/usr/bin/env python
"""Filters count files on a gene list of interest and merges them for analysis.

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
"""

import argparse
import sys
import pandas as pd
from functools import reduce

_INDEX_NAME = 'Ensembl'


def load_count_files(files, gene_list):
    """Returns a list of dataframes given a list of count files"""
    dfs = []
    for file in files:
        # load and filter
        df = pd.read_csv(file, index_col=0)
        df = df[df.index.isin(gene_list)]
        # set index name
        df.index.name = _INDEX_NAME
        dfs.append(df)
    return dfs


def main():
    # Defined the command line interface
    parser = argparse.ArgumentParser()
    parser.add_argument('output_file', help='The path where the output file should be written.', default="merged.csv")
    parser.add_argument("gene_list", type=str,
                        help="File path to the csv file containing the list of target genes")
    parser.add_argument('count_files', nargs='+', help='File path(s) for the count files to be filtered and merged.')
    # Do the business, show help on error
    try:
        # Try to read command line arguments
        args = parser.parse_args()
        # Get the gene list from the csv file -- always column 0
        gene_list = pd.read_csv(args.gene_list).iloc[:, 0].to_list()
        # load count files and filter indices for gene_list
        dfs_count = load_count_files(args.count_files, gene_list)
        # Merge the count file data-frames
        df_merged = reduce(
            lambda left, right: pd.merge(left, right, on=_INDEX_NAME, how='outer'),
            dfs_count)
        # Write to file
        df_merged.to_csv(args.output_file)
    except Exception as e:
        # Show help and exit with an error if a bad thing happened
        print(e)
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    # execute only if run as a script
    main()
