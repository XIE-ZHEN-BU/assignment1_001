from heapq import merge

import pandas as pd


def clean(input1,input2):
    df1 = pd.read_csv(input1)
    df2=pd.read_csv(input2)
    x1=pd.merge(df1, df2,left_on='respondent_id',right_on='id', how='right')
    x2=x1.dropna(axis=0,how='any')
    x3=x2[~ x2['job'].str.contains('insurance')]
    x4 = x3[~ x3['job'].str.contains('Insurance')]
    x5=  x4.drop(labels='id', axis=1)



    return x5


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input1',help='Data file (CSV)')
    parser.add_argument('input2', help='Data file (CSV)')
    parser.add_argument('output', help='Cleaned data file (CSV)')
    args = parser.parse_args()

    cleaned = clean(args.input1,args.input2)
    cleaned.to_csv(args.output, index=False)
