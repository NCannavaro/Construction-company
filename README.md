# Construction-company

Task manager for a construction company.
- Use the command to configure the database and tables:
```bash
python manage.py migrate
```
- Use the following command to load prepared data from fixture to test code:
```bash
python manage.py loaddata db_data.json
```

- After loading data from fixture you can use following superuser (or create another one by yourself):
  - Login: `admin.user`
  - Password: `Us2ddTX7`

Feel free to add more data using admin panel, if needed.

**BD structure :**

![BD structure](screens/arch_bd.png)

   **1. Login page :**

![Login page](screens/login.png)

   **2. Home page :**

![Home page](screens/Home.png)

   **3. Task list page :**

![Task list](screens/task_list.png)

   **4. Task detail page :**

![Task detail](screens/task_detail.png)

   **5. Employees list page :**

![Employees list](screens/employees_list.png)

   **6. Employyes detail page:**

![Employee detail](screens/employees_detail.png)