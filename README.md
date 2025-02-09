# Chess Workshop
## UCI AI Club Chess

### Download

Press the green **"Code"** button and click **"Download ZIP"**.

Save the folder to your computer, and extract the contents.

Open a **Terminal (Mac/Linux)** or **CMD (Windows)** and follow the instructions below.

---

## Prerequisites

We have provided a `requirements.txt` file to help you set up your Python environment.

🔗 **Python Latest Version Download:**  
[https://www.python.org/downloads/](https://www.python.org/downloads/)

### Setup

Navigate to the project directory:
```sh
cd /path/to/chess/folder/
```

#### Mac OSX / Linux

1. Install virtual environment tool:
   ```sh
   pip3 install virtualenv
   ```
2. Create and activate a virtual environment:
   ```sh
   python3 -m venv chessenv
   source chessenv/bin/activate
   ```
3. Install dependencies:
   ```sh
   pip3 install -r requirements.txt
   ```

#### Windows

1. Install virtual environment tool:
   ```sh
   pip3 install --user virtualenv
   ```
2. Create and activate a virtual environment:
   ```sh
   py -m venv chessenv
   chessenv\Scripts\activate.bat
   ```
3. Install dependencies:
   ```sh
   pip3 install -r requirements.txt
   ```

---

## Running the Game

Once the virtual environment is activated, run the following command:

#### Mac OSX / Linux
```sh
python3 chess.py
```

#### Windows
```sh
py chess.py
```



---

## Improving AI Performance

If you have a powerful computer, consider increasing the **depth parameter** of the Minimax algorithm. To do this:
1. Open the `chess.py` file in the project directory.
2. Locate the function named `determine_move`.
3. Increase the depth value (default is 3).

⚠️ **Warning:** A depth beyond 100 may cause recursion errors. Keep the value below this limit for stability.

---



---



