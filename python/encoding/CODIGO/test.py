
import csv

SCHEMA = ""

def currentDate():
    return ""

def formatDocument(inputFile, sqlOutputFile, csvOutputFile=None):
        #with open(inputFile) as file:
        #    csvOutputFile.writelines(file) # Guarda info original para registro en csvOutputFile (sin problema)
        #csvOutputFile.close()
 
        with open(inputFile, "r") as f:  #He probado mil cosas!
            fileRows = csv.reader(f, delimiter="|")
            next(fileRows)                                                          # Salta Headers
            for row in fileRows:

                #print(row)

                idComercio = str(int(row[0])).strip()                              # NIP
                cuit = row[1].strip()                                               # CUIT
                tipoAlta = row[2][2:].strip()                                       # Ej: RESPONSABLE INSCRIPTO
               
                sqlOutputFile.write("{}INS_UPD_C5(\'{}\', \'{}\', \'{}\',  \'{}\');\n".format(SCHEMA, idComercio, cuit, tipoAlta, currentDate()))
        sqlOutputFile.write(u"UPDATE {}C5 SET COM_ESTADO = \'BAJA_SCRIPT\' WHERE COM_PROCESO_ACTUALIZACION < \'{}\';\n".format(SCHEMA, currentDate()))
        sqlOutputFile.write(u"COMMIT;\n")
        sqlOutputFile.write(u"END;\n")
        sqlOutputFile.write(u"/\n")
        sqlOutputFile.write(u"quit 0")
        sqlOutputFile.close()

with open("output.sql", "wb") as f:
    formatDocument("data.cvs", f)


