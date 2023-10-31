solicitud = input("¿desea solicitar asistencia? (responda si o no)")

if solicitud == "si":
    numero = input("por favor proporcione su numero telefonico y lo contactaremos ")
    print("Su solicitud ha sido recibida, en breve un ejecutivo se contactará con usted")
    
elif solicitud == "no":
    print("gracias por su preferencia, en caso de problemas contacte al correo de ayuda")
else: 
    print("error en la solicitud, intente de nuevo más tarde")
    