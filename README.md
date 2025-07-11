# Proyecto con SQLAlchemy + Alembic + PostgreSQL

Este proyecto usa **SQLAlchemy** como ORM y **Alembic** para las migraciones, conectando a una base de datos **PostgreSQL**.

---

## 🔧 Configuración rápida

1. **Copia y edita la configuración**

```bash
cp sample.env .env
````

Edita `.env` y cambia `DATABASE_URI` con tu conexión PostgreSQL:

```
DATABASE_URI=postgresql://usuario:password@localhost:5432/mi_base
```

---

2. **(Opcional recomendado)** Crea entorno virtual

```bash
python -m venv env
source env/bin/activate  # en Windows: .\env\Scripts\activate
```

---

3. **Instala dependencias**

```bash
pip install -r requirements.txt
```

---

4. **Crea y aplica migraciones**

```bash
alembic revision --autogenerate -m "primer modelo"
alembic upgrade head
```

---

5. **Listo para usar**

Ahora puedes importar modelos y usar SQLAlchemy normalmente con la base de datos migrada.

---

6. **Aplicación FastAPI (opcional)**

Para lanzar el servidor FastAPI:

```bash
fastapi dev main.py
```

---

## 📁 Archivos importantes

* `.env`: configuración local (no lo subas)
* `sample.env`: plantilla para `.env`
* `app/models.py`: define tus modelos aquí
* `app/db.py`: define `Base` y conexión

---

## 📝 Notas

* Las migraciones quedan en `alembic/versions/`.
* Usa `alembic downgrade -1` si necesitas deshacer una migración.
