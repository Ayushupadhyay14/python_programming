import random

def generate_otp(length=4):
    digits = "0123456789"
    OTP = ""
    for _ in range(length):
        OTP += digits[random.randint(0, 9)]
    return OTP

# Generate a 6-digit OTP
otp = generate_otp()
print(f"Your OTP is: {otp}")
