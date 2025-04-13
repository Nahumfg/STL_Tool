import subprocess
import sys

def instalar_dependencias():
    """
    Instala las dependencias necesarias para el programa usando pip.
    """
    try:
        # Lista de dependencias
        dependencias = ["wxPython", "numpy", "pyvista", "numpy-stl", "pyperclip"]

        # Instalar cada dependencia
        for paquete in dependencias:
            print(f"Instalando {paquete}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", paquete])
        print("\nTodas las dependencias se instalaron correctamente.")

    except Exception as e:
        print(f"\nError al instalar las dependencias: {e}")

if __name__ == "__main__":
    instalar_dependencias()
