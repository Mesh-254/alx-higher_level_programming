#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    char = sentence[0] if len(sentence) > 0 else None
    return (length, char)
