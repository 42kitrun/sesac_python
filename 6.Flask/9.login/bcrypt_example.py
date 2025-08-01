# pip install bcrypt
import bcrypt

# bcrypt 내부 함수...

def generate_hash(password):
    salt = bcrypt.gensalt() # 검정하려면 salt가 동일해야한다. 결과값에 salt와 password가 동일해야한다.
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed

def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password)

hashed1 = generate_hash("hello123")
hashed2 = generate_hash("hello123")

print("Hash1: ", hashed1)
print("Hash2: ", hashed2)

print("Hash1 암호검증: ", verify_password("hello222", hashed1))
print("Hash1 암호검증: ", verify_password("hello123", hashed1))