#!/bin/bash

# Variables
DB_NAME="medical_images_db"
DB_USER="django_user"
DB_PASS="securepassword"
DB_HOST="localhost"
DB_PORT="5432"
SQLITE_DB="db.sqlite3"
DJANGO_MANAGE="python manage.py"
SETTINGS_FILE="punto4/settings.py"

# Function to check if PostgreSQL is available
function check_postgres() {
  pg_isready -h $DB_HOST -p $DB_PORT -q
  return $?
}

# Function to create or drop (if exists) PostgreSQL database and user
# Improved function to create or drop (if exists) PostgreSQL database, user, and role
function create_postgres_db() {
  echo "Attempting to check for existing PostgreSQL database, user, and role..."
  PSQL="psql -U postgres -h $DB_HOST -p $DB_PORT"

  # Check if the role exists and drop it if necessary
  $PSQL -tAc "SELECT rolname FROM pg_roles WHERE rolname = 'nombre_del_rol';" | grep -q "nombre_del_rol"
  if [[ $? -eq 0 ]]; then
    echo "Role 'nombre_del_rol' already exists. Dropping it..."
    $PSQL -c "DROP ROLE nombre_del_rol;"
  fi

  # Check if the user exists and drop it if necessary
  $PSQL -tAc "SELECT usename FROM pg_user WHERE usename='$DB_USER';" | grep -q "$DB_USER"
  if [[ $? -eq 0 ]]; then
    echo "User '$DB_USER' already exists. Dropping it..."
    $PSQL -c "DROP USER $DB_USER;"
  fi

  # Check if the database exists and drop it if necessary
  $PSQL -tAc "SELECT datname FROM pg_database WHERE datname='$DB_NAME';" | grep -q "$DB_NAME"
  if [[ $? -eq 0 ]]; then
    echo "Database '$DB_NAME' already exists. Dropping it..."
    $PSQL -c "DROP DATABASE $DB_NAME;"
  fi

  # Create the role, the user, and the database
  $PSQL -c "CREATE ROLE nombre_del_rol;" &&  # Create the role
  $PSQL -c "CREATE USER $DB_USER WITH PASSWORD '$DB_PASS';" &&  # Create the user
  $PSQL -c "ALTER ROLE $DB_USER SET ROLE nombre_del_rol;" &&  # Assign the role to the user
  $PSQL -c "CREATE DATABASE $DB_NAME OWNER $DB_USER;" &&  # Create the database with the user as owner
  echo "PostgreSQL database, user, and role created successfully." &&
  return 0

  echo "Failed to create PostgreSQL database."
  return 1
}

# Update Django settings for PostgreSQL
function update_settings_postgres() {
  echo "Updating Django settings for PostgreSQL..."
  sed -i "s/'ENGINE': 'django.db.backends.sqlite3'/'ENGINE': 'django.db.backends.postgresql'/g" $SETTINGS_FILE
  sed -i "/'ENGINE': 'django.db.backends.postgresql'/a\        'NAME': '$DB_NAME',\n        'USER': '$DB_USER',\n        'PASSWORD': '$DB_PASS',\n        'HOST': '$DB_HOST',\n        'PORT': '$DB_PORT'," $SETTINGS_FILE
  sed -i "/'NAME': BASE_DIR \/ 'db.sqlite3'/d" $SETTINGS_FILE
}

# Update Django settings for SQLite
function update_settings_sqlite() {
  echo "Updating Django settings for SQLite..."
  sed -i "s/'ENGINE': 'django.db.backends.postgresql'/'ENGINE': 'django.db.backends.sqlite3'/g" $SETTINGS_FILE
  sed -i "s/'NAME': '$DB_NAME'/NAME': BASE_DIR \/ 'db.sqlite3'/g" $SETTINGS_FILE
  sed -i "/'USER': '$DB_USER'/d" $SETTINGS_FILE
  sed -i "/'PASSWORD': '$DB_PASS'/d" $SETTINGS_FILE
  sed -i "/'HOST': '$DB_HOST'/d" $SETTINGS_FILE
  sed -i "/'PORT': '$DB_PORT'/d" $SETTINGS_FILE
}

# Main script
if check_postgres; then
  echo "PostgreSQL is available. Setting up database..."
  if create_postgres_db; then
    update_settings_postgres
  else
    echo "Switching to SQLite..."
    update_settings_sqlite
  fi
else
  echo "PostgreSQL is not available. Using SQLite database."
  update_settings_sqlite
fi

#Install dependencies
echo "Run pip"
pip install -r requirements.txt
# Run migrations and start the server
echo "Installing dependencies..."
$DJANGO_MANAGE migrate

echo "Starting Django development server..."
$DJANGO_MANAGE runserver