import sqlite3

miConexion=sqlite3.connect("tejido")

mitejido=miConexion.TejidoMama()

mitejido.execute("CREATE TABLE TEJIDO (PARTP_NUMERO INTEGER, TEMPERATURA FLOAT , COLOR FLOAT ,INFLAMACION FLOAT)")

miConexion.close()