import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
print(sys.path)


from app import create_app  # Import the app factory function

# Create the Flask app
app = create_app()

if __name__ == '__main__':
    # Run the app
    app.run(debug=True)
