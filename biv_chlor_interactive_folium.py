import folium
import pandas as pd
import branca
import json
import requests


#url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
#county_data = f'{url}/us_county_data.csv'
#county_geo = f'{url}/us_counties_20m_topo.json'


#with open('us_counties_20m_topo.json') as data_file:
with open('caCountiesTopo.json') as data_file:
#with open('caCountiesGeo.json') as data_file:
    county_geo = json.load(data_file)
    #print(county_geo['features'])
    print(county_geo)
    #exit()

with open('caCountiesGeo.json') as data_file:
    county_geo_2 = json.load(data_file)
    #print(county_geo['features'])
    print(county_geo_2)
    #exit()


with open('ca-counties.json') as data_file:
    county_geo_3 = json.load(data_file)
    #print(county_geo['features'])
    print(county_geo_3)
    #exit()



with open('ca-counties_fixed.json') as data_file:
    county_geo_3_fixed = json.load(data_file)
    #print(county_geo['features'])
    print(county_geo_3)
    #exit()




#df = pd.read_csv(county_data, na_values=[' '])
df = pd.read_csv('ca_county_data.csv', na_values=[' '])

list_sample = []

USE_LOCAL_FILES = True
SAVE_DATAFILES_LOCALLY = False

def extract_ppicj(fips_code, file_url, list):
    ''' get ppicj from online excel file
    ppiicj stands for projected percent increase in computer jobs '''

    if(USE_LOCAL_FILES == True):
        file_url = file_url.rsplit('/', 1)[-1]
        #print(file_url)
        #exit()

    if(SAVE_DATAFILES_LOCALLY == True):
        temp_df_2 = pd.read_excel(file_url, skiprows=0)
        local_name = file_url.rsplit('/', 1)[-1]
        temp_df_2.to_excel(local_name)

    temp_df = pd.read_excel(file_url, skiprows=3)
    print("getting percentage change in computer jobs forcast data for county with FIPS code" + str(fips_code))

    temp_df = temp_df[temp_df['Occupational Title'] == 'Computer Occupations']
    # print(temp_df.columns)
    try:
        percent_change = temp_df['Percent-age Change 2016-2026']
    except:
        percent_change = temp_df['Percentage-Change 2016-2026']

    # muliply by 100 to get the percentage
    ppiicj = float(percent_change) * 100
    list.append([str(fips_code), ppiicj])

    return list





# since more than one county is represented in a district, we
# could download files a lot less and assign to the correct counties
# Currently we are downloading much more than necessary
# These links can be found on the page at https://www.labormarketinfo.edd.ca.gov/data/employment-projections.html

