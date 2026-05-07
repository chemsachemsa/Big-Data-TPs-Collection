import pandas as pd

# 1. قراءة البيانات الخام
df = pd.read_csv('sales_data_sample.csv')

# 2. تنظيف التواريخ لكي يتعرف عليها Power BI كتواريخ حقيقية
df['OrderDate'] = pd.to_datetime(df['OrderDate']).dt.date

# 3. حفظ البيانات في ملف جديد جاهز ومُنظف
df.to_csv('cleaned_data.csv', index=False)

print("تم تنظيف البيانات بنجاح! اذهب الآن إلى Power BI.")