Docker Setup

// Make image
docker build --progress=plain --no-cache -t syncfusion-webapi-docker -f Dockerfile .

// Start container with image
docker run -p 80:80/tcp -it --rm syncfusion-webapi-docker