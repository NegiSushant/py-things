import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text= "Hey There! My name is Sushant Singh Negi."

token = enc.encode(text)

print(token) #[25216, 3274, 0, 3673, 1308, 382, 336, 1776, 493, 44807, 22837, 72, 13]

decode = enc.decode([25216, 3274, 0, 3673, 1308, 382, 336, 1776, 493, 44807, 22837, 72, 13])


print("Decoded", decode) # Decoded Hey There! My name is Sushant Singh Negi.
