import matplotlib.pyplot as plt
from config_SimPy import *
from environment import *
import numpy as np

'''
def visualization(export_Daily_Report):
    Visual_Dict = {
        'MATERIAL 1': [],
        'WIP': [],
        'Product': [],
        'Keys': {'MATERIAL 1': [], 'WIP': [], 'Product': []}
    }
    Key = ['MATERIAL 1', 'WIP', 'Product']

    for id in I.keys():
        temp = []
        for x in range(SIM_TIME):
            temp.append(export_Daily_Report[x][id*7+7])#Record Onhand inventory at day end
        Visual_Dict[export_Daily_Report[0][id*7+2]].append(temp)#Update 
        Visual_Dict['Keys'][export_Daily_Report[0][2+id*7]].append(export_Daily_Report[0][id *7+1])#Update Keys
    visual = VISUALIZATION.count(1)
    count_type = 0
    cont_len = 1
    for x in VISUALIZATION:
        cont = 0
        if x == 1:
            plt.subplot(int(f"{visual}1{cont_len}"))
            cont_len += 1
            for lst in Visual_Dict[Key[count_type]]:
                plt.plot(lst, label=Visual_Dict['Keys'][Key[count_type]][cont])
                plt.axhline(y=S_REORDER_POINT, color='r', linestyle='--', label='S_REORDER_POINT')
                plt.legend()
                cont += 1
            plt.xticks(ticks=np.arange(0, 14, 1), labels=np.arange(1, 15, 1))
        count_type += 1
    plt.savefig("Graph")
    plt.clf()
'''

import pandas as pd
import matplotlib.pyplot as plt

# Daily_Report 파일에서 데이터 로드
df = pd.read_csv("C:\\Users\\지예림\\Desktop\\SimPy_IMS-master_update\\Daily_Report.csv")

# 필요한 데이터 추출 (product onhand, material onhand)
# 여기서 'Product Onhand', 'Material Onhand' 컬럼 이름이 정확하다면 그대로 사용하고,
# 아니면 실제 CSV 파일의 컬럼명을 확인해서 변경해야 합니다.
product_onhand = df["PRODUCT's ONHAND"]
material_onhand = df["MATERIAL 1's ONHAND"]
days = df['DAY']  # 'Day' 컬럼이 있다고 가정

# 그래프 시각화
plt.figure(figsize=(10, 6))

# 첫 번째 그래프: Product Onhand
plt.subplot(2, 1, 1)
plt.plot(days, product_onhand, label='Product Onhand', color='blue')
plt.axhline(y=3, color='red', linestyle='--', label='s_Reorder Point')
plt.title('Product Onhand Inventory')
plt.ylabel('Product Onhand')
plt.legend()

# 두 번째 그래프: Material Onhand
plt.subplot(2, 1, 2)
plt.plot(days, material_onhand, label='Material Onhand', color='green')
plt.axhline(y=3, color='red', linestyle='--', label='s_Reorder Point')
plt.title('Material Onhand Inventory')
plt.ylabel('Material Onhand')
plt.legend()

plt.tight_layout(pad=3.0)
plt.savefig("Graph")
plt.clf()