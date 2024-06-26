FROM python:3.9-slim

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any dependencies
RUN pip install --no-cache-dir flask
RUN pip install --upgrade pip
# Install dependecies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
#CMD ["flask", "run"]
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
