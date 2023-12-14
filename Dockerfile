# Use an official gcc image as the base image
FROM gcc:latest

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the source files into the container
COPY . .

# Compile the C++ program
RUN g++ main.cpp operations.h fs.h -o filesystem

# Set the entry point for the container
ENTRYPOINT ["./filesystem"]
