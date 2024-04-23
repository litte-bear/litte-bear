import requests
import pandas as pd

# 读取CSV文件
# file_path = 'data.xlsx'
file_path = 'venezuela.xlsx'
df = pd.read_excel(file_path)
df = pd.DataFrame(df)


def get_coordinates(osm_id):
    # url = f"https://nominatim.openstreetmap.org/details?osmtype=N&osmid=250129465&format=json"
    url = f"https://nominatim.openstreetmap.org/details?osmtype=N&osmid={osm_id}&format=json"

    response = requests.get(url)
    data = response.json()
    print(data)
    if 'centroid' in data:
        latitude = data['centroid']['coordinates'][0]
        longitude = data['centroid']['coordinates'][1]
        return float(latitude), float(longitude)
    else:
        return None

# 调用函数并传入osm_id
osm_ids = df['osm_id'].to_numpy()
# coordinates = []
for i in range(len(osm_ids)):
    try:
        coordinate = get_coordinates(osm_ids[i])
        # df = df.append({'lng': coordinate[0], 'lat': coordinate[1]}, ignore_index=True)
        df.loc[i,'lng'] = coordinate[0]
        df.loc[i,'lat'] = coordinate[1]
        # 每次迭代后保存到Excel文件
        df.to_excel('output_file.xlsx', index=False)
    except Exception as e:
        print(f"Error processing osm_id {osm_ids[i]}: {str(e)}")

# df.to_excel('output_file.xlsx', index=False)
# print(coordinates)