# Alameda County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/oak$occproj.xlsx'
list_sample = extract_ppicj('006001', file_url, list_sample)
# Alpine County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/esregoccproj.xlsx'
list_sample = extract_ppicj('006003', file_url, list_sample)
# Amador County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/mlroccproj.xlsx'
list_sample = extract_ppicj('006005', file_url, list_sample)
# Butte County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/chic$occproj.xlsx'
list_sample = extract_ppicj('006007', file_url, list_sample)
# Calaveras County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/mlroccproj.xlsx'
list_sample = extract_ppicj('006009', file_url, list_sample)
# Colusa County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/nvregoccproj.xlsx'
list_sample = extract_ppicj('006011', file_url, list_sample)
# Contra Costa County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/oak$occproj.xlsx'
list_sample = extract_ppicj('006013', file_url, list_sample)
# Del Norte County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/norcoastoccproj.xlsx'
list_sample = extract_ppicj('006015', file_url, list_sample)
# El Dorado County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/sacr$occproj.xlsx'
list_sample = extract_ppicj('006017', file_url, list_sample)
# Fresno County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/frsn$occproj.xlsx'
list_sample = extract_ppicj('006019', file_url, list_sample)
# Glenn County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/nvregoccproj.xlsx'
list_sample = extract_ppicj('006021', file_url, list_sample)
# Humboldt County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/norcoastoccproj.xlsx'
list_sample = extract_ppicj('006023', file_url, list_sample)
# Imperial County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/ecen$occproj.xlsx'
list_sample = extract_ppicj('006025', file_url, list_sample)
# Inyo County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/esregoccproj.xlsx'
list_sample = extract_ppicj('006027', file_url, list_sample)
# Kern County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/bake$occproj.xlsx'
list_sample = extract_ppicj('006029', file_url, list_sample)
# Kings County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/hanf$occproj.xlsx'
list_sample = extract_ppicj('006031', file_url, list_sample)
# Lake County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/norcoastoccproj.xlsx'
list_sample = extract_ppicj('006033', file_url, list_sample)
# Lassen County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/nmregoccproj.xlsx'
list_sample = extract_ppicj('006035', file_url, list_sample)
# Los Angeles County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/la$occproj.xlsx'
list_sample = extract_ppicj('006037', file_url, list_sample)
# Madera County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/mad$occproj.xlsx'
list_sample = extract_ppicj('006039', file_url, list_sample)
# Marin County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/sanrf$occproj.xlsx'
list_sample = extract_ppicj('006041', file_url, list_sample)
# Mariposa County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/mlroccproj.xlsx'
list_sample = extract_ppicj('006043', file_url, list_sample)
# Mendocino County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/norcoastoccproj.xlsx'
list_sample = extract_ppicj('006045', file_url, list_sample)
# Merced County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/merc$occproj.xlsx'
list_sample = extract_ppicj('006047', file_url, list_sample)
# Modoc County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/nmregoccproj.xlsx'
list_sample = extract_ppicj('006049', file_url, list_sample)
# Mono County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/esregoccproj.xlsx'
list_sample = extract_ppicj('006051', file_url, list_sample)
# Monterey County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/sali$occproj.xlsx'
list_sample = extract_ppicj('006053', file_url, list_sample)
# Napa County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/napa$occproj.xlsx'
list_sample = extract_ppicj('006055', file_url, list_sample)
# Nevada County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/nmregoccproj.xlsx'
list_sample = extract_ppicj('006057', file_url, list_sample)
# Orange County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/oran$occproj.xlsx'
list_sample = extract_ppicj('006059', file_url, list_sample)
# Placer County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/sacr$occproj.xlsx'
list_sample = extract_ppicj('006061', file_url, list_sample)
# Plumas County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/nmregoccproj.xlsx'
list_sample = extract_ppicj('006063', file_url, list_sample)
# Riverside County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/rive$occproj.xlsx'
list_sample = extract_ppicj('006065', file_url, list_sample)
# Sacramento County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/sacr$occproj.xlsx'
list_sample = extract_ppicj('006067', file_url, list_sample)
# San Benito County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/sjos$occproj.xlsx'
list_sample = extract_ppicj('006069', file_url, list_sample)
# San Bernardino County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/rive$occproj.xlsx'
list_sample = extract_ppicj('006071', file_url, list_sample)
# San Diego County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/sand$occproj.xlsx'
list_sample = extract_ppicj('006073', file_url, list_sample)
# San Francisco County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/sanf$occproj.xlsx'
list_sample = extract_ppicj('006075', file_url, list_sample)
# San Joaquin County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/stoc$occproj.xlsx'
list_sample = extract_ppicj('006077', file_url, list_sample)
# San Luis Obispo County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/slo$occproj.xlsx'
list_sample = extract_ppicj('006079', file_url, list_sample)
# San Mateo County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/sanf$occproj.xlsx'
list_sample = extract_ppicj('006081', file_url, list_sample)
# Santa Barbara County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/satb$occproj.xlsx'
list_sample = extract_ppicj('006083', file_url, list_sample)
# Santa Clara County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/sjos$occproj.xlsx'
list_sample = extract_ppicj('006085', file_url, list_sample)
# Santa Cruz County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/scrz$occproj.xlsx'
list_sample = extract_ppicj('006087', file_url, list_sample)
# Shasta County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/redd$occproj.xlsx'
list_sample = extract_ppicj('006089', file_url, list_sample)
# Sierra County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/nmregoccproj.xlsx'
list_sample = extract_ppicj('006091', file_url, list_sample)
# Siskiyou County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/nmregoccproj.xlsx'
list_sample = extract_ppicj('006093', file_url, list_sample)
# Solano County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/vall$occproj.xlsx'
list_sample = extract_ppicj('006095', file_url, list_sample)
# Sonoma County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/satr$occproj.xlsx'
list_sample = extract_ppicj('006097', file_url, list_sample)
# Stanislaus County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/mode$occproj.xlsx'
list_sample = extract_ppicj('006099', file_url, list_sample)
# Sutter County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/yuba$occproj.xlsx'
list_sample = extract_ppicj('006101', file_url, list_sample)
# Tehama County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/nvregoccproj.xlsx'
list_sample = extract_ppicj('006103', file_url, list_sample)
# Trinity County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/nmregoccproj.xlsx'
list_sample = extract_ppicj('006105', file_url, list_sample)
# Tulare County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/visa$occproj.xlsx'
list_sample = extract_ppicj('006107', file_url, list_sample)
# Tuolumne County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/mlroccproj.xlsx'
list_sample = extract_ppicj('006109', file_url, list_sample)
# Ventura County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/vent$occproj.xlsx'
list_sample = extract_ppicj('006111', file_url, list_sample)
# Yolo County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/sacr$occproj.xlsx'
list_sample = extract_ppicj('006113', file_url, list_sample)
# Yuba County
file_url = 'https://www.labormarketinfo.edd.ca.gov/file/occproj/yuba$occproj.xlsx'
list_sample = extract_ppicj('006115', file_url, list_sample)



