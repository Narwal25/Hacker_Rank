def designerPdfViewer(h, word):
    return len(word) * max([h[ord(letter) - 97] for letter in word])
