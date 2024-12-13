from flask import Blueprint, render_template, request
import random

main = Blueprint('main', __name__)


# Helper functions for encryption and decryption
def encrypt_message(message, key):
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    encrypted = ''.join(str(int(b) ^ key[i % len(key)]) for i, b in enumerate(binary_message))
    return encrypted


def decrypt_message(encrypted, key):
    decrypted_binary = ''.join(str(int(b) ^ key[i % len(key)]) for i, b in enumerate(encrypted))
    decrypted = ''.join(chr(int(decrypted_binary[i:i + 8], 2)) for i in range(0, len(decrypted_binary), 8))
    return decrypted


# QKD Functions
def generate_random_bits_and_bases(length):
    bits = [random.randint(0, 1) for _ in range(length)]
    bases = [random.choice(['+', 'x']) for _ in range(length)]
    return bits, bases


def encode_qubits(bits, bases):
    return [(bit, base) for bit, base in zip(bits, bases)]


def transmit_qubits(qubits, eavesdrop_probability=0.0):
    transmitted = []
    for bit, base in qubits:
        if random.random() < eavesdrop_probability:
            tampered_bit = random.randint(0, 1)
            tampered_base = random.choice(['+', 'x'])
            transmitted.append((tampered_bit, tampered_base))
        else:
            transmitted.append((bit, base))
    return transmitted


def measure_qubits(qubits, bob_bases):
    measured_bits = []
    for (bit, alice_base), bob_base in zip(qubits, bob_bases):
        if alice_base == bob_base:
            measured_bits.append(bit)
        else:
            measured_bits.append(random.randint(0, 1))
    return measured_bits


def reconcile_keys(alice_bases, bob_bases, alice_bits, bob_bits):
    shared_key = []
    for a_base, b_base, a_bit, b_bit in zip(alice_bases, bob_bases, alice_bits, bob_bits):
        if a_base == b_base and a_bit == b_bit:
            shared_key.append(a_bit)
    return shared_key


def detect_eavesdropping(alice_bases, bob_bases, alice_bits, bob_bits):
    mismatches = 0
    for a_base, b_base, a_bit, b_bit in zip(alice_bases, bob_bases, alice_bits, bob_bits):
        if a_base != b_base or a_bit != b_bit:
            mismatches += 1
    eavesdrop_probability = mismatches / len(alice_bases)
    return eavesdrop_probability, mismatches


@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form['message']
        key_length = int(request.form['key_length'])
        eavesdrop_probability_input = float(request.form['eavesdrop_probability'])

        alice_bits, alice_bases = generate_random_bits_and_bases(key_length)
        qubits = encode_qubits(alice_bits, alice_bases)
        transmitted_qubits = transmit_qubits(qubits, eavesdrop_probability_input)

        bob_bases = [random.choice(['+', 'x']) for _ in range(key_length)]
        bob_bits = measure_qubits(transmitted_qubits, bob_bases)

        shared_key = reconcile_keys(alice_bases, bob_bases, alice_bits, bob_bits)

        if len(shared_key) < len(message) * 8:
            return render_template('index.html', error="Shared key is too short for the message.")

        encrypted_message = encrypt_message(message, shared_key)
        decrypted_message = decrypt_message(encrypted_message, shared_key)

        eavesdrop_probability, mismatches = detect_eavesdropping(alice_bases, bob_bases, alice_bits, bob_bits)

        detection_result = "Eavesdropping detected!" if eavesdrop_probability > eavesdrop_probability_input else "No eavesdropping detected."

        return render_template('result.html', shared_key=shared_key, encrypted_message=encrypted_message,
                               decrypted_message=decrypted_message, eavesdrop_probability=eavesdrop_probability,
                               mismatches=mismatches, detection_result=detection_result)

    return render_template('index.html')


@main.route('/result')
def result():
    return render_template('result.html')
