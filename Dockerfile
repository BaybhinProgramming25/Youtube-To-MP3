FROM python:3.8

# Run apt-get update
RUN apt-get update

# Create converter directory
WORKDIR /converter

# Install app dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code to the container 
COPY . .

# Run the app
CMD [ "python", "./main.py" ]