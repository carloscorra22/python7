from operaciones import op

def main():
    sumar = op.suma(2, 3)
    restar = op.resta(9, 7)
    multiplica = op.multiplicar(5, 5)
    divide = op.dividir(10, 2)
    print("El resultado es:", sumar, restar, multiplica, divide)


if __name__ == '__main__':
    main()

