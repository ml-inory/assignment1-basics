example_corpus = """
low low low low low
lower lower widest widest widest
newest newest newest newest newest newest
"""

def init_vocab(special_tokens=['<|endoftext|>']):
    vocab = [chr(i).encode('utf-8') for i in range(256)]
    for t in special_tokens:
        vocab.append(t)
    return vocab


def pre_tokenize(corpus):
    tokens = corpus.split()
    # print(tokens)
    freq_table = {}
    for t in tokens:
        key = tuple(s.encode('utf-8') for s in t)
        if key in freq_table:
            freq_table[key] += 1
        else:
            freq_table[key] = 1

    return freq_table


def merge(freq_table, vocab):
    # byte pair frequency
    bp_freq = {}

    for word, freq in freq_table.items():
        if len(word) == 1:
            continue
        for key in [(word[i], word[i+1]) for i in range(len(word)-1)]:
            # print (key)
            if key in bp_freq:
                bp_freq[key] += freq
            else:
                bp_freq[key] = freq

    # print(bp_freq)
    # most freq pairs
    max_freq = max(bp_freq.values())
    #  take the lexicographically greater pair
    greatest_pair = None
    # greatest_pairs = []
    for key, freq in bp_freq.items():
        if freq == max_freq:
            # greatest_pairs.append(key)

            if greatest_pair is None:
                greatest_pair = key
            else:
                if key[0] > greatest_pair[0]:
                    greatest_pair = key
                elif key[0] < greatest_pair[0]:
                    continue
                else:
                    if key[1] > greatest_pair[1]:
                        greatest_pair = key
                    else:
                        continue

    # print(greatest_pair)
    # print(greatest_pair[0] + greatest_pair[1])
    # print(f"greatest_pairs: {greatest_pairs}")
    merge_word = greatest_pair[0] + greatest_pair[1]
    # print(f"merge_word: {merge_word}")
    
    # merge key in freq_table
    replace_keys = []
    for word in freq_table.keys():
        if len(word) == 1:
            continue

        new_key = []
        i = 0
        key_changed = False
        while i < len(word):
            if greatest_pair[0] == word[i] and greatest_pair[1] == word[i+1]:
                new_key.append(merge_word)
                key_changed = True
                i += 2
            else:
                new_key.append(word[i])
                i += 1
        
        if key_changed:
            replace_keys.append((word, tuple(new_key)))

    for old_key, new_key in replace_keys:
        freq = freq_table.pop(old_key)
        freq_table[new_key] = freq

    # add to vocab
    vocab.append(merge_word)


if __name__ == "__main__":
    vocab = init_vocab()
    freq_table = pre_tokenize(example_corpus)
    print(freq_table)
    for i in range(6):
        merge(freq_table, vocab)
        print(freq_table)
        print(vocab[256:])
        print()