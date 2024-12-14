
# Quantum Key Distribution Simulation with Flask

This project implements a Quantum Key Distribution (QKD) simulation using Flask. It allows users to encrypt and decrypt messages securely while simulating the detection of potential eavesdropping during the quantum key exchange process.

## Features

- **Quantum Key Distribution (QKD):** Implements a simplified QKD protocol using random bits and bases.
- **Message Encryption and Decryption:** Uses the shared key generated during QKD for encrypting and decrypting messages.
- **Eavesdropping Simulation:** Simulates eavesdropping during the quantum transmission with a configurable probability.
- **Eavesdropping Detection:** Detects eavesdropping based on mismatches in bases or bits during the QKD process.
- **Web Interface:** A user-friendly Flask-based web interface to interact with the simulation.

---

## Technologies Used

- **Flask:** For building the web application.
- **Python:** For implementing the QKD algorithm and encryption/decryption logic.
- **HTML/CSS:** For the front-end interface.

---

## How It Works

1. **Quantum Key Distribution (QKD):**
   - Alice generates random bits and bases.
   - Bob measures the transmitted qubits with his random bases.
   - A shared key is derived from matching bases and bits.

2. **Eavesdropping Simulation:**
   - The simulation introduces an eavesdropper with a configurable probability.
   - If eavesdropping occurs, the qubits may be tampered with, introducing errors.

3. **Encryption and Decryption:**
   - A message is encrypted using the shared key.
   - The encrypted message is then decrypted using the same shared key.

4. **Eavesdropping Detection:**
   - The application checks for mismatches in bases or bits to determine if eavesdropping occurred.

---

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/shr3yashx/qkd-flask-simulation.git
   cd qkd-flask-simulation
   ```

2. **Set Up a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application:**

   ```bash
   flask run
   ```

5. **Open the Application:**
   - Go to `http://127.0.0.1:5000/` in your browser.

---

## Usage

1. Enter the following details on the web interface:
   - Message to encrypt.
   - Key length (number of qubits).
   - Eavesdropping probability (0.0 to 1.0).

2. View the simulation results:
   - Shared key.
   - Encrypted message.
   - Decrypted message.
   - Eavesdropping detection result.

---

---

## File Structure

```
qkd-flask-simulation/
├── app/
│   ├── __init__.py        # Flask app factory
│   ├── routes.py          # Routes and QKD logic
│   ├── templates/
│       ├── index.html     # Home page template
│       ├── result.html    # Results page template
├── run.py                 # Application entry point
├── requirements.txt       # Dependencies
└── README.md              # Project documentation
```

---

## Future Enhancements

- **Improved Eavesdropping Detection:** Enhance detection algorithms to include real-world scenarios.
- **Integration with Quantum Hardware:** Use quantum simulators or actual quantum hardware for QKD.
- **Enhanced Visualization:** Add graphical representations of qubits and their transmission.

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

---

## Contact

For any questions or suggestions, feel free to reach out at:

- **Email:** [shr3yashx@gmail.com](mailto:shr3yashx@gmail.com)
- **GitHub:** [shr3yashx](https://github.com/shr3yashx)
