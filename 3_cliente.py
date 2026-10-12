import requests

URL_SERVIDOR = "http://127.0.0.1:5000/procesar_comando"

def inicio_cliente():
    print("\n" + "="*50)
    print("🤖 J.A.R.V.I.S. SISTEMA DE SEGURIDAD POR PIN")
    print("==================================================")
    
    while True:
        try:
            # 1. Ingresar contraseña
            pin = input("\n🔑 Ingresá tu PIN de acceso: ")

            if not pin.strip():
                continue

            # 2. Ingresar la orden
            comando_texto = input("⌨️  Escribí tu orden (ej: 'abrir spotify'): ")

            if not comando_texto.strip():
                continue

            payload = {
                "pin": pin,
                "texto": comando_texto
            }

            print("📡 Verificando credenciales...")
            respuesta = requests.post(URL_SERVIDOR, json=payload)

            if respuesta.status_code == 200:
                resultado = respuesta.json()
                print("\n✅ ACCESO PERMITIDO")
                print(f"🤖 J.A.R.V.I.S.: {resultado['respuesta']}")
            else:
                error = respuesta.json()
                print("\n⛔ ACCESO DENEGADO")
                print(f"Motivo: {error.get('message')}")

        except KeyboardInterrupt:
            print("\nDesconectando sistema...")
            break
        except Exception as e:
            print(f"❌ Error de conexión: {e}")

if __name__ == "__main__":
    inicio_cliente()