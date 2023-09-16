# after you have created both the Python script and the Dockerfile, you can now use the Docker build command to build your Docker Image.
docker image build -t python:0.0.1 /local/path/to/dockerfileandpythonscript

# now you can use the Docker run command to run your Docker Container
docker run python:0.0.1
