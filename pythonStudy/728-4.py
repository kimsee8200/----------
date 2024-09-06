import pandas as pd
import openpyxl

s = pd.Series([1,2,3,4,5])

data = {
  '이름': ["이정국","김필제","박주희","김제숙"],
  '나이': [47,40,32,53],
  '직첵':["부장","대리","사원","이사"]
}

df =  pd.DataFrame(data)
df.to_excel('file.xlsx', index=False)

print(s)
print(data)
print(df)

#당신도 함께 주소를 