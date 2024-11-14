# Use NGINX to serve the static content
FROM nginx:alpine

# Copy the website content to the NGINX container
COPY src/ /usr/share/nginx/html/

# Expose the default NGINX port
EXPOSE 8080
