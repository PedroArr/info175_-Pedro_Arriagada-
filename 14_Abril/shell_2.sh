#! /bin/bash

VALID_PASSWORD="password"

echo "Ingrese la password"
read password

#Importante los espacio al inicio y al final
if [ $password == $VALID_PASSWORD ]; then
	echo "Acceso concedido"
else
	echo "Acceso denegado"
fi