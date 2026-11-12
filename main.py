from aritmetica import operaciones, division, multiplicacion, resta, suma
from es.entrada import recibir_opcion, recibir_entrada
from es.salida import producir_archivo

if __name__ == "__main__":
    print(f"{'*' * 6} MENU {'*' * 6}")

    historial = []

    while True:
        try:
            opcion = recibir_opcion("Introduce una opción: ", operaciones)
            a = recibir_entrada("Introduce un numero: ")
            b = recibir_entrada("Introduce otro numero: ")
            
            resultado = operaciones[opcion](a, b)
            
        except ValueError:
            print("Error: Ingresaste un valor que no se puede convertir a número (ValueError).")
        except KeyError:
            print("Error: La operación elegida no existe en el diccionario (KeyError).")
        except ZeroDivisionError:
            print("Error: Intento de división entre cero (ZeroDivisionError).")
        except (TypeError, NameError) as e:
            print(f"Error inesperado ({type(e).__name__}): {e}")
        else:
            historial.append({
                "Operacion": opcion,
                "A": a,
                "B": b
            })
            producir_archivo("historial.csv", historial)
            print(f"#=> {resultado}")
        finally:
            print("El programa continua\n")