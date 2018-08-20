'''
import pandas as pd
data=pd.read_excel("G:\\data\\jigou.xlsx")
explor=data.describe(percentiles=[],include='all').T
explor['null']=len(data)-explor['count']
explor=explor[['null','max','min']]
explor.columns=[u'空值数',u'最大值',u'最小值']
print(explor)
'''
'''
#报告完备性
import pandas as pd
data=pd.read_csv('G:\data\hubei.csv',encoding='GB18030')
df=data.ix[:,['JBXX_XMMC','JBXX_BGMC','JBXX_BGBH','JBXX_GJMD','JBXX_WTF','JBXX_WTRDH','JBXX_WTRYB','JBXX_WTRDZ',
              'JBXX_WCXS','JBXX_XMFZR','JBXX_ZDS','JBXX_ZDZMJ','JBXX_ZGJE','JBXX_GJSFE','JBXX_GJRQ_KS','JBXX_GJRQ_JS','JBXX_GJJZR','JBXX_BMQ','JBXX_GJS','JBXX_GJJG','JBXX_BASJ']]
format=lambda x: None if x==0 else x
df=df.applymap(format)
df=pd.isnull(df)
format=lambda x: 1 if x==False else 0
df=df.applymap(format)
s=df
df=pd.concat([data['JBXX_BAH'],s],axis=1)
df[df['JBXX_BAH']=='4211815BA0021'].to_excel('G:\dafen_1.xlsx',index=None)
#df.to_excel('G:\dafen.xlsx',index=None)
'''
'''
#宗地完备性
import pandas as pd
data=pd.read_csv('G:\data\hubei.csv',encoding='GB18030')
df=data.ix[:,['ZDJBXX_ZDBH','ZDJBXX_TDSYZBH','ZDJBXX_MJ','ZDJBXX_DWMJDJ','ZDJBXX_ZDJ','ZDJBXX_GJQR',
              'ZDJBXX_TDSYQXZ','ZDJBXX_TDSTQNX','ZDJBXX_ZDWZ','ZDJBXX_TDLYZK','ZDJBXX_SJYT','ZDJBXX_GHRJL_XX1'
              ,'ZDJBXX_GHRJL_SX1','ZDJBXX_SJKFCD','ZDJBXX_TDQLXZ']]
format_1=lambda x: None if x==0  else x
df=df.applymap(format_1)
format_2=lambda x: None if x== '/'  else x
df=df.applymap(format_2)
format_3=lambda x: None if x== '无' else x
df=df.applymap(format_3)
format_4=lambda x: None if x=='一' else x
df=df.applymap(format_4)
df=pd.isnull(df)
format=lambda x: 1 if x==False else 0
df=df.applymap(format)
s=df
df_1=data.ix[:,['SCBJFPG_SEC','XSXZFPG_SEC','SYHYFPG_SEC'
              ,'SYFPG_SEC','LXJF_SEC','JSKFFPG_SEC','CBBJFPG_SEC']]
df_1=pd.isnull(df_1)
format=lambda x: 1 if x==False else 0
df_1=df_1.applymap(format)
c=df_1['SCBJFPG_SEC']+df_1['XSXZFPG_SEC']+df_1['SYHYFPG_SEC']+df_1['SYFPG_SEC']+df_1['LXJF_SEC']+df_1['JSKFFPG_SEC']+df_1['CBBJFPG_SEC']
f=lambda x: 1 if x>=2 else 0
c=c.map(f)
c=pd.DataFrame(c)
c.columns=['gjfa']
df_2=pd.concat([data['ZDJBXX_GUID'],s,c],axis=1)
print(df_2)
#df.to_excel('G:\dafen.xlsx',index=None)
'''

