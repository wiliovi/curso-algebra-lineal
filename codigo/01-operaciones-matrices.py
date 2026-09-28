"""
Tema 1: Matrices - Ejercicios de Operaciones Básicas
Curso de Álgebra Lineal de Cero a Experto
=====================================================

Este script contiene ejercicios prácticos sobre operaciones con matrices
usando Python y NumPy.
"""

import numpy as np

print("=" * 70)
print("TEMA 1: MATRICES - EJERCICIOS DE OPERACIONES BÁSICAS")
print("=" * 70)

# ============================================================================
# 1. CREAR MATRICES
# ============================================================================
print("\n1. CREAR MATRICES")
print("-" * 70)

# Matriz de ejemplo 1
A = np.array([[3, 5, -2, 0],
              [0, 1, 2, -1],
              [3, 2, 7, 4]])

print("Matriz A (3×4):")
print(A)
print(f"Dimensiones: {A.shape}")
print(f"Tipo: {A.dtype}")

# Matriz de ejemplo 2
B = np.array([[1, -4, 5, 2],
              [3, 2, -4, 6],
              [1, -3, -5, 0]])

print("\nMatriz B (3×4):")
print(B)

# ============================================================================
# 2. SUMA DE MATRICES
# ============================================================================
print("\n\n2. SUMA DE MATRICES")
print("-" * 70)

C = A + B
print("A + B =")
print(C)

print("\nVerificación: C = A + B, entonces c[0,0] = a[0,0] + b[0,0]")
print(f"c[0,0] = {C[0, 0]}, a[0,0] = {A[0, 0]}, b[0,0] = {B[0, 0]}")
print(f"Verificación: {A[0, 0]} + {B[0, 0]} = {C[0, 0]} ✓")

# ============================================================================
# 3. PRODUCTO POR UN ESCALAR
# ============================================================================
print("\n\n3. PRODUCTO POR UN ESCALAR")
print("-" * 70)

lambda_val = 3
D = lambda_val * A

print(f"λ = {lambda_val}")
print(f"\n{lambda_val} × A =")
print(D)

print(f"\nVerificación: d[0,0] = {lambda_val} × {A[0, 0]} = {D[0, 0]} ✓")

# ============================================================================
# 4. PRODUCTO DE MATRICES
# ============================================================================
print("\n\n4. PRODUCTO DE MATRICES")
print("-" * 70)

# Crear matrices compatibles para multiplicación
E = np.array([[-1, 2, 3, 1],
              [3, -2, 1, 0]])

F = np.array([[2, 1],
              [0, 2],
              [-1, 3],
              [0, 1]])

print("Matriz E (2×4):")
print(E)
print("\nMatriz F (4×2):")
print(F)

# Producto E × F debe dar 2×2
G = np.dot(E, F)

print(f"\nE × F =")
print(G)

print(f"\nVerificación del cálculo [0,0]:")
print(f"g[0,0] = e[0,0]×f[0,0] + e[0,1]×f[1,0] + e[0,2]×f[2,0] + e[0,3]×f[3,0]")
print(f"g[0,0] = (-1)×2 + 2×0 + 3×(-1) + 1×0")
print(f"g[0,0] = -2 + 0 - 3 + 0 = {G[0, 0]} ✓")

# ============================================================================
# 5. PROPIEDAD NO CONMUTATIVA
# ============================================================================
print("\n\n5. PROPIEDAD NO CONMUTATIVA: AB ≠ BA")
print("-" * 70)

H = np.array([[0, 1],
              [0, 0]])

I = np.array([[0, 0],
              [1, 0]])

print("Matriz H:")
print(H)
print("\nMatriz I:")
print(I)

HI = np.dot(H, I)
IH = np.dot(I, H)

print("\nH × I =")
print(HI)

print("\nI × H =")
print(IH)

print(f"\n¿H × I = I × H? {np.array_equal(HI, IH)} ✗")
print("Esto demuestra que el producto de matrices NO es conmutativo")

# ============================================================================
# 6. MATRIZ TRANSPUESTA
# ============================================================================
print("\n\n6. MATRIZ TRANSPUESTA")
print("-" * 70)

