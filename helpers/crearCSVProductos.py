import csv

def crearCSV(lista, nombreCSV):
<<<<<<< HEAD
     with open('data/' +nombreCSV, mode='w', newline='', encoding='utf-8') as archivo_csv:
          writer=csv.writer(archivo_csv)
          writer.writerow(['Id', 'Nombre', 'CostoUnitario', 'Iva'])
          writer.writerows(lista)
=======
    with open('data/' +nombreCSV, mode='w', newline='', encoding='utf-8') as archivo_csv:
        writer=csv.writer(archivo_csv)
        writer.writerow(['Id', 'Nombre', 'CostoUnitario', 'Iva'])
        writer.writerows(lista)
>>>>>>> eeef6a0a1f5217f1efbf1a13761203d470ec9a66
