GRID = [
    ".XX.....XX.",
    "XooX...XooX",
    "XoooXXXoooX",
    "XoooooooooX",
    "XoeoooooeoX",
    "XooosnsoooX",
    "XoosssssooX",
    ".XosssssoX.",
    "..XXXXXXX..",
]
COL = {
    "X": "#1a0f08",
    "o": "#A9714B",
    "e": "#120a04",
    "s": "#E8C9A0",
    "n": "#3B2416",
}

print(
    "box-shadow:\n    "
    + ",\n    ".join(
        f"calc(var(--px)*{x}) calc(var(--px)*{y}) 0 {COL[c]}"
        for y, row in enumerate(GRID)
        for x, c in enumerate(row)
        if c != "."
    )
    + ";"
)