df_sample = pd.DataFrame(list_sample, columns = ['FIPS', 'PROJECTED_PERCENT_INCREASE_COMPUTER_JOBS'])
print('\n\n')
print(df_sample)
print('\n\n')
print(df_sample['PROJECTED_PERCENT_INCREASE_COMPUTER_JOBS'].describe())
print(df_sample.columns)
#exit()
#df = df_sample

##colorscale = branca.colormap.linear.YlOrRd_09.scale(0, 50e3)
#colorscale = branca.colormap.linear.YlOrRd_09.scale(50e3, 0)
##colorscale = branca.colormap.linear.PuRd_09.scale(0, 1000000)
####colorscale = branca.colormap.linear.PuRd_09.scale(0, 20)
employed_series_old = df.set_index('FIPS_Code')['Employed_2011']
#employed_series = df_sample.set_index('FIPS')['PROJECTED_PERCENT_INCREASE_COMPUTER_JOBS']
df_sample.columns = ['FIPS_Code', 'PROJECTED_PERCENT_INCREASE_COMPUTER_JOBS']
print(df_sample.columns)
#exit()
employed_series = df_sample.set_index('FIPS_Code')['PROJECTED_PERCENT_INCREASE_COMPUTER_JOBS']

print('111111111111111111111')
print(employed_series_old.describe())
print(employed_series_old)
print('22222222222222222222')
print(employed_series.describe())
print(employed_series)
print(employed_series.min())
print(employed_series.max())
#exit()
print('3333333333333333')
print(employed_series.get('006001', None))
#exit()

#colorscale = branca.colormap.linear.PuRd_09.scale(employed_series.min(), employed_series.max())
colorscale = branca.colormap.linear.PuBu_09.scale(employed_series.min(), employed_series.max())
#colorscale = branca.colormap.linear.001A_R100cospi.scale(employed_series.min(), employed_series.max())

def style_function(feature):

    print(feature['id'])
    #exit()
    #employed = employed_series.get(int(feature['id'][-5:]), None)
    #employed = employed_series.get(int(feature['id']), None)
    ##employed = employed_series.get('006001', None)
    employed = employed_series.get('0' + str(feature['id']), None)
    print('got ' + str(employed))
    return {
        'fillOpacity': 0.5,
        'weight': 0,
        #'fillColor': '#green' if employed is None else colorscale(employed)
        'fillColor': 'green' if employed is None else colorscale(employed)
    }

def style_function_2(feature):

    #print(feature['id'])
    print(feature['properties']['geoid'])
    #exit()
    #employed = employed_series.get(int(feature['id'][-5:]), None)
    #employed = employed_series.get(int(feature['id']), None)
    ##employed = employed_series.get('006001', None)
    employed = employed_series.get('0' + str(feature['properties']['geoid'][-5:]), None)
    print('got ' + str(employed))
    return {
        'fillOpacity': 0.5,
        'weight': 0,
        #'fillColor': '#green' if employed is None else colorscale(employed)
        'fillColor': 'green' if employed is None else colorscale(employed)
    }


def style_function_3(feature):

    #print(feature['id'])
    print(feature['properties']['geoid'])
    #exit()
    #employed = employed_series.get(int(feature['id'][-5:]), None)
    #employed = employed_series.get(int(feature['id']), None)
    ##employed = employed_series.get('006001', None)
    employed = employed_series.get('0' + str(feature['properties']['geoid'][-5:]), None)
    print('got ' + str(employed))
    return {
        'fillOpacity': 0.5,
        'weight': 0,
        #'fillColor': '#green' if employed is None else colorscale(employed)
        'fillColor': 'green' if employed is None else colorscale(employed)
    }


m = folium.Map(
    #location=[48, -102],
    location=[38, -121.5],
    #tiles='cartodbpositron',
    #tiles='Mapbox Bright',
    #tiles='stamentoner',
    #tiles='Mapbox Control Room',
    tiles=None,
    zoom_start=6
)

#folium.TileLayer('Mapbox Bright').add_to(m)

#folium.TopoJson(
#    json.loads(requests.get(county_geo).text),
#    'objects.us_counties_20m',
#    style_function=style_function
#).add_to(m)

#folium.TopoJson(
#    county_geo,
    #'objects.us_counties_20m',
#    'objects.subunits',
    #'features.Feature',
#'   features.geometry',
#    style_function=style_function
#).add_to(m)

'''
folium.TopoJson(
    county_geo,
    'objects.subunits',
    style_function=style_function
).add_to(m)
'''


'''
folium.GeoJson(
    county_geo_2,
    style_function=style_function_2
).add_to(m)
'''

'''
folium.GeoJson(
    county_geo_3,
    style_function=style_function_3
).add_to(m)
'''


folium.GeoJson(
    county_geo_3_fixed,
    style_function=style_function_3
).add_to(m)


m
m.save('new_map_6.html')