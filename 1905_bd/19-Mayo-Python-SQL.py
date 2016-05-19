#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import sqlite3 as lite
import sys
 
con = None
 
try:
    con = lite.connect("pos_empresa.db")
    cur = con.cursor()
    print("1. Cantidad de Ventas 2013:")
    cur.execute("select round(sum(gross_total)) from sale where [date] like '2013%';")
    filas = cur.fetchall()
    print(int(filas[0][0]))
    
    print("\n2.Precio promedio de venta por producto:")
    cur.execute("select avg(net_unit_price),product.name from sale_product join product ON product_id = product.id group by product_id limit 10;")
    filas = cur.fetchall()
    for fila in filas:
        print ("Precio:",int(fila[0]),"\tProducto:",fila[1])
        
    print("\n3.Total de ventas por cliente:")
    cur.execute("select sum(gross_total),entity.rut from sale join entity ON entity_id = entity.id group by entity.rut order by entity.rut limit 10;")
    filas = cur.fetchall()
    for fila in filas:
        print("Total de ventas:",int(fila[0])," \tRUT cliente:",fila[1])
        
    print("\n4.Total de ventas por cliente en 2014:")
    cur.execute("select sum(gross_total),entity.rut from sale join entity ON entity_id = entity.id where sale.date like '2014%' group by entity.rut order by entity.rut limit 10;")
    filas = cur.fetchall()
    for fila in filas:
        print("Total de ventas:",int(fila[0])," \tRUT cliente:",fila[1])
    
    print("\n5.Cantidad y monto total de ventas por dia, noviembre 2013:")
    cur.execute("select [date], count(*), sum(gross_total) from sale where [date] like '2014-11%' group by [date] limit 10;")
    filas = cur.fetchall()
    for fila in filas:
        print("Fecha:",fila[0],"\tCantidad:",fila[1],"\tMonto:",fila[2])
    
    print("\n6.Cantidad y montos totales agrupados por producto:")
    cur.execute("select sum(sale_product.quantity), sum(sale_product.gross_total), product.name from sale_product join product on product_id = product.id group by product.name order by sale_product.quantity desc limit 10;")
    filas = cur.fetchall()
    for fila in filas:
        print("Cantidad:",int(fila[0]),"\tMonto Total:",int(fila[1]),"\tProducto:",fila[2])
    
except (lite.Error, e):   
    print ("Error %s:" % e.args[0])
    sys.exit(1)
finally:    
    if con:
        con.close()
