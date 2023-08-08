python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt

npm install

npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch
