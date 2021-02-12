def Mak():
    import re
    import pandas as pd
    df=pd.read_pickle('.\\class.pkl')
    df=df.drop([1,3,5,7,9,11,13])
    df=df.set_index(df.columns[0])
    ls=[]
    print(df.columns)
    for col in df.columns:
        ls.append(re.findall("[一-龥]", col[0])[0])
    df.columns=ls
    week=['月', '火', '水', '木', '金', '土', '日']
    df.reindex(week,axis=1)
    dr_ls=[x for x in df.isnull().sum().index[df.isnull().sum()==7]]
    df.drop(dr_ls,axis=1,inplace=True)

    class_dic={}
    for week_col in df.columns:
        class_dic[week_col]={}
        for i,class_ in enumerate(pd.Series(df.loc[:,week_col]).values):
            if pd.isnull(class_)==True:
                continue
            else:
                if not class_ in class_dic[week_col].values():
                    class_dic[week_col][str(i+1)]=class_
                else:
                    continue
    return class_dic

