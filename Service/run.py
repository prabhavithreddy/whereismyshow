from Services.mock_service import MockService
import os
from main import *
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=app.config['DEBUG'], port=port)