#Build an Arithmetic Formatter Project

"""The function will return the correct conversion if the supplied problems
 are properly formatted, otherwise, it will return a string that describes 
 an error that is meaningful to the user."""

def arithmetic_arranger(problems, show_answers=False):

    """If there are too many problems supplied to the function. 
    The limit is five, anything more will return: 'Error: Too many problems.'"""
    # Debería poder comprobar esto con la longitud del array problems
    if len(problems)>5:
        return 'Error: Too many problems.'

    """The appropriate operators the function will accept are addition and 
    subtraction. Multiplication and division will return an error. 
    Other operators not mentioned in this bullet point will not 
    need to be tested. The error returned will be: "Error: Operator 
    must be '+' or '-'."""
    # Para llegar a hacer esto debería descomponer cada elemento del array
    operacion = []
    for problem in problems:
        print(problem)
          ## Igual podría usar finds en vez de un bucle
        primer_espacio = problem.find(" ")
        primer_operando = problem[0:problem.find(" ")]        
        # Tengo que añadir 1 para que busque el siguiente
        segundo_espacio = problem.find(" ",primer_espacio+1) 
        operador = problem[primer_espacio+1:segundo_espacio] 

        # Aquí ya puedo hacer la comprobación de si el operador es '+' or '-' 
        if operador != '+' and operador != '-':
            return "Error: Operator must be '+' or '-'."

        segundo_operando = problem[segundo_espacio+1:]
        
        ## Guardo en un diccionario y lo añado al array
        # expenses.append({'amount': amount, 'category': category})
        operacion.append({'primer_operando':primer_operando,'operador':operador,'segundo_operando':segundo_operando})

    print(operacion)




    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["32 * 698", "3801 / 2", "45 + 43", "123 + 49"])}')