from flask import Flask, render_template, request, jsonify, redirect, url_for
import json
import re
import math

app = Flask(__name__)




@app.route('/')
def index():
    
    return render_template('index.html')

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'ponto']
operators = ['divisao', 'mutiplicacao', 'subtracao', 'adicao']

dict_valores = {
    
    'num1': '',
    'op': '', 
    'num2': '',
    'resultado': ''
}


resultado = 0

def calculo(numero1, numero2, op):

    if op == 'adicao':
        operacao = float(numero1) + float(numero2)
        operacao = round(operacao,5)
    elif op == 'subtracao':
        operacao = float(numero1) - float(numero2)
        operacao = round(operacao,5)
    elif op == 'mutiplicacao':
        operacao = float(numero1) * float(numero2)
        operacao = round(operacao,5)
    elif op == 'divisao':
        if numero2 == '0':
            return 'Erro'
        else:
            operacao = float(numero1) / float(numero2)
            operacao = round(operacao,5)
    elif op == 'raiz' and numero2 == None:
        if float(numero1) < 0:
            return 'Erro'
        else:
            operacao = math.sqrt(float(numero1))
            operacao = round(operacao,2)
    elif op == 'porcentagem' and numero2 == None:
        operacao = float(numero1)/100
    
    print(operacao)
    
    if str(operacao)[-1] == '0' and str(operacao)[-2] == '.':
        operacao = int(operacao)
        
    return operacao
            
