import datetime
print(datetime.datetime.today())

def xor_binary(a, b):
    
  
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    result = ""
    for i in range(max_len):
        result += '1' if a[i] != b[i] else '0'
    
    return result

def encoding(msg, poly):
    
    mod_msg = msg + "0"*(len(poly)-1)
    remainder = remainder_finder(mod_msg, poly)
    
    if len(remainder)<5:
        zeros_needed = 5 - len(remainder)

        remainder = '0' * zeros_needed + remainder
    encoded_output = msg + remainder
    return encoded_output

def remainder_finder(dividend, divisor):

    if int(divisor, 2) == 0:
        raise ZeroDivisionError("Division by zero (divisor is zero)")

    quotient = ""
    remainder = dividend[:len(divisor)]

    for i in range(len(divisor), len(dividend)):
        quotient_bit = remainder[0]
        if quotient_bit == '1':
            remainder = xor_binary(remainder, divisor)
        else:
            remainder = xor_binary(remainder, '0' * len(divisor))

        remainder = remainder[1:] + dividend[i]

        quotient += quotient_bit

    quotient_bit = remainder[0]
    if quotient_bit == '1':
        remainder = xor_binary(remainder, divisor)
    else:
        remainder = xor_binary(remainder, '0' * len(divisor))

    remainder = remainder[1:]

    return remainder

def decoding(rcv, poly):
    
    remainder = remainder_finder(rcv,poly)
    if int(remainder) == 0:
        return "No error Found"
    else:
        return "Error"

user_bit = input("Enter a binary number to be encoded: ")
POLY = "100101" #always fix for 4 bit number


print(f"Encoded message is : {encoding(user_bit, POLY)}")

encoded_number = input("Enter the number you received: ")


print(decoding(encoded_number, POLY))



# ''''explanation:


# Cyclic Redundancy Check (CRC) is an used method, for detecting errors in data transmission and storage. However the effectiveness of CRC in detecting errors depends on the CRC polynomial used and the length of the data block being checked. Here's a general overview;

# Single Bit Errors; When using a polynomial with two terms CRC can successfully detect any single bit error where only one bit in the data packet has changed.

# Double Bit Errors; CRCs can generally detect double bit errors. However it's important to note that not all possible combinations of double bit errors can be guaranteed to be detected unless certain mathematical properties are present in the polynomial used and the total bit length (data plus CRC) is limited relative to the length of the CRC.

# Odd Number of Bit Errors; If the CRC polynomial consists of than one term and includes a factor of (x+1) it becomes capable of detecting any error patterns with a number of bits.

# Burst Errors; For errors CRC can effectively identify those that're equal to or shorter, than its polynomial degree. 
# A burst error refers to a situation where two or more bits, in the data sequence have changed. These changes occur consecutively and the total number of changed bits is less than the length of the CRC field. For instance if you are utilizing a CRC 16 polynomial it can identify errors that're 16 bits or shorter.

# The detection of errors depends on factors such as the length of the data block and the specific CRC polynomial used. As the block length increases relative to the CRC bit length there is a chance of errors occurring.

# In terms no error detection method can guarantee foolproof protection. The CRC method operates under the assumption that an error pattern in corrupted data will match a condition of divisibility. If by chance the error pattern forms a sequence that appears valid under the CRC check then those errors will not be detected. However this likelihood decreases with CRC polynomials and when designed properly to match specific conditions and requirements.

# When dealing with data it is practice to employ additional layers of error detection or correction, alongside CRC to further minimize the risk of undetected errors.
# """


