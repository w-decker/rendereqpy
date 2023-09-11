# import
import rendereq as req

# latex
latex = '\\frac{x_1}{x_2}'

# execute
OUT = req.rendereq(latex=latex, filename='output', format='pdf')