#评估方法完备性
import pandas as pd
import numpy as np
data=pd.read_csv('G:\data\hubei.csv',encoding='GB18030')
'''
#市场比较法
df1=data.ix[:,['SCBJFPG_ALMC','SCBJFPG_TDKFCD','SCBJFPG_WZ'
              ,'SCBJFPG_SJYT','SCBJFPG_ZYT','SCBJFPG_YTMX','SCBJFPG_ZJ','SCBJFPG_CJDMALJG',
             'SCBJFPG_TDDJ','SCBJFPG_BZDMJG','SCBJFPG_RJL','SCBJFPG_JYQK','SCBJFPG_JYFS','SCBJFPG_JYSJ']]
df1=pd.isnull(df1)
format=lambda x: 1 if x==False else 0
df1=df1.applymap(format)

#基准地价系数修正法
df2=data.ix[:,['XSXZFPG_TDYT','XSXZFPG_KFCD','XSXZFPG_GBSJ'
              ,'XSXZFPG_JZR','XSXZFPG_RJL','XSXZFPG_ZGSYNQ','XSXZFPG_DJFDXX','XSXZFPG_DJFDSX',
             'XSXZFPG_TDZJ']]
df2=pd.isnull(df2)
format=lambda x: 1 if x==False else 0
df2=df2.applymap(format)

#收益还原法
df3=data.ix[:,['SYHYFPG_NSYZJ','SYHYFPG_NSYDJ','SYHYFPG_NFYZJ'
              ,'SYHYFPG_NFYDJ','SYHYFPG_KBALMC','SYHYFPG_KBALWZ','SYHYFPG_KBALZJ','SYHYFPG_KBALDJ',
             'SYHYFPG_ZHHYL','SYHYFPG_FWHYL','SYHYFPG_TDHYL','SYHYFPG_FWNZJL','SYHYFPG_FWCSY','SYHYFPG_TDCSY',
               'SYHYFPG_FWXZDJ','SYHYFPG_FWXZZJ','SYHYFPG_TDZJ']]
df3=pd.isnull(df3)
format=lambda x: 1 if x==False else 0
df3=df3.applymap(format)
'''

#剩余法
df4=data.ix[:,['SYFPG_FDCJZZJ','SYFPG_JZCZJZJ','SYFPG_FWXZZJ'
              ,'SYFPG_FDCJZDJ','SYFPG_JZCZJDJ','SYFPG_FWXZDJ','SYFPG_FWNZJL','SYFPG_ZJNX',
             'SYFPG_SFL','SYFPG_TDZJ']]
format_1=lambda x: None if x==0  else x
df4=df4.applymap(format_1)
df4=pd.isnull(df4)
format=lambda x: 1 if x==False else 0
df4=df4.applymap(format)
#统计缺失数量
#df5=len(df4)-df4.sum()
#print(df5)
df4=df4.as_matrix()
x=[5,5,5,5,5,5,5,5,5,5]
x=np.mat(x)
x=x.T
score=df4*x
score=pd.DataFrame(score)
print(score)
'''

#假设开发法
df5=data.ix[:,['JSKFFPG_YJKFJZZJ','JSKFFPG_YJKFJZDJ','JSKFFPG_KFZQ'
              ,'JSKFFPG_YJKFCBZJ','JSKFFPG_YJKFCBDJ','JSKFFPG_LXL','JSKFFPG_SYL','JSKFFPG_ZHSFL',
             'JSKFFPG_TDZJ']]
df5=pd.isnull(df5)
format=lambda x: 1 if x==False else 0
df5=df5.applymap(format)
#成本逼近法
df6=data.ix[:,['CBBJFPG_TDQDCBZJ','CBBJFPG_TDQDCBDJ','CBBJFPG_KFZQ'
              ,'CBBJFPG_TDKFCBZJ','CBBJFPG_TDLFCNDJ','CBBJFPG_LXL','CBBJFPG_TDZZLX','CBBJFPG_TDZZ',
             'CBBJFPG_LRL','CBBJFPG_TDZJ']]
df6=pd.isnull(df6)
format=lambda x: 1 if x==False else 0
df6=df6.applymap(format)
#路线价法
df7=data.ix[:,['LXJF_MC','LXJF_TDYT','LXJF_KFCD'
              ,'LXJF_GBSJ','LXJF_JZR','LXJF_RJL','LXJF_ZGSYNQ','LXJF_DJFDXXZ',
             'LXJF_DJFDSX','LXJF_TDZJ']]
df7=pd.isnull(df7)
format=lambda x: 1 if x==False else 0
df7=df7.applymap(format)
print(df2)
'''
















