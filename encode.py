import jwt


def encode_user():
    encoded_data = jwt.encode(payload={"user": "sys-test-admin2", "access": " approved"},
                              key='sy-secret',
                              algorithm="HS256")
                    
    return encoded_data

def decode_user(token: str):
    """
    :param token: jwt token
    :return:
    """
    decoded_data = jwt.decode(jwt=token,
                              key='sy-secret',
                              algorithms=["HS256"])

    return decoded_data

if __name__ == "__main__":
    token = encode_user()
    decoder = decode_user(token)
    print(encode_user())
    print(" decoded value 2is224424444444444444 : ")
    print(decoder)