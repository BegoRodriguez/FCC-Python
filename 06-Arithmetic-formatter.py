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

    # Para llegar a hacer esto debería descomponer cada elemento del array
    first_row = ""
    second_row = ""
    third_row = ""
    fourth_row = ""
    for problem in problems:

          ## Igual podría usar finds en vez de un bucle
        primer_espacio = problem.find(" ")
        primer_operando = problem[0:primer_espacio]        
        # Tengo que añadir 1 para que busque el siguiente espacio
        segundo_espacio = problem.find(" ",primer_espacio+1)
        operador = problem[primer_espacio+1:segundo_espacio]
        segundo_operando = problem[segundo_espacio+1:]
        
        """The appropriate operators the function will accept are addition and 
        subtraction. Multiplication and division will return an error. 
        Other operators not mentioned in this bullet point will not 
        need to be tested. The error returned will be: "Error: Operator 
        must be '+' or '-'."""
        # Aquí ya puedo hacer la comprobación de si el operador es '+' or '-' 
        if operador != '+' and operador != '-':
            return "Error: Operator must be '+' or '-'."

        """Each number (operand) should only contain digits. Otherwise, 
        the function will return: 'Error: Numbers must only contain digits.'"""
        # ¿Cómo compruebo esto?
        if not(primer_operando.isdigit()) or not(segundo_operando.isdigit()):
            return "Error: Numbers must only contain digits."
        
        """Each operand (aka number on each side of the operator) has a max of 
        four digits in width. Otherwise, the error string returned will be: 
        'Error: Numbers cannot be more than four digits.'"""
        len_primer_operando = len(primer_operando)
        len_segundo_operando = len(segundo_operando)
        # Puedo hacer esta comprobación con los operandos
        if len_primer_operando>4 or len_segundo_operando>4 :
           return "Error: Numbers cannot be more than four digits."

        # Comprobaciones realizadas, paso a formatear
        """If the user supplied the correct format of problems, 
        the conversion you return will follow these rules:
        There should be a single space between the operator and the longest of the 
        two operands, the operator will be on the same line as the second operand, 
        both operands will be in the same order as provided (the first will be the 
        top one and the second will be the bottom).
        Numbers should be right-aligned.
        There should be four spaces between each problem.
        There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)"""

        cadena_aux = "" + operador
        # Primero tengo que ver cual de los dos dígitos es mayor
        if (len_segundo_operando>len_primer_operando):
            
            cadena_aux = cadena_aux + " " + segundo_operando 
            second_row = second_row + cadena_aux + "    "
            diff = len(cadena_aux) - len(primer_operando)

            for d in range(diff):
                first_row += " "
            first_row += primer_operando + "    " # Los 4 espacios
       

        elif (len_segundo_operando<len_primer_operando):
      
            # Añadimos dos espacios a la primera cadena y el operando
            first_row += "  " + primer_operando + "    " # Los 4 espacios

            # Hay que calcular los espacios a añadir en la segunda cadena
            diff = len(primer_operando) - len(segundo_operando)
            for d in range(diff+1):
                cadena_aux += " "
            cadena_aux = cadena_aux + segundo_operando # Erroneo
            second_row = second_row + cadena_aux + "    "
            # Tendremos que calcular la segunda cadena más detalladamente
            
        else: 
            # Añadimos dos espacios a la primera cadena y el operando
            first_row += "  " + primer_operando + "    " # Los 4 espacios
            cadena_aux = cadena_aux + " " + segundo_operando 
            second_row = second_row + cadena_aux + "    "
           
        len_cadena_aux = len(cadena_aux)
        # Depende de si la primera o la segunda cadena es la mayor
        for c in range(len_cadena_aux):
            third_row += "-"
        third_row += "    " # Los 4 espacios

        """When the second argument is set to True, the answers should be displayed."""
        # voy a hacer una cuarta fila que solo se rellene si hay que mostrar respuestas
        if show_answers:
            first = int(primer_operando)
            second = int(segundo_operando)
            resultado = 0
            if operador == "+":
                resultado = first+second
            else:
                resultado = first-second
            fourth_row = fourth_row + "  " + str(resultado) + "    " # Los 4 espacios
    
    if show_answers:
        return first_row[:-4]+"\n"+second_row[:-4]+"\n"+third_row[:-4]+"\n"+fourth_row[:-4]
    return first_row[:-4]+"\n"+second_row[:-4]+"\n"+third_row[:-4]

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True)}')