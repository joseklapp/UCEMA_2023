import pandas as pd
import os
import numpy as np
from math import radians, sin, cos, asin, sqrt

def normalize_name(filename):
    return filename.replace("olist_", "").replace("_dataset", "").replace(".csv", "")
def load_all_data(path):
    ''' read all datasets in folder and usea as name'''
    files = [f for f in os.listdir(path) if f.endswith(".csv")]
    data = {normalize_name(filename): pd.read_csv(f"{path}/{filename}") for filename in files}
    return data

def transformar_columnas_datetime(df):
    for columna in df:
        if ('-' in df[columna][0]) == True:
            df[columna] = pd.to_datetime(df[columna])
    return df
     
    
def tiempo_de_espera(orders, is_delivered=True):
    # filtrar por entregados y crea la varialbe tiempo de espera
    if is_delivered:
        orders = orders.query("order_status=='delivered'").copy()
    # compute wait time
    orders.loc[:, 'tiempo_de_espera'] = \
        (orders['order_delivered_customer_date'] -
         orders['order_purchase_timestamp']) / np.timedelta64(24, 'h')
    return orders



def real_vs_esperado(orders):
    orders['tiempo_de_espera_esperado'] = (orders['order_estimated_delivery_date'] - orders['order_purchase_timestamp']) / np.timedelta64(24, 'h')
    orders['real_vs_esperado'] = orders['tiempo_de_espera'] - orders['tiempo_de_espera_esperado']
    for i in range(len(orders['real_vs_esperado'])):
                   if orders['real_vs_esperado'][i] < 0:
                       orders['real_vs_esperado'][i] = 0
        
    return orders

    

def es_cinco_estrellas(x):
    if x == 5:
        return 1
    else:
        return 0

def es_una_estrella(x):
    if x == 1:
        return 1
    else:
        return 0

    
def puntaje_de_compra(df):
    df['es_cinco_estrellas'] = df['review_score'].apply(es_cinco_estrellas)
    df['es_una_estrella'] = df['review_score'].apply(es_una_estrella)
    df_final = df[['order_id', 'review_score', 'es_cinco_estrellas', 'es_una_estrella']]
    return df_final


 

def calcular_numero_productos(data):
    for df in data:
        if df == 'order_items':
            order_items = data[df].copy()
    
    numero_de_productos = order_items.groupby('order_id').agg(numero_productos=('product_id', 'count'))
    return numero_de_productos


def vendedores_unicos(data):
    for df in data:
        if df == 'order_items':
            order_items = data[df].copy()
    
    numero_de_vendedores = order_items.groupby('order_id').agg(numero_vendedores_unicos=('seller_id', 'nunique'))
    return numero_de_vendedores



def calcular_precio_y_transporte(data):
    for df in data:
        if df == 'order_items':
            order_items = data[df].copy()
    
    precio_y_transporte = order_items.groupby('order_id').agg(precio=('price', 'sum'), valor_transporte=('freight_value', 'sum'))
    return precio_y_transporte


def haversine_distance(lon1, lat1, lon2, lat2):
    """
    Computa distancia entre dos pares (lat, lng)
    Ver - (https://en.wikipedia.org/wiki/Haversine_formula)
    """
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    return 2 * 6371 * asin(sqrt(a))




def calcular_distancia_vendedor_comprador(data):
    for df in data:
        if df == 'order_items':
            order_items = data[df].copy()
        elif df == 'orders':
            orders = data[df].copy()
        elif df == 'sellers':
            sellers = data[df].copy()
        elif df == 'customers':
            customers = data[df].copy()
        elif df == 'geolocation':
            geolocation = data[df].copy()
            geo = geolocation.groupby('geolocation_zip_code_prefix').first()

    orders_customers = orders[['order_id', 'customer_id']]
    df_customers = pd.merge(orders_customers, customers,how= 'inner', on='customer_id')
    df_customers = df_customers.drop('customer_city', axis=1)
    df_customers = df_customers.drop('customer_state', axis=1)
    df_customers = df_customers.rename(columns={'customer_zip_code_prefix':'geolocation_zip_code_prefix'})
    df_customers = pd.merge(df_customers, geo, how='inner', on='geolocation_zip_code_prefix')
    df_customers = df_customers.rename(columns={'geolocation_lat': 'lat_customer', 'geolocation_lng':'lng_customer'})
    df_sellers = pd.merge(orders_customers, order_items, how='inner', on='order_id')
    columnas_excluir = ['order_item_id','product_id','shipping_limit_date','price', 'freight_value']
    df_sellers = df_sellers.drop(columnas_excluir, axis=1)
    df_sellers = pd.merge(df_sellers, sellers, how='inner', on='seller_id')
    columnas_excluir = ['seller_city', 'seller_state']
    df_sellers = df_sellers.drop(columnas_excluir, axis=1)
    df_sellers = df_sellers.rename(columns={'seller_zip_code_prefix':'geolocation_zip_code_prefix'})
    df_sellers = pd.merge(df_sellers, geo, how='inner', on='geolocation_zip_code_prefix')
    columnas_excluir = ['customer_id', 'geolocation_city','geolocation_state']
    df_sellers = df_sellers.drop(columnas_excluir, axis=1)
    df_sellers = df_sellers.rename(columns={'geolocation_lat': 'lat_seller', 'geolocation_lng':'lng_seller'})
    df_final = pd.merge(df_customers, df_sellers, how='inner', on='order_id')
    df_final = df_final.dropna()
    df_final['lat_seller'] = pd.to_numeric(df_final['lat_seller'], errors = 'coerce')
    df_final['lng_seller'] = pd.to_numeric(df_final['lng_seller'], errors = 'coerce')
    df_final['lat_customer'] = pd.to_numeric(df_final['lat_customer'], errors = 'coerce')
    df_final['lng_customer'] = pd.to_numeric(df_final['lng_customer'], errors = 'coerce')
    
    distances = []
    for index, row in df_final.iterrows():
        distance = haversine_distance(row['lng_customer'], row['lat_customer'], row['lng_seller'], row['lat_seller'])
        distances.append(distance)
    df_final['distancia_a_la_orden'] = distances

    return df_final[['order_id','distancia_a_la_orden']]





    








