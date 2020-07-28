import os
from main import *
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 9000))
    app.run(debug=True, port=port)