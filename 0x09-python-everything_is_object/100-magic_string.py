#!/usr/bin/python3
def magic_string(fig=[0]):
    fig[0] += 1
    return "BestSchool" + ", BestSchool" * (fig[0] - 1)
