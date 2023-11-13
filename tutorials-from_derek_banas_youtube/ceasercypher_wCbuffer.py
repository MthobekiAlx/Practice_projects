class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.head = 0
        self.tail = 0
        self.count = 0

        # Initialize the buffer with ASCII characters A-Z, a-z
        ascii_values = [i for i in range(65, 91)] + [i for i in range(97, 123)]
        for i in range(size):
            self.buffer[i] = chr(ascii_values[i])

    def shift(self, amount):
        for i in range(self.size):
            self.buffer[i] = chr(((ord(self.buffer[i]) - 65 + amount) % 52) + 65)

    def display(self):
        if self.count == 0:
            return []
        elif self.head < self.tail:
            return self.buffer[self.head:self.tail]
        else:
            return self.buffer[self.head:] + self.buffer[:self.tail]

# Create a circular buffer with uppercase and lowercase letters (A-Z, a-z)
buffer_size = 52
circ_buffer = CircularBuffer(buffer_size)

# Receive input from the user
ceaser_string = input("Enter a message to decrypt: ")

# Store the input string
secret_cstring = ""

# Receive the number to shift by
shift_num = int(input("Please enter the number to shift between -12 and 12: "))
print("num is: ", shift_num)

# Use isupper to check which Unicode to work with
if ceaser_string.isupper():
    circ_buffer.shift(shift_num)  # Shift the circular buffer
    for char in ceaser_string:
        if char.isalpha():  # Ignore non-alphabetic characters
            secret_cstring += circ_buffer.buffer[ord(char) - 65]
        else:
            secret_cstring += char

elif ceaser_string.islower():
    circ_buffer.shift(shift_num)  # Shift the circular buffer
    for char in ceaser_string:
        if char.isalpha():  # Ignore non-alphabetic characters
            secret_cstring += circ_buffer.buffer[ord(char) - 97 + 26]
        else:
            secret_cstring += char

else:
    if operator == "+" and -12 <= shift_num <= 12:
        circ_buffer.shift(shift_num)  # Shift the circular buffer
        for char in ceaser_string:
            if char.isalpha():  # Ignore non-alphabetic characters
                if char.isupper():
                    secret_cstring += circ_buffer.buffer[ord(char) - 65]
                else:
                    secret_cstring += circ_buffer.buffer[ord(char) - 97 + 26]
            else:
                secret_cstring += char
    elif operator == "-" and -12 <= shift_num <= 12:
        circ_buffer.shift(shift_num)  # Shift the circular buffer in the opposite direction
        for char in ceaser_string:
            if char.isalpha():  # Ignore non-alphabetic characters
                if char.isupper():
                    secret_cstring += circ_buffer.buffer[ord(char) - 65]
                else:
                    secret_cstring += circ_buffer.buffer[ord(char) - 97 + 26]
            else:
                secret_cstring += char
    else:
        print("Error input, try again")

print("The decrypted message is: ", secret_cstring)
