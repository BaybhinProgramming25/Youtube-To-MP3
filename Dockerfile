FROM python:3.8

# Install ffmpeg as well 
RUN apt-get update && \
    apt-get install -y ffmpeg

# Create converter directory
WORKDIR /converter

# Install app dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code to the container 
COPY . .

# Run the app
CMD [ "python", "./main.py" ]