J = np.array([[1, 0, 3],
              [2, 1, -1]])

print("Matriz J (2×3):")
print(J)

J_t = J.T

print("\nMatriz transpuesta J^t (3×2):")
print(J_t)

print(f"\nVerificación: (J^t)^t = J")
J_tt = J_t.T
print("(J^t)^t =")
print(J_tt)
print(f"¿(J^t)^t = J? {np.array_equal(J_tt, J)} ✓")

# ============================================================================
# 7. TRAZA DE UNA MATRIZ
# ============================================================================
print("\n\n7. TRAZA DE UNA MATRIZ (solo matrices cuadradas)")
print("-" * 70)

K = np.array([[1, 2, 3],
              [-1, -2, 5],
              [1, -3, 7]])

print("Matriz K (3×3):")
print(K)

traza = np.trace(K)

print(f"\ntr(K) = k[0,0] + k[1,1] + k[2,2]")
print(f"tr(K) = {K[0, 0]} + ({K[1, 1]}) + {K[2, 2]}")
print(f"tr(K) = {traza}")

# ============================================================================
# 8. MATRIZ IDENTIDAD
# ============================================================================
print("\n\n8. MATRIZ IDENTIDAD")
print("-" * 70)

I_2 = np.eye(2, dtype=int)
I_3 = np.eye(3, dtype=int)

print("Matriz identidad I_2:")
print(I_2)

print("\nMatriz identidad I_3:")
print(I_3)

# Verificar propiedad: A × I_n = A
L = np.array([[2, 3],
              [-1, 0]])

L_result = np.dot(L, I_2)

print(f"\nVerificación: A × I_2 = A")
print("Matriz L:")
print(L)
print("\nL × I_2 =")
print(L_result)
print(f"¿L × I_2 = L? {np.array_equal(L_result, L)} ✓")

# ============================================================================
# 9. MATRIZ INVERSA
# ============================================================================
print("\n\n9. MATRIZ INVERSA")
print("-" * 70)

M = np.array([[1, 1, 0],
              [0, 1, 0],
              [1, 0, 1]], dtype=float)

print("Matriz M (3×3):")
print(M)

# Calcular determinante (necesario para inversibilidad)
det_M = np.linalg.det(M)
print(f"\nDeterminante de M: {det_M:.4f}")

if det_M != 0:
    M_inv = np.linalg.inv(M)
    print("\nMatriz inversa M^(-1):")
    print(M_inv)

    # Verificar: M × M^(-1) = I
    result = np.dot(M, M_inv)
    print("\nVerificación: M × M^(-1) =")
    print(np.round(result, decimals=10))  # Redondear para evitar errores numéricos
    print(f"¿M × M^(-1) = I? {np.allclose(result, np.eye(3))} ✓")
else:
    print("La matriz M es singular (no invertible)")

# ============================================================================
# 10. RANGO DE UNA MATRIZ
# ============================================================================
print("\n\n10. RANGO DE UNA MATRIZ")
print("-" * 70)

N = np.array([[1, 2, 3],
              [2, 4, 6],
              [1, 2, 3]], dtype=float)

print("Matriz N (3×3):")
print(N)

rango_N = np.linalg.matrix_rank(N)
print(f"\nRango de N: {rango_N}")
print("Nota: Las filas 1 y 3 son iguales, y la fila 2 es el doble de la fila 1")

O = np.array([[1, 0, 0, 2],
              [0, 1, 0, 1],
              [0, 0, 1, -1],
              [0, 0, 0, 0]], dtype=float)

print("\n\nMatriz O (escalonada reducida):")
print(O)

rango_O = np.linalg.matrix_rank(O)
print(f"\nRango de O: {rango_O}")
print("El rango es igual al número de filas no nulas (pivotes)")

# ============================================================================
# EJERCICIOS PROPUESTOS
# ============================================================================
print("\n\n" + "=" * 70)
print("EJERCICIOS PROPUESTOS")
print("=" * 70)

