# Proyecto Integrador - TSDS - ISPC
### Programación, Bases de Datos, Competencias Comunicacionales 2 


Éste es el proyecto integrador del grupo "Programando 18"
El nombre del proyecto es Mis Acciones

## Descripción

El Broker de Inversiones es una plataforma diseñada para facilitar la gestión de inversiones financieras. Los usuarios pueden registrarse y acceder a una interfaz amigable donde pueden comprar y vender acciones de manera intuitiva. La aplicación proporciona herramientas para monitorear el rendimiento de las inversiones y obtener insights mediante gráficos y estadísticas detalladas.

El objetivo principal de esta aplicación es ofrecer una experiencia de usuario fluida y eficiente para los inversores, permitiéndoles tomar decisiones informadas sobre sus portafolios.

## Funcionalidades

**Registro y Autenticación**: Los inversores pueden registrarse y autenticarse para acceder a su cuenta.
- **Gestión de Portafolio**: Los inversores pueden ver y gestionar su portafolio de inversiones.
- **Compra y Venta de Acciones**: Los usuarios pueden comprar y vender acciones a través de la plataforma.
- **Visualización de Datos**: Los usuarios pueden ver los montos, ganancias y pérdidas de sus inversiones.
- **Recuperación de Contraseña**: Los usuarios pueden recuperar su contraseña en caso de olvido.

## Instalación
1. Clona el repositorio:
   ```bash
   git clone https://github.com/programando18/proyecto_integrador_broker
   ```
2. Navega hasta la ubicación correcta
   ```bash
   cd proyecto_integrador/programacion/mis_acciones
   ```
3. Instalar dependencias de Python
   ```bash
   pip install -r requirements.txt
   ```
4. Modificar archivo config.json para acceder a la Base de Datos
   ```bash
   cd core/config
   ```
   *abrir config.json con tu editor de texto y reemplazar user y password de ser necesario
   
6. Poblar Base de Datos
   ```bash
   cd ..
   python setup/poblar_bbdd.py
   ```
7. (Opcional) Correr simulador de variación de precios (en terminal separada para que corra en segundo plano)
   ```bash
   python setup/simulador.py
   ```
   Éste script simula una variación de precios de compra en las acciones disponibles. Cada 60 segundos, las acciones cambian de precio.
   Si no se ejecuta, la variable Rendimiento en el Portafolio no va a mostrar ningun cambio.
9. Ejecutar app
   ```bash
   python main.py
   ```

## Equipo de trabajo

### Franco Bulacio

### Milagros Magaly Cabrera

### Evelin Andrea Checa

### Christian Caracach
