from services.mock_service import MockService
import os
from main import *
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 9000))
    app.run(debug=app.config['DEBUG'], port=port)