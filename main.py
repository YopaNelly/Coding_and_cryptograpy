def viginere_encrypt(plaintext, keyword):
  """
  Encrypts plaintext using the Vigenère cipher with the given keyword.

  Args:
      plaintext: The text to encrypt (string).
      keyword: The keyword to use for encryption (string).

  Returns:
      The encrypted ciphertext (string).
  """
  ciphertext = ""
  # Make sure the keyword is uppercase and remove non-alphabetic characters
  keyword = keyword.upper().replace(" ", "")
  # Create a cyclic keyword by repeating the original keyword
  cyclic_keyword = keyword * (len(plaintext) // len(keyword)) + keyword[:len(plaintext) % len(keyword)]

  for i in range(len(plaintext)):
    # Get the character from the plaintext and its corresponding character from the cyclic keyword
    char = plaintext[i]
    key_char = cyclic_keyword[i]

    # Check if the character is alphabetic
    if char.isalpha():
      # Convert the character to uppercase for easier handling
      char = char.upper()
      # Get the shift value based on the keyword character
      shift = ord(key_char) - ord('A')
      # Perform the Caesar cipher shift
      new_char = chr((ord(char) + shift) % 26 + ord('A'))
    else:
      # Keep non-alphabetic characters as they are
      new_char = char

    ciphertext += new_char

  return ciphertext

# Get user input for message and keyword
message = input("Enter the message you want to encode: ")
keyword = input("Enter the keyword for encryption: ")

# Encrypt the message
ciphertext = viginere_encrypt(message, keyword)

# Print the results
print("Plaintext:", message)
print("Keyword:", keyword)
print("Ciphertext:", ''.join(ciphertext.split()))  # Join words in ciphertext without spaces
