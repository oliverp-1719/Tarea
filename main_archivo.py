from aritmetica import operaciones, division, multiplicacion, resta, suma
from es.entrada import recibir_opcion, recibir_entrada, validar_entrada, validar_opcion, recibir_ruta, procesar_archivo

if __name__ == "__main__":
    print(f"{'*' * 6} MENU {'*' * 6}")

    try:
        ruta = recibir_ruta("Introduce la dirección de un archivo: ")
        
        for fila in procesar_archivo(ruta):
            try:
                opcion = validar_opcion(fila["Operacion"], operaciones)
                a = validar_entrada(fila["A"])
                b = validar_entrada(fila["B"])
                
                resultado = operaciones[opcion](a, b)
                
            except ValueError:
                print(f"Error en fila: El valor no es un número válido (ValueError). Fila: {fila}")
            except KeyError:
                print(f"Error en fila: La operación no existe (KeyError). Fila: {fila}")
            except ZeroDivisionError:
                print(f"Error en fila: División entre cero (ZeroDivisionError). Fila: {fila}")
            except (TypeError, NameError) as e:
                print(f"Error inesperado en fila ({type(e).__name__}): {e}")
            else:
                print(f"#=> {resultado}")
            finally:
                print("El programa continua\n")
                
    except Exception as e:
        print(f"Error crítico al intentar abrir o leer el archivo: {e}")