print("""
1. Dadas las matrices:
   A = [[2, 3],
        [5, 2]]

   B = [[1, 0, -1],
        [2, 3, 5]]

   Calcula:
   a) 3A
   b) A + A
   c) AB
   d) Verifica que (AB)^t = B^t A^t

2. Dada la matriz:
   C = [[1, 2, 3],
        [0, 1, 4],
        [5, 6, 0]]

   a) Encuentra su rango
   b) Calcula su traza
   c) Verifica si es invertible
   d) Si es invertible, calcula su inversa y verifica C × C^(-1) = I

3. Demuestra que el producto de matrices NO es conmutativo usando
   las matrices H e I del ejemplo anterior.

4. Para las matrices diagonales:
   D1 = [[2, 0, 0],
         [0, -3, 0],
         [0, 0, 5]]

   D2 = [[1, 0, 0],
         [0, 4, 0],
         [0, 0, -2]]

   a) Calcula D1 × D2
   b) Calcula D2 × D1
   c) ¿Son iguales? ¿Por qué?
""")

# ============================================================================
# SOLUCIONES DE LOS EJERCICIOS
# ============================================================================
print("\n" + "=" * 70)
print("SOLUCIONES DE LOS EJERCICIOS PROPUESTOS")
print("=" * 70)

print("\n1. Ejercicio 1:")
A_ej = np.array([[2, 3],
                 [5, 2]])

B_ej = np.array([[1, 0, -1],
                 [2, 3, 5]])

print("\nMatriz A:")
print(A_ej)
print("\nMatriz B:")
print(B_ej)

print("\na) 3A =")
print(3 * A_ej)

print("\nb) A + A =")
print(A_ej + A_ej)

print("\nc) AB =")
AB_ej = np.dot(A_ej, B_ej)
print(AB_ej)

print("\nd) Verificación de (AB)^t = B^t A^t:")
AB_t = AB_ej.T
B_t_A_t = np.dot(B_ej.T, A_ej.T)
print("(AB)^t =")
print(AB_t)
print("\nB^t A^t =")
print(B_t_A_t)
print(f"¿(AB)^t = B^t A^t? {np.array_equal(AB_t, B_t_A_t)} ✓")

print("\n" + "-" * 70)
print("\n2. Ejercicio 2:")
C_ej = np.array([[1, 2, 3],
                 [0, 1, 4],
                 [5, 6, 0]], dtype=float)

print("\nMatriz C:")
print(C_ej)

print(f"\na) Rango de C: {np.linalg.matrix_rank(C_ej)}")
print(f"\nb) Traza de C: {np.trace(C_ej)}")

det_C = np.linalg.det(C_ej)
print(f"\nc) Determinante de C: {det_C:.4f}")
print(f"   ¿Es invertible? {det_C != 0}")

if det_C != 0:
    C_inv = np.linalg.inv(C_ej)
    print("\nd) Matriz inversa C^(-1):")
    print(C_inv)

    result_C = np.dot(C_ej, C_inv)
    print("\n   Verificación: C × C^(-1) =")
    print(np.round(result_C, decimals=10))

print("\n" + "-" * 70)
print("\n4. Ejercicio 4 (matrices diagonales conmutan):")
D1_ej = np.array([[2, 0, 0],
                  [0, -3, 0],
                  [0, 0, 5]])

D2_ej = np.array([[1, 0, 0],
                  [0, 4, 0],
                  [0, 0, -2]])

print("\nMatriz D1:")
print(D1_ej)
print("\nMatriz D2:")
print(D2_ej)

D1D2 = np.dot(D1_ej, D2_ej)
D2D1 = np.dot(D2_ej, D1_ej)

print("\na) D1 × D2 =")
print(D1D2)

print("\nb) D2 × D1 =")
print(D2D1)

print(f"\nc) ¿D1 × D2 = D2 × D1? {np.array_equal(D1D2, D2D1)} ✓")
print("    Las matrices diagonales CONMUTAN (propiedad especial)")

print("\n" + "=" * 70)
print("FIN DEL SCRIPT")
print("=" * 70)
