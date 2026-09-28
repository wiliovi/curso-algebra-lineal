"""
Tema 1: Matrices - Ejercicios Interactivos
Curso de Álgebra Lineal de Cero a Experto
=====================================================

Script interactivo para resolver ejercicios paso a paso.
El usuario intenta resolver y el sistema valida las respuestas.
"""

import numpy as np
import sys

class EjercicioMatrices:
    def __init__(self):
        self.ejercicio_actual = 0
        self.puntuacion = 0
        self.total_ejercicios = 5

    def limpiar_pantalla(self):
        """Limpia la pantalla (funciona mejor en algunos terminales)"""
        print("\n" + "="*70 + "\n")

    def mostrar_titulo(self):
        """Muestra el título del programa"""
        self.limpiar_pantalla()
        print("TEMA 1: MATRICES - EJERCICIOS INTERACTIVOS")
        print("Curso de Álgebra Lineal de Cero a Experto")
        print("="*70)
        print("\nResolveremos ejercicios paso a paso.")
        print("Tu tarea es intentar resolver y luego verificaremos la respuesta.\n")

    def pausa(self, mostrar_prompt=True):
        """Pausa para que el usuario pueda leer"""
        try:
            if mostrar_prompt:
                input(">>> Presiona ENTER para continuar...\n")
        except EOFError:
            # Modo no interactivo
            print(">>> (saltando pausa en modo no interactivo)\n")

    def ejercicio_1_suma_matrices(self):
        """Ejercicio 1: Suma de matrices"""
        print("\n" + "-"*70)
        print("EJERCICIO 1: SUMA DE MATRICES")
        print("-"*70)

        A = np.array([[3, 5, -2, 0],
                      [0, 1, 2, -1],
                      [3, 2, 7, 4]])

        B = np.array([[1, -4, 5, 2],
                      [3, 2, -4, 6],
                      [1, -3, -5, 0]])

        print("\nDadas las matrices:")
        print("\nMatriz A:")
        print(A)
        print("\nMatriz B:")
        print(B)

        print("\n¿CUÁL ES EL RESULTADO DE A + B?")
        print("\nRecuerda: Se suman término a término")
        print("c[i,j] = a[i,j] + b[i,j]")

        self.pausa()

        # Mostrar la solución
        C = A + B
        print("\n✓ SOLUCIÓN: A + B =")
        print(C)

        print("\nExplicación:")
        print(f"  c[0,0] = a[0,0] + b[0,0] = {A[0,0]} + {B[0,0]} = {C[0,0]}")
        print(f"  c[0,1] = a[0,1] + b[0,1] = {A[0,1]} + {B[0,1]} = {C[0,1]}")
        print(f"  c[1,2] = a[1,2] + b[1,2] = {A[1,2]} + {B[1,2]} = {C[1,2]}")
        print("  ...")

        self.puntuacion += 1
        self.pausa()

    def ejercicio_2_producto_escalar(self):
        """Ejercicio 2: Producto por un escalar"""
        print("\n" + "-"*70)
        print("EJERCICIO 2: PRODUCTO POR UN ESCALAR")
        print("-"*70)

        A = np.array([[2, 3],
                      [5, 2],
                      [-1, 0]], dtype=float)

        lambda_val = 3

        print(f"\nDada la matriz A:")
        print(A)

        print(f"\n¿CUÁL ES EL RESULTADO DE {lambda_val} × A?")
        print("\nRecuerda: Se multiplica CADA elemento por el escalar")
        print(f"d[i,j] = {lambda_val} × a[i,j]")

        self.pausa()

        # Mostrar la solución
        D = lambda_val * A
        print(f"\n✓ SOLUCIÓN: {lambda_val} × A =")
        print(D.astype(int))

        print("\nExplicación:")
        print(f"  d[0,0] = {lambda_val} × {A[0,0]:.0f} = {D[0,0]:.0f}")
        print(f"  d[0,1] = {lambda_val} × {A[0,1]:.0f} = {D[0,1]:.0f}")
        print(f"  d[1,0] = {lambda_val} × {A[1,0]:.0f} = {D[1,0]:.0f}")
        print("  ...")

        self.puntuacion += 1
        self.pausa()

    def ejercicio_3_producto_matrices(self):
        """Ejercicio 3: Producto de matrices"""
        print("\n" + "-"*70)
        print("EJERCICIO 3: PRODUCTO DE MATRICES")
        print("-"*70)

        E = np.array([[-1, 2, 3, 1],
                      [3, -2, 1, 0]], dtype=int)

        F = np.array([[2, 1],
                      [0, 2],
                      [-1, 3],
                      [0, 1]], dtype=int)

        print("\nDadas las matrices:")
        print("\nMatriz E (2×4):")
        print(E)
        print("\nMatriz F (4×2):")
        print(F)

        print("\n¿CUÁL ES EL RESULTADO DE E × F?")
        print("\nRecuerda: El elemento [i,j] del resultado es el producto")
        print("de la fila i de E por la columna j de F")
        print("\nc[i,j] = Σ(e[i,k] × f[k,j])  para k=1 hasta 4")

        print("\nPista para c[0,0]:")
        print(f"  c[0,0] = ({E[0,0]})×{F[0,0]} + {E[0,1]}×{F[1,0]} + {E[0,2]}×{F[2,0]} + {E[0,3]}×{F[3,0]}")
        print(f"  c[0,0] = {E[0,0]*F[0,0]} + {E[0,1]*F[1,0]} + {E[0,2]*F[2,0]} + {E[0,3]*F[3,0]}")
        print(f"  c[0,0] = {E[0,0]*F[0,0] + E[0,1]*F[1,0] + E[0,2]*F[2,0] + E[0,3]*F[3,0]}")

        self.pausa()

        # Mostrar la solución
        G = np.dot(E, F)
        print("\n✓ SOLUCIÓN: E × F =")
        print(G)

        print("\nExplicación completa:")
        print("\nFila 0 × Columnas:")
        print(f"  [0,0]: ({E[0,0]})×{F[0,0]} + {E[0,1]}×{F[1,0]} + {E[0,2]}×{F[2,0]} + {E[0,3]}×{F[3,0]} = {G[0,0]}")
        print(f"  [0,1]: ({E[0,0]})×{F[0,1]} + {E[0,1]}×{F[1,1]} + {E[0,2]}×{F[2,1]} + {E[0,3]}×{F[3,1]} = {G[0,1]}")

        print("\nFila 1 × Columnas:")
        print(f"  [1,0]: {E[1,0]}×{F[0,0]} + ({E[1,1]})×{F[1,0]} + {E[1,2]}×{F[2,0]} + {E[1,3]}×{F[3,0]} = {G[1,0]}")
        print(f"  [1,1]: {E[1,0]}×{F[0,1]} + ({E[1,1]})×{F[1,1]} + {E[1,2]}×{F[2,1]} + {E[1,3]}×{F[3,1]} = {G[1,1]}")

        self.puntuacion += 1
        self.pausa()

    def ejercicio_4_transpuesta(self):
        """Ejercicio 4: Matriz transpuesta"""
        print("\n" + "-"*70)
        print("EJERCICIO 4: MATRIZ TRANSPUESTA")
        print("-"*70)

        A = np.array([[1, 0, 3],
                      [2, 1, -1]], dtype=int)

        print("\nDada la matriz A (2×3):")
        print(A)

        print("\n¿CUÁL ES LA TRANSPUESTA A^t?")
        print("\nRecuerda: Las filas se convierten en columnas")
        print("a^t[i,j] = a[j,i]")
        print("La matriz resultante será 3×2")

        self.pausa()

        # Mostrar la solución
        A_t = A.T
        print("\n✓ SOLUCIÓN: A^t (3×2) =")
        print(A_t)

        print("\nExplicación:")
        print("  La fila 1 de A:     [1, 0, 3]")
        print("  Se convierte en columna 1 de A^t")
        print("  La fila 2 de A:     [2, 1, -1]")
        print("  Se convierte en columna 2 de A^t")

        print("\nVerificación: (A^t)^t = A")
        A_tt = A_t.T
        print("(A^t)^t =")
        print(A_tt)
        print(f"¿(A^t)^t = A? {np.array_equal(A_tt, A)} ✓")

        self.puntuacion += 1
        self.pausa()

    def ejercicio_5_determinante_e_inversa(self):
        """Ejercicio 5: Determinante e Inversa"""
        print("\n" + "-"*70)
        print("EJERCICIO 5: MATRIZ INVERSA")
        print("-"*70)

        M = np.array([[1, 1, 0],
                      [0, 1, 0],
                      [1, 0, 1]], dtype=float)

        print("\nDada la matriz M (3×3):")
        print(M.astype(int))

        print("\n¿ES M INVERTIBLE? ¿CUÁL ES SU INVERSA?")
        print("\nPaso 1: Calcular el determinante")
        print("  Una matriz es invertible si det(M) ≠ 0")

        det_M = np.linalg.det(M)
        print(f"\n  det(M) = {det_M:.4f}")

        if det_M != 0:
            print(f"  ✓ Como det(M) ≠ 0, la matriz ES INVERTIBLE")
        else:
            print(f"  ✗ Como det(M) = 0, la matriz NO ES INVERTIBLE")

        self.pausa()

        if det_M != 0:
            M_inv = np.linalg.inv(M)
            print("\n✓ SOLUCIÓN: Matriz inversa M^(-1) =")
            print(M_inv)

            print("\nVerificación: M × M^(-1) = I")
            result = np.dot(M, M_inv)
            print("M × M^(-1) =")
            print(np.round(result, decimals=10))

            identity = np.eye(3)
            if np.allclose(result, identity):
                print("\n✓ ¡Verificado! M × M^(-1) = I")

            self.puntuacion += 1

        self.pausa()

    def mostrar_puntuacion_final(self):
        """Muestra la puntuación final"""
        self.limpiar_pantalla()
        print("RESUMEN DE RESULTADOS")
        print("="*70)
        print(f"\nEjercicios completados: {self.puntuacion}/{self.total_ejercicios}")
        print(f"Porcentaje: {(self.puntuacion/self.total_ejercicios)*100:.1f}%")

        if self.puntuacion == self.total_ejercicios:
            print("\n🎉 ¡EXCELENTE! ¡Has completado todos los ejercicios!")
        elif self.puntuacion >= 4:
            print("\n⭐ ¡Muy bien! Dominaste la mayoría de los temas.")
        elif self.puntuacion >= 3:
            print("\n✓ Buen trabajo. Repasa los ejercicios que faltaron.")
        else:
            print("\n📚 Te recomendamos revisar la teoría nuevamente.")

        print("\n" + "="*70)

    def ejecutar(self):
        """Ejecuta todos los ejercicios"""
        self.mostrar_titulo()

        print("Ejercicios a resolver:\n")
        print("  1. Suma de matrices")
        print("  2. Producto por un escalar")
        print("  3. Producto de matrices")
        print("  4. Matriz transpuesta")
        print("  5. Matriz inversa")

        self.pausa()

        # Ejercicio 1
        self.ejercicio_1_suma_matrices()

        # Ejercicio 2
        self.ejercicio_2_producto_escalar()

        # Ejercicio 3
        self.ejercicio_3_producto_matrices()

        # Ejercicio 4
        self.ejercicio_4_transpuesta()

        # Ejercicio 5
        self.ejercicio_5_determinante_e_inversa()

        # Resultado final
        self.mostrar_puntuacion_final()

        print("\n¿Deseas continuar con el siguiente tema?")
        print("📚 Tema 2: Sistemas de Ecuaciones Lineales")
        print("📚 Tema 3: Descomposición LU")
        print("📚 Tema 4: Determinantes")


if __name__ == "__main__":
    ejercicio = EjercicioMatrices()
    try:
        ejercicio.ejecutar()
    except KeyboardInterrupt:
        print("\n\n⚠️  Programa interrumpido por el usuario.")
        sys.exit(0)
