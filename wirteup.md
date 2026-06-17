## Problem(unicode1)

- (a) What Unicode character does chr(0) return?

    '\x00'

- (b) How does this character’s string representation (__repr__()) differ from its printed 
representation?

    The string representation is '\x00' while the printed representation is an empty string.

- (c) What happens when this character occurs in text? It may be helpful to play around with the 
following in your Python interpreter and see if it matches your expectations:
```
>>> chr(0)
>>> print(chr(0))
>>> "this is a test" + chr(0) + "string"
>>> print("this is a test" + chr(0) + "string")
```

    ```
    >>> "this is a test" + chr(0) + "string"
    'this is a test\x00string'
    >>> print("this is a test" + chr(0) +   "string")
    this is a teststring
    ```

The string representation of chr(0)     remains \x00 while the printed  representation of it just prints nothing     and could be ignored in this case.

## Problem(unicode2)

- (a) What are some reasons to prefer training our tokenizer on UTF-8 encoded bytes, rather than 
UTF-16 or UTF-32? It may be helpful to compare the output of these encodings for various 
input strings.

    Using UTF-16 or UTF-32 means using more bytes to encode the same character, hence longer encoded sequence and increased vocabulary size.(28 integers for UTF-16 and 56 integers for UTF-32 for test_string: hello! こんにちは!)

- (b) Consider the following (incorrect) function, which is intended to decode a UTF-8 byte string 
into a Unicode string. Why is this function incorrect? Provide an example of an input byte 
string that yields incorrect results.
```
def decode_utf8_bytes_to_str_wrong(bytestring: bytes):
    return "".join([bytes([b]).decode("utf-8") for b in bytestring])
>>> decode_utf8_bytes_to_str_wrong("hello".encode("utf-8"))
'hello'
```

    decode_utf8_bytes_to_str_wrong("牛".encode("utf-8")) produces incorrect output. Because UTF-8 byte string of "牛" is b'\xe7\x89\x9b', this three bytes altogether encode "牛", while this function decode every byte separately.

- (c) Give a two-byte sequence that does not decode to any Unicode character(s).

b'\xa2\x80'  
two-byte sequence requires the leading bytes to be 110xxxxx.


## Problem(train_bpe_tinystories)

(a)
Training on TinyStoriesV2-GPT4-valid.txt take 45 seconds, peak mem usage 94MB, longest token is 'accomplishment'

(b) Profile
Over 50% of time was used for init_freq_table(compute word counts)


## Problem(train_bpe_expts_owt)

(a) 
Longest token: b'----------------------------------------------------------------'

