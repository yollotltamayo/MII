import time

# from sympy import init_printing,
# init_printing()
import matplotlib.pyplot as plt
import numpy as np
import sympy

#
# def estiliza_string(fucn):
#     superscript_map = {"0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸",
#                        "9": "⁹", "x": "ˣ", "y": "ʸ", "z": "ᶻ"}
#     nuevo = ''
#     c = 0
#     p = len(fucn)
#
#     while c < p:
#         if fucn[c] == '*':
#             if fucn[c + 1] == '*':
#                 nuevo += superscript_map[fucn[c + 2]]
#                 c += 2
#         else:
#             nuevo += fucn[c]
#         c += 1
#     return nuevo
#
#
{
    #
    # print("Newton multivariable")
    # x, y = sympy.symbols('x y')
    #
    # f1 = sympy.sympify("x**2-y**2-1")
    # f2 = sympy.sympify("x**2+y**2+x*y-4")
    #
    # # derivadas parciales
    # f1x = sympy.diff(f1, x)
    # f1y = sympy.diff(f1, y)
    #
    # f2x = sympy.diff(f2, x)
    # f2y = sympy.diff(f2, y)
    #
    # # vector de las funciones iniciales
    # v = sympy.Matrix([[f1], [f2]])
    #
    # j = sympy.Matrix([[f1x, f1y],
    #                   [f2x, f2y]])
    #
    # j_inv = j ** -1  # inversa,de la jacobiana
    #
    # jaco = sympy.lambdify([x, y], j_inv, 'numpy')
    # fxfy = sympy.lambdify([x, y], v, 'numpy')
    #
    # x = np.ones((2, 1))
    #
    # iteraciones = 1000
    #
    # start = time.time()
    #
    # for n in range(iteraciones):
    #     j = jaco(x[0][0], x[1][0]).dot(fxfy(x[0][0], x[1][0]))
    #     x = x - j
    # sol = fxfy(x[0][0], x[1][0])
    #
    # print(sol)
    # print(f'{float(sol[0]):.6f}')
    #
    # end = time.time()
    # # print(end - start)
    # print(x)

    # print((' '.join(map(str, j))))

    # -----------------------------------------------------------------------------------------

    # import sympy
    # from sympy import *
    # import time
    #
    # # Calculando valores
    #
    # iteraciones = 10000
    # resul = {'titulos': ['n', 'Xn', 'Yn', 'f(x, y)', 'g(x, y)'], 'filas': []}
    #
    # x, y = sympy.symbols('x y')
    #
    # # Ejemplos de Curiel
    # funx = "x**2-10*x+y**2+8"
    # funy = "x*y**2+x-10*y+8"
    #
    # # despejes
    # fx = "(x**2+y**2+8)/(10)"
    # fy = "(x*y**2+x+8)/(10)"
    #
    # x0 = 0
    # y0 = 0
    #
    # fux = sympy.sympify(funx)
    # fuy = sympy.sympify(funy)
    #
    # fxx = sympy.sympify(fx)
    # fyy = sympy.sympify(fy)
    #
    # #-------------------------------------------
    # start = time.time()
    #
    # fxn = sympy.lambdify([x,y], fux, "numpy")
    # fyn = sympy.lambdify([x,y], fuy, "numpy")
    #
    # fxxn = sympy.lambdify([x,y], fx, "numpy")
    # fyyn = sympy.lambdify([x,y], fy, "numpy")
    #
    #
    # for q in range(1, iteraciones + 1):
    #
    #     x0 = fxxn(x0, y0)
    #     y0 = fyyn(x0, y0)
    #
    #     num = fxn(x0, y0)
    #     num2 = fyn(x0, y0)
    #
    #     print(q, x0, y0, num, num2)
    #     resul['filas'].append([q, x0, y0, num, num2])
    #
    # end = time.time()
    # print(end - start)
# }
# -----------------------------------------
# print("Polinomio de Lagrange")
# #         x|f(x)
# #        -------
# #         0|1
#
# start = time.time()
# datos = [(1, 1),
#          (2, 8),
#          (3, 27)]
# grado = 0
#
# x = sympy.symbols('x')
#
#
# def poli_lag(grado, datos):
#     x = sympy.symbols('x')
#     resul = ""
#
#     for i in range(0, grado + 1):
#         resul += f"{datos[i][1]}"
#         for j in range(0, grado + 1):
#             if j != i:
#                 resul += f"*((x-{datos[j][0]})/({datos[i][0]}-{datos[j][0]}))"
#
#         resul += '+'
#     resul = resul.strip("+")
#     print(resul)
#     return sympy.lambdify(x, resul, "math"), sympy.sympify(resul)
#
#
# f, fx = poli_lag(len(datos) - 1, datos)
#
# t = np.arange(datos[0][0] - 2, datos[-1][0] + 2, (datos[1][0] - datos[0][0]) / 5)
# s = []
# m = []
# gx = "x**3"
# g = sympy.lambdify(x, gx, "math")
# for n in t:
#     s.append(f(n))
#     m.append(g(n))
#
# fig, ax = plt.subplots()
# plt.rc_context({"axes.titlesize": "large", 'legend.fontsize': 'large'})
#
# ax.plot(t, s, label=f'Polinomio de Lagrange = {estiliza_string(str(sympy.simplify(fx)))}', color='#40E0D0')
# ax.plot(t, m, label=f'Función Original = {estiliza_string(gx)}', color='green')
#
# for n in range(len(datos) - 1):
#     plt.plot(datos[n][0], datos[n][1], marker='o', markersize=5, color="red")
# plt.plot(datos[-1][0], datos[-1][1], marker='o', markersize=5, color="red", label=f"Puntos dados")
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.grid(color="gray")
# plt.legend(loc='best')
# # plt.tight_layout()
#
# print("Simplificando: ", estiliza_string(str(sympy.simplify(fx))))
# print("Todo en " + str(time.time() - start) + " segundos.")
# plt.show()