def estrutura_calculo(valor):
    
    global resultado
    
    if valor in numbers and dict_valores.get('op') == '':
        if valor == 'ponto' and dict_valores.get('num1') != '':
            if '.' not in dict_valores.get('num1'):
                numero = dict_valores.get('num1') + '.'
                dict_valores.update({'num1': numero})
        else:
            if valor != 'ponto':
                
                if len(dict_valores.get('num1')) == 1 and dict_valores.get('num1')[0] == '0':
                    numero = dict_valores.get('num1')
                    numero  = numero + '.' + valor
                    dict_valores.update({'num1': numero})
                    
                else:
                    numero = dict_valores.get('num1') + valor
                    dict_valores.update({'num1': numero})
                
                
            
    elif valor in numbers and dict_valores.get('op') != '':
        if valor == 'ponto'and dict_valores.get('num2') != '':
            if '.' not in dict_valores.get('num2'):
                numero = dict_valores.get('num2') + '.'
                dict_valores.update({'num2': numero})
                
        else:
            if valor != 'ponto':
                
                numero = dict_valores.get('num2') + valor
                dict_valores.update({'num2': numero})
                
                if dict_valores.get('num2')[0] == '0' and '.' not in dict_valores.get('num2') and len(dict_valores.get('num2')) >= 2:
                    
                    
                    numero = list(dict_valores.get('num2'))
                    numero.insert(1,'.')
                    numero = ''.join(numero)
                    
                    dict_valores.update({'num2': numero})
                    
                    #realiza calculo
                    
                    if dict_valores.get('num1') == '':
                        dict_valores.update({'num1': 0})
                        
        
                        resultado = calculo(dict_valores.get('num1'), dict_valores.get('num2'), dict_valores.get('op'))
                        
                        if resultado == 'Erro':
                            
                            dict_result = {
                            'valor': 'Não foi possível fazer divisão por 0.',
                            'data': True
                            }
                        
                            
                            return dict_result
                        else:
                            dict_valores.update({'resultado': resultado})
                        
                            
                    else:
                        
                        resultado = calculo(dict_valores.get('num1'), dict_valores.get('num2'), dict_valores.get('op'))
                        
                        if resultado == 'Erro':
                            
                            dict_result = {
                            'valor': 'Não foi possível fazer divisão por 0.',
                            'data': True
                            }
                            
                            return dict_result
                        else:
                            dict_valores.update({'resultado': resultado})
                            
                            
                else:
                    
                    if dict_valores.get('num1') == '':
                        dict_valores.update({'num1': 0})
                        
        
                        resultado = calculo(dict_valores.get('num1'), dict_valores.get('num2'), dict_valores.get('op'))
                        
                        if resultado == 'Erro':
                            
                            dict_result = {
                            'valor': 'Não foi possível fazer divisão por 0.',
                            'data': True
                            }
                        
                            
                            return dict_result
                        else:
                            dict_valores.update({'resultado': resultado})
                        
                            
                    else:
                        
                        resultado = calculo(dict_valores.get('num1'), dict_valores.get('num2'), dict_valores.get('op'))
                        
                        if resultado == 'Erro':
                            
                            dict_result = {
                            'valor': 'Não foi possível fazer divisão por 0.',
                            'data': True
                            }
                            
                            return dict_result
                        else:
                            dict_valores.update({'resultado': resultado})
                    
                    
    elif valor in operators and dict_valores.get('resultado') == '':
        if valor == 'subtracao':        
            if dict_valores.get('num1') == '':
                dict_valores.update({'num1': '-'})
            else:
                dict_valores.update({'op': valor})
                
        else:
            dict_valores.update({'op': valor})
            
    
    elif dict_valores.get('resultado') != '' and valor in operators:
        dict_valores.update({'num1': resultado})
        dict_valores.update({'op': valor})
        dict_valores.update({'num2': ''})
        dict_valores.update({'resultado': ''})
        
    elif valor == 'C':
        dict_valores.update({'num1': '','op': '', 'num2': '', 'resultado': ''})
        
        return '0'
    
    elif valor == 'reload':
        
        dict_valores.update({'num1': '','op': '', 'num2': '', 'resultado': ''})
        
        return '0'
        
    
    elif valor == 'total':
        
        if dict_valores.get('resultado') != '':
        
            resp = str(dict_valores.get('resultado'))
            
            dict_result = {
                'valor': resp,
                'data': True
            }
            
            dict_valores.update({'num1': resp})
            dict_valores.update({'op': ''})
            dict_valores.update({'num2': ''})
            dict_valores.update({'resultado': ''})
            
            return dict_result
            
            
        elif dict_valores.get('resultado') == 'Raíz inválida!':
            
            dict_result = {
                'valor': 'Raíz inválida!',
                'data': True
            }
            
            return dict_result
        
        elif dict_valores.get('resultado') == 'Porcentagem inválida!':
            
            dict_result = {
                'valor': 'Porcentagem inválida!',
                'data': True
            }
            return dict_result
        
            
    
    elif valor == 'raiz':
        if dict_valores.get('num1') != '' and dict_valores.get('resultado') == '' and dict_valores.get('num2') == '':
            dict_valores.update({'op': valor})
            
            resultado = calculo(dict_valores.get('num1'),None, dict_valores.get('op'))
            
            if resultado == 'Erro':
                
                dict_result = {
                'valor': 'Raíz inválida!',
                'data': True
                }
                
                return dict_result

            else:
               
                num1 = dict_valores.get('num1')
                op = dict_valores.get('op')
                
                dict_result = {'num1': num1, 
                                'op': op, 
                                'resultado': resultado }
                
                dict_valores.update({'resultado': ''})
                dict_valores.update({'op': ''})
                dict_valores.update({'num1': ''})
            
                
                
                return dict_result
                
                
                         
            
            
        elif dict_valores.get('resultado') != '':
            dict_valores.update({'op': valor})
            
            resultado = dict_valores.get('resultado')            
            dict_valores.update({'num1': resultado})
            
            resultado = calculo(dict_valores.get('num1'),None, dict_valores.get('op'))
            
            if resultado == 'Erro':
                
                dict_result = {
                'valor': 'Raíz inválida!',
                'data': True
                }
                
                return dict_result
            
            else:
                dict_valores.update({'num2': ''})
                dict_valores.update({'resultado': resultado})
        
    elif valor == 'porcentagem':
        
        if dict_valores.get('num1') != '' and dict_valores.get('resultado') == '':
            dict_valores.update({'op': valor})
            
            resultado = calculo(dict_valores.get('num1'),None, dict_valores.get('op'))
            
            if resultado == 'Erro':
                
                dict_result = {
                'valor': 'Porcentagem inválida!',
                'data': True
                }
                
                return dict_result

            else:
                dict_valores.update({'resultado': resultado})
        
        
        elif dict_valores.get('resultado') != '':
            
            dict_valores.update({'op': valor})
            
            resultado = dict_valores.get('resultado')            
            dict_valores.update({'num1': resultado})
            
            resultado = calculo(dict_valores.get('num1'),None, dict_valores.get('op'))
            
            if resultado == 'Erro':
                
                dict_result = {
                'valor': 'Porcentagem inválida!',
                'data': True
                }
                
                return dict_result
            
            else:
                dict_valores.update({'num2': ''})
                dict_valores.update({'resultado': resultado})
            
            
            
        
    
        
    return dict_valores

def ajusta_calculo(result): 
    texto = ''
    
    if result == '0':
        texto = '0'
        
    elif result.get('data') == True:
        texto = result.get('valor')
    
    else:
    
        for key, value in result.items():
            if key == 'resultado' and value != '':
                texto = texto + ' = ' + str(value)
            
            else:
                if value != '':
                    texto = texto + ' ' + str(value)
                
        texto = texto.replace('adicao', '+')
        texto = texto.replace('subtracao', '-')
        texto = texto.replace('mutiplicacao', '*')
        texto = texto.replace('divisao', '/')
        texto = texto.replace('raiz', '√')
        texto = texto.replace('porcentagem', '%') 
        
        
    return texto
     
@app.route('/calculadora', methods=['GET', 'POST'])
def calculadora():
    
    
    if request.method == 'POST':
        
        data = list(request.form)
        data = ''.join(data)

        
        result = estrutura_calculo(data)
        print(result)

        
        texto =  ajusta_calculo(result)

        
        return texto
        
    else:
        result = 'erro'
        return result
    

if __name__ == ('__main__'):
    app.run(debug=